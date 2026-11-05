# Case 1: ablasjon av MOT-modellen, hvilke signaler bærer (smed2, #2045)

Modell: beste fra #2044 (logreg tfidf+kategorier ⊕ LGBM, rangsnitt, løpende historikk `--hist 2`, lekkasjefri).
Én featuregruppe fjernes om gangen. Samme grense-regel som #2044: C og grense velges på VAL 2025 (trent <2025),
test 2026 kjøres én gang med den grensen. real_votes test 2026: 1539 rader, 66 MOT.
Siste kolonne: parret bootstrap (2000 trekk) av F1-forskjellen mot full modell på test.
Full modell reproduserer 0,482 fra #2044.

| fjernet gruppe | VAL F1 | TEST F1-MOT | P | R | flagget | PR-AUC | diff mot full [95 % KI] |
|---|---|---|---|---|---|---|---|
| ingen (full) | 0.522 | **0.482** | 0.46 | 0.50 | 71 | 0.525 | 0 |
| tekst (tfidf på forslagsteksten) | 0.506 | 0.488 | 0.53 | 0.45 | 57 | 0.498 | +0.006 [-0.047, +0.050] |
| selskapshistorikk (selskap, selskap+tekst) | 0.494 | 0.372 | 0.28 | 0.56 | 133 | 0.504 | **-0.109 [-0.169, -0.050]** |
| teksthistorikk (samme tekst i andre selskaper) | 0.511 | 0.469 | 0.43 | 0.52 | 79 | 0.508 | -0.012 [-0.040, +0.020] |
| all historikk | 0.337 | 0.282 | 0.19 | 0.52 | 175 | 0.429 | **-0.199 [-0.277, -0.121]** |
| forslagstype (proposal_type) | 0.511 | 0.504 | 0.52 | 0.48 | 61 | 0.502 | +0.022 [-0.015, +0.055] |
| forslagsstiller (proponent) | 0.514 | 0.500 | 0.50 | 0.50 | 66 | 0.520 | +0.018 [+0.000, +0.038] |
| land (country, market) | 0.492 | 0.469 | 0.48 | 0.45 | 62 | 0.490 | -0.013 [-0.073, +0.043] |
| styrets anbefaling (mgmt_rec) | 0.525 | 0.496 | 0.49 | 0.50 | 67 | 0.514 | +0.015 [+0.003, +0.031] |
| bare historikk igjen | 0.473 | 0.460 | 0.55 | 0.39 | 47 | 0.422 | -0.022 [-0.113, +0.061] |
| bare tekst igjen (logreg) | 0.390 | 0.409 | 0.33 | 0.55 | 110 | 0.424 | -0.072 [-0.157, +0.017] |

## Én setning per gruppe (til juryen)
- **Selskapshistorikk:** Det sterkeste signalet er om NBIM har stemt mot styret i samme selskap før; uten det faller F1 fra 0,48 til 0,37, og uten all historikk til 0,28.
- **Tekst:** Forslagsteksten alene gir 0,41, men når historikken er med legger den nesten ingenting til (±0,05, innenfor støyen).
- **Forslagstype og forslagsstiller:** Typen sak og hvem som fremmet den er allerede fanget av teksten og historikken; å fjerne dem endrer ikke resultatet målbart.
- **Land:** Land og marked bidrar lite (−0,01, innenfor støyen); modellen er ikke en landsregel.
- **Styrets anbefaling:** Nesten konstant i dataene, så den bærer ingenting.

## Ærlig vurdering
- Med 66 MOT-saker i test er ±0,05 F1 støy. Bare historikken er signifikant (KI over null).
- Noen fjerninger ser litt bedre ut på test (type 0,504, stiller 0,500), men de er dårligere på VAL. Vi velger ikke modell på test, så full modell står. Eneste kandidat for forenkling som også holder på VAL er å fjerne styrets anbefaling (0,525 vs 0,522), en ren forenkling uten gevinst.
- Konsekvens for agenten: begrunnelsen for et MOT-flagg bør først vise selskapets tidligere MOT-stemmer (det er det modellen faktisk bruker), deretter retningslinje-sitatet.

Kjøring: `cd arbeid/oppgave_2045 && uv run --project ../oppgave_2023 python train.py ../../state/opplastet/20261105_114241_real_votes.csv --variant miks --hist 2 --uten <gruppe,...>`; tabell: `python tabell.py`. Logger og prediksjoner i `arbeid/oppgave_2045/`.
