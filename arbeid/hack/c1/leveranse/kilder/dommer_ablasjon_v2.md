# Dommer sak 2098: ablasjon v2 (sak 2089) verifisert fra kald kopi: PASS

**PASS.** Full og h1 reproduserer eksakt fra kald kopi, grensen er valgt på val, og h2-historikken lekker ikke fra samme møte.

| Sjekk | Smed3 | Dommer kald kopi | Status |
|---|---|---|---|
| Full test 2026 F1 MOT (P/R, flagget) | 0,4818 | 0,4818 (0,465/0,500, 71 av 66) | PASS |
| Full val 2025 | 0,522 | 0,5217 (C=3, grense 0,9188) | PASS |
| h1 test 2026 | 0,386 | 0,386 (0,458/0,333, 48) | PASS |
| h1 val 2025 | 0,448 | 0,4483 (C=0,3, grense 0,9446) | PASS |
| Svarfiler full/hist1 _val/_test | | byte-identiske med <arbeidsmappe>/oppgave_2089 | PASS |
| Grense valgt på val, ikke test | | C og grense velges i løkka over `p[va]` (abl.py:105–110); SCORE bruker rå val-grense (l.117, 125) | PASS |
| h2 ingen lekkasje fra samme møte | | 400 tilfeldige rader 2025/26 × 3 nøkler sjekket mot brute force (`dato < radens dato`): 0 avvik, 0 etiketter fra samme møte | PASS |

Detaljer om h2: `merge_asof(..., allow_exact_matches=False)` på møtedato gir bare møter strengt før radens dato. Datoene har ikke klokkeslett, hvert møte har én dato, og year = datoens år for alle rader. 33 selskap+dato-par har to møter samme dag; de ser ikke hverandre (strengt før), så det er konservativt.

Forbehold (ikke feil):
- Linja «samme andel flagget» (l.118–119) bruker testfordelingen uten etiketter. Den er ikke hovedtallet og skal ikke brukes i juryteksten (Full ville da vist 0,50).
- Docstringen i abl.py (l.5–6) sier «ingen etiketter fra samme sesong», som bare gjelder h1. Bør rettes før koden vises til juryen.
- h2 forutsetter at NBIMs stemmer fra tidligere møter er kjent når neste sak predikeres. Rapporten sier det ærlig; h1 = 0,386 er tallet uten den antakelsen.

Kommandoer:
```
K=/tmp/kald_2098; mkdir -p $K; cp <arbeidsmappe>/oppgave_2089/abl.py $K/
cp arbeid/hack/CASE/20261105_114241_real_votes.csv $K/rv.csv   # sha256 71ba5135…
cd $K; P=<repo>/<arbeidsmappe>/oppgave_2023
uv run --project $P python abl.py rv.csv --ut full.csv  --hist 2 --variant miks > full.log
uv run --project $P python abl.py rv.csv --ut hist1.csv --hist 1 --variant miks > hist1.log
uv run --project $P python <arbeidsmappe>/oppgave_2098/sjekk_h2_2098.py   # kjørt fra $K, lekkasjesjekk h2
cmp full_test.csv <repo>/<arbeidsmappe>/oppgave_2089/full_test.csv   # osv. for val/hist1
```
abl.py sha256 81fac3c9…
