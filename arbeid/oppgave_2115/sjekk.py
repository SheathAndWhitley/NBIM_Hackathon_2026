"""#2115 dommer2: stikkprøve 20 sitater (seed 2115) fra smed2s test 2026-svar mot speiderens jsonl (#2105).
  python3 arbeid/oppgave_2115/sjekk.py [svarfil]"""
import json, re, sys, pandas as pd
SVAR = sys.argv[1] if len(sys.argv) > 1 else "arbeid/oppgave_2106/test2026_mot.csv"
KILDE = "arbeid/hack/retningslinjer/nbim_retningslinjer.jsonl"
n = lambda t: re.sub(r"\s+", " ", str(t).replace("’", "'").replace("“", '"').replace("”", '"')).strip().lower()
K = [json.loads(l) for l in open(KILDE, encoding="utf-8")]
byid = {k["id"]: k for k in K}
D = pd.read_csv(SVAR)
U = D.sample(20, random_state=2115)
ok_ord = ok_id = 0
for i, r in U.iterrows():
    s = n(r.sitat)
    ordrett = any(s in n(k["tekst"]) for k in K)
    idok = r.pid in byid and s in n(byid[r.pid]["tekst"])
    ok_ord += ordrett; ok_id += idok
    print(f"--- {r.id} | {r.type} | {r.tekst[:90]}\n  pid={r.pid} sek={r.sek} fasit={r.fasit} gull={r.gull} ordrett={ordrett} id_stemmer={idok}")
    print(f"  SITAT: {str(r.sitat)[:260]}\n  NBIM:  {str(r.begr)[:200]}")
print(f"\nordrett i kilden {ok_ord}/20, id+tekst stemmer {ok_id}/20, seksjon=fasit {(U.sek.astype(str)==U.fasit.astype(str)).sum()}/20")
print(f"hele settet: ordrett {sum(any(n(x) in n(k['tekst']) for k in K) for x in D.sitat)}/{len(D)}")
