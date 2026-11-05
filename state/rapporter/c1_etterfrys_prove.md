# Case 1 etterfrys-sjekk: GRØNN (2026-11-05 13:14)

Kommando: `bash arbeid/verktoy/c1_etterfrys.sh --prove`  
Modus: PRØVE: midlertidig frys /tmp/c1_etterfrys_logg.zzC8/prove_frys.json (ikke den ekte state/c1_frys.json)  
Total tid: 42 s. Kald kopi: /tmp/c1_etterfrys. Fulle logger: /tmp/c1_etterfrys_logg.zzC8

| Steg | Status | Utgang | Tid |
|---|---|---|---|
| 1 frysvakt | GRØNN | 0 | 1 s |
| 2 tallvakt (landsbymappen) | GRØNN | 0 | 0 s |
| 3 fremmed.sh (kald kopi) | GRØNN | 0 | 41 s |

HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190 (fra kald kopi)

## 1_frys: siste linjer
```
FRYSVAKT GRØNN: 9 filer like som ved frys 2026-11-05T13:13:36
```
## 2_tallvakt: siste linjer
```
Måler v3 --score mot på arbeid/hack/levering/kjor_agent_real_maskin_alene.csv: F1 0.4762  P 0.4412  R 0.5172  TP 30 FP 38 FN 28  (58 MOT i fasit, 66 avvik)
Kjøring: til menneske 188 av 1578 inn (11.9%), 183 av 1539 med fasit (11.9%)
14 filer, 138 påstander om hovedtallet stemmer, 0 avviker
OK
```
## 3_fremmed: siste linjer
```
  streng MOT: TP 0 FP 0 FN 0  P 0.0000  R 0.0000  F1 0.0000
  ruting (konfidens < 0.6): 183 til menneske (11.9%)
SCORE 0.481752
RETNING maks
skrev /tmp/c1_etterfrys/ut/agent.csv
tid: uv sync 0 s, kjøring 40 s, totalt 40 s
HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190
Måler v3 --score mot på ut/pred_maaler.csv: F1 0.4762  P 0.4412  R 0.5172  TP 30 FP 38 FN 28  (58 MOT i fasit, 66 avvik)
Kjøring: til menneske 188 av 1578 inn (11.9%), 183 av 1539 med fasit (11.9%)
14 filer, 138 påstander om hovedtallet stemmer, 0 avviker
OK
TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring
```

Utgangskoder: frysvakt 2 = avvik/ikke frosset; tallvakt 1 = tall i .md avviker, 2 = måleren feilet;
fremmed.sh 4 = frysvakt rød i kopien, 1 = tallvakt rød i kopien, annet = kjøringen krasjet.

## Arkitektens notat (#2187)
- Til dommeren i #1972 kl. 18:30: `bash arbeid/verktoy/c1_etterfrys.sh` (uten --prove). Rapport: state/rapporter/c1_etterfrys.md, utgang 0 = alle grønne.
- Prøven over: alle tre grønne, 42 s totalt, HOVEDTALL F1 MOT 0,476190 fra kald kopi, tallvakt 138 påstander stemmer, 0 avviker.
- Rød vei prøvd 13:14 uten --prove (før frys): frysvakt RØD (utgang 2, ikke frosset), tallvakt og fremmed GRØNN, total RØD, skriptet går ut med 1. state/c1_frys.json ble ikke laget eller rørt.
- Kald kopi går til /tmp/c1_etterfrys, ikke /tmp/fremmed, så den ikke kolliderer med dommerens egne kaldstarter.
