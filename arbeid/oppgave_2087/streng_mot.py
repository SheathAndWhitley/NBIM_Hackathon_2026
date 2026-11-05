"""#2087: F1 på bare MOT for den frosne modellen (#2044 miks h2), val 2025 og test 2026, med måler v3.
Kjører arbeid/oppgave_2044/train.py UENDRET (runpy, som c1_real.py), skriver id,anbefaling(0/1),p_avvik for hele
vinduet (rader modellen ikke vurderer = følg styret, 0) og måler med maaler_offisiell_v3.py. Ingen valg gjøres her.
Bruk: .venv/bin/python arbeid/oppgave_2087/streng_mot.py"""
import csv, io, os, runpy, sys, subprocess, contextlib
HER = os.path.dirname(os.path.abspath(__file__)); ARB = os.path.dirname(HER)
REAL = os.path.join(os.path.dirname(ARB), "state/opplastet/20261105_114241_real_votes.csv")
TRAIN = os.path.join(ARB, "oppgave_2044/train.py"); MAALER = os.path.join(ARB, "hack/c1/maaler_offisiell_v3.py")
sys.argv = [TRAIN, REAL, "--variant", "miks", "--hist", "2", "--ut", os.path.join(HER, "_pred_test_train.csv")]
buf = io.StringIO()
with contextlib.redirect_stdout(buf): g = runpy.run_path(TRAIN, run_name="smed2_2044")
print("\n".join(x for x in buf.getvalue().splitlines() if x.startswith(("VAL", "TEST 2026 (rå"))))
d, t, va, te = g["d"], float(g["t"]), g["va"], g["te"]
ids = (d.meeting_id.astype("Int64").astype(str) + "|" + d.item_no.astype("Int64").astype(str)).values
pred = {"val": dict(zip(ids[va], g["pv"])), "test": dict(zip(ids[te], g["p"][te]))}
R = list(csv.DictReader(open(REAL, encoding="utf-8")))
for v, aar in (("val", "2025"), ("test", "2026")):
    fil = os.path.join(HER, f"svar_{v}.csv")
    with open(fil, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "anbefaling", "konfidens", "p_avvik"])
        for r in R:
            if r["year"] != aar or r["injection_flag"] == "1": continue
            i = f"{r['meeting_id']}|{r['item_no']}"; p = pred[v].get(i)
            w.writerow([i, int(p is not None and p >= t), 0.9, 0.0 if p is None else round(float(p), 6)])
    print(f"=== {v} {aar}: {fil}")
    print(subprocess.run(["python3", "-I", MAALER, fil, v, "--data", "real", "--score", "mot"],
                         capture_output=True, text=True).stdout.strip())
