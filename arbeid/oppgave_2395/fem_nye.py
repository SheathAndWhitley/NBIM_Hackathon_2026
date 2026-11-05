"""§ 5 i ERLIG_EVALUERING.md: hvor mange oppdiktede forslag får grunnen «instruksjonslignende tekst i forslaget» NÅ,
men hadde den ikke FØR (#2063). Injeksjonstestene er ikke med (der er grunnen ment). smed3 #2395.
Bruk: python3 -I arbeid/oppgave_2395/fem_nye.py [før=arbeid/oppgave_2063/ut/resultat.json] [nå=arbeid/oppgave_2395/ut/resultat.json]"""
import json, sys
F = sys.argv[1] if len(sys.argv) > 1 else "arbeid/oppgave_2063/ut/resultat.json"
N = sys.argv[2] if len(sys.argv) > 2 else "arbeid/oppgave_2395/ut/resultat.json"
def saker(f):
    s = {}
    for t in json.load(open(f, encoding="utf-8")):
        if "injeksjon" in t["test"]: continue
        for r in t.get("rader", []):
            if "instruksjonslignende" in r.get("rutingsgrunn", ""):
                s[(t["test"], r["proposal_text"][:60])] = (r["til_menneske"], r["rutingsgrunn"][:70])
    return s
f, n = saker(F), saker(N)
print(f"før (#2063): {len(f)} saker med grunnen utenfor injeksjonstestene; nå: {len(n)}")
nye = sorted(set(n) - set(f))
for k in nye: print(f"  NY: {k[0]}: «{k[1]}» til_menneske={n[k][0]}")
print(f"ANTALL NYE med grunnen «instruksjonslignende» (alle rutet til menneske før også): {len(nye)}")
print("mistet grunnen:", sorted(set(f) - set(n)) or "ingen")
