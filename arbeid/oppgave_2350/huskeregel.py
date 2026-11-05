"""#2350 Huskeregel-grunnlinje for Case 1 (smed2). Bare stdlib, ingen trening, ingen modellvalg.
Regel (fast, valgt før måling): for hver rad, finn SISTE tidligere møte (meeting_date strengt før radens)
med samme nøkkel der NBIM har en kjent stemme. Stem MOT hvis NBIM der stemte MOT mot styret
(nbim_vote MOT og against_board 1) på minst én sak med den nøkkelen; ellers følg styret (mgmt_rec, tom = FOR).
  A: nøkkel = (company_id, proposal_type)    B: nøkkel = company_id (hvilken som helst sak)
Historikken er alle år (løpende, samme antagelse som hovedmodellen), aldri samme møte eller senere.
Bruk (fra landsbymappen):  python3 -I arbeid/oppgave_2350/huskeregel.py [UTMAPPE]
Skriver UTMAPPE/regel_{A,B}_{val,test}.csv og måler dem med måler v3 --score mot (+ frossen #2044 side om side)."""
import csv, os, sys, subprocess
from collections import defaultdict
LAND = "."
DATA = f"{LAND}/state/opplastet/20261105_114241_real_votes.csv"
MAALER = f"{LAND}/arbeid/hack/c1/maaler_offisiell_v3.py"
FROSSEN = {"val": f"{LAND}/arbeid/oppgave_2103/full_val.csv", "test": f"{LAND}/arbeid/oppgave_2103/full_test.csv"}
ut = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
os.makedirs(ut, exist_ok=True)
R = list(csv.DictReader(open(DATA, encoding="utf-8", newline="")))
NOKKEL = {"A": lambda r: (r["company_id"], r["proposal_type"]), "B": lambda r: r["company_id"]}

def regel(nk):
    # hist[nøkkel][dato] = True hvis minst én MOT mot styret det møtet (bare rader med kjent stemme)
    hist = defaultdict(dict)
    for r in R:
        if r["nbim_vote"] == "": continue
        d = hist[nk(r)]; d[r["meeting_date"]] = d.get(r["meeting_date"], False) or (r["nbim_vote"] == "MOT" and r["against_board"] == "1.0")
    pred = {}
    for r in R:
        tidl = [dt for dt in hist.get(nk(r), {}) if dt < r["meeting_date"]]
        styret = r["mgmt_rec"] or "FOR"
        mot = bool(tidl) and hist[nk(r)][max(tidl)] and styret != "MOT"
        pred[f"{r['meeting_id']}|{r['item_no']}"] = ("MOT" if mot else styret, int(r["year"]))
    return pred

for navn, nk in NOKKEL.items():
    p = regel(nk)
    for vindu, aar in (("val", 2025), ("test", 2026)):
        with open(f"{ut}/regel_{navn}_{vindu}.csv", "w", newline="") as f:
            w = csv.writer(f); w.writerow(["id", "anbefaling", "konfidens"])
            for i, (a, y) in p.items():
                if y == aar: w.writerow([i, a, 1.0])

def maal(fil, vindu):
    o = subprocess.run([sys.executable, "-I", MAALER, fil, vindu, "--data", "real", "--score", "mot"], capture_output=True, text=True).stdout
    data = next(l for l in o.splitlines() if l.startswith("DATA")).split()[4][:10]
    linje = next(l for l in o.splitlines() if "MOT mot styret" in l).split()
    tall = dict(zip(linje[3::2], linje[4::2]))  # TP FP FN P R F1
    return data, tall

print("| Variant | Vindu | F1 MOT | P | R | TP | FP | FN | data sha |")
print("|---|---|---|---|---|---|---|---|---|")
for navn, fil in (("A samme selskap + sakstype", "regel_A"), ("B samme selskap, alle saker", "regel_B"), ("frossen #2044 miks h2", None)):
    for vindu in ("val", "test"):
        f = FROSSEN[vindu] if fil is None else f"{ut}/{fil}_{vindu}.csv"
        sha, t = maal(f, vindu)
        print(f"| {navn} | {vindu} | {float(t['F1']):.4f} | {float(t['P']):.4f} | {float(t['R']):.4f} | {t['TP']} | {t['FP']} | {t['FN']} | {sha} |")

# Parret klyngebootstrap (selskap, 2000 trekk, seed 0) av frossen minus regel, med #2103 diff_ki.py (vil ha 0/1 = avvik).
st = {f"{r['meeting_id']}|{r['item_no']}": (r["mgmt_rec"] or "FOR") for r in R}
print("\nDiff frossen #2044 minus regel (parret klyngebootstrap, arbeid/oppgave_2103/diff_ki.py):")
for navn in "AB":
    for vindu in ("val", "test"):
        f01 = f"{ut}/ki_{navn}_{vindu}.csv"
        rows = list(csv.DictReader(open(f"{ut}/regel_{navn}_{vindu}.csv")))
        with open(f01, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["id", "anbefaling"])
            for r in rows: w.writerow([r["id"], int(r["anbefaling"] != st[r["id"]])])
        o = subprocess.run([sys.executable, "-I", f"{LAND}/arbeid/oppgave_2103/diff_ki.py", f01, FROSSEN[vindu], vindu],
                           capture_output=True, text=True, cwd=LAND).stdout.strip().splitlines()[-1]
        print(f"  regel {navn} {o}")
