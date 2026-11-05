# Case 1: frysvakt slo ut 18:18 på c1_real.py. Dom: GODTA (dommer2 #2738)

**Dom:** GODTA. Endringen er bare feilhåndtering, prediksjonene er uendret. Frys-hashen for
`arbeid/hack/levering/c1_real.py` er den nye i `state/c1_frys.json`, begrunnelsen ligger i feltet
`godkjent` og i `state/c1_frys.log`. Frysvakta er grønn.

**Prosessbrudd, bare til protokolls:** smed3 kjørte `c1_frys.py frys --tving` selv kl. 18:19:39
(c1_robusthet_rettet.md) uten dommerens ja, som c1_frysvakt.md krever. Innholdet var i orden, så det får
ingen følge nå, men frystida i fila ble 18:19:39 mens pakka (KANDIDATER.md:7, demo_utskrift linje 5)
sier 17:18:18. Jeg har satt tida tilbake til 17:18:18: modell og prediksjoner er fra den frysen,
bare hashen for c1_real.py er ny.

## 1. Diffen og hvem
- Endret 18:18:16 av smed3 i #2724 (kommentaren i koden sier #2724: krasjfiks i robusthetstesten).
- Frossen hash 3a6da13b51fa…, ny d9c239a2c483…. Frossen versjon lå i GitHub-repoens commit b9b397c
  (synk 17:11). Repo-historikken ble skrevet om til én commit mens jeg jobbet (#2730), så den frosne
  fila ble rekonstruert ved å reversere diffen; hashen stemte eksakt med frysen (3a6da13b51fa).
- Hele diffen (linje 149 i `main`): én linje `inn = list(csv.DictReader(open(f, encoding="utf-8-sig", ...)))`
  er pakket i `try/except UnicodeDecodeError`. Ved UTF-8-fil (alle juryens og våre filer) kjører
  nøyaktig samme linje. Bare når fila ikke er UTF-8 skjer noe nytt: forsøk med latin-1 og varsel,
  og en pen `sys.exit`-feil ved binært i stedet for traceback. Ingen modell-, terskel- eller rutingkode berørt.

## 2. Kald kopi før og etter (fremmed.sh, egne frysfiler i /tmp)
| | frossen c1_real.py | ny c1_real.py |
|---|---|---|
| F1 MOT (v3) | 0,512000 | 0,512000 |
| P / R / TP FP FN | 0,4776 / 0,5517 / 32 35 26 | 0,4776 / 0,5517 / 32 35 26 |
| til menneske | 164 av 1578 (10,4 %) | 164 av 1578 (10,4 %) |
| tallvakt | GRØNN, 174 påstander, 0 avvik | GRØNN, 174 påstander, 0 avvik |
| agent.csv | 1579 linjer | byte-identisk med frossen (cmp) |
| pred_maaler.csv, _pred_uten_ruting.csv | | 0 ulike rader |
KJORING.txt skiller seg bare i klokkeslett og sekunder.

## 3. Merknader
- Tallsjekk-varselet i før-kjøringen (IKKE FUNNET 3311) kommer av at mitt minimale kildetre mangler
  kildetabellene; det er et varsel om kildetreet, ikke om pakka. Etter-kjøringen fra landsbymappen
  er normal (avledet 9, funnet 2139/1163).
- Om fila endres igjen slår frysvakta ut på nytt; da må #2739 (godkjenning av krasjfiksen) eller en
  ny dom til. Selve virkemåten av fiksen på latin-1/binær fil dømmes i #2739, ikke her.
- Midlertidige kopier i /tmp/d2738 er slettet (disken har 7 GB ledig).
