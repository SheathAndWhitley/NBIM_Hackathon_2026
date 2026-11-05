# Case 1: arrangørens rettede data, offisiell måler og baseline (dommer2, #2034)

Filene i state/opplastet/20261105_114240_npx_votes.csv og 20261105_114241_real_votes.csv er
md5-like med kopiene i arbeid/hack/CASE/.

## Hva er nytt mot våre egne SEC-data (data_vif, data_nbim)
- data_vif var amerikanske fond (Vanguard m.fl.) fra SEC N-PX, 2023-07..2026-06, der vi selv
  utledet styret fra kilde. Nå kommer **NBIMs egne stemmer** med `mgmt_rec` gitt av arrangøren.
- npx: 52 906 saker, 51 % USA, med `split_year` (≠ `year`: 6 915 saker er flyttet ett år frem).
- real (NBIM API): 13 757 saker 2019–2026 i 194 selskaper (mest Japan, USA, Kina, UK) og
  `rationale_text` på 627 saker (618 av dem er avvik).
- **Ingen overlapp** mellom npx og real (0 felles selskaper, møter og saker). Det er ingen krysslekkasje,
  men de kan heller ikke slås sammen per selskap.
- data_nbim/ (11:43, #2020) var allerede splittet, men `npx_train.csv` inneholder 42 injeksjonsrader.
  **Bruk data_off/**, der injeksjonsradene er tatt ut.

## Avvik fra styret (against_board=1, inkl. avstå) per år
| real år | saker | avvik | | npx split_year | saker | avvik | uten fasit |
|---|---|---|---|---|---|---|---|
| ≤2024 (train) | 10 209 | 575 | | 2024 train | 18 838 | 572 | 1 276 |
| 2025 (val) | 1 970 | 103 | | 2025 val | 16 451 | 729 | 1 554 |
| 2026 (test) | 1 578 | 66 | | 2026 test | 17 476 | 634 | 1 021 |

Per år i real: 2019 97, 2020 83, 2021 97, 2022 117, 2023 83, 2024 98, 2025 103, 2026 66.
I npx test er 297 av 634 avvik AVSTÅ mot styrets MOT, og 302 er aksjonærforslag. Ekte «MOT mot styrets FOR» er få.

## Tidssplitt og injeksjon (krav 2 og 4)
- npx: train split_year 2024, val 2025, test 2026. real: train ≤2024, val 2025, test 2026.
- injection_flag=1: 141 rader, bare i npx (42/62/37 i 2024/25/26). De ligger i et eget vindu
  `inj` (data_off/npx_inj_input.csv) og **aldri i train, val eller test**. Bare 84 har fasit (1 avvik),
  så motstandstesten (#2038) må måle om agenten lar seg lure, ikke F1.

## Måler (krav 3): arbeid/hack/c1/maaler_offisiell.py
`python3 -I arbeid/hack/c1/maaler_offisiell.py SVAR.csv val|test|inj --data real|npx`
- SCORE = F1 på avvik fra styret. Den skriver også P/R, PR-AUC, streng MOT (P/R/F1) og ruting.
- Svarfila skal ha `id,anbefaling[,konfidens,p_avvik]`, med id = meeting_id|item_no. Mangler id, avvises fila.
- `lag` skriver data_off/, og input-filene har ingen lekkasjekolonner. `baseline` kjører tre enkle regler.
- Rundens måler (sha e8f70d3904) = **real val 2025**. Test 2026 måles én gang, av dommer.
- Lekkasje, aldri feature: nbim_vote(_raw), against_board, rationale_text, rationale_section,
  position_paper, funds_disagree, n_funds.

## Baseline, F1 på avvik (P / R)
| regel | real val | real test | npx val | npx test |
|---|---|---|---|---|
| følg styret | **0** (0/0) | **0** | **0** | **0** |
| alltid avvik | 0,102 | 0,082 | 0,093 | 0,074 |
| aksjonærforslag=MOT | 0 | 0,058 | 0,588 (1,00/0,42) | 0,583 (1,00/0,41) |

Følg styret har 96 % treff (accuracy), men F1 0. Ordre #231 sier vi må prediktere avvik, så F1 på avvik
er hovedtallet. NB: på **streng MOT** gir «følg styret» 0,63 på npx test, fordi styret selv sier MOT
til aksjonærforslag. Derfor er streng MOT et misvisende hovedmål.
Aksjonærregelen virker på npx, men ikke på NBIMs ekte stemmer (0,06). Real er det ærlige målet.

Forsøk: #1034 (følg styret, real val, målt av måleren), #1035 (alle vinduer).
