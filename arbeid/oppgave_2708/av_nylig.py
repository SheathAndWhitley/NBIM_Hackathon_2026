"""#2708: «av»-regelen (#2701) bare når siste FOR-stemme er fra T-1/T-2. Regel i REGEL.md."""
import csv, os, collections
g = {"__file__": "arbeid/oppgave_2701/siste_repo4.py"}
exec(open(g["__file__"]).read().split("res = {k")[0], g)
R, F, norm, les, mål, B = g["R"], g["F"], g["norm"], g["les"], g["mål"], g["B"]
U = os.path.dirname(os.path.abspath(__file__))
def hist(aar):
    h = collections.defaultdict(list)
    for r in sorted((r for r in R if int(r["year"]) < aar and r["nbim_vote"] in ("FOR", "MOT")), key=lambda r: r["meeting_date"]):
        h[(r["company_id"], norm(r["proposal_text"]))].append((r["nbim_vote"], int(r["year"])))
    return h
def bruk(rows, aar, nylig, f):
    h = hist(aar); n = 0
    with open(f, "w") as o:
        o.write("id,anbefaling,p_avvik\n")
        for x in rows:
            a = x["anbefaling"] == "1"; r = F.get(x["id"])
            if r is not None and a:
                v = h.get((r["company_id"], norm(r["proposal_text"])), [])
                if v and v[-1][0] == "FOR" and (not nylig or v[-1][1] >= aar - 2): a = False; n += 1
            o.write(f"{x['id']},{int(a)},{x['p_avvik']}\n")
    return n
res = {"av": [], "av-nylig": []}
for T in (2024, 2025, 2026):
    S = les(f"{B}/repo4_{T}_test.csv"); fj = {}
    for navn, ny in (("av", False), ("av-nylig", True)):
        f = f"{U}/{navn}_{T}_test.csv"; fj[navn] = bruk(S, T, ny, f); res[navn].append(mål(f, f"y{T}"))
    print(T, "fjernet", fj, {k: round(v[-1], 4) for k, v in res.items()}, flush=True)
r4 = [0.5057, 0.5309, 0.5120]
for k, v in res.items(): print(f"{k:9s} snitt {sum(v)/3:.4f}", [round(x, 4) for x in v], "diff mot repo4", [round(a-b, 4) for a, b in zip(v, r4)])
