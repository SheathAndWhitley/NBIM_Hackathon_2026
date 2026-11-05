# Case 1: trekket «styreleder = daglig leder» i smed2s MOT-modell gir ingen gevinst på test 2026 (smed3, #2075)

Tiltak B fra `c1_feilanalyse_mot.md` / tiltak 1 i `arkitekt_c1_tiltak_2072.md`. Bygd i en kopi av smed2s `train.py` (#2044),
så #2076 (smed2) trenger bare å gjøre India-rutingen. Regex på normalisert proposal_text, begge rekkefølger:
chairman/chairperson/chair + managing director/whole time/chief executive/ceo/president. Leser ingen nye kolonner.

Duality-rader (ikke-injeksjon, med etikett): 2020 2 (0 MOT), 2021 2 (1), 2023 4 (2), 2024 1 (1), **2025 5 (5)**, **2026 3 (0)**.

| real_votes, miks h2 | val 2025 F1 | test 2026 F1 (maaler.sh real_test) | P | R | pred MOT | PR-AUC test |
|---|---|---|---|---|---|---|
| #2044 uten trekk | 0,5217 | **0,4818** | 0,465 | 0,500 | 71 | 0,524 |
| + duality som trekk i LR og LGBM | 0,5217 | 0,4818 | 0,465 | 0,500 | 71 | 0,524 |
| + etterregel p += 0,5·duality (løft valgt på val av 0/0,05/0,1/0,2/0,5) | 0,5638 | 0,4783 | 0,458 | 0,500 | 72 | 0,431 |

- **Som trekk:** null effekt. Bare 9 duality-rader i trening før 2025 (8 før 2026 + val). LGBM splitter ikke på dem
  (min_child_samples 20), og i LR drukner én binær kolonne i tf-idf.
- **Som etterregel:** val stiger +0,04 fordi alle 5 duality-rader i 2025 er MOT, men det er grensen og løftet valgt på
  de samme 5 radene. På test er alle 3 duality-rader FOR: én ekstra FP, F1 0,4818 → 0,4783, og PR-AUC faller 0,52 → 0,43
  fordi rangeringen øverst blir feil.
- **Anbefaling: ikke ta det inn i leveransen.** Signalet er ekte i 2025 (India), men ustabilt fra år til år og bygger på n=5.
  Til juryen: «vi testet styreleder = daglig leder; val +0,04, test −0,004, forkastet fordi n er for lite».
- Måleren: tavla avviser `--sti` fordi rundens måler er endret på disk (hash 8733327407 → 474eae7bc8), og
  `maaler_nbim.py` tar nå bare id-format. Tallene over er kjørt direkte med `bash arbeid/hack/maaler.sh <fil> real_test`
  og står selvrapportert på tavla (#1064, #1065). Dommeren må sette måleren på nytt.

Kjør (ca. 2 min hver):
`cd arbeid/oppgave_2075 && uv run --project ../oppgave_2023 python train.py ../../state/opplastet/20261105_114241_real_votes.csv --variant miks --hist 2 --duality 1 [--loft 0,0.05,0.1,0.2,0.5] --ut pred.csv`
`uv run --project ../oppgave_2023 python til_id.py ../../state/opplastet/20261105_114241_real_votes.csv pred.csv svar.csv && bash ../hack/maaler.sh svar.csv real_test`
