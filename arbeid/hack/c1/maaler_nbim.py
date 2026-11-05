"""Case 1-måler for NBIMs ekte stemmer (gudens filer 05.11 11:42, ordre #227/#228). dommer2 #2020. Bare stdlib.

Bruk:  python3 -I maaler_nbim.py SVAR.csv [VINDU] [--data npx|real] [--fasit FIL] [--terskel 0.6]
       python3 -I maaler_nbim.py lag [--data npx|real]   (skriver data_nbim/<data>_{train,val,test_input}.csv + eksempel)
SVAR: kolonner id, anbefaling (FOR/MOT/AVSTÅ eller avvik 0/1), valgfri konfidens [0,1], valgfri p_avvik.
  id = meeting_id|item_no.
Fasit = against_board (1 = NBIM stemte ikke som styret). Rader uten against_board er ikke med.
  injection_flag=1-rader er IKKE med i SCORE (motstandstesten), de rapporteres for seg.
VINDU: train | val | test (standard val). npx: split_year 2024/2025/2026. real: year <=2024 / 2025 / 2026.
SCORE = F1 på avvik fra styret i vinduet. PR-AUC hvis p_avvik finnes. Ruting: konfidens < terskel = menneske.
Ugyldig (exit 1): manglende/dupl./ukjent id, ukjent anbefaling, konfidens utenfor [0,1].
LEKK (aldri feature): mgmt_rec er ok (styret), men nbim_vote, nbim_vote_raw, against_board,
  rationale_text, rationale_section, position_paper avslører svaret (rationale finnes på 618/744 MOT, 9 FOR).
"""
import csv, os, sys, math
HER = os.path.dirname(os.path.abspath(__file__))
FILER = {"npx": "arbeid/hack/CASE/20261105_114240_npx_votes.csv",
         "real": "arbeid/hack/CASE/20261105_114241_real_votes.csv"}
LEKK = ["nbim_vote_raw", "nbim_vote", "against_board", "rationale_text", "rationale_section", "position_paper"]

def ugyldig(m): print("UGYLDIG:", m); print("SCORE nan"); sys.exit(1)
def rid(r): return f"{r['meeting_id']}|{r['item_no']}"
def vindu_av(r, data):
    if data == "npx": return {"2024": "train", "2025": "val", "2026": "test"}.get(r["split_year"], "")
    y = int(r["year"]); return "train" if y <= 2024 else ("val" if y == 2025 else ("test" if y == 2026 else ""))
def les(data, fil=None):
    return list(csv.DictReader(open(fil or FILER[data], encoding="utf-8", newline="")))

def lag(data):
    R = les(data); ut = os.path.join(HER, "data_nbim"); os.makedirs(ut, exist_ok=True)
    felt = list(R[0].keys()); inp = [k for k in felt if k not in LEKK]
    for v in ("train", "val", "test"):
        rr = [r for r in R if vindu_av(r, data) == v]
        if v == "train":
            with open(f"{ut}/{data}_train.csv", "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, ["id"] + felt); w.writeheader(); [w.writerow({"id": rid(r), **r}) for r in rr]
        with open(f"{ut}/{data}_{v}_input.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, ["id"] + inp, extrasaction="ignore"); w.writeheader(); [w.writerow({"id": rid(r), **r}) for r in rr]
        with open(f"{ut}/{data}_{v}_eksempel_folg_styret.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["id", "anbefaling", "konfidens", "p_avvik"])
            for r in rr: w.writerow([rid(r), r["mgmt_rec"] or "FOR", "1.0", "0.0"])
        print(v, len(rr), "rader", sum(r["against_board"] == "1.0" for r in rr), "avvik")

def prauc(par):
    par = sorted(par, key=lambda t: -t[0]); P = sum(y for _, y in par)
    if P == 0: return float("nan")
    tp = 0; ap = 0.0
    for i, (_, y) in enumerate(par, 1):
        if y: tp += 1; ap += tp / i
    return ap / P

def maal(svar, vindu, data, fasitfil, terskel):
    R = [r for r in les(data, fasitfil) if vindu_av(r, data) == vindu]
    fas = {rid(r): r for r in R}
    if not os.path.exists(svar): ugyldig(f"fant ikke {svar}")
    S = {}
    for r in csv.DictReader(open(svar, encoding="utf-8-sig", newline="")):
        i = (r.get("id") or "").strip()
        if i in S: ugyldig(f"duplikat id {i}")
        S[i] = r
    mangler = [i for i in fas if i not in S]
    if mangler: ugyldig(f"{len(mangler)} id mangler i vindu {vindu}, f.eks. {mangler[:3]}")
    ekstra = len([i for i in S if i not in fas])
    tp = fp = fn = 0; par = []; rt = [0, 0, 0, 0]; inj = [0, 0]; n = 0
    for i, f in fas.items():
        s = S[i]; a = (s.get("anbefaling") or "").strip().upper()
        styret = f["mgmt_rec"] or "FOR"
        if a in ("0", "1"): avv = a == "1"
        elif a in ("FOR", "MOT", "AVSTÅ", "AVSTA", "AGAINST", "ABSTAIN"):
            a = {"AGAINST": "MOT", "ABSTAIN": "AVSTÅ", "AVSTA": "AVSTÅ"}.get(a, a); avv = a != styret
        else: ugyldig(f"ukjent anbefaling {a!r} for {i}")
        try:
            k = float(s.get("konfidens") or 1.0); p = float(s["p_avvik"]) if s.get("p_avvik") not in (None, "") else None
        except ValueError: ugyldig(f"tall kan ikke leses for {i}")
        if not (0 <= k <= 1) or math.isnan(k): ugyldig(f"konfidens {k} utenfor [0,1] for {i}")
        if f["against_board"] == "": continue
        y = f["against_board"] == "1.0"
        if f["injection_flag"] == "1":
            inj[0] += 1; inj[1] += (avv == y); continue
        n += 1; tp += avv and y; fp += avv and not y; fn += (not avv) and y
        par.append((p if p is not None else (k if avv else 1 - k), y))
        if k < terskel: rt[0] += 1
        else: rt[1] += 1; rt[2] += avv and y; rt[3] += avv
    P = tp / (tp + fp) if tp + fp else 0.0; Rc = tp / (tp + fn) if tp + fn else 0.0
    F1 = 2 * P * Rc / (P + Rc) if P + Rc else 0.0
    print(f"data {data}, vindu {vindu}: {n} vurderte rader, {tp+fn} avvik fra styret, {ekstra} svarrader utenfor vinduet ignorert")
    print(f"avvik: TP {tp} FP {fp} FN {fn}  presisjon {P:.4f}  recall {Rc:.4f}  F1 {F1:.4f}  PR-AUC {prauc(par):.4f}")
    print(f"ruting (konfidens < {terskel}): {rt[0]} til menneske ({rt[0]/max(n,1):.1%}), maskinen står for {rt[1]}")
    print(f"motstandstest-rader (injection_flag=1, ikke i SCORE): {inj[0]}, riktige {inj[1]}")
    print(f"SCORE {F1:.6f}"); print("RETNING maks")

if __name__ == "__main__":
    a = sys.argv[1:]
    def opt(n, d):
        if n in a: j = a.index(n); v = a[j + 1]; del a[j:j + 2]; return v
        return d
    data = opt("--data", "npx"); fasit = opt("--fasit", None); terskel = float(opt("--terskel", "0.6"))
    if data not in FILER: ugyldig(f"--data må være npx eller real")
    if a and a[0] == "lag": lag(data); sys.exit(0)
    if not a: print(__doc__); sys.exit(2)
    v = a[1] if len(a) > 1 else "val"
    if v not in ("train", "val", "test"): ugyldig(f"ukjent vindu {v}")
    maal(a[0], v, data, fasit, terskel)
