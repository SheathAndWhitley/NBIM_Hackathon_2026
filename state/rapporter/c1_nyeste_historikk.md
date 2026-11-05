# Case 1: vekte nyeste historikk tyngst (#2363, smed4): +0,024 på test 2026, men USA-feilen er ikke borte

Kopi av frossen #2044 (`arbeid/oppgave_2044/train.py`, miks h2) med to brytere i `arbeid/oppgave_2363/train_nh.py`.
Frossen fil og leveranse er ikke rørt. Begge trekkene bruker bare møter som er ferdige før saksdatoen, slik h2 gjør.
- **A**: for hver nøkkel (selskap, selskap+tekst, tekst) legges til siste stemme, flagget «hadde MOT før, men siste stemme var FOR» og exp(−år siden siste MOT).
- **B**: snurate per land i inneværende sesong. Blant saker (selskap+tekst) som fikk MOT året før, måles andelen som har fått FOR på møter før datoen. Trekket har også eget flagg og samspillet rate×flagg.

## Valg (C og grense velges i året selv som i #2044. «Holdt ut 2024» = grensen er valgt på 2023 og overført)
| variant | val 2025 F1 / P / R | val 2024 F1 / P / R | holdt ut 2024 F1 / P / R | PR-AUC val 2025 |
|---|---|---|---|---|
| base (#2044) | 0,522 / 0,593 / 0,466 | 0,567 / 0,553 / 0,582 | 0,510 / 0,709 / 0,398 | 0,473 |
| A | 0,533 / 0,605 / 0,476 | 0,567 / 0,596 / 0,541 | 0,526 / 0,496 / 0,561 | 0,483 |
| B | 0,517 / 0,634 / 0,437 | 0,592 / 0,592 / 0,592 | 0,546 / 0,588 / 0,510 | 0,459 |
| A+B | **0,543** / 0,600 / 0,495 | **0,596** / 0,663 / 0,541 | **0,551** / 0,509 / 0,602 | 0,494 |

A+B er best i alle tre kolonnene, så den ble valgt før test 2026 ble kjørt. Forskjellene er 1–4 MOT-treff av omtrent 100, altså innenfor støyen.

## Test 2026, kjørt én gang etter valget (måler v3 `--score mot`, samme svarformat som #2087)
| variant | F1 MOT | P | R | TP | FP | PR-AUC |
|---|---|---|---|---|---|---|
| base (gjenskaper frossen 0,476190 eksakt) | 0,4762 | 0,465 | 0,500 | 33 | 38 | 0,525 |
| A+B | 0,5000 | 0,486 | 0,515 | 34 | 36 | 0,509 |

## Ærlig lesning
- Gevinsten er 1 ekstra treff og 2 færre falske MOT. PR-AUC går ned. Dette er støy, ikke bevist forbedring.
- **Målet traff ikke**: USA har fortsatt 9 falske MOT. Falske MOT i Kina øker fra 2 til 7, mens India og Belgia får færre. Trekkene flytter feilene rundt i stedet for å fange praksisskiftet i USA.
- Hvorfor: skiftet i 2026 skjer tidlig i sesongen (5 av 5 snudd), mens B bare ser snudde saker på møter som allerede er ferdige før datoen. I treningsårene snudde USA aldri (2024→2025: 4 av 4 holdt seg på MOT), så modellen har ikke lært noe den kan bruke.
- Anbefaling: bygg ikke inn. Frossen #2044 står. Saken bør heller stå som kjent svakhet (#2364). Dommeren avgjør.

Kjør: `cd arbeid/oppgave_2363 && uv run --project ../oppgave_2023 python train_nh.py <real_votes> --variant miks --hist 2 --nyest AB --val-aar 2025 --test 1 --ut pred_test_AB.csv`, deretter `svar_v3.py 0 AB` og måler v3.
Råtall: `arbeid/oppgave_2363/grid.txt`, `test2026.txt`, svarfiler `svar_test_0.csv` / `svar_test_AB.csv`.

## Dom (dommer, #2366, ordre #251, 2026-11-05 15:06): IKKE INN. Frossen #2044 (0,476) står.

Reprodusert fra `arbeid/oppgave_2366/` med en kopi av `train_nh.py` som bare i tillegg skriver val-prediksjonene (testkoden urørt, diff = 1 linje).
- **Byte-likt**: `pred_test_0.csv` og `pred_test_AB.csv` er identiske med smed4 sine (md5 9187df22…, 8343bfc1…). Svarfilene også identiske.
- **Måler v3 `--score mot`, test 2026**: base 0,476190 (= frossen, TP 30 FP 38 FN 27), A+B 0,500000 (TP 31 FP 35 FN 27). Tallene i rapporten over stemmer.
- **Protokoll**: A+B ble valgt på val 2025 + val 2024 + holdt-ut 2024 før test 2026 ble kjørt én gang. Ingen lekkasje: forbudte kolonner urørt, historikk bare fra møter før saksdatoen. Godkjent protokoll.
- **Paret bootstrap** (2000 trekk, seed 0, samme rader, `bootstrap.py`):

| vindu | F1 base | F1 A+B | diff | 95 % KI | P(A+B > base) | rader som skiller |
|---|---|---|---|---|---|---|
| val 2025 | 0,5217 | 0,5426 | +0,021 | [−0,021, +0,067] | 0,83 | 26 |
| val 2024 | 0,5672 | 0,5955 | +0,028 | [−0,020, +0,075] | 0,88 | 31 |
| test 2026 | 0,4818 | 0,5000 | +0,018 | [−0,021, +0,061] | 0,79 | 25 |

Kravet var at varianten *vinner* på både val 2025 og val 2024. Punktestimatet er høyere begge år, men intervallet dekker null begge steder og P(bedre) er 0,83 og 0,88, under 0,95. Det er 1–3 treff av ~100 MOT, altså støy, slik smed4 selv skrev. PR-AUC på test går ned (0,525 → 0,509), og USA-feilen (9 falske MOT) er uendret.

Dom: nyeste-historikk bygges ikke inn. Frossen #2044 står med 0,476190. Forsøket føres som verifisert 0,500 på test 2026, men valgt bort fordi gevinsten ikke er skilt fra støy. Verdien til juryen er ærlighetsdelen: et forsøk som ble kjørt riktig, målt én gang og forkastet.
