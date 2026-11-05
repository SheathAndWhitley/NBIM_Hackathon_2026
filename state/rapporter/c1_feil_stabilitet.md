# Case 1: holder feilmønsteret fra test 2026 på val 2025, og hva skjer om styrevalg i USA går til et menneske? (#2274)

Bygger på `state/rapporter/c1_feil_per_gruppe.md` (#2272). Frossen agent #2044, agent og terskel er urørt; bare lesing og måling.
Val 2025-prediksjonene er modellen trent <2025 (train.py uendret, kjørt via runpy som i c1_real.py), MOT når rå score ≥ grensen
valgt på val. C og grensen ble valgt på val 2025, så val-tallet er litt optimistisk, men ingen val-sak er i treningen.
(Å kjøre `kjor_agent.py` på 2025-saker ville gitt tall fra en modell som har sett dem; det er ikke gjort.)
Test 2026: `arbeid/hack/levering/kjor_agent_real_maskin_alene.csv`. Måler v3 `--score mot`, data sha 71ba5135….

| | val 2025 | test 2026 |
|---|---:|---:|
| saker med fasit / MOT i fasit | 1909 / 99 | 1539 / 58 |
| TP / FP / FN | 45 / 29 / 54 | 30 / 38 / 28 |
| presisjon / treff / **F1 på MOT** | 0,61 / 0,45 / **0,520** | 0,44 / 0,52 / **0,476** |
| 95 % klynge-KI (meeting_id) | 0,41–0,63 | 0,36–0,59 |

Reproduser: `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2274/val_pred.py arbeid/oppgave_2274/val2025_maskin_alene.csv`,
`python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2274/val2025_maskin_alene.csv val --data real --score mot` (SCORE 0,520231),
`python3 -I arbeid/oppgave_2274/feil_per_gruppe_aar.py --svar ... --aar 2025|2026`, `python3 -I arbeid/oppgave_2274/ruting_varianter.py [--aar 2025 --svar ...]`.

## To setninger til juryen

1. Av de tre feilfunnene fra test 2026 holder to på val 2025: styrevalg er den store feilkilden i volum (68–76 % av de falske MOT begge år) og «andre styresaker» (OTHER_MGMT, 1 av 12 MOT truffet over to år) og revisorvalg (5 av 13) er verst i andel; at USA er svakest er støy fra test 2026, der USA bare hadde 7 MOT i fasit, mens USA på val 2025 lå på snittet (F1 0,45 av 0,52) og India var landet der agenten traff 0 av 14.
2. Å rute alle styrevalg i USA til et menneske hadde løftet test 2026 fra 0,476 til 0,504 (7 falske MOT bort, 161 saker til menneske) men senket val 2025 fra 0,520 til 0,488 (6 ekte MOT mistet), og de 7 falske MOT ligger allerede i båndet agenten ruter i dag, så regelen er en tilpasning til én sesong og er ikke lagt inn.

## Steg 1: holder funnene? Val 2025 mot test 2026

| funn fra #2272 (test 2026) | test 2026 | val 2025 | holder? |
|---|---|---|---|
| **USA svakest** | USA F1 0,00 (TP 0, FP 9, FN 7 av 7 MOT), KI 0,00–0,00 | USA F1 0,45 (TP 10, FP 12, FN 12 av 22 MOT), KI 0,22–0,72, hele 2025 var 0,52 | **Nei, støy.** USA er ikke svakere enn snittet på val. Det som holder: USA har flest falske MOT begge år (12 av 29 på val, 9 av 38 på test), og styrevalg i USA har lav presisjon begge år (6 TP / 7 FP på val, 0 / 7 på test). Landet der agenten treffer ingenting begge år er **India**: 0 av 14 på val (F1 0,00, KI 0,00–0,00), 1 av 4 på test (F1 0,18). |
| **Styrevalg er største feilkilde i volum** | 26 av 38 FP (68 %), 13 av 28 FN (46 %), presisjon 0,37 | 22 av 29 FP (76 %), 34 av 54 FN (63 %), presisjon 0,56 | **Ja.** Volumet holder begge år. Presisjonen på styrevalg er lavere på test (0,37 mot 0,56), som er hele fallet fra 0,52 til 0,48. |
| **OTHER_MGMT og revisor verst i andel** | OTHER_MGMT 1 av 6 (F1 0,25); AUDITOR 3 av 7 (F1 0,60, treff 0,43) | OTHER_MGMT 0 av 6 (F1 0,00, KI 0,00–0,00); AUDITOR 2 av 6 (F1 0,50, treff 0,33) | **Ja.** Over to år: OTHER_MGMT 1 av 12 MOT, AUDITOR 5 av 13. Begge år nesten uten falske MOT (FP 1 og 0): agenten tier der NBIMs grunn ikke står i forslagsteksten. |

Andre forskjeller som er verdt å vite: SAY_ON_PAY hadde 12 MOT på val (F1 0,67, KI 0,42–0,83) men 3 på test med 8 falske MOT. DM/EM: på val er EM mer presis (0,76 mot 0,55), på test også (0,57 mot 0,35), så «EM mer presis enn DM» holder. Fulle tabeller: `arbeid/oppgave_2274/feil_val2025.md` (val) og rapport #2272 (test).

## Steg 2: ruting til menneske i stedet for automatisk MOT/FOR, test 2026

Agenten er urørt; bare merkingen «til menneske» endres. Tre lesninger per variant:
- **A, måler v3 `--score mot`** (hovedtallet): rutede saker får «følg styret» (anbefaling 0, konfidens 0,5). Det er tallet hvis mennesket ikke rekker å stemme.
- **B, menneske treffer:** rutede saker får fasit. Øvre grense, mennesket antas feilfritt.
- **C, bare automatiske:** F1 på MOT på sakene som ikke rutes.

| variant | til menneske | TP | FP | FN | presisjon A | **F1 A (måler v3)** | F1 B | presisjon C | F1 C |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V0 frossen, ingen ruting (levert tall) | 0 | 30 | 38 | 28 | 0,441 | **0,4762** | 0,476 | 0,441 | 0,476 |
| V0b frossen, bånd [0,15; 0,85) som levert, men rutede saker IKKE autostemt | 183 (11,9 %) | 9 | 0 | 49 | 1,000 | **0,2687** | 0,828 | 1,000 | 0,514 |
| **V1 styrevalg i USA → menneske** | **161 (10,5 %)** | 30 | 31 | 28 | 0,492 | **0,5042** | 0,517 | 0,492 | 0,509 |
| V2 bånd + styrevalg i USA | 335 (21,8 %) | 9 | 0 | 49 | 1,000 | **0,2687** | 0,840 | 1,000 | 0,529 |
| V3 alle saker i USA → menneske | 217 (14,1 %) | 30 | 29 | 28 | 0,508 | **0,5128** | 0,597 | 0,508 | 0,545 |
| V4 styrevalg i DM → menneske | 541 (35,2 %) | 22 | 20 | 36 | 0,524 | **0,4400** | 0,644 | 0,524 | 0,518 |
| V5 OTHER_MGMT + AUDITOR → menneske | 217 (14,1 %) | 26 | 37 | 32 | 0,413 | **0,4298** | 0,582 | 0,413 | 0,481 |
| V6 alle styrevalg → menneske | 739 (48,0 %) | 15 | 12 | 43 | 0,556 | **0,3529** | 0,782 | 0,556 | 0,526 |

Merk om V0b: den leverte fila `kjor_agent_real_pred_maaler.csv` beholder agentens stemme også på rutede saker (bare konfidensen senkes), så den måler 0,476. V0b viser hva båndet koster hvis de 183 sakene ikke stemmes automatisk: alle 38 falske MOT er i båndet, men også 21 av 30 treff.

**Samme varianter på val 2025** (båndet finnes ikke som fil for val):

| variant | til menneske | TP | FP | FN | presisjon A | **F1 A (måler v3)** | F1 B | F1 C |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| V0 frossen, ingen ruting | 0 | 45 | 29 | 54 | 0,608 | **0,5202** | 0,520 | 0,520 |
| **V1 styrevalg i USA → menneske** | **239 (12,5 %)** | 39 | 22 | 60 | 0,639 | **0,4875** | 0,625 | 0,542 |
| V3 alle saker i USA → menneske | 324 (17,0 %) | 35 | 17 | 64 | 0,673 | **0,4636** | 0,659 | 0,543 |
| V4 styrevalg i DM → menneske | 675 (35,4 %) | 27 | 10 | 72 | 0,730 | **0,3971** | 0,775 | 0,575 |
| V5 OTHER_MGMT + AUDITOR → menneske | 271 (14,2 %) | 43 | 28 | 56 | 0,606 | **0,5059** | 0,604 | 0,544 |
| V6 alle styrevalg → menneske | 903 (47,3 %) | 17 | 7 | 82 | 0,708 | **0,2764** | 0,854 | 0,557 |

Lesning: styrevalg i USA var 161 saker med **1** MOT i fasit på test 2026 (0 TP, 7 FP), men 239 saker med **16** MOT på val 2025 (6 TP, 7 FP, 10 FN).
Regelen fjerner 7 falske MOT begge år, men på val koster den 6 treff, og tallet faller. Presisjonen stiger begge år (0,44 → 0,49 og 0,61 → 0,64), treffen
holder bare på test. Mennesket får 10–12 % flere saker for å rette 7 falske MOT, som det leverte båndet allerede fanger (V2 har ingen FP igjen å ta, bare 152 flere saker).
Ingen av gruppereglene slår den frosne agenten på begge år med lesning A. Lesning B (mennesket treffer) løftes alltid, men det er en egenskap ved å sende mer til mennesket, ikke ved regelen.

## Konklusjon for beslutningsstøtten

- Behold båndet [0,15; 0,85) som ruting; legg ikke inn «styrevalg i USA → menneske». Den regelen er tilpasset én sesong.
- Det som er stabilt og kan sies til juryen: styrevalg gir mest volum av feil, OTHER_MGMT og revisorvalg fanges nesten aldri (grunnen står ikke i forslagsteksten), og India er et land der agenten treffer 0–1 MOT begge år. Vil man rute en gruppe, er OTHER_MGMT + AUDITOR (V5) den eneste som ikke koster treff på val (−2 TP, 0,520 → 0,506) og som gir mennesket saker agenten faktisk bommer på (11 av 12 MOT på val, 9 av 13 på test), men også den senker målerens tall, så den er ikke lagt inn.
- Alt ligger i `arbeid/oppgave_2274/` (val_pred.py, feil_per_gruppe_aar.py, ruting_varianter.py, varianter_2025/, varianter_2026/). Ingen endring i `arbeid/hack/levering`.
