# Case 1: presisjon og recall på MOT ved ulike terskler, frossen agent #2044 (#2376, smed4)

> **Merk (smed4, 15:20):** Denne fila erstattet ved en feil #2261-versjonen (smed2/smed, 14:05, samme navn, ikke i git). Tallene fra #2261 er gjenskapt under («Kontroll mot #2261»), og de stemmer på hvert punkt. Prosaen fra #2261 er tapt: linjene om #2254-sonen og #2032-tid. Kjør `arbeid/oppgave_2261/terskel.py` på nytt for å få dem tilbake. Den enda eldre #2084-tabellen står i `arbeid/oppgave_2261/c1_terskeltabell_2084_gammel.md`.

Beslutningsstøtte, ingen modellendring. Den leverte svarfila `arbeid/hack/levering/kjor_agent_real_maskin_alene.csv` er brukt uendret. Bare `anbefaling = (p_avvik >= t)` er skrevet om, og hvert punkt er målt med `maaler_offisiell_v3.py --score mot`. Test 2026: 1539 saker med fasit, 58 MOT mot styret.
**Aksept:** ved levert terskel 0,9188 gir måleren **0,476190** (TP 30, FP 38, FN 28). Det er samme tall som `oppgave_2103/full_test.csv` og hovedtallet. Kontroll: 0 rader der levert anbefaling avviker fra `p_avvik >= 0,9188`.

## Test 2026 (v3, MOT mot styret)
| terskel P(avvik) | flagget MOT | riktige MOT (TP) | falske MOT (FP) | oversette MOT (FN) | presisjon | recall | F1 |
|---|---|---|---|---|---|---|---|
| 0,70 | 404 | 44 | 360 | 14 | 0,109 | 0,759 | 0,190 |
| 0,80 | 217 | 41 | 176 | 17 | 0,189 | 0,707 | 0,298 |
| 0,90 | 85 | 34 | 51 | 24 | 0,400 | 0,586 | 0,476 |
| **0,9188 (levert)** | **68** | **30** | **38** | **28** | **0,441** | **0,517** | **0,476** |
| 0,94 | 56 | 29 | 27 | 29 | 0,518 | 0,500 | 0,509 |
| 0,96 | 39 | 26 | 13 | 32 | 0,667 | 0,448 | 0,536 |
| 0,98 | 19 | 16 | 3 | 42 | 0,842 | 0,276 | 0,416 |

## Samme terskler på val 2025, der terskelen ble valgt (modell trent <2025; 1909 saker, 99 MOT)
| terskel | flagget | TP | FP | FN | P | R | F1 |
|---|---|---|---|---|---|---|---|
| 0,70 | 394 | 68 | 326 | 31 | 0,173 | 0,687 | 0,276 |
| 0,80 | 244 | 64 | 180 | 35 | 0,262 | 0,647 | 0,373 |
| 0,90 | 85 | 46 | 39 | 53 | 0,541 | 0,465 | 0,500 |
| **0,9188 (levert)** | **74** | **45** | **29** | **54** | **0,608** | **0,455** | **0,520** |
| 0,94 | 61 | 38 | 23 | 61 | 0,623 | 0,384 | 0,475 |
| 0,96 | 44 | 29 | 15 | 70 | 0,659 | 0,293 | 0,406 |
| 0,98 | 26 | 20 | 6 | 79 | 0,769 | 0,202 | 0,320 |

## Hva koster færre falske MOT? (test 2026, regnet fra levert terskel)
- **Strammere til 0,96:** 25 færre falske MOT (38 → 13) koster 4 tapte MOT (30 → 26). Mennesket leser 39 flagg i stedet for 68.
- **Strammere til 0,98:** 35 færre falske MOT koster 14 tapte MOT. Agenten finner da bare 28 % av MOT-stemmene.
- **Løsere til 0,90:** 4 flere riktige MOT koster 13 flere falske.
- **Løsere til 0,80:** 11 flere riktige MOT koster 138 flere falske. Det er 217 flagg å lese per 1539 saker.

## Ærlig lesning
- På test gir 0,94 og 0,96 høyere F1 enn levert terskel (0,509 og 0,536 mot 0,476). Det ser vi bare fordi vi kjenner fasiten for 2026. På val, der terskelen ble låst, var 0,96 klart dårligere (0,406 mot 0,520). Vi kunne altså ikke ha visst det på forhånd. Å bytte terskel nå ville vært å velge på test, så levert terskel står.
- For brukeren betyr det at kurven er bratt mellom 0,90 og 0,96. Det er der en forvalter som vil ha færre falske alarmer bør stille inn. Over 0,96 faller recall fort.
- Ruting til menneske (bånd rundt terskelen) står i den eldre tabellen `arbeid/hack/c1/terskeltabell_ut.md` (#2084). Denne tabellen er uten bånd, slik måleren teller hovedtallet.

## Usikkerhet (bootstrap per møte, 140 møter, 2000 trekk, parret mot levert terskel)
| terskel | F1 test | 95 %-intervall F1 | F1 minus levert | 95 %-intervall forskjell |
|---|---|---|---|---|
| 0,70 | 0,190 | 0,137–0,252 | −0,286 | −0,380 til −0,181 |
| 0,80 | 0,298 | 0,214–0,384 | −0,178 | −0,259 til −0,091 |
| 0,90 | 0,476 | 0,345–0,592 | −0,001 | −0,051 til +0,060 |
| **0,9188 (levert)** | **0,476** | **0,344–0,594** | 0 | |
| 0,94 | 0,509 | 0,368–0,632 | +0,033 | +0,002 til +0,063 |
| 0,96 | 0,536 | 0,388–0,667 | +0,060 | −0,003 til +0,119 |
| 0,98 | 0,416 | 0,250–0,553 | −0,061 | −0,186 til +0,052 |

Telling uavhengig av måleren (`arbeid/oppgave_2376/bootstrap.py`, samme regel som v3), og den gir 30/38/28 ved levert terskel. Lesning: alt fra 0,90 til 0,96 er innenfor støyen for hovedtallet. Intervallet rundt 0,476 dekker målet 0,5. Løsere enn 0,85 er klart dårligere. På test er 0,94 så vidt bedre enn levert, men på val var den dårligere (0,475 mot 0,520). Vi har ingen grunn som ikke kommer fra testfasiten til å flytte terskelen.

## Kontroll mot #2261 (modellen kjørt på nytt via `c1_real.kjor_modell`, ikke den leverte fila)
`uv run --project arbeid/oppgave_2023 python arbeid/oppgave_2261/terskel.py` gir samme TP/FP/FN på test og val for 0,70, 0,80, 0,85, 0,90 og 0,9188. Den har også 0,95 (test P 0,569, R 0,500, F1 0,532, 51 flagget; val F1 0,461) og 0,97 (test P 0,742, R 0,397, F1 0,517, 31 flagget; val F1 0,376). Utskriften står i `arbeid/oppgave_2376/gjenskapt_2261.txt`. Den leverte svarfila og en ny kjøring av modellen gir altså samme tabell.

Kjør på nytt: `python3 -I arbeid/oppgave_2376/sveip.py` fra landsbymappen (utskrift i `arbeid/oppgave_2376/sveip_ut.txt`); `python3 -I arbeid/oppgave_2376/bootstrap.py` for usikkerheten.
