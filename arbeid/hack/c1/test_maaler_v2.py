"""Test for #2054: maaler_offisiell_v2 godtar smedenes rad,p-format, og forsok-vakt --id måler
et forsøk på nytt etter en feilet automåling. Kjør: python3 -I arbeid/hack/c1/test_maaler_v2.py"""
import os, subprocess, sys, tempfile, csv
ROT = "."
V2 = f"{ROT}/arbeid/hack/c1/maaler_offisiell_v2.py"
T2 = f"{ROT}/arbeid/oppgave_2023/m_real_t2.csv"

def kjor(*a):
    p = subprocess.run([sys.executable, "-I", V2, *a], capture_output=True, text=True)
    return p.returncode, p.stdout

def score(ut): return float([l for l in ut.splitlines() if l.startswith("SCORE")][-1].split()[1])

# 1) rad,p på test 2026 gir smed2s tall (maaler_ny.py: 0,4810)
rc, ut = kjor(T2, "test", "--data", "real"); assert rc == 0, ut
assert abs(score(ut) - 0.481013) < 1e-5, ut
# 2) id-formatet virker som før, og duplikat rad / tom id er fortsatt UGYLDIG
d = tempfile.mkdtemp()
R = list(csv.DictReader(open(f"{ROT}/state/opplastet/20261105_114241_real_votes.csv")))
with open(f"{d}/id.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "anbefaling"])
    [w.writerow([f"{r['meeting_id']}|{r['item_no']}", r["mgmt_rec"] or "FOR"]) for r in R]
rc, ut = kjor(f"{d}/id.csv", "test", "--data", "real"); assert rc == 0 and score(ut) == 0.0, ut
open(f"{d}/dup.csv", "w").write("rad,p\n0,0.1\n0,0.2\n")
rc, ut = kjor(f"{d}/dup.csv", "test", "--data", "real"); assert rc == 1 and "duplikat rad" in ut, ut
open(f"{d}/tom.csv", "w").write("id,anbefaling\n,FOR\n")
rc, ut = kjor(f"{d}/tom.csv", "test", "--data", "real"); assert rc == 1 and "tom id" in ut, ut
# 3) tavla: feilmerket fra en gammel automåling fjernes ved forsok-vakt --id
sys.path.insert(0, ROT); import tavle
n = "x [automål feilet: UGYLDIG (exit 1): UGYLDIG: duplikat id \nSCORE nan\n]"
assert tavle.FEILET_RE.sub("", n).strip() == "x"
print("OK test_maaler_v2")
