# Case 1 (#2612): kontrollregning av repo4-tallene, tre testår — dommer2, 05.11 17:12

**Kort: 0 avvik.** Alle seks F1 MOT-tall i byttedommen (#2570, `c1_byttedom_265.md`) er regnet på nytt fra pakkens
kode og stemmer på fjerde desimal. Prediksjonsfilene er byte-like dem dommen bygde på. Ingenting å melde over 0,005.

## Hva som ble kjørt (egen mappe, egen datakopi: `arbeid/oppgave_2612/kjor/`, kjøring 17:09:36–17:09:46)
- Modell: `arbeid/hack/c1/bytte/modell_repo4.py` (= `arbeid/hack/levering/modell_repo4.py`, cmp lik; `stemmeagent/` lik)
  kopiert til `modell_rull.py` med ett tillegg: `--testaar T` (val = T−1 trent <T−1, test T trent <T). Diff: 7 linjer,
  bare årstallene 2025/2026 byttet mot VA/TA. Samme flagg som pakken (`c1_real.py:86`): `--variant miks --hist 2`,
  repo4 i tillegg `--repo prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate`.
- Måler: pakkens `maaler_offisiell_v3.py` med `--score mot`, vindu `y<år>` i stedet for train/val/test (diff: 2 linjer).
- Data: arrangørens `20261105_114241_real_votes.csv`, sha256 71ba5135, 13 757 rader (datavakta grønn).
- Python: `arbeid/kandidater/smed2_c1_mot/.venv` (samme som `bytt.sh` steg 3), `python3 -I`.
- Bindeledd til pakken: pakkens **uendrede** `modell_repo4.py` kjørt på 2026 gir byte-lik `_test.csv` som kopien
  (`pakke_repo4_test.csv` = `repo4_2026_test.csv`, `pakke_frossen_test.csv` = `frossen_2026_test.csv`).

## Tabell: F1 på MOT mot styret
| modell | testår | min kjøring F1 (TP/FP/FN) | dommens tall (TP/FP/FN) | avvik | byte-lik #2570-fil |
|---|---|---|---|---|---|
| frossen #2044 | 2024 | 0,4545 (30/14/58) | 0,4545 (30/14/58) | 0,0000 | ja |
| repo4 | 2024 | 0,5057 (44/42/44) | 0,5057 (44/42/44) | 0,0000 | ja |
| frossen #2044 | 2025 | 0,5143 (45/31/54) | 0,5143 (45/31/54) | 0,0000 | ja |
| repo4 | 2025 | 0,5309 (43/20/56) | 0,5309 (43/20/56) | 0,0000 | ja |
| frossen #2044 | 2026 | 0,4762 (30/38/28) | 0,4762 (30/38/28) | 0,0000 | ja |
| repo4 | 2026 | 0,5120 (32/35/26) | 0,5120 (32/35/26) | 0,0000 | ja |

Snitt frossen 0,4817, repo4 0,5162, differanse +0,0345; verste år 2025 +0,017. Byttregelen (snitt ≥ +0,02, intet år
under −0,02) holder også i kontrollen. Val-valg i loggene: frossen C=3/C=3/C=1, repo4 C=3/C=3/C=3 for test 2026/2025/2024.

## Ærlige forbehold
1. Jeg (dommer2) skrev også byttedommen. Kontrollen er uavhengig i kode-sti (pakkens fil, ikke `oppgave_2023/abl_rull.py`)
   og datakopi, men ikke i person. Modellen er deterministisk (byte-like filer), så kontrollen viser at tallene følger av
   koden, ikke at koden er riktig; lekkasjesjekken står i #2575.
2. `stemmeagent/ballot.py` beregner `base_rate` som én skalar over møter 2019–2023 (brukt som prior i
   `hist_type_dev_rate`). For testår 2024 (val 2023) inneholder den altså val-årets etiketter. Det rører ikke testårene
   og er samme forbehold som i byttedommen pkt. 5. For 2025 og 2026 ligger alt før val.
3. Tallene i denne rapporten gjelder modellen alene (`_test.csv`, uten ruting); hovedtallet i pakken måles på
   `_pred_uten_ruting.csv` fra kald kopi (#2596).

## Gjenskap
`bash arbeid/oppgave_2612/kjor/kjor.sh` (10 s), så `python3 -I arbeid/oppgave_2612/sammenlign.py`.
