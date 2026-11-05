"""Hvor mye arbeid får mennesket, og hvor mange MOT fanger det? (smed2 #2377). Bare stdlib, modellen røres ikke.
Bruk: python3 -I arbeid/oppgave_2377/arbeidsmengde.py UTMAPPE [UTMAPPE ...]   (ut/ fra fremmed.sh med --baand LO,HI)
Fasit som måler v3 --score mot: test 2026, rader med against_board, ekte MOT = nbim_vote MOT og against_board 1.
Agentens MOT-flagg = maskin alene (_pred_uten_ruting.csv: anbefaling MOT der styret ikke sier MOT), samme fil som v3 måler.
Hver sak havner i én bunke: til menneske (til_menneske=1 i agent.csv), ellers auto MOT (flagget) eller auto FOR (resten).
"""
import csv, sys, os, re
FASIT = "state/opplastet/20261105_114241_real_votes.csv"
F = [r for r in csv.DictReader(open(FASIT, encoding="utf-8", newline=""))
     if r.get("injection_flag") != "1" and r["year"] == "2026" and r["against_board"] != ""]
k = lambda x: f"{x:.1f}".replace(".", ",")
print("| bånd P(MOT) | til menneske (per 100 saker) | ekte MOT: auto MOT (TP) / til menneske / auto FOR (FN) | falske flagg: auto / til menneske | F1 maskin alene (TP/FP/FN) | F1 hvis mennesket treffer på bunken | F1 hvis mennesket følger styret |")
print("|---|---|---|---|---|---|---|")
for d in sys.argv[1:]:
    A = {r["id"]: r for r in csv.DictReader(open(os.path.join(d, "agent.csv"), encoding="utf-8-sig", newline=""))}
    M = {r["id"]: r for r in csv.DictReader(open(os.path.join(d, "_pred_uten_ruting.csv"), encoding="utf-8-sig", newline=""))}
    baand = re.search(r"P\(MOT\) i \[([0-9.]+), ([0-9.]+)\)", open(os.path.join(d, "KJORING.txt"), encoding="utf-8").read())
    c = dict(tp_auto=0, mot_rut=0, fn_auto=0, fp_auto=0, fp_rut=0, rut=0, mot_rut_flagg=0, tp=0, fp=0, fn=0)
    for f in F:
        i = f"{f['meeting_id']}|{f['item_no']}"
        y = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"
        x = M[i]["anbefaling"] in ("MOT", "1") and (f["mgmt_rec"] or "FOR") != "MOT"
        r = A[i]["til_menneske"] == "1"
        c["rut"] += r; c["tp"] += x and y; c["fp"] += x and not y; c["fn"] += (not x) and y
        c["mot_rut_flagg"] += y and r and x
        if y: c["mot_rut" if r else ("tp_auto" if x else "fn_auto")] += 1
        elif x: c["fp_rut" if r else "fp_auto"] += 1
    f1 = lambda tp, fp, fn: 2 * tp / (2 * tp + fp + fn) if tp else 0.0
    n = len(F); nmot = c["tp_auto"] + c["mot_rut"] + c["fn_auto"]
    ovre = f1(c["tp_auto"] + c["mot_rut"], c["fp_auto"], c["fn_auto"])
    gulv = f1(c["tp_auto"], c["fp_auto"], c["mot_rut"] + c["fn_auto"])
    print(f"| [{baand.group(1)}; {baand.group(2)}) | {c['rut']} av {n} ({k(100 * c['rut'] / n)}) | "
          f"{c['tp_auto']} / {c['mot_rut']} ({c['mot_rut_flagg']} flagget) / {c['fn_auto']} av {nmot} | {c['fp_auto']} / {c['fp_rut']} | "
          f"{f1(c['tp'], c['fp'], c['fn']):.3f} ({c['tp']}/{c['fp']}/{c['fn']}) | {ovre:.3f} | {gulv:.3f} |".replace("0.", "0,"))
