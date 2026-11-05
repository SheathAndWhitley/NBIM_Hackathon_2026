# Case 1: hvilke MOT-stemmer smed2s modell bommer på, val 2025 (arkitekt, #2067)

Modell: smed2 #2044/#1037 (miks LR+LGBM, løpende historikk `--hist 2`). Val-prediksjoner laget på nytt med en kopi av train.py som
stopper før test: `arbeid/oppgave_2067/val_pred.py` → `pred_val.csv`. **Test 2026 er ikke rørt.**
KP: forventet val-F1 0,5217 (smed2s rapport), fikk 0,5217 (P 0,59, R 0,47). 1909 rader, 103 MOT: **tp 48, fp 33, fn 55**.
Forbehold: grensen er valgt på val selv, så 0,52 er litt optimistisk. Alle varianter under er målt på samme måte og kan derfor sammenlignes.

## Bommer per gruppe (val 2025)
| gruppe | n | MOT | tp | fp | fn | F1 |
|---|---|---|---|---|---|---|
| **Styrevalg** | 903 | 63 | 28 | 22 | **35** | 0,50 |
| Say-on-pay | 84 | 12 | 8 | 4 | 4 | 0,67 |
| OTHER_MGMT (utnevnelser, lån §185/186) | 98 | 6 | 0 | 1 | 6 | 0,00 |
| Revisor | 173 | 6 | 2 | 0 | 4 | 0,50 |
| Styreforslag (Management) | 1887 | 99 | 45 | 29 | 54 | 0,52 |
| Aksjonærforslag | 22 | 4 | 3 | 4 | 1 | 0,55 |
| **India** | 137 | 14 | **0** | 1 | **14** | **0,00** |
| USA | 324 | 26 | 13 | 14 | 13 | 0,49 |
| Japan | 281 | 11 | 6 | 3 | 5 | 0,60 |
| Canada | 41 | 6 | 2 | 0 | 4 | 0,50 |
| Selskap med MOT før | 1207 | 93 | 46 | 28 | 47 | 0,55 |
| **Selskap med bare FOR før** | 604 | 7 | 0 | 3 | 7 | 0,00 |
| Ingen historikk | 98 | 3 | 2 | 2 | 1 | 0,57 |

Aksjonærforslag er ikke problemet: bare 22 av 1909 på val, og 99 av 103 MOT gjelder styrets egne forslag der styret anbefaler FOR.
Kode og alle enkeltbommer: `arbeid/oppgave_2067/feil.py` → `val_med_grupper.csv`.

## Tre feilmønstre
1. **MOT kommer i klynger per møte.** Fluence Energy har 8 MOT av 14 i ett møte og 0 truffet, med rang 512–879. Modellen flagget i stedet den ene direktøren NBIM stemte FOR (fp).
   GFL har 4 fn av 6 MOT. Det er hele styret som blir straffet (uavhengighet eller ansvar), ikke enkeltpersoner. 12 av 55 fn ligger i to møter.
2. **India: 0 av 14.** MOT-raten i India hoppet fra 0,046 (2024) til 0,102 (2025). Bommene er statseide selskaper (Indian Oil, IRFC, NMDC, Bharat Dynamics) og **styreleder og daglig leder i samme person** («Chairman and Managing Director», «Whole-time Director and Chairman»).
3. **Selskaper med bare FOR før:** 7 fn, 0 tp. Historikken trekker dem ned, så ingenting kan fange dem uten fakta utenfra (samme funn som dommer2 #1983 på v3).

## Mekanismer prøvd på val (samme grensevalg)
| variant | val F1 | flagget | Konklusjon |
|---|---|---|---|
| grunnlinje smed2 | 0,5217 | 81 | |
| **B: flagg for kombinert styreleder/daglig leder i tekst, +0,1 på p** | **0,5543** | 81 | **testes** |
| A: møteklumping, maks-p på andre forslag av samme type i møtet (w 0,1–0,5) | 0,50 → 0,28 | | forkastet |
| A': møtesnitt av p (w 0,1–0,5) | 0,50 → 0,40 | | forkastet |
| Trukket vinkel (aktuarfag): kredibilitetsvektet MOT-rate per land (k=50), w 0,5–2 | 0,52 → 0,37 | | forkastet: hoppet i India 2025 er nytt og finnes ikke i historikken |

**B er støttet av train, ikke bare av val.** Regex `chairman.*(managing director|whole-time|chief executive|ceo|president)` (begge rekkefølger) treffer 8 rader i train før 2025, alle i India, og 3 av dem er MOT (37,5 % mot 5,8 % i snitt). På val treffer den 5 rader, og alle 5 er MOT.
Løftet er +2 til 3 tp. Det er lite (n = 5) og har bred usikkerhet. Det følger NBIMs uttalte prinsipp om å skille styreleder og daglig leder, så det kan siteres i agenten.

## Til smedene før modellfrysen kl. 16
1. **Bygg B som feature, ikke som etterregel:** binær `duality` (regex over) inn i både LR og LGBM i `train.py`. Velg grensen på val som før og kjør test én gang. Forventet på val ca. +0,03. Gir test mindre, er det fordi n er lite, og det skal rapporteres ærlig.
2. **Ikke bygg møteklumping med p alene**: det sprer modellens egne feil til hele møtet (målt over). Et klyngesignal trenger fakta på styrenivå (andel uavhengige, ansvar for styret), og det finnes ikke i real_votes. Lukk sporet for denne frysen.
3. Til jurysvaret: India og «bare FOR før» er de blinde flekkene (18 av 55 fn, når de 3 i Indian Oil som hører til begge, telles én gang). De bør gå til et menneske i stedet for å telles som trygge FOR.
