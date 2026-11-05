"""Audit of the organizers' data files against each other and against NBIM's SEC filing.

Findings this reproduces (see README):
  * real_votes.csv: 'with the board' 94.4% (2025: 94.6%), matching NBIM's published 94%.
  * npx_votes.csv: mgmt_rec mirrors NBIM's vote. 2,538 MANAGEMENT proposals are marked
    'board recommends MOT', so the provided against_board misses real deviations; its
    96.0% 'with the board' falls to 92.0% once the board recommendation is corrected.
  * NBIM's SEC N-PX filing (US say-on-pay) agrees with real_votes.csv on 97.7% of matched
    votes, but npx_votes.csv catches only 11 of its 51 AGAINST votes.
"""
from __future__ import annotations

import re

import pandas as pd

from . import ballot
from .config import DATA_PROCESSED


def _norm(s) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def run() -> dict:
    real = pd.read_csv(ballot.REAL_FILE, low_memory=False, parse_dates=["meeting_date"])
    npx = ballot.load_npx_fixed()
    out: dict = {}
    for name, d in (("real_votes", real), ("npx_votes", npx)):
        voted = d[d["nbim_vote"].notna()]
        lab = d[d["against_board"].notna()]
        mgmt = d[d["proponent"] == "Management"]
        out[name] = {
            "rows": int(len(d)), "meetings": int(d["meeting_id"].nunique()),
            "companies": int(d["company_id"].nunique()),
            "date_range": [str(d["meeting_date"].min().date()), str(d["meeting_date"].max().date())],
            "always_for_share": float((voted["nbim_vote"] == "FOR").mean()),
            "with_board_provided_label": float(1 - lab["against_board"].mean()),
            "mgmt_proposals_with_board_rec_MOT": int((mgmt["mgmt_rec"] == "MOT").sum()),
            "of_which_nbim_voted_MOT": int(((mgmt["mgmt_rec"] == "MOT") & (mgmt["nbim_vote"] == "MOT")).sum()),
        }
    out["npx_votes"]["with_board_corrected"] = float(1 - npx["y_fixed"].dropna().mean())
    out["npx_votes"]["injection_flag_rows"] = int((npx["injection_flag"] == 1).sum())
    lab = real[real["against_board"].notna()]
    out["real_votes"]["with_board_by_year"] = {int(y): float(1 - g["against_board"].mean())
                                               for y, g in lab.groupby(lab["meeting_date"].dt.year)}

    # Cross-check with NBIM's SEC N-PX filing (US say-on-pay only)
    sec_file = DATA_PROCESSED / "sec_nbim_npx_sop.csv"
    if sec_file.exists():
        e = pd.read_csv(sec_file, parse_dates=["meeting_date"], dtype={"cusip": str})
        e = e[e["proposal_type"] == "sop"]
        e["k"] = e["issuer_name"].map(_norm).str[:12]
        rs = real[(real["proposal_type"] == "SAY_ON_PAY") & (real["country"] == "United States")].copy()
        rs["k"] = rs["company"].map(_norm).str[:12]
        j = rs.merge(e[["k", "meeting_date", "how_voted"]], on=["k", "meeting_date"])
        agree = ((j["nbim_vote"] == "MOT") == (j["how_voted"] == "AGAINST")).mean()
        ns = npx[(npx["proposal_type"] == "SAY_ON_PAY") & (npx["country"] == "United States")].copy()
        ns["cusip"] = ns["company_id"].astype(str)
        jn = ns.merge(e[["cusip", "meeting_date", "how_voted"]], on=["cusip", "meeting_date"])
        out["sec_crosscheck"] = {
            "real_vs_sec_matched": int(len(j)), "real_vs_sec_agreement": float(agree),
            "npx_vs_sec_matched": int(len(jn)),
            "npx_vs_sec_agreement": float(((jn["nbim_vote"] == "MOT") == (jn["how_voted"] == "AGAINST")).mean()),
            "sec_against_votes_in_npx_match": int((jn["how_voted"] == "AGAINST").sum()),
            "of_which_npx_says_MOT": int(((jn["how_voted"] == "AGAINST") & (jn["nbim_vote"] == "MOT")).sum()),
        }
    return out
