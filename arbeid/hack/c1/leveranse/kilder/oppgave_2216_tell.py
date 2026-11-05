# Teller TP/FP/FN på MOT mot styret per forslagskilde og ruting, frossen agent (kald kjøring /tmp/c1_kald).
import csv, collections, sys
ut = sys.argv[1] if len(sys.argv) > 1 else "/tmp/c1_kald/ut"
D = {f"{r['meeting_id']}|{r['item_no']}": r for r in csv.DictReader(open(f"{ut}/_data/data.csv"))}
A = list(csv.DictReader(open(f"{ut}/agent.csv")))
c = collections.Counter(); n = 0; rut = 0
for a in A:
    r = D.get(a["id"])
    if not r or r["nbim_vote"] not in ("FOR", "MOT", "AVSTÅ", "AVSTA") and not r["nbim_vote"]: continue
    if r["nbim_vote"] == "" or r.get("injection_flag") == "1": continue
    n += 1
    y = r["nbim_vote"] == "MOT" and r["against_board"] in ("1", "1.0")
    p = a["mot_styret"] == "1"
    kilde = "aksjonaer" if r["proponent"].lower().startswith("share") else "styret"
    k = "TP" if y and p else "FP" if p else "FN" if y else "TN"
    m = a["til_menneske"] == "1"; rut += m
    c[(kilde, k, m)] += 1
print("rader med fasit", n, "rutet", rut)
for kilde in ("styret", "aksjonaer"):
    for k in ("TP", "FP", "FN", "TN"):
        print(kilde, k, "maskin", c[(kilde, k, False)], "menneske", c[(kilde, k, True)])
print("proponent-verdier", collections.Counter(D[a['id']]['proponent'] for a in A if a['id'] in D))
