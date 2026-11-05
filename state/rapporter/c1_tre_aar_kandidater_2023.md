# Case 1 (#2573): kandidatene på 2023 som fjerde testår (val 2022, train <=2021)

Samme 7 kandidater og verktøy som #2567 (abl_rull.py, rull3.py, maaler_aar.py --score mot, diff_ki_aar.py).
Data er ikke for tynt: train 2019-2021 = 4607 rader, 244 MOT mot styret; val 2022 117 MOT (modellens telling); test 2023 = 77 MOT i fasit.
Kode og filer: `arbeid/oppgave_2573/` (benk.sh -> benk.txt, ki4.sh -> ki_snitt4.txt).

## 2023 alene (F1 på MOT mot styret, offisiell måler)
| kandidat | TP | FP | FN | P | R | F1 | minus frossen, 95 % KI (selskap-bootstrap) |
|---|---|---|---|---|---|---|---|
| frossen | 36 | 105 | 41 | 0.255 | 0.468 | **0.3303** | 0 |
| person | 37 | 106 | 40 | 0.259 | 0.481 | 0.3364 | +0.006 [-0.023; +0.036] |
| repo4 | 34 | 92 | 43 | 0.270 | 0.442 | 0.3350 | +0.005 [-0.035; +0.049] |
| V1 | 35 | 101 | 42 | 0.257 | 0.455 | 0.3286 | -0.002 [-0.039; +0.040] |
| V1p | 27 | 38 | 50 | 0.415 | 0.351 | 0.3803 | +0.050 [-0.026; +0.117] |
| V2 | 27 | 38 | 50 | 0.415 | 0.351 | 0.3803 | +0.050 [-0.026; +0.117] (= V1p, samme valg på val) |
| NBIMhybrid | 34 | 100 | 43 | 0.254 | 0.442 | 0.3223 | -0.008 [-0.053; +0.037] |

2023 er et svakt år for alle (0,32-0,38 mot 0,45-0,55 i 2024-26): grensen valgt på 2022 flagger for mye (frossen 141 flagg for 77 MOT, P 0,26).

## Fire år samlet (2023-2026), snitt av F1-differanse mot frossen
| kandidat | 2023 | 2024 | 2025 | 2026 | snitt 3 år (24-26) | snitt 4 år, 95 % KI | verste år |
|---|---|---|---|---|---|---|---|
| repo4 | +0.005 | +0.051 | +0.017 | +0.036 | +0.035 | **+0.027 [-0.006; +0.060]**, B<A 0.05 | +0.005 |
| V2 | +0.050 | -0.047 | +0.033 | +0.040 | +0.009 | +0.019 [-0.021; +0.061] | -0.047 |
| person | +0.006 | -0.037 | +0.001 | +0.049 | +0.005 | +0.005 [-0.024; +0.034] | -0.037 |
| V1p | +0.050 | -0.052 | +0.005 | +0.016 | -0.010 | +0.005 [-0.031; +0.042] | -0.052 |
| NBIMhybrid | -0.008 | -0.047 | -0.005 | +0.069 | +0.006 | +0.002 [-0.038; +0.044] | -0.047 |
| V1 | -0.002 | -0.050 | +0.005 | +0.005 | -0.013 | -0.010 [-0.044; +0.027] | -0.050 |

## Funn
- Byttregelen (snitt >= +0,02, intet år <= -0,02) holder for repo4 også med 2023 med: snitt 4 år +0,027, verste år +0,005 (2023). Ingen andre kandidater består, verken over 3 eller 4 år.
- Men 2023-gevinsten til repo4 er nær null (+0,005, 21 ulike prediksjoner), så fordelen er mindre stabil enn de tre årene antydet; 4-års-KI krysser 0 svakt (nedre -0,006, 5 % av trekkene B<A).
- Regelen ble fastsatt for tre testår; 2023 er tilleggsinformasjon for dommeren, ikke en ny regel.
- Merknad: i rull3.py-loggen står «ref frossen alene (p>=t valgt 2023)»; for test 2023 er t valgt på 2022 (hardkodet tekst, tall riktige).
