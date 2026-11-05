"""#2357: hvor ofte snur NBIM i 2026 for samme person som fikk MOT i 2025? Per land. Og begrunnelsen fra 2025."""
import re, pandas as pd
d = pd.read_csv("state/opplastet/20261105_114241_real_votes.csv", dtype=str, keep_default_na=False)
d = d[(d.injection_flag != "1") & (d.proposal_type == "DIRECTOR_ELECTION")].copy()
def norm(x): return re.sub(r"^(re-?elect|elect)\s+(director\s+)?|\s+as\s+director.*$", "", x.lower()).strip()
d["p"] = d.company_id + "#" + d.proposal_text.str.lower().apply(norm)
for a, b in [("2024", "2025"), ("2025", "2026")]:
    m = d[(d.year == a) & (d.nbim_vote == "MOT") & (d.mgmt_rec == "FOR")]
    n = d[(d.year == b) & d.p.isin(m.p)].drop_duplicates("p")
    n = n.assign(us=n.country.eq("United States"))
    print(f"MOT {a} -> {b}:", n.groupby("us").nbim_vote.value_counts().to_dict())
m25 = d[(d.year == "2025") & (d.nbim_vote == "MOT")]
for nav in ["dueser", "kemper", "swift", "bryan jordan", "havner", "michael s. dell", "durban"]:
    for yr in ["2025", "2026", "2022"]:
        r = d[(d.year == yr) & d.p.str.contains(nav)]
        if len(r): print(nav, yr, r.nbim_vote.iloc[0], "|", r.rationale_text.iloc[0][:150])
