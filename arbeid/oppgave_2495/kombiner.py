"""#2495: repoets hybrid som første filter + frossen #2044-rangering for resten. Alle valg på val 2025, brukes uendret på test 2026.
Regel: h_score >= a -> MOT-flagg (hybriden sikker ja); h_score < b -> ikke flagg (hybriden sikker nei); ellers vår p_avvik >= t."""
import csv, itertools
B = "arbeid/oppgave_2103/"
REAL = "state/opplastet/20261105_114241_real_votes.csv"
H = {r["id"]: (float(r["h_score"]), int(r["h_flag"])) for r in csv.DictReader(open("hybrid.csv"))}
TF = min(s for s, f in H.values() if f)  # hybridens egen terskel
fas = {}
for f in csv.DictReader(open(REAL)):
    if f["against_board"] == "": continue
    fas[f"{f['meeting_id']}|{f['item_no']}"] = (f["mgmt_rec"] or "FOR", f["nbim_vote"] == "MOT" and f["against_board"] == "1.0")
def les(fil): return list(csv.DictReader(open(fil)))
def flagg(r, a, b, t):
    h = H[r["id"]][0]
    if h >= a: return True
    if h < b: return False
    return float(r["p_avvik"]) >= t
def f1(rows, a, b, t):
    tp = fp = fn = 0
    for r in rows:
        if r["id"] not in fas: continue
        st, y = fas[r["id"]]; fl = flagg(r, a, b, t)
        mm = (("FOR" if st == "MOT" else "MOT") if fl else st) == "MOT" and st != "MOT"
        tp += mm and y; fp += mm and not y; fn += y and not mm
    return 2 * tp / max(2 * tp + fp + fn, 1), tp, fp, fn
val, test = les(B + "full_val.csv"), les(B + "full_test.csv")
ts = sorted({round(float(r["p_avvik"]), 3) for r in val}) + [9.0]
hs = sorted({round(H[r["id"]][0], 3) for r in val})
bs = [0.0] + [hs[int(len(hs) * q)] for q in (0.2, 0.4, 0.5, 0.6, 0.7, 0.8)]
varianter = {
    "V1 hybridflagg ELLER vår p>=t": [(TF, 0.0, t) for t in ts],
    "V1p presedens ELLER vår p>=t": [(1.0, 0.0, t) for t in ts],
    "V2 hybrid sikker ja/nei, vår p i midten": [(a, b, t) for a in (TF, 1.0) for b in bs for t in ts if b < a],
}
res = {}
for navn, gitter in varianter.items():
    best = max(gitter, key=lambda g: (f1(val, *g)[0], -g[2]))
    v, te = f1(val, *best), f1(test, *best)
    res[navn] = best
    print(f"{navn}: a={best[0]:.4f} b={best[1]:.4f} t={best[2]}  val F1 {v[0]:.4f} (tp{v[1]} fp{v[2]} fn{v[3]})  test F1 {te[0]:.4f} (tp{te[1]} fp{te[2]} fn{te[3]})")
print("ref: hybrid alene val", "%.4f" % f1(val, TF, 0.0, 9.0)[0], "test", "%.4f" % f1(test, TF, 0.0, 9.0)[0])
for navn, (a, b, t) in res.items():
    fil = "svar_" + navn.split()[0] + "_t2026.csv"
    with open(fil, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["id", "anbefaling", "p_avvik"])
        for r in test:
            h = H[r["id"]][0]; p = float(r["p_avvik"])
            # konfidens: hybrid-avgjort -> hybridens score, ellers vår p
            w.writerow([r["id"], int(flagg(r, a, b, t)), min(h, 1.0) if (h >= a or h < b) else p])
    print("skrev", fil)
