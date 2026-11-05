"""Før (#2063/#2071-tabellen) mot nå (#2380 kald kopi): én rad per testtype med utfall krasj/ok/rutet til menneske."""
import sys
def les(f):
    d = {}
    for l in open(f, encoding="utf-8"):
        if not l.startswith("| ") or l.startswith("| test"): continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        d[c[0]] = dict(inn=int(c[1]), ut=int(c[2]), krasj=c[3], mot=int(c[4]), men=int(c[6]), ugr=int(c[7]), merk=c[9])
    return d
def utfall(r):
    if r["krasj"] != "nei": return "KRASJ"
    if r["inn"] == 0: return "ok (0 saker, tom fil)"
    if r["men"] == r["ut"]: return f"rutet til menneske ({r['men']}/{r['ut']})"
    if r["men"] == 0: return f"ok, svar uten ruting ({r['mot']} MOT)"
    return f"ok, {r['men']}/{r['ut']} til menneske, {r['mot']} MOT"
F, N = les(sys.argv[1]), les(sys.argv[2])
print("| testtype | saker | før (#2063/#2071, landsbymiljø) | nå (#2380, kald kopi) | likt |")
print("|---|---|---|---|---|")
likt = 0
for t in F:
    f, n = F[t], N.get(t)
    if n is None: print(f"| {t} | {f['inn']} | {utfall(f)} | (ikke kjørt) | nei |"); continue
    same = (f["krasj"], f["mot"], f["men"], f["ugr"], f["ut"]) == (n["krasj"], n["mot"], n["men"], n["ugr"], n["ut"])
    likt += same
    print(f"| {t} | {n['inn']} | {utfall(f)} | {utfall(n)} | {'ja' if same else 'NEI'} |")
print(f"\n{likt}/{len(F)} testtyper byte-likt i krasj/MOT/menneske/uten grunn.")
krasj = [t for t, r in N.items() if r["krasj"] != "nei"]
print("KRASJ NÅ:", krasj if krasj else "ingen")
