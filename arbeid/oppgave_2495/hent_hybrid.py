"""#2495: repoets hybrid på vår splitt (train ≤2024, valg 2025). Dumper hybridscore og flagg for 2025 og 2026."""
import sys, pathlib
REPO = pathlib.Path("arbeid/hack/CASE/20261105_155545_NBIM_Hackathon_2026-main_1__ut/NBIM_Hackathon_2026-main")
sys.path.insert(0, str(REPO / "src"))
from stemmeagent import ballot, ballot_model as bm
import pandas as pd
ballot.REAL_FILE = pathlib.Path("state/opplastet/20261105_114241_real_votes.csv")
ballot.SPLITS = [("train", "2019-01-01", "2024-12-31"), ("valid", "2025-01-01", "2025-12-31"), ("test", "2026-01-01", "2026-12-31")]
d = bm.add_model_columns(ballot.load_real())
lab = d[d["labelled"]]
tr, va = (lab[lab["split"] == s].copy() for s in ("train", "valid"))
m = bm.fit_select(tr, va)
print("valgt", m.name, "t_flag", m.t_flag)
d["id"] = d["meeting_id"].astype(str) + "|" + d["item_no"].astype(str)
p = m.predict_proba(d); sc = m.score(d, p)
u = pd.DataFrame({"id": d["id"], "aar": d["meeting_date"].dt.year, "h_score": sc, "h_flag": (sc >= m.t_flag).astype(int), "prev_same": (d["prev_same"] == 1).astype(int)})
u[u["aar"] >= 2025].to_csv("hybrid.csv", index=False)
print(u[u["aar"] >= 2025].groupby("aar")[["h_flag", "prev_same"]].sum())
