# Teller MOT mot styret per år og møter/selskaper i test 2026 (#2345, H6). Utskrift: kilder/tell_aar.txt.
# Kjør: python3 -I tell_aar.py [real_votes.csv]  (standard: landsbyens frosne datafil)
import csv, collections, sys
data = sys.argv[1] if len(sys.argv) > 1 else "state/opplastet/20261105_114241_real_votes.csv"
R = list(csv.DictReader(open(data, encoding="utf-8-sig")))
mot = collections.Counter(r["year"] for r in R if r["nbim_vote"] == "MOT" and r["against_board"] in ("1", "1.0"))
print(f"data: {data}, {len(R)} rader")
print("MOT mot styret per år (nbim_vote == MOT og against_board == 1):")
for aar in sorted(mot): print(f"  {aar}: {mot[aar]}")
t = [r for r in R if r["year"] == "2026"]
tf = [r for r in t if r["against_board"] != ""]
for navn, rr in (("test 2026, alle rader", t), ("test 2026, rader med fasit", tf)):
    print(f"{navn}: {len(rr)} saker, {len({r['meeting_id'] for r in rr})} møter, {len({r['company_id'] for r in rr})} selskaper")
