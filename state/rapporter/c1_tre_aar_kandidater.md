# Case 1 #2567: alle kandidater målt på tre testår (F1 på stemmer MOT styret)

Oppsett: test T = 2024/2025/2026, val = T-1, trening < T (hybriden: trent <= T-2, valgt på T-1). Alle
terskler, C, a/b/t og hybridens modellvalg er valgt på val. Teståret er kjørt én gang. Tallene er målt med
den offisielle måleren (`maaler_aar.py --score mot`, datafil sha 71ba5135). KI = parret klyngebootstrap over
selskaper, 2000 trekk, seed 0, kandidat minus frossen. Byttregelen (ordre #265) ble satt FØR målingen:
snitt minst 0,02 over frossen og intet år mer enn 0,02 dårligere.

## F1 / P / R på MOT, per år
| kandidat | 2024 F1 (P/R) | 2025 F1 (P/R) | 2026 F1 (P/R) | snitt | mot frossen |
|---|---|---|---|---|---|
| frossen #2044 | 0,4545 (0,68/0,34) | 0,5143 (0,59/0,45) | 0,4762 (0,44/0,52) | 0,4817 | – |
| +prev_same_person | 0,4179 (0,61/0,32) | 0,5155 (0,53/0,51) | 0,5254 (0,52/0,53) | 0,4863 | +0,005 |
| **+fire repotrekk (repo4)** | **0,5057 (0,51/0,50)** | **0,5309 (0,68/0,43)** | **0,5120 (0,48/0,55)** | **0,5162** | **+0,035** |
| hybrid V1 | 0,4048 (0,43/0,39) | 0,5189 (0,56/0,48) | 0,4812 (0,43/0,55) | 0,4683 | −0,013 |
| hybrid V1p | 0,4023 (0,41/0,40) | 0,5193 (0,57/0,47) | 0,4923 (0,44/0,55) | 0,4713 | −0,010 |
| hybrid V2 | 0,4072 (0,43/0,39) | 0,5474 (0,57/0,53) | 0,5161 (0,48/0,55) | 0,4902 | +0,009 |
| NBIM-repoets hybrid alene | 0,4072 (0,43/0,39) | 0,5091 (0,64/0,42) | 0,5455 (0,58/0,52) | 0,4873 | +0,006 |

## Differanse mot frossen per år, 95 % KI
| kandidat | 2024 | 2025 | 2026 | snitt 3 år |
|---|---|---|---|---|
| person | −0,037 [−0,133; +0,058] | +0,001 [−0,042; +0,050] | +0,049 [+0,016; +0,090] | +0,005 [−0,035; +0,041] |
| repo4 | +0,051 [−0,065; +0,160] | +0,017 [−0,031; +0,068] | +0,036 [−0,008; +0,085] | +0,035 [−0,005; +0,078] |
| V1 | −0,050 [−0,174; +0,090] | +0,005 [−0,025; +0,040] | +0,005 [−0,035; +0,051] | −0,013 [−0,057; +0,037] |
| V1p | −0,052 [−0,171; +0,075] | +0,005 [−0,018; +0,034] | +0,016 [−0,019; +0,058] | −0,010 [−0,050; +0,035] |
| V2 | −0,047 [−0,173; +0,092] | +0,033 [−0,039; +0,103] | +0,040 [−0,007; +0,095] | +0,009 [−0,040; +0,063] |
| NBIM-hybrid | −0,047 [−0,173; +0,092] | −0,005 [−0,063; +0,056] | +0,069 [+0,007; +0,133] | +0,006 [−0,043; +0,058] |

## Byttregelen
- **repo4 består begge krav**: snitt 0,5162 er +0,035 over 0,4817, og den er bedre enn frossen alle tre år
  (verste år +0,017). Den er den eneste kandidaten som er bedre hvert år.
- Ærlig forbehold: KI for snittet [−0,005; +0,078] krysser 0. 4 % av trekkene gir repo4 dårligere enn
  frossen, og 23 % gir under +0,02. Den består regelen, men gevinsten er ikke statistisk sikker.
- Alle andre stryker. Hybridene og person faller med 0,04–0,05 i 2024. Gevinsten i 2026 holdt altså ikke
  bakover i tid, og NBIM-hybridens 0,5455 i 2026 er en ettårstopp.
- Om byttet skjer etter frysen kl. 16 må ordføreren/dommeren avgjøre. Jeg har ikke rørt frosne filer.
  Står frossen, går repo4 (0,5162 snitt) inn i NESTE_VERSJON.

## Sidefunn (ikke på kandidatlista, ikke en del av regelen)
Frossen med grensen valgt på val etter F1 MOT i stedet for avvik-F1 (ref-linja i `rull3.py`) gir
0,497/0,514/0,488, snitt 0,4997 (+0,018). Det er under 0,02, så den stryker.

## Reproduser (arbeid/oppgave_2567/)
- `bash kjor_repo4.sh`: repo4 for 2024/2025 (`abl_rull.py --repo prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate`). 2026 = oppgave_2490/repo4_test.csv.
- `uv run --project ../oppgave_2531 python rull3.py T`: V1/V1p/V2 og NBIM-hybrid for test T. 2026 gjenskaper #2495 (V2 0,5161).
- `bash benk.sh > benk.txt`: offisiell måler + KI per år. `bash ki_alle.sh`: KI for snittet over tre år (`ki_snitt.py`).
- Tavla: forsøk #1203–#1209 (ett per kandidat med tall per år i `--vinduer`).

## Ekstra kontroll: fjerde år 2023 (val 2022), utenfor regelen
Frossen-oppsettet 0,3303 (P 0,26 / R 0,47) og repo4 0,3350 (P 0,27 / R 0,44), diff +0,005 [−0,035; +0,049].
Begge er svake i 2023, men repo4 er ikke dårligere der heller. Med fire år er repo4 aldri under frossen.
(`full_2023_test.csv`, `repo4_2023_test.csv` i arbeid/oppgave_2567/.)
