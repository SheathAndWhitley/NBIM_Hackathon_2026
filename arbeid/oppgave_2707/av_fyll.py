"""#2707: repo4 + «av» (#2701) + fyll frigjorte flagg med neste p_avvik som ikke rammes av «av». Regel i REGEL.md."""
import sys, os
sys.path.insert(0, "arbeid/oppgave_2701")
import importlib.util
spec = importlib.util.spec_from_file_location("s", "arbeid/oppgave_2701/siste_repo4.py")
src = open(spec.origin).read().split("res = {k")[0]
exec(src)
U = os.path.dirname(os.path.abspath(__file__))
def fyll(rows, aar, f):
    h = hist(aar)
    def rammes(x):
        r = F.get(x["id"])
        if r is None: return False
        v = h.get((r["company_id"], norm(r["proposal_text"])), []); return bool(v) and v[-1] == "FOR"
    flagg = {x["id"] for x in rows if x["anbefaling"] == "1"}
    fjern = {i for i in flagg if rammes(next(x for x in rows if x["id"] == i))}
    ny = flagg - fjern
    for x in sorted(rows, key=lambda x: -float(x["p_avvik"])):
        if len(ny) >= len(flagg): break
        if x["id"] not in flagg and not rammes(x): ny.add(x["id"])
    with open(f, "w") as o:
        o.write("id,anbefaling,p_avvik\n")
        for x in rows: o.write(f"{x['id']},{int(x['id'] in ny)},{x['p_avvik']}\n")
    return len(flagg), len(fjern)
res = []
for T in (2024, 2025, 2026):
    S = les(f"{B}/repo4_{T}_test.csv"); ft = f"{U}/avfyll_{T}_test.csv"
    n, k = fyll(S, T, ft); res.append(mål(ft, f"y{T}")); print(T, "flagg", n, "fjernet/fylt", k, "test", round(res[-1], 4), flush=True)
print(f"av+fyll snitt {sum(res)/3:.4f}", [round(x, 4) for x in res])
