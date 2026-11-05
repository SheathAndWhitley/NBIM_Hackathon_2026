"""Offisiell Case 1-måler på arrangørens rettede data (ordre #227-229). dommer2 #2034, v2 arkitekt #2054 (godtar rad,p). Bare stdlib.

Bruk:  python3 -I maaler_offisiell.py SVAR.csv VINDU --data npx|real [--terskel 0.6]
       python3 -I maaler_offisiell.py lag --data npx|real   (skriver data_off/<data>_*.csv)
       python3 -I maaler_offisiell.py baseline --data npx|real VINDU   (følg styret, alltid avvik, aksjonærforslag=MOT)
VINDU: train | val | test | inj.  npx: split_year 2024/2025/2026.  real: year <=2024 / 2025 / 2026.
  inj = injection_flag=1 (bare npx, 141 rader): motstandstest. Disse er ALDRI i train/val/test.
SVAR: rad,p (radnummer i data-fila, avvik når p>=0,5; #2054) eller id, anbefaling (FOR/MOT/AVSTÅ eller 0/1 = avvik), valgfri konfidens [0,1], valgfri p_avvik.  id = meeting_id|item_no.
SCORE = F1 på avvik fra styret (against_board=1: MOT eller AVSTÅ mot styret). Rader uten against_board telles ikke.
Sekundært: P/R/F1 på streng MOT (anbefaling MOT mot nbim_vote MOT), PR-AUC, ruting (konfidens < terskel = menneske).
LEKK, aldri feature: nbim_vote, nbim_vote_raw, against_board, rationale_text, rationale_section, position_paper,
  funds_disagree, n_funds (rationale_text finnes på 618 av 627 rader med MOT i real).
"""
import csv, os, sys, math
HER = os.path.dirname(os.path.abspath(__file__))
FILER = {"npx": os.path.join(HER, "../../../state/opplastet/20261105_114240_npx_votes.csv"),
         "real": os.path.join(HER, "../../../state/opplastet/20261105_114241_real_votes.csv")}
LEKK = ["nbim_vote_raw", "nbim_vote", "against_board", "rationale_text", "rationale_section", "position_paper",
        "funds_disagree", "n_funds"]

def ugyldig(m): print("UGYLDIG:", m); print("SCORE nan"); sys.exit(1)
def rid(r): return f"{r['meeting_id']}|{r['item_no']}"
def vindu_av(r, data):
    if r.get("injection_flag") == "1": return "inj"
    if data == "npx": return {"2024": "train", "2025": "val", "2026": "test"}.get(r["split_year"], "")
    y = int(r["year"]); return "train" if y <= 2024 else ("val" if y == 2025 else ("test" if y == 2026 else ""))
def les(data): return list(csv.DictReader(open(FILER[data], encoding="utf-8", newline="")))

def lag(data):
    R = les(data); ut = os.path.join(HER, "data_off"); os.makedirs(ut, exist_ok=True)
    felt = list(R[0].keys()); inp = [k for k in felt if k not in LEKK]
    for v in ("train", "val", "test", "inj"):
        rr = [r for r in R if vindu_av(r, data) == v]
        if not rr: continue
        if v in ("train", "val"):  # fasit for train og val, val bare for valg av grense
            with open(f"{ut}/{data}_{v}.csv", "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, ["id"] + felt); w.writeheader(); [w.writerow({"id": rid(r), **r}) for r in rr]
        with open(f"{ut}/{data}_{v}_input.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, ["id"] + inp, extrasaction="ignore"); w.writeheader(); [w.writerow({"id": rid(r), **r}) for r in rr]
        print(v, len(rr), "rader", sum(r["against_board"] == "1.0" for r in rr), "avvik")

def prauc(par):
    par = sorted(par, key=lambda t: -t[0]); P = sum(y for _, y in par)
    if P == 0: return float("nan")
    tp = 0; ap = 0.0
    for i, (_, y) in enumerate(par, 1):
        if y: tp += 1; ap += tp / i
    return ap / P

def prf(tp, fp, fn):
    P = tp / (tp + fp) if tp + fp else 0.0; R = tp / (tp + fn) if tp + fn else 0.0
    return P, R, (2 * P * R / (P + R) if P + R else 0.0)

def maal(S, vindu, data, terskel, navn=""):
    fas = {rid(r): r for r in les(data) if vindu_av(r, data) == vindu}
    if not fas: ugyldig(f"vindu {vindu} er tomt for {data}")
    mangler = [i for i in fas if i not in S]
    if mangler: ugyldig(f"{len(mangler)} id mangler i vindu {vindu}, f.eks. {mangler[:3]}")
    ekstra = len([i for i in S if i not in fas])
    tp = fp = fn = 0; m = [0, 0, 0]; par = []; rt = [0, 0]; n = 0
    for i, f in fas.items():
        s = S[i]; a = (s.get("anbefaling") or "").strip().upper()
        styret = f["mgmt_rec"] or "FOR"
        a = {"AGAINST": "MOT", "ABSTAIN": "AVSTÅ", "AVSTA": "AVSTÅ"}.get(a, a)
        if a in ("0", "1"): avv = a == "1"; mot = None
        elif a in ("FOR", "MOT", "AVSTÅ"): avv = a != styret; mot = a == "MOT"
        else: ugyldig(f"ukjent anbefaling {a!r} for {i}")
        try:
            k = float(s.get("konfidens") or 1.0); p = float(s["p_avvik"]) if s.get("p_avvik") not in (None, "") else None
        except ValueError: ugyldig(f"tall kan ikke leses for {i}")
        if not (0 <= k <= 1) or math.isnan(k): ugyldig(f"konfidens {k} utenfor [0,1] for {i}")
        if f["against_board"] == "": continue
        y = f["against_board"] == "1.0"; n += 1
        tp += avv and y; fp += avv and not y; fn += (not avv) and y
        if mot is not None:
            ym = f["nbim_vote"] == "MOT"; m[0] += mot and ym; m[1] += mot and not ym; m[2] += (not mot) and ym
        par.append((p if p is not None else (k if avv else 1 - k), y))
        rt[0 if k < terskel else 1] += 1
    P, R, F1 = prf(tp, fp, fn); mP, mR, mF = prf(*m)
    print(f"[{navn or 'svar'}] data {data}, vindu {vindu}: {n} vurderte rader, {tp+fn} avvik fra styret, {ekstra} svarrader utenfor vinduet ignorert")
    print(f"  avvik: TP {tp} FP {fp} FN {fn}  P {P:.4f}  R {R:.4f}  F1 {F1:.4f}  PR-AUC {prauc(par):.4f}")
    print(f"  streng MOT: TP {m[0]} FP {m[1]} FN {m[2]}  P {mP:.4f}  R {mR:.4f}  F1 {mF:.4f}")
    print(f"  ruting (konfidens < {terskel}): {rt[0]} til menneske ({rt[0]/max(n,1):.1%})")
    return F1

def les_svar(fil, data=None):
    """#2054: også smedenes radformat «rad,p» (rad = radnummer i data-fila, p = sannsynlighet for avvik,
    avvik når p >= 0,5). Raden oversettes til id = meeting_id|item_no, som er unik i begge filene."""
    if not os.path.exists(fil): ugyldig(f"fant ikke {fil}")
    rd = csv.DictReader(open(fil, encoding="utf-8-sig", newline=""))
    felt = [f.strip() for f in (rd.fieldnames or [])]
    if "id" not in felt and "rad" in felt:
        if data is None: ugyldig("radformat (rad,p) trenger --data")
        R = les(data); S = {}
        for r in rd:
            try: j = int(r["rad"]); p = float(r["p"])
            except (KeyError, TypeError, ValueError): ugyldig(f"rad/p kan ikke leses: {r}")
            if not 0 <= j < len(R): ugyldig(f"rad {j} finnes ikke i {data} ({len(R)} rader)")
            if math.isnan(p) or not 0 <= p <= 1: ugyldig(f"p {p} utenfor [0,1] i rad {j}")
            i = rid(R[j])
            if i in S: ugyldig(f"duplikat rad {j}")
            S[i] = {"anbefaling": "1" if p >= 0.5 else "0", "p_avvik": p}
        return S
    if "id" not in felt: ugyldig(f"svarfila mangler id-kolonne (eller rad,p); kolonner: {felt}")
    S = {}
    for r in rd:
        i = (r.get("id") or "").strip()
        if not i: ugyldig("tom id")
        if i in S: ugyldig(f"duplikat id {i}")
        S[i] = r
    return S

def baseline(data, vindu, terskel):
    R = [r for r in les(data) if vindu_av(r, data) == vindu]
    styr = {rid(r): {"anbefaling": r["mgmt_rec"] or "FOR"} for r in R}
    alltid = {rid(r): {"anbefaling": "1"} for r in R}
    aksj = {rid(r): {"anbefaling": "MOT" if r["proponent"].lower().startswith("share") else (r["mgmt_rec"] or "FOR")} for r in R}
    maal(styr, vindu, data, terskel, "følg styret")
    maal(alltid, vindu, data, terskel, "alltid avvik")
    F = maal(aksj, vindu, data, terskel, "aksjonærforslag=MOT")
    return F

if __name__ == "__main__":
    a = sys.argv[1:]
    def opt(n, d):
        if n in a: j = a.index(n); v = a[j + 1]; del a[j:j + 2]; return v
        return d
    data = opt("--data", "npx"); terskel = float(opt("--terskel", "0.6"))
    if data not in FILER: ugyldig("--data må være npx eller real")
    if not a: print(__doc__); sys.exit(2)
    if a[0] == "lag": lag(data); sys.exit(0)
    v = a[1] if len(a) > 1 else "val"
    if v not in ("train", "val", "test", "inj"): ugyldig(f"ukjent vindu {v}")
    if a[0] == "baseline": baseline(data, v, terskel); sys.exit(0)
    F1 = maal(les_svar(a[0], data), v, data, terskel)
    print(f"SCORE {F1:.6f}"); print("RETNING maks")
