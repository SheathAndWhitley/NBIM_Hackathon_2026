"""#2357: for hver falsk MOT (FP) i test 2026: hva stemte NBIM på samme sakstekst (samme person) hos samme selskap før?
Bruk: .venv/bin/python arbeid/oppgave_2357/fp_historikk.py"""
import os, re, pandas as pd
ROT = "."
d = pd.read_csv(f"{ROT}/state/opplastet/20261105_114241_real_votes.csv", dtype=str, keep_default_na=False)
d = d[d.injection_flag != "1"].copy(); d["id"] = d.meeting_id + "|" + d.item_no
s = pd.read_csv(f"{ROT}/arbeid/oppgave_2087/svar_test.csv", dtype={"id": str})
t = d[d.year == "2026"].merge(s, on="id", how="left")
t = t[t.against_board != ""].copy()
styret = t.mgmt_rec.replace("", "FOR")
t["pred"] = (t.anbefaling == 1) & (styret != "MOT")
t["fasit"] = (t.nbim_vote == "MOT") & (t.against_board == "1.0")
fp = t[t.pred & ~t.fasit]
def norm(x): return re.sub(r"^(re-?elect|elect)\s+(director\s+)?|\s+as\s+director.*$", "", x.lower()).strip()
for _, r in fp.sort_values(["country", "proposal_type"]).iterrows():
    h = d[(d.company_id == r.company_id) & (d.year < "2026")]
    if r.proposal_type == "DIRECTOR_ELECTION":
        h = h[h.proposal_text.str.lower().apply(norm) == norm(r.proposal_text)]
    else:
        h = h[h.proposal_type == r.proposal_type]
    hist = " ".join(f"{y}:{v}" for y, v in zip(h.year, h.nbim_vote))
    snu = "SNUDD" if (h.nbim_vote == "MOT").any() else ("aldri MOT" if len(h) else "ingen historikk")
    print(f"{r.country[:14]:14s} {r.proposal_type[:10]:10s} {r.company[:28]:28s} | {r.proposal_text[:45]:45s} | 2026:{r.nbim_vote} | {hist} | {snu} | {r.rationale_text[:60]}")
