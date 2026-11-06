"""Full-ballot dataset from NBIM's own voting records (data/real_votes.csv).

Ground truth: `against_board` = 1 when NBIM's vote differs from the board's
recommendation (MOT or AVSTÅ on a FOR recommendation, FOR or AVSTÅ on a MOT one).
Rows without an NBIM vote or without a board recommendation (3.1%) have no label
and are excluded from training and evaluation.

Walk-forward split by meeting date: train 2019-2023, validate 2024 (model choice,
calibration and thresholds), test 2025-2026 (evaluated once).

History features use strictly earlier meetings of the same company only. In
production that is legitimate: NBIM knows its own past votes. NEVER features:
rationale_text, rationale_section, position_paper (exist only for against votes),
nbim_vote*, against_board.
"""
from __future__ import annotations

import re
from collections import defaultdict

import numpy as np
import pandas as pd

from .config import ROOT

REAL_FILE = ROOT / "data" / "real_votes.csv"

SPLITS = [("train", "2019-01-01", "2023-12-31"), ("valid", "2024-01-01", "2024-12-31"),
          ("test", "2025-01-01", "2026-12-31")]
LEAKY_COLUMNS = ["nbim_vote_raw", "nbim_vote", "against_board", "rationale_text",
                 "rationale_section", "position_paper"]
PRIOR_STRENGTH = 5.0  # smoothing for company-level deviation rates

_DIRECTOR_PATTERNS = [
    # "Elect Director Fujita, Taisuke" / "Elect Director Patricia L. Kampling" (name ends the text)
    re.compile(r"(?i)\belect(?:ion of)?\s+directors?\s+(?:nominee\s+)?(?P<name>[A-Z][\w'.\- ]+(?:,\s*[A-Z][\w'.\- ]+)?)\s*$"),
    re.compile(r"(?i)\belect(?:ion of)?\s+directors?\s+(?:nominee\s+)?(?P<name>[^,;:(]+?)(?:\s*[,;(]|\s+to\s+|\s+as\s+|$)"),
    re.compile(r"(?i)\b(?:re-?)?elect(?:ion of)?\s+(?P<name>[A-Z][^,;:(]+?)\s+(?:as|to)\s+(?:an?\s+)?(?:director|member|chair|board|supervisory|non-executive|independent|outside)"),
]


def item_key(text: str) -> str:
    """Normalized proposal text: recurring items ('Approve Discharge ... for FY 2023') match across years."""
    t = str(text).lower()
    t = re.sub(r"\d+", " ", t)
    t = re.sub(r"[^a-z]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()[:160]


def person_key(text: str, proposal_type: str) -> str | None:
    if proposal_type != "DIRECTOR_ELECTION":
        return None
    for pat in _DIRECTOR_PATTERNS:
        m = pat.search(str(text))
        if m:
            name = re.sub(r"(?i)\b(mr|ms|mrs|dr|prof)\.?\s+", "", m.group("name"))
            name = re.sub(r"[^a-z]+", " ", name.lower()).strip()
            if 2 <= len(name.split()) <= 6:
                return " ".join(sorted(name.split()))  # order-free: 'tsuruha jun' == 'jun tsuruha'
    return None


def model_text(text: str, person: str | None) -> str:
    """Text the classifier sees: no digits (years) and no person names.

    Without this the TF-IDF model memorised names ('davis', 'ichiro') and years
    ('fiscal 2018'). Person-level history is handled explicitly by `prev_same_person`.
    """
    t = str(text)
    if isinstance(person, str) and person:
        for tok in set(person.split()):
            if len(tok) > 1:
                t = re.sub(rf"(?i)\b{re.escape(tok)}\b\.?", " ", t)
        t = "PERSON " + t
    t = re.sub(r"\d+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def load_real() -> pd.DataFrame:
    d = pd.read_csv(REAL_FILE, low_memory=False, parse_dates=["meeting_date"])
    d["row_id"] = np.arange(len(d))
    d["split"] = None
    for name, lo, hi in SPLITS:
        d.loc[d["meeting_date"].between(lo, hi), "split"] = name
    d["labelled"] = d["against_board"].notna()
    d["y"] = d["against_board"].fillna(0).astype(int)
    d["proposal_text"] = d["proposal_text"].fillna("")
    d["item_key"] = d["proposal_text"].map(item_key)
    d["person_key"] = [person_key(t, p) for t, p in zip(d["proposal_text"], d["proposal_type"])]
    d["model_text"] = [model_text(t, k) for t, k in zip(d["proposal_text"], d["person_key"])]
    d["board_rec"] = d["mgmt_rec"].fillna("NONE")
    n_items = d.groupby("meeting_id")["row_id"].transform("size")
    d["meeting_n_items"] = n_items
    d["meeting_has_shp"] = d.groupby("meeting_id")["proponent"].transform(lambda s: (s == "Shareholder").any()).astype(int)
    return add_history(d)


def add_history(d: pd.DataFrame) -> pd.DataFrame:
    """Company-level voting history from strictly earlier meetings."""
    d = d.sort_values(["meeting_date", "meeting_id", "item_no"]).copy()
    base_rate = d.loc[d["labelled"] & (d["split"] == "train"), "y"].mean()
    comp = defaultdict(lambda: [0, 0])          # company -> [n, deviations]
    ctype = defaultdict(lambda: [0, 0])         # (company, type) -> [n, dev]
    item = {}                                   # (company, item_key) -> last label
    person = {}                                 # (company, person) -> last label
    item_sec, person_sec = {}, {}               # ... -> NBIM's published section when it deviated
    last_meeting_dev = {}                       # company -> any deviation at its last meeting
    cols = {k: np.full(len(d), np.nan) for k in
            ("hist_n", "hist_dev", "hist_dev_rate", "hist_type_n", "hist_type_dev_rate",
             "prev_same_item", "prev_same_person", "prev_meeting_any_dev")}
    prev_section = np.full(len(d), None, dtype=object)
    pos = {rid: i for i, rid in enumerate(d["row_id"])}
    for (mdate, mid), g in d.groupby(["meeting_date", "meeting_id"], sort=False):
        c = g["company_id"].iloc[0]
        for r in g.itertuples():
            i = pos[r.row_id]
            pk = r.person_key if isinstance(r.person_key, str) else None  # NaN is truthy!
            n, dev = comp[c]
            cols["hist_n"][i] = n
            cols["hist_dev"][i] = dev
            cols["hist_dev_rate"][i] = (dev + PRIOR_STRENGTH * base_rate) / (n + PRIOR_STRENGTH)
            tn, tdev = ctype[(c, r.proposal_type)]
            cols["hist_type_n"][i] = tn
            cols["hist_type_dev_rate"][i] = (tdev + PRIOR_STRENGTH * base_rate) / (tn + PRIOR_STRENGTH)
            if (c, r.item_key) in item:
                cols["prev_same_item"][i] = item[(c, r.item_key)]
            if pk and (c, pk) in person:
                cols["prev_same_person"][i] = person[(c, pk)]
            if c in last_meeting_dev:
                cols["prev_meeting_any_dev"][i] = last_meeting_dev[c]
            if pk and (c, pk) in person_sec:
                prev_section[i] = person_sec[(c, pk)]
            elif (c, r.item_key) in item_sec:
                prev_section[i] = item_sec[(c, r.item_key)]
        lab = g[g["labelled"]]
        for r in lab.itertuples():  # update AFTER the whole meeting: no same-meeting leakage
            pk = r.person_key if isinstance(r.person_key, str) else None
            comp[c][0] += 1
            comp[c][1] += r.y
            ctype[(c, r.proposal_type)][0] += 1
            ctype[(c, r.proposal_type)][1] += r.y
            item[(c, r.item_key)] = r.y
            if pk:
                person[(c, pk)] = r.y
            sec = r.rationale_section if isinstance(r.rationale_section, str) and r.rationale_section.startswith("GVG") else None
            if r.y == 1 and sec:  # published with the vote, so known at later meetings
                item_sec[(c, r.item_key)] = sec
                if pk:
                    person_sec[(c, pk)] = sec
        if len(lab):
            last_meeting_dev[c] = int(lab["y"].max())
    for k, v in cols.items():
        d[k] = v
    d["prev_same_section"] = prev_section
    d["has_history"] = (d["hist_n"] > 0).astype(int)
    # The single most informative history signal: the same item/person voted on before.
    d["prev_same"] = d["prev_same_person"].fillna(d["prev_same_item"])
    return d.sort_values("row_id").reset_index(drop=True)
