# Teller TP/FP/FN for MOT mot styret (samme definisjon som velg.py/måler v3) delt på ruting, og skriver demosakenes linjer.
import csv, sys
ag = sys.argv[1]
fas = {f"{r['meeting_id']}|{r['item_no']}": r for r in csv.DictReader(open("state/opplastet/20261105_114241_real_votes.csv"))}
n = {}
for i, r in enumerate(csv.DictReader(open(ag)), start=2):
    f = fas.get(r["id"])
    if f is None or f["against_board"] == "": continue
    pm = r["anbefaling"] == "MOT" and r["styret"] != "MOT"
    ym = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"
    k = "TP" if pm and ym else "FP" if pm else "FN" if ym else "TN"
    rut = "menneske" if r["til_menneske"] == "1" else "maskin"
    n[(k, rut)] = n.get((k, rut), 0) + 1
    if i in (15, 89, 276): print("linje", i, r["id"], r["company"], "anbefaling", r["anbefaling"], "p_mot", r["p_mot"], "til_menneske", r["til_menneske"], "fasit", f["nbim_vote"], k)
for k in ("TP", "FP", "FN", "TN"):
    print(k, "maskin", n.get((k, "maskin"), 0), "menneske", n.get((k, "menneske"), 0))
