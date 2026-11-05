"""#2744: streng variant av NBIM-repoets ballot.add_history: historikk bare fra møter med STRENGT tidligere dato.
Eneste forskjell fra originalen: gruppering på (meeting_date, company_id) i stedet for (meeting_date, meeting_id),
så etikettene oppdateres først etter ALLE møter selskapet har samme dag. Ingen frosne filer rørt."""
from collections import defaultdict
import numpy as np, pandas as pd

def lag(ballot):
    PRIOR_STRENGTH = ballot.PRIOR_STRENGTH
    def add_history_strengt(d: pd.DataFrame) -> pd.DataFrame:
        d = d.sort_values(["meeting_date", "meeting_id", "item_no"]).copy()
        base_rate = d.loc[d["labelled"] & (d["split"] == "train"), "y"].mean()
        comp = defaultdict(lambda: [0, 0]); ctype = defaultdict(lambda: [0, 0])
        item = {}; person = {}; item_sec, person_sec = {}, {}; last_meeting_dev = {}
        cols = {k: np.full(len(d), np.nan) for k in
                ("hist_n", "hist_dev", "hist_dev_rate", "hist_type_n", "hist_type_dev_rate",
                 "prev_same_item", "prev_same_person", "prev_meeting_any_dev")}
        prev_section = np.full(len(d), None, dtype=object)
        pos = {rid: i for i, rid in enumerate(d["row_id"])}
        for (mdate, c), g in d.groupby(["meeting_date", "company_id"], sort=False):  # <- ENDRINGEN
            for r in g.itertuples():
                i = pos[r.row_id]
                pk = r.person_key if isinstance(r.person_key, str) else None
                n, dev = comp[c]
                cols["hist_n"][i] = n; cols["hist_dev"][i] = dev
                cols["hist_dev_rate"][i] = (dev + PRIOR_STRENGTH * base_rate) / (n + PRIOR_STRENGTH)
                tn, tdev = ctype[(c, r.proposal_type)]
                cols["hist_type_n"][i] = tn
                cols["hist_type_dev_rate"][i] = (tdev + PRIOR_STRENGTH * base_rate) / (tn + PRIOR_STRENGTH)
                if (c, r.item_key) in item: cols["prev_same_item"][i] = item[(c, r.item_key)]
                if pk and (c, pk) in person: cols["prev_same_person"][i] = person[(c, pk)]
                if c in last_meeting_dev: cols["prev_meeting_any_dev"][i] = last_meeting_dev[c]
                if pk and (c, pk) in person_sec: prev_section[i] = person_sec[(c, pk)]
                elif (c, r.item_key) in item_sec: prev_section[i] = item_sec[(c, r.item_key)]
            lab = g[g["labelled"]]
            for r in lab.itertuples():
                pk = r.person_key if isinstance(r.person_key, str) else None
                comp[c][0] += 1; comp[c][1] += r.y
                ctype[(c, r.proposal_type)][0] += 1; ctype[(c, r.proposal_type)][1] += r.y
                item[(c, r.item_key)] = r.y
                if pk: person[(c, pk)] = r.y
                sec = r.rationale_section if isinstance(r.rationale_section, str) and r.rationale_section.startswith("GVG") else None
                if r.y == 1 and sec:
                    item_sec[(c, r.item_key)] = sec
                    if pk: person_sec[(c, pk)] = sec
            if len(lab): last_meeting_dev[c] = int(lab["y"].max())
        for k, v in cols.items(): d[k] = v
        d["prev_same_section"] = prev_section
        d["has_history"] = (d["hist_n"] > 0).astype(int)
        d["prev_same"] = d["prev_same_person"].fillna(d["prev_same_item"])
        return d.sort_values("row_id").reset_index(drop=True)
    return add_history_strengt
