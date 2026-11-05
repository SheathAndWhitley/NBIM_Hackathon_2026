# Kilde: tall for levert repo4 (#2592), kald kjøring 05.11 17:03
- test 2026 F1 MOT 0,5120 TP 32 FP 35 FN 26 P 0,4776 R 0,5517, TN 1446, accuracy 96,0 % (følg styret 96,2 %)
- KI klynge (oppgave_2095/ki_mot.py): [0,400; 0,621]; rad-bootstrap 2000 trekk: [0,397; 0,616]
- val 2025 (oppgave_2490/repo4_val.csv): 0,5301 [0,417; 0,638] (frossen 0,5202 [0,407; 0,627])
- repo4 - b2 (diff_ki.py): +0,147 [+0,040; +0,247]; repo4 - frossen test 2026: +0,036 [-0,008; +0,085]
- P/R KI (treffsikkerhet_ki.py): P 47,8 % [36,4; 59,6], R 55,2 % [42,6; 67,9]

```
[alle saker] n 1539: TP 32 FP 35 FN 26 TN 1446
  accuracy 0.9604  recall MOT 0.5517  presisjon MOT 0.4776  riktig på FOR/ikke-MOT (TN/(TN+FP)) 0.9764  følg styret ville hatt accuracy 0.9623
[maskinen avgjør selv (konfidens >= 0.6)] n 1378: TP 11 FP 3 FN 18 TN 1346
  accuracy 0.9848  recall MOT 0.3793  presisjon MOT 0.7857  riktig på FOR/ikke-MOT (TN/(TN+FP)) 0.9978  følg styret ville hatt accuracy 0.9790
[går til menneske (konfidens < 0.6)] n 161: TP 21 FP 32 FN 8 TN 100
  accuracy 0.7516  recall MOT 0.7241  presisjon MOT 0.3962  riktig på FOR/ikke-MOT (TN/(TN+FP)) 0.7576  følg styret ville hatt accuracy 0.8199
| terskel p >= | val P | val R | val F1 | test P | test R | test F1 | test TP/FP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0.70 | 0.179 | 0.727 | 0.287 | 0.114 | 0.741 | 0.198 | 43/334 |
| 0.80 | 0.277 | 0.646 | 0.388 | 0.186 | 0.707 | 0.295 | 41/179 |
| 0.85 | 0.376 | 0.596 | 0.461 | 0.260 | 0.655 | 0.373 | 38/108 |
| 0.90 | 0.566 | 0.475 | 0.516 | 0.427 | 0.603 | 0.500 | 35/47 |
| **0.9232 (valgt)** | 0.657 | 0.444 | **0.530** | 0.478 | 0.552 | 0.512 | 32/35 |
| 0.95 | 0.690 | 0.404 | 0.510 | 0.633 | 0.534 | **0.579** | 31/18 |
| 0.97 | 0.732 | 0.303 | 0.429 | 0.765 | 0.448 | 0.565 | 26/8 |
| oppsett | saker til menneske | MOT mot styret blant dem | maskin alene | maskin + menneske (øvre grense, antar riktig menneskelig avgjørelse) | gulv: menneske følger styret |
|---|---|---|---|---|---|
| ingen til menneske | 0 av 1539 (0,0 %) | 0 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,48 / R 0,55 / F1 0,512 |
| bare båndet: kalibrert P(MOT) i [0,15; 0,85) | 99 av 1539 (6,4 %) | 25 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,92 / R 0,62 / F1 0,742 (TP 36 FP 3 FN 22) | P 0,79 / R 0,19 / F1 0,306 | <!-- kolonnene etter maskin alene er maskin + menneske, ikke hovedtall; tallvakt: ignorer -->
| **standard** (bånd + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat) | 161 av 1539 (10,5 %) | 29 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,93 / R 0,69 / F1 0,792 (TP 40 FP 3 FN 18) | P 0,79 / R 0,19 / F1 0,306 | <!-- kolonnene etter maskin alene er maskin + menneske, ikke hovedtall; tallvakt: ignorer -->
usette MOT 18 maks p_mot 0.1071 land [('United States', 7), ('British Virgin Islands', 2), ('South Korea', 1), ('Thailand', 1)]
typer [('DIRECTOR_ELECTION', 8), ('OTHER_MGMT', 4), ('ARTICLES', 2), ('AUDITOR', 2)]
MOT-flagg utenfor sonen {'ekte': 11, 'falsk': 3}
lesing per 100: (161+14)/1539*100 = 11,4; accuracy 1478 av 1539
```
