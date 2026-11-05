"""#2464: kjør det opplastede NBIM-repoets persistence og hybrid, skriv svarfiler for vår test 2026 (og deres test 2025-26).
Kjøres med python -I herfra; repoets src legges inn i sys.path eksplisitt. Datafila er vår offisielle (samme sha256)."""
import sys, pathlib
REPO = pathlib.Path("arbeid/hack/CASE/20261105_155545_NBIM_Hackathon_2026-main_1__ut/NBIM_Hackathon_2026-main")
sys.path.insert(0, str(REPO / "src"))
from stemmeagent import ballot, ballot_model as bm
import numpy as np, pandas as pd
ballot.REAL_FILE = pathlib.Path("state/opplastet/20261105_114241_real_votes.csv")
SPLIT = sys.argv[1]  # deres | vaar
if SPLIT == "vaar":
    ballot.SPLITS = [("train", "2019-01-01", "2024-12-31"), ("valid", "2025-01-01", "2025-12-31"), ("test", "2026-01-01", "2026-12-31")]
d = bm.add_model_columns(ballot.load_real())
lab = d[d["labelled"]]
tr, va = (lab[lab["split"] == s].copy() for s in ("train", "valid"))
m = bm.fit_select(tr, va)
print("valgt", m.name, "t_flag", m.t_flag, "t_flag_model", m.t_flag_model)
for s in m.selection: print(" ", s)
d["id"] = d["meeting_id"].astype(str) + "|" + d["item_no"].astype(str)
p = m.predict_proba(d); sc = m.score(d, p)
pers = (d["prev_same"] == 1).astype(int)
for navn, pred, prob in [("persistence", pers.values, pers.values.astype(float)),
                         ("hybrid", (sc >= m.t_flag).astype(int), np.minimum(sc, 1.0)),
                         ("modell", (p >= m.t_flag_model).astype(int), p)]:
    for vind, maske in [("t2026", d["meeting_date"].dt.year == 2026), ("t2526", d["meeting_date"].dt.year >= 2025)]:
        u = pd.DataFrame({"id": d["id"], "anbefaling": pred, "p_avvik": prob})[maske.values]
        u.to_csv(f"svar_{SPLIT}_{navn}_{vind}.csv", index=False)
        l = maske & d["labelled"]; y = d.loc[l, "y"].values; f = pred[l.values]
        tp = int((f * y).sum()); print(f"{SPLIT} {navn} {vind}: avvik-F1 {2*tp/max(2*tp+(f==1).sum()-tp+(y==1).sum()-tp,1):.3f} flagget {int(f.sum())} avvik {int(y.sum())}")
