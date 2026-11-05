"""#2703: midt-terskel (#2699) + av-regel (#2701) på repo4. Regel i REGEL.md."""
import csv, os, sys, importlib.util
U = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("s", "arbeid/oppgave_2701/siste_repo4.py")
src = open(spec.origin).read().split("res = {k")[0]  # bare hjelpefunksjonene
g = {"__file__": spec.origin}; exec(src, g)
B = g["B"]; les, bruk, mål = g["les"], g["bruk"], g["mål"]
def midt(V, T):
    andel = sum(r["anbefaling"] == "1" for r in V) / len(V)
    k = round((round(andel * len(T)) + sum(r["anbefaling"] == "1" for r in T)) / 2)
    o = set(sorted(range(len(T)), key=lambda i: -float(T[i]["p_avvik"]))[:k])
    return [dict(r, anbefaling="1" if i in o else "0") for i, r in enumerate(T)], k
res = {"repo4": [], "midt": [], "midt+av": []}
for T in (2024, 2025, 2026):
    V, S = les(f"{B}/repo4_{T}_val.csv"), les(f"{B}/repo4_{T}_test.csv")
    M, k = midt(V, S)
    for navn, rows, regel in (("repo4", S, ""), ("midt", M, ""), ("midt+av", M, "av")):
        f = f"{U}/{navn}_{T}_test.csv"; bruk(rows, T, regel, f); res[navn].append(mål(f, f"y{T}"))
    print(T, "k", k, "rå", sum(r["anbefaling"] == "1" for r in S), {n: round(v[-1], 4) for n, v in res.items()}, flush=True)
for n, v in res.items(): print(f"{n:8s} snitt {sum(v)/3:.4f}", [round(x, 4) for x in v], "diff", [round(a-b, 4) for a, b in zip(v, res["repo4"])])
