# Case 1: hva koster det å sende saker til et menneske (smed2, #2100)

Modell: frossen #2044 miks h2, grense T = 0,9188 (F1-maks på val 2025). Ruting: symmetrisk bånd rundt grensen, |logit(p) − logit(T)| < bredde.
Breddene for 0/5/10/15/20 % er **låst på val 2025** (0 / 0,609 / 0,946 / 1,309 / 1,570 i logit) og brukt uendret på test 2026. Ingen India-regel her (se #2079).
Kode: `arbeid/oppgave_2100/kost.py` (`cd arbeid/oppgave_2100 && uv run --project ../oppgave_2023 python kost.py`, ca. 3 s). Tabeller: `val.csv`, `test.csv`.

Kolonner: **F1 rest** = F1 på MOT for sakene agenten avgjør selv. **MOT hos menneske** = ekte MOT-stemmer blant de rutede. **Nytt lag** = MOT-rate i de sakene som kommer til fra forrige trinn.
**System F1 (øvre)** antar at mennesket avgjør alle rutede saker riktig, så det er en øvre grense, ikke et målt tall.

## Val 2025 (1909 saker, 103 MOT, snitt-rate 0,054)
| til menneske | rutet | F1 rest | P / R rest | MOT hos menneske | MOT-rate rutet | nytt lag | System F1 (øvre) |
|---|---|---|---|---|---|---|---|
| 0 % | 0 | 0,522 | 0,59 / 0,47 | 0 av 103 (0 %) | – | – | 0,522 |
| 5 % | 96 | 0,544 | 0,64 / 0,47 | 25 (24 %) | 0,260 | 0,260 | 0,667 |
| **10 %** | **191** | **0,514** | 0,63 / 0,44 | **41 (40 %)** | 0,215 | **0,168** | 0,727 |
| 15 % | 287 | 0,527 | 0,73 / 0,41 | 45 (44 %) | 0,157 | 0,042 | 0,762 |
| 20 % | 382 | 0,486 | 0,75 / 0,36 | 53 (51 %) | 0,139 | 0,084 | 0,789 |

## Test 2026, samme bredder (1539 saker, 66 MOT, snitt-rate 0,043)
| til menneske (mål fra val) | rutet (faktisk andel) | F1 rest | P / R rest | MOT hos menneske | MOT-rate rutet | nytt lag | System F1 (øvre) |
|---|---|---|---|---|---|---|---|
| 0 % | 0 | 0,482 | 0,47 / 0,50 | 0 av 66 (0 %) | – | – | 0,482 |
| 5 % | 84 (5,5 %) | 0,571 | 0,60 / 0,55 | 11 (17 %) | 0,131 | 0,131 | 0,646 |
| **10 %** | **170 (11,0 %)** | **0,627** | 0,77 / 0,53 | **17 (26 %)** | 0,100 | 0,070 | 0,735 |
| 15 % | 269 (17,5 %) | 0,636 | 0,78 / 0,54 | 27 (41 %) | 0,100 | 0,101 | 0,800 |
| 20 % | 393 (25,5 %) | 0,667 | 0,85 / 0,55 | 35 (53 %) | 0,089 | 0,065 | 0,860 |

## Anbefaling: 10 % til menneske (valgt på val)
Regel, satt før test ble sett: utvid båndet så lenge MOT-raten i det nye laget er minst **2 × snittet** (2 × 0,054 = 0,108), ellers lønner det seg ikke å bruke menneskets tid der.
På val: 0–5 % har 0,260 og 5–10 % har 0,168 (begge over 0,108), men 10–15 % har bare **0,042**, under snittet. Stopp ved 10 %.
Det gir mennesket ca. 190 saker i året, der 1 av 5 er en MOT-stemme, og 40 % av alle MOT-stemmene på val.

## Ærlig lesning
- **F1 på resten er ikke et godt mål for ruting.** Den svinger (val 0,49–0,54, ingen trend), fordi båndet tar ut både treff og bom nær grensen. På test stiger den (0,48 → 0,63), men det kan ikke brukes til å velge terskel: val viser ikke det samme.
- **Kostnaden** er det mennesket får: på test går 26 % av de ekte MOT-stemmene til mennesket ved 10 %, mot 40 % på val. Rutede saker har MOT-rate 0,10 på test (2,3 × snittet), mot 0,215 på val. Båndet virker, men svakere i 2026.
- På test ville 15 % gitt 10 MOT til (nytt lag 0,101), mens val sa 0,042. Det er støy med 66 MOT; vi bytter ikke terskel etter test.
- Testandelen blir 11 % og ikke 10 % fordi 2026 har flere saker nær grensen enn 2025. Det er en drift å nevne for juryen.
- System F1 (0,735 ved 10 %) forutsetter et feilfritt menneske. Det er et tak, ikke et resultat. Hovedtallet står: **0,48 for maskinen alene** på test 2026 i denne fila (pred_miks_h2.csv, 1539 saker). Det offisielle tallet 0,476 (#2090) er målt av dommeren på kald kopi; 0,006-avviket kommer trolig av en litt annen grense eller radliste, og jeg har ikke undersøkt det her.
