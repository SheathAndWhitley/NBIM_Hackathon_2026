"""F1 per variant: agent.csv fra /tmp/inj2212 -> id,anbefaling (B-id mappes tilbake -900000000) -> maaler_offisiell_v3 test --data real."""
import csv, glob, os, subprocess, re
for d in sorted(glob.glob("/tmp/inj2212/*/")):
    ut = d + "svar_off.csv"
    with open(ut, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "anbefaling"])
        for r in csv.DictReader(open(d + "agent.csv", encoding="utf-8")):
            m, i = r["id"].split("|"); m = int(m); m = m - 900000000 if m > 900000000 else m
            w.writerow([f"{m}|{i}", r["anbefaling"] if r["anbefaling"] in ("FOR", "MOT", "AVSTÅ") else r["styret"] if "styret" in r else "FOR"])
    o = subprocess.run(["python3", "-I", "arbeid/hack/c1/maaler_offisiell_v3.py", ut, "test", "--data", "real"], capture_output=True, text=True)
    s = o.stdout + o.stderr
    sc = re.search(r"SCORE[^\n]*", s); ms = re.search(r"MOT mot styret:[^\n]*", s)
    print(os.path.basename(d.rstrip("/")), "|", sc.group(0) if sc else s[-300:], "|", ms.group(0) if ms else "")
