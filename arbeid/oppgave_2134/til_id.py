"""rad,p,mot_pred (train.py) -> id,anbefaling,p_avvik for alle test 2026-rader; rader uten prediksjon (uten fasit) får 0."""
import csv, sys
R = list(csv.DictReader(open("state/opplastet/20261105_114241_real_votes.csv", encoding="utf-8")))
P = {int(r["rad"]): r for r in csv.DictReader(open(sys.argv[1]))}
w = csv.writer(open(sys.argv[2], "w", newline="")); w.writerow(["id", "anbefaling", "p_avvik"])
for j, r in enumerate(R):
    if r.get("injection_flag") == "1" or int(r["year"]) != 2026: continue
    q = P.get(j); w.writerow([f"{r['meeting_id']}|{r['item_no']}", q["mot_pred"] if q else 0, q["p"] if q else 0.0])
