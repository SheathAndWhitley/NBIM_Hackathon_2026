"""Svartid for Case 1-agenten (#2259): 100 saker fra test 2026 (frø 0), hver kjørt alene som egen prosess,
pluss én samlet kjøring av de samme 100. Nettet er sperret med sandbox-exec (deny network*): en sak som
trenger nettet feiler da med rc != 0. Ingen fasit leses.

    python3 -I arbeid/oppgave_2259/svartid.py [--n 100] [--ut arbeid/oppgave_2259/ut]
"""
import csv, os, random, statistics, subprocess, sys, time
HER = os.path.dirname(os.path.abspath(__file__)); ROT = os.path.abspath(os.path.join(HER, "../.."))
PY = os.path.join(ROT, "arbeid/kandidater/smed2_c1_mot/.venv/bin/python")
AGENT = os.path.join(ROT, "arbeid/hack/levering/kjor_agent.py")
INN = os.path.join(ROT, "arbeid/hack/c1/data_off/real_test_input.csv")
N = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 100
UT = os.path.abspath(sys.argv[sys.argv.index("--ut") + 1]) if "--ut" in sys.argv else os.path.join(HER, "ut")
SANDKASSE = ["sandbox-exec", "-p", "(version 1)(allow default)(deny network*)"]


def kjor(inn, ut):
    t0 = time.time()
    o = subprocess.run(SANDKASSE + [PY, AGENT, "--csv", inn, "--ut", ut], capture_output=True, text=True, cwd=ROT)
    return o.returncode, time.time() - t0, (o.stderr or "").strip()[-300:]


if __name__ == "__main__":
    rader = list(csv.DictReader(open(INN, encoding="utf-8"))); felt = list(rader[0].keys())
    utvalg = random.Random(0).sample(rader, N)
    os.makedirs(f"{UT}/saker", exist_ok=True)
    def skriv(sti, rr):
        with open(sti, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=felt); w.writeheader(); w.writerows(rr)
    res = []
    for i, r in enumerate(utvalg):
        sti = f"{UT}/saker/{i:03d}.csv"; skriv(sti, [r])
        rc, sek, err = kjor(sti, f"{UT}/en/{i:03d}")
        ok = rc == 0 and os.path.exists(f"{UT}/en/{i:03d}/agent.csv")
        res.append((i, r["id"], rc, sek, ok, err.splitlines()[-1] if (err and not ok) else ""))
        print(i, r["id"], rc, f"{sek:.2f}s", "ok" if ok else "FEIL " + res[-1][5], flush=True)
    skriv(f"{UT}/alle.csv", utvalg)
    rc_s, sek_s, err_s = kjor(f"{UT}/alle.csv", f"{UT}/samlet")
    n_s = len(list(csv.DictReader(open(f"{UT}/samlet/agent.csv")))) if rc_s == 0 else 0
    with open(f"{UT}/svartid.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t"); w.writerow(["nr", "id", "rc", "sek", "ok", "feil"]); w.writerows(res)
    s = [x[3] for x in res]; verst = max(res, key=lambda x: x[3])
    print(f"\nENKELTSAKER n={N}: ok {sum(x[4] for x in res)}/{N}, snitt {statistics.mean(s):.2f} s, "
          f"median {statistics.median(s):.2f} s, verste {verst[3]:.2f} s ({verst[1]}), beste {min(s):.2f} s")
    print(f"SAMLET: rc {rc_s}, {n_s} rader, {sek_s:.1f} s totalt = {sek_s / N:.3f} s per sak {err_s[-200:] if rc_s else ''}")
