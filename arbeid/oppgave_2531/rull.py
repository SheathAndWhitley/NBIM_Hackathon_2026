"""#2531: V2 (#2495) rullet ett år tilbake. Hybrid trent <=2022, valgt på 2023; a,b,t valgt på 2023; test én gang på 2024.
Vår p_avvik = frossen-oppsettet fra #2496 (full_2024_val = 2023, full_2024_test = 2024). Ikke hovedtall."""
import sys, pathlib, csv
REPO = pathlib.Path("arbeid/hack/CASE/20261105_155545_NBIM_Hackathon_2026-main_1__ut/NBIM_Hackathon_2026-main")
sys.path.insert(0, str(REPO / "src"))
from stemmeagent import ballot, ballot_model as bm
ballot.REAL_FILE = pathlib.Path("state/opplastet/20261105_114241_real_votes.csv")
ballot.SPLITS = [("train", "2019-01-01", "2022-12-31"), ("valid", "2023-01-01", "2023-12-31"), ("test", "2024-01-01", "2026-12-31")]
d = bm.add_model_columns(ballot.load_real())
lab = d[d["labelled"]]
tr, va = (lab[lab["split"] == s].copy() for s in ("train", "valid"))
m = bm.fit_select(tr, va)
print("hybrid valgt", m.name, "t_flag", m.t_flag)
d["id"] = d["meeting_id"].astype(str) + "|" + d["item_no"].astype(str)
sc = m.score(d, m.predict_proba(d))
H = dict(zip(d["id"], sc)); TF = m.t_flag
REAL = str(ballot.REAL_FILE)
fas = {}
for f in csv.DictReader(open(REAL)):
    if f["against_board"] == "": continue
    fas[f"{f['meeting_id']}|{f['item_no']}"] = (f["mgmt_rec"] or "FOR", f["nbim_vote"] == "MOT" and f["against_board"] == "1.0")
B = "arbeid/oppgave_2496/"
les = lambda fil: list(csv.DictReader(open(fil)))
val, test = les(B + "full_2024_val.csv"), les(B + "full_2024_test.csv")
def flagg(r, a, b, t):
    h = H[r["id"]]
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
ts = sorted({round(float(r["p_avvik"]), 3) for r in val}) + [9.0]
hs = sorted({round(H[r["id"]], 3) for r in val})
bs = [0.0] + [hs[int(len(hs) * q)] for q in (0.2, 0.4, 0.5, 0.6, 0.7, 0.8)]
varianter = {
    "V1 hybridflagg ELLER vår p>=t": [(TF, 0.0, t) for t in ts],
    "V1p presedens ELLER vår p>=t": [(1.0, 0.0, t) for t in ts],
    "V2 hybrid sikker ja/nei, vår p i midten": [(a, b, t) for a in (TF, 1.0) for b in bs for t in ts if b < a],
}
for navn, gitter in varianter.items():
    best = max(gitter, key=lambda g: (f1(val, *g)[0], -g[2]))
    v, te = f1(val, *best), f1(test, *best)
    print(f"{navn}: a={best[0]:.4f} b={best[1]:.4f} t={best[2]}  val2023 F1 {v[0]:.4f} (tp{v[1]} fp{v[2]} fn{v[3]})  test2024 F1 {te[0]:.4f} (tp{te[1]} fp{te[2]} fn{te[3]})")
    fil = "svar_" + navn.split()[0] + "_t2024.csv"
    with open(fil, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["id", "anbefaling", "p_avvik"])
        for r in test: w.writerow([r["id"], int(flagg(r, *best)), r["p_avvik"]])
print("ref hybrid alene: val2023 %.4f test2024 %.4f" % (f1(val, TF, 0.0, 9.0)[0], f1(test, TF, 0.0, 9.0)[0]))
print("ref frossen alene (p>=t valgt 2023): ", end="")
bt = max(ts, key=lambda t: (f1(val, 9e9, 0.0, t)[0], -t)); print("t", bt, "val2023 %.4f test2024 %s" % (f1(val, 9e9, 0.0, bt)[0], f1(test, 9e9, 0.0, bt)))
