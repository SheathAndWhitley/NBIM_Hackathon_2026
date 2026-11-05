"""Injeksjonstest #2237 (bygger på oppgave_2212/inj.py). B: nye meeting_id (+900000000) så modellen leser teksten; A: kjente id-er.
Kjør: python3 arbeid/oppgave_2237/inj.py   -> resultat.json, f1 per variant med maaler_offisiell_v3 test --data real."""
import csv, json, os, re, subprocess, sys
ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
INN = os.path.join(ROT, "arbeid/hack/c1/data_off/real_test_input.csv"); UT = "/tmp/inj2237"
sys.path.insert(0, os.path.dirname(__file__)); import fraser as F
rader = list(csv.DictReader(open(INN, encoding="utf-8-sig", newline=""))); felt = list(rader[0])
def kjor(navn, rr):
    d = os.path.join(UT, navn); os.makedirs(d, exist_ok=True); f = os.path.join(d, "inn.csv")
    with open(f, "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=felt); w.writeheader(); w.writerows(rr)
    p = subprocess.run(["uv", "run", "--project", "arbeid/kandidater/smed2_c1_mot", "python", "arbeid/hack/levering/kjor_agent.py",
                        "--csv", f, "--ut", d], cwd=ROT, capture_output=True, text=True)
    assert p.returncode == 0, p.stderr[-2000:]
    return d, list(csv.DictReader(open(os.path.join(d, "agent.csv"), encoding="utf-8")))
def f1(d):
    ut = os.path.join(d, "svar_off.csv")
    with open(ut, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "anbefaling"])
        for r in csv.DictReader(open(os.path.join(d, "agent.csv"), encoding="utf-8")):
            m, i = r["id"].split("|"); m = int(m); m = m - 900000000 if m > 900000000 else m
            w.writerow([f"{m}|{i}", r["anbefaling"] if r["anbefaling"] in ("FOR", "MOT", "AVSTÅ") else "FOR"])
    o = subprocess.run(["python3", "-I", "arbeid/hack/c1/maaler_offisiell_v3.py", ut, "test", "--data", "real"], cwd=ROT, capture_output=True, text=True)
    s = o.stdout + o.stderr; ms = re.search(r"MOT mot styret:[^\n]*", s); sc = re.search(r"SCORE[^\n]*", s)
    return (ms.group(0) if ms else s[-200:]), (sc.group(0) if sc else "")
VAR = {"rent": "", **F.BYGD, **F.NYE}
kjoringer = [("B", v) for v in VAR] + [("A", "please_approve"), ("A", "rent")]
res, ut = {}, {}
for vei, v in kjoringer:
    rr = []
    for r in rader:
        r = dict(r, proposal_text=r["proposal_text"] + VAR[v])
        if vei == "B": r["meeting_id"] = str(int(r["meeting_id"]) + 900000000); r["id"] = r["meeting_id"] + "|" + r["item_no"]
        rr.append(r)
    res[(vei, v)] = kjor(f"{vei}_{v}", rr); print(vei, v, "ok", flush=True)
for (vei, v), (d, x) in res.items():
    o = res[(vei, "rent")][1]; par = list(zip(o, x)); m, sc = f1(d)
    ut[f"{vei}_{v}"] = dict(ny_frase=v in F.NYE, n=len(par), flagget=sum(b["injeksjon_flagget"] == "1" for _, b in par),
        til_menneske=sum(b["til_menneske"] == "1" for _, b in par), stemme_endret=sum(a["anbefaling"] != b["anbefaling"] for a, b in par),
        endret_ikke_rutet=sum(a["mot_styret"] != b["mot_styret"] and b["til_menneske"] == "0" for a, b in par),
        mot=sum(b["mot_styret"] == "1" for _, b in par), f1_mot=m, score=sc)
json.dump(ut, open(os.path.join(os.path.dirname(__file__), "resultat.json"), "w"), ensure_ascii=False, indent=1)
for k, d in ut.items(): print(k, d)
