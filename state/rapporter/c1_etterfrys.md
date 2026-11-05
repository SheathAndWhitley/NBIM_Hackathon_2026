# Case 1 etterfrys-sjekk: GRØNN (2026-11-05 17:23)

Kommando: `bash arbeid/verktoy/c1_etterfrys.sh`  
Modus: EKTE: state/c1_frys.json, --krev (ikke frosset = rødt)  
Total tid: 70 s. Kald kopi: /tmp/c1_etterfrys. Fulle logger: /tmp/c1_etterfrys_logg.HImN

| Steg | Status | Utgang | Tid |
|---|---|---|---|
| 1 frysvakt | GRØNN | 0 | 0 s |
| 2 tallvakt (landsbymappen) | GRØNN | 0 | 1 s |
| 3 fremmed.sh (kald kopi) | GRØNN | 0 | 69 s |

HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000 (fra kald kopi)

## 1_frys: siste linjer
```
FRYSVAKT GRØNN: 21 filer like som ved frys 2026-11-05T17:18:18
```
## 2_tallvakt: siste linjer
```
Måler v3 --score mot på arbeid/hack/levering/kjor_agent_real_maskin_alene.csv: F1 0.5120  P 0.4776  R 0.5517  TP 32 FP 35 FN 26  (58 MOT i fasit, 66 avvik)
Kjøring: til menneske 164 av 1578 inn (10.4%), 161 av 1539 med fasit (10.5%)
22 filer, 175 påstander om hovedtallet stemmer, 0 avviker
OK
```
## 3_fremmed: siste linjer
```
  ruting (konfidens < 0.6): 161 til menneske (10.5%)
SCORE 0.529412
RETNING maks
skrev /tmp/c1_etterfrys/ut/agent.csv
tid: uv sync 0 s, kjøring 66 s, totalt 66 s
HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000
TALLSJEKK (varsel): 3054 tall i 22 filer: avledet A 6, funnet A 1835, funnet B 1213. Kilder A 367 tall, B 128120 tall. 1.9 s.
Måler v3 --score mot på ut/pred_maaler.csv: F1 0.5120  P 0.4776  R 0.5517  TP 32 FP 35 FN 26  (58 MOT i fasit, 66 avvik)
Kjøring: til menneske 164 av 1578 inn (10.4%), 161 av 1539 med fasit (10.5%)
22 filer, 175 påstander om hovedtallet stemmer, 0 avviker
OK
TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring
```

Utgangskoder: frysvakt 2 = avvik/ikke frosset; tallvakt 1 = tall i .md avviker, 2 = måleren feilet;
fremmed.sh 4 = frysvakt rød i kopien, 1 = tallvakt rød i kopien, annet = kjøringen krasjet.
