"""#2274 steg 2: hva skjer med F1 på MOT, presisjon og antall saker til menneske på test 2026 hvis grupper rutes til
menneske i stedet for automatisk MOT/FOR? Agenten er urørt: vi endrer bare hvilke rader som merkes «til menneske».
Tre lesninger per variant:
  A «maskin alene»: rutede saker svarer følg styret (anbefaling 0, konfidens 0,5) -> måler v3 --score mot (DET er tallet).
  B «menneske treffer»: rutede saker får fasit (øvre grense, mennesket antas feilfritt), regnet med målerens regler.
  C «bare automatiske»: F1 på MOT på de sakene som IKKE rutes (hva den automatiske delen leverer).
Bruk: python3 -I arbeid/oppgave_2274/ruting_varianter.py [--aar 2026|2025 --svar STI]  (2025: val-prediksjonene fra val_pred.py; båndvariantene finnes bare for 2026)
"""
import csv, hashlib, os, subprocess, re, sys
DATA = "state/opplastet/20261105_114241_real_votes.csv"
SHA = "71ba5135e7ba9d64c943f158bb510ffab53f34203f4c2875fc43352419e525e6"
SVAR = "arbeid/hack/levering/kjor_agent_real_maskin_alene.csv"
MED_RUTING = "arbeid/hack/levering/kjor_agent_real_pred_maaler.csv"
MAALER = "arbeid/hack/c1/maaler_offisiell_v3.py"
A = sys.argv[1:]
AAR = A[A.index("--aar") + 1] if "--aar" in A else "2026"
if "--svar" in A: SVAR = A[A.index("--svar") + 1]
VINDU = "test" if AAR == "2026" else "val"
UT = f"arbeid/oppgave_2274/varianter_{AAR}"; os.makedirs(UT, exist_ok=True)

def prf(tp, fp, fn):
    P = tp / (tp + fp) if tp + fp else 0.0; R = tp / (tp + fn) if tp + fn else 0.0
    return P, R, (2 * P * R / (P + R) if P + R else 0.0)

b = open(DATA, "rb").read(); assert hashlib.sha256(b).hexdigest() == SHA
F = {f"{f['meeting_id']}|{f['item_no']}": f for f in csv.DictReader(b.decode("utf-8").splitlines()) if f["year"] == AAR}
S = list(csv.DictReader(open(SVAR, encoding="utf-8-sig", newline="")))
band = {r["id"]: float(r["konfidens"]) < 0.6 for r in csv.DictReader(open(MED_RUTING, encoding="utf-8-sig", newline=""))} if AAR == "2026" else None

def er(f, land=None, typer=None):
    return (land is None or f["country"] in land) and (typer is None or f["proposal_type"] in typer)

VARIANTER = [
    ("V0 frossen, ingen ruting", lambda f, i: False),
    ("V0b frossen, bånd [0,15;0,85) (levert)", lambda f, i: band[i]),
    ("V1 styrevalg i USA -> menneske", lambda f, i: er(f, {"United States"}, {"DIRECTOR_ELECTION"})),
    ("V2 bånd + styrevalg i USA", lambda f, i: band[i] or er(f, {"United States"}, {"DIRECTOR_ELECTION"})),
    ("V3 alle saker i USA -> menneske", lambda f, i: er(f, {"United States"})),
    ("V4 styrevalg i DM -> menneske", lambda f, i: f["market"] == "DM" and er(f, None, {"DIRECTOR_ELECTION"})),
    ("V5 OTHER_MGMT + AUDITOR -> menneske", lambda f, i: er(f, None, {"OTHER_MGMT", "AUDITOR"})),
    ("V6 alle styrevalg -> menneske", lambda f, i: er(f, None, {"DIRECTOR_ELECTION"})),
]
rader = []
if band is None: VARIANTER = [v for v in VARIANTER if "bånd" not in v[0]]
for navn, rute in VARIANTER:
    fil = os.path.join(UT, re.sub(r"[^a-z0-9]+", "_", navn.lower()).strip("_") + ".csv")
    tpA = fpA = fnA = tpB = fpB = fnB = tpC = fpC = fnC = 0; nr = 0; n = 0
    with open(fil, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["id", "anbefaling", "konfidens", "p_avvik"])
        for s in S:
            i = s["id"]; f = F[i]; r = rute(f, i)
            w.writerow([i, "0" if r else s["anbefaling"], 0.5 if r else 0.9, s["p_avvik"]])
            if f["against_board"] == "": continue
            n += 1; nr += r
            styret = f["mgmt_rec"] or "FOR"; avv = s["anbefaling"].strip() == "1"
            a = ("FOR" if styret == "MOT" else "MOT") if avv else styret
            x = a == "MOT" and styret != "MOT"; y = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"
            if r:
                fnA += y                       # A: følg styret -> aldri MOT
                tpB += y                       # B: mennesket treffer
            else:
                tpA += x and y; fpA += x and not y; fnA += (not x) and y
                tpB += x and y; fpB += x and not y; fnB += (not x) and y
                tpC += x and y; fpC += x and not y; fnC += (not x) and y
    o = subprocess.run(["python3", "-I", MAALER, fil, VINDU, "--data", "real", "--score", "mot"], capture_output=True, text=True)
    sc = re.search(r"SCORE ([0-9.]+)", o.stdout); mm = re.search(r"MOT mot styret: TP (\d+) FP (\d+) FN (\d+)  P ([0-9.]+)", o.stdout)
    rt = re.search(r"ruting .*?: (\d+) til menneske", o.stdout)
    assert sc and mm, o.stdout + o.stderr
    PA, RA, FA = prf(tpA, fpA, fnA); PB, RB, FB = prf(tpB, fpB, fnB); PC, RC, FC = prf(tpC, fpC, fnC)
    assert abs(FA - float(sc.group(1))) < 1e-5, (navn, FA, sc.group(1))
    assert int(rt.group(1)) == nr
    rader.append((navn, nr, n, int(mm.group(1)), int(mm.group(2)), int(mm.group(3)), float(mm.group(4)), RA, float(sc.group(1)), PB, FB, tpC + fnC, PC, FC, os.path.relpath(fil, ".")))
print("| variant | til menneske | av | TP | FP | FN | presisjon A | treff A | **F1 A (måler v3)** | presisjon B | F1 B (menneske treffer) | MOT i fasit, automatisk | presisjon C | F1 C (bare automatiske) | fil |")
print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
for r in rader:
    print(f"| {r[0]} | {r[1]} ({r[1]/r[2]:.1%}) | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]:.3f} | {r[7]:.3f} | **{r[8]:.4f}** | {r[9]:.3f} | {r[10]:.4f} | {r[11]} | {r[12]:.3f} | {r[13]:.4f} | `{r[14]}` |")
