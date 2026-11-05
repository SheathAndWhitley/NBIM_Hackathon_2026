# Case 1: usikre saker og alle India-saker til et menneske (smed2, #2079)

Modell: frossen #2044 miks h2, grense T = 0,9188 (F1-maks på val 2025, samme rutenett som train.py). Modellen er ikke endret.
Regel: saken går til et menneske når |logit(p) − logit(T)| < bredde, **eller** når country == India. Grunn i svaret for India:
«MOT-rate i India doblet i 2025 (0,046 -> 0,102), modellen fanget 0 av 14 på val». Duality-trekket er ikke bygd (forkastet, #2075).
Kode: `arbeid/oppgave_2079/ruting.py`. Kjør med `cd arbeid/oppgave_2079 && uv run --project ../oppgave_2023 python ruting.py [--test 0.10]` (ca. 3 s).

## Val 2025 (1909 saker, 103 MOT, maskin alene F1-MOT 0,5217)
| usikre (andel av val) | India | rutet | andel | MOT blant rutede | MOT-rate rutet | F1-MOT maskin på resten | P / R resten |
|---|---|---|---|---|---|---|---|
| 0 % | nei | 0 | 0 % | 0 | – | 0,522 | 0,59 / 0,47 |
| 0 % | ja | 137 | 7,2 % | 14 | 0,102 | 0,568 | 0,60 / 0,54 |
| 5 % | nei | 96 | 5,0 % | 25 | 0,260 | 0,544 | 0,64 / 0,47 |
| 5 % | ja | 224 | 11,7 % | 37 | 0,165 | 0,602 | 0,65 / 0,56 |
| **10 %** | nei | 191 | 10,0 % | 41 | 0,215 | 0,514 | 0,63 / 0,44 |
| **10 %** | **ja (valgt)** | **305** | **16,0 %** | **50 av 103** | **0,164** | **0,563** | 0,63 / 0,51 |
| 15 % | ja | 394 | 20,6 % | 53 | 0,135 | 0,578 | 0,73 / 0,48 |

Valg av bånd (på val, før test): båndet utvides lag for lag så lenge MOT-raten i det nye laget er minst dobbelt snittet (0,054).
Lag 0–3 %: 0,264, 3–5 %: 0,265, 5–10 %: 0,160, 10–15 %: **0,034** (under snittet). Stopp ved 10 % → bredde 0,946 i logit.
Merk: F1 på resten er ikke målet for ruting. Når saker nær grensen tas ut, forsvinner både treff og bom, så F1 på resten svinger (0,51–0,60).
Målet er hvor mange MOT mennesket får se per rutet sak.

## Test 2026, kjørt én gang (1539 saker, 66 MOT, maskin alene F1-MOT 0,482)
| regel | rutet | andel | MOT blant rutede | MOT-rate rutet | F1-MOT maskin på resten | P / R resten |
|---|---|---|---|---|---|---|
| usikre 10 % (bånd fra val) | 170 | 11,0 % | 17 | 0,100 | 0,627 | 0,77 / 0,53 |
| usikre 10 % + India (valgt) | 238 | 15,5 % | 19 | 0,080 | 0,625 | 0,76 / 0,53 |

India på test 2026: 103 saker, 4 MOT (rate 0,039, under testsnittet 0,043). Maskinen fanget 1 av dem, og India-regelen gir mennesket bare 2 MOT ekstra utover båndet.

## Ærlig lesning
- Båndet rundt grensen holder på test: de 170 usikre sakene har MOT-rate 0,10, mot 0,043 i snitt (2,3×). Det er svakere enn på val (0,215).
- **India-regelen holder ikke på test.** Doblingen i 2025 kom ikke igjen i 2026. Regelen sender 68 ekstra saker til mennesket og gir 2 MOT. Den er bygd etter ordre og står i koden, men jeg anbefaler at juryteksten sier dette rett ut. Alternativet er å slå regelen av (`bruk_india=False`) før frys. Ordføreren avgjør.
- «F1 på resten» (0,63) er ikke systemets F1, og den skal ikke stå som hovedtall. Hovedtallet er fortsatt 0,48 for maskinen alene på alle sakene.
- Per-sak-fil for test med grunn: `arbeid/oppgave_2079/test_ruting_2026.csv` (kolonnene til_menneske og grunn).
