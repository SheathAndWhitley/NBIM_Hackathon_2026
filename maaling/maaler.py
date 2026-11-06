"""Måleren for Case 1 (bare standardbiblioteket). Fasit: NBIMs egne stemmer i data/real_votes.csv.

Bruk:  python3 -I maaling/maaler.py SVAR.csv VINDU [--score mot|avvik] [--terskel 0.6]
       python3 -I maaling/maaler.py baseline VINDU          (følg styret, alltid avvik, aksjonærforslag = MOT)
VINDU: test (= 2026), val (= 2025) eller yÅÅÅÅ, f.eks. y2024.
SVAR: id,anbefaling (FOR/MOT/AVSTÅ, eller 0/1 = avvik fra styret), valgfri konfidens [0,1] og p_avvik. id = meeting_id|item_no.
Hovedtallet er linja «MOT mot styret»: fasit = NBIM stemte MOT og against_board = 1; svaret teller når agenten
anbefaler MOT der styret ikke sier MOT. --score mot gjør F1 på den til SCORE (standard: avvik fra styret, AVSTÅ medregnet).
Rader uten against_board (styret ga ingen anbefaling) telles ikke. Konfidens under --terskel = sendt til menneske.
Datavakt: datafila må være arrangørens fil (fast sha256 og radantall), ellers exit 3. C1_DATA=STI bytter datafil.
Fasit- og begrunnelsesfeltene (LEKK) er aldri features.
"""
import csv, os, sys, math, hashlib
SCORE_MOT = False
HER = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.dirname(HER)
FILER = {"real": os.environ.get("C1_DATA", os.path.join(ROT, "data/real_votes.csv"))}
SHA = {"real": "71ba5135e7ba9d64c943f158bb510ffab53f34203f4c2875fc43352419e525e6"}  # arrangørens fil 05.11
RADER = {"real": 13757}
ALIAS = {"test": "y2026", "val": "y2025"}
LEKK = ["nbim_vote_raw", "nbim_vote", "against_board", "rationale_text", "rationale_section", "position_paper",
        "funds_disagree", "n_funds"]

def ugyldig(m): print("UGYLDIG:", m); print("SCORE nan"); sys.exit(1)
def rid(r): return f"{r['meeting_id']}|{r['item_no']}"
def vindu_av(r, data):
    if r.get("injection_flag") == "1": return "inj"
    y = int(r["year"]); return "y%d" % y  # vindu = årstall, f.eks. y2024
def datavakt(data):
    """Stopp (exit 3) hvis datafila ikke er arrangørens fil; skriv sha256 og radantall øverst."""
    sti = FILER[data]
    try: b = open(sti, "rb").read()
    except OSError as e: print(f"FEIL DATAFIL ({data}): kan ikke lese {sti}: {e}"); print("SCORE nan"); sys.exit(3)
    sha = hashlib.sha256(b).hexdigest()
    n = sum(1 for _ in csv.DictReader(b.decode("utf-8").splitlines()))
    print(f"DATA {data} {os.path.basename(sti)} sha256 {sha} rader {n}")
    if sha != SHA[data] or n != RADER[data]:
        print(f"FEIL DATAFIL ({data}): forventet sha256 {SHA[data]} og {RADER[data]} rader (arrangørens fil 05.11),")
        print(f"  fikk sha256 {sha} og {n} rader. Bruk den nye fila; gammel eller annen data gir tall som ikke kan sammenlignes.")
        print("SCORE nan"); sys.exit(3)

def les(data): return list(csv.DictReader(open(FILER[data], encoding="utf-8", newline="")))

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
    tp = fp = fn = 0; m = [0, 0, 0]; ms = [0, 0, 0]; par = []; rt = [0, 0]; n = 0; avst = [0, 0]
    for i, f in fas.items():
        s = S[i]; a = (s.get("anbefaling") or "").strip().upper()
        styret = f["mgmt_rec"] or "FOR"
        a = {"AGAINST": "MOT", "ABSTAIN": "AVSTÅ", "AVSTA": "AVSTÅ"}.get(a, a)
        if a in ("0", "1"):  # avvik -> agentens anbefaling, som i agent/kjerne.py
            avv = a == "1"; a = ("FOR" if styret == "MOT" else "MOT") if avv else styret; mot = a == "MOT"
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
            xs = mot and styret != "MOT"; ys = ym and y  # MOT mot styret
            ms[0] += xs and ys; ms[1] += xs and not ys; ms[2] += (not xs) and ys
        if f["nbim_vote"] == "AVSTÅ": avst[0] += 1; avst[1] += y
        par.append((p if p is not None else (k if avv else 1 - k), y))
        rt[0 if k < terskel else 1] += 1
    P, R, F1 = prf(tp, fp, fn); mP, mR, mF = prf(*m); sP, sR, sF = prf(*ms)
    print(f"[{navn or 'svar'}] data {data}, vindu {vindu}: {n} vurderte rader, {tp+fn} avvik fra styret, {ekstra} svarrader utenfor vinduet ignorert")
    print(f"  avvik: TP {tp} FP {fp} FN {fn}  P {P:.4f}  R {R:.4f}  F1 {F1:.4f}  PR-AUC {prauc(par):.4f}")
    print(f"  streng MOT: TP {m[0]} FP {m[1]} FN {m[2]}  P {mP:.4f}  R {mR:.4f}  F1 {mF:.4f}")
    print(f"  MOT mot styret: TP {ms[0]} FP {ms[1]} FN {ms[2]}  P {sP:.4f}  R {sR:.4f}  F1 {sF:.4f}  ({ms[0]+ms[2]} i fasit)")
    print(f"  AVSTÅ i fasit: {avst[0]} rader, {avst[1]} av dem er avvik fra styret")
    print(f"  ruting (konfidens < {terskel}): {rt[0]} til menneske ({rt[0]/max(n,1):.1%})")
    return sF if SCORE_MOT else F1

def les_svar(fil, data=None):
    """Godtar også radformatet «rad,p» (rad = radnummer i data-fila, p = sannsynlighet for avvik, avvik når p >= 0,5).
    Raden oversettes til id = meeting_id|item_no."""
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
    data = opt("--data", "real"); terskel = float(opt("--terskel", "0.6"))
    sc = opt("--score", "avvik")
    if sc not in ("avvik", "mot"): ugyldig("--score må være avvik eller mot")
    SCORE_MOT = sc == "mot"
    if data not in FILER: ugyldig("--data må være real")
    fil = opt("--fil", None)
    if fil: FILER[data] = os.path.abspath(fil)
    datavakt(data)
    if not a: print(__doc__); sys.exit(2)
    v = a[1] if len(a) > 1 else "val"
    v = ALIAS.get(v, v)
    if not v.startswith("y"): ugyldig(f"ukjent vindu {v} (test, val eller yÅÅÅÅ)")
    if a[0] == "baseline": baseline(data, v, terskel); sys.exit(0)
    F1 = maal(les_svar(a[0], data), v, data, terskel)
    print(f"SCORE {F1:.6f}"); print("RETNING maks")
