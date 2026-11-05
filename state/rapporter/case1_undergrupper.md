# Case 1 (#1992): uten lekkasjen holder fallskjerm-svakheten, men "uten NBIM-historikk" er ikke lenger svak, og på val 2025 er lederen bare like god som gulvet i saker med historikk

**Hva er målt:** `grupper.py` fra #1989 er kjørt på nytt på dommerens prediksjoner fra #1988 (`arbeid/oppgave_1988/{full,a,b}_data_v3*.csv`). Det er ingen trening. Variant b (uten float og med PvP 100 d) er den som leveres kl. 13, så tabellene under gjelder b. Full reproduserer tabellene fra #1989 nøyaktig, og a ligger mellom full og b. Kjør på nytt med `cd arbeid/oppgave_1992 && uv run --project ../kandidater/smed2_c1_mot python grupper.py b` og `uv run python ruting_alt.py b`. Rå utdata for alle tre ligger i `ut_full.md`, `ut_a.md` og `ut_b.md`.

## Hva endret seg fra full til b

| Gruppe | full test / val | a test / val | b test / val | gulv test / val |
|---|---|---|---|---|
| Alle | 0,51 / 0,42 | 0,51 / 0,40 | 0,49 / 0,40 | 0,38 / 0,36 |
| Uten NBIM-historikk | 0,49 / **0,29** | 0,49 / 0,36 | 0,49 / **0,40** | 0 / 0 |
| Med NBIM-historikk | 0,51 / 0,43 | 0,51 / 0,40 | 0,49 / 0,40 | 0,41 / 0,39 |
| Golden parachute | 0,42 / 0,39 | 0,40 / 0,39 | 0,40 / 0,39 (P 0,25) | 0,30 / 0 |
| Liten (float < median) | 0,49 / 0,37 | 0,45 / 0,34 | 0,43 / 0,36 | 0,26 / 0,31 |
| Stor | 0,56 / 0,43 | 0,56 / 0,41 | 0,55 / 0,41 | 0,47 / 0,41 |

1. **Golden parachute holder som svakhet.** F1 er 0,40 og 0,39. På val gir 24 varsler bare 6 treff (P 0,25). Gruppen er liten (n = 46 og 34, 15 og 7 MOT). Regelen om å alltid sende den til et menneske står.
2. **"Uten NBIM-historikk" er ikke lenger svak.** På val gikk F1 fra 0,29 til 0,40, som er samme nivå som saker med historikk. Det er 17 MOT, så tallet er usikkert. Svakheten i #1989 var trolig delvis en effekt av float-kjennetegnet. Gruppen er fortsatt der modellen slår gulvet mest: +0,49 [0,26; 0,67] på test og +0,40 [0,17; 0,59] på val.
3. **Ærlig funn for juryen:** I saker *med* historikk er b på val bare +0,02 [−0,07; 0,10] over gulvet. Hos store selskap er forskjellen 0,00. På val kommer modellens fordel nesten bare fra selskap NBIM ikke har stemt på før, og fra fallskjerm. På test er fordelen +0,08 [0,03; 0,14] også med historikk.
4. Små selskap ligger fortsatt 0,05–0,12 under store i begge år. Ikke-USA er fortsatt støy (4–8 MOT).

## Rutingen på nytt (variant b)

| Variant | Sett | Regel | til menneske | MOT der | modell F1 auto | gulv F1 auto |
|---|---|---|---|---|---|---|
| b | TEST 2026 | ingen | 0 (0 %) | 0 | 0,49 | 0,38 |
| b | TEST 2026 | uten hist + fallskjerm | 146 (12 %) | 31 | 0,51 | 0,41 |
| b | TEST 2026 | bare fallskjerm | 46 (4 %) | 15 | 0,50 | 0,39 |
| b | TEST 2026 | bare uten hist | 109 (9 %) | 19 | 0,49 | 0,41 |
| b | VAL 2025 | ingen | 0 (0 %) | 0 | 0,40 | 0,36 |
| b | VAL 2025 | uten hist + fallskjerm | 148 (10 %) | 24 | 0,40 | 0,40 |
| b | VAL 2025 | bare fallskjerm | 34 (2 %) | 7 | 0,40 | 0,37 |
| b | VAL 2025 | bare uten hist | 119 (8 %) | 17 | 0,40 | 0,39 |

- **Regelen fra #1989 (uten historikk + fallskjerm)** sender 10–12 % av sakene til et menneske. MOT-andelen i den køen er 16–21 %. F1 på den automatiske delen er 0,51 på test (fra 0,49) og 0,40 på val (uendret). Med full var det +0,02 i begge år. Uten lekkasjen gir regelen altså ingen gevinst på val.
- Regelen fjerner nettopp de sakene der gulvet har 0. Derfor er **modell og gulv like på den automatiske delen på val (0,40 mot 0,40)**. Det betyr ikke at modellen er verdiløs: fordelen ligger i sakene som rutes, og der får mennesket modellens varsel som støtte.
- **Anbefaling:** Behold fallskjerm → menneske, fordi det er en målt svakhet. Begrunn "uten NBIM-historikk → menneske" med styring og ikke med at modellen treffer dårlig: agenten har ingen egen presedens å sitere. Ruter vi bare modellens MOT-varsler uten historikk (18 saker), får mennesket en liten kø med ca. 40–50 % treff. Juryen skal ikke få høre at modellen er svak der. Det er den ikke lenger.
- Konfidensrutingen fra smed2 (#1955) bør måles på b-prediksjonene (`p_avvik` i `arbeid/oppgave_1988/b_*.csv`) før modellfrysen kl. 16, siden den er laget på full.

## Variant b per undergruppe (bootstrap 1000, parret)

#### TEST 2026

| Gruppe | n | MOT | modell F1 | P | R | ant. MOT-varsler | gulv F1 | gulv P | gulv R | diff F1 [95 %] |
|---|---|---|---|---|---|---|---|---|---|---|
| Alle | 1246 | 129 | **0,49** | 0,47 | 0,52 | 143 | 0,38 | 0,35 | 0,43 | 0,11 [0,05; 0,17] |
| USA (ISIN US) | 1152 | 121 | **0,49** | 0,46 | 0,52 | 138 | 0,39 | 0,35 | 0,45 | 0,09 [0,03; 0,15] |
| Ikke-USA (ISIN ellers) | 94 | 8 | **0,62** | 0,80 | 0,50 | 5 | 0,17 | 0,25 | 0,12 | 0,45 [0,00; 0,78] |
| Stor (float ≥ median 9.0 mrd USD) | 522 | 70 | **0,55** | 0,51 | 0,60 | 82 | 0,47 | 0,42 | 0,54 | 0,08 [0,01; 0,15] |
| Liten (float < median) | 529 | 38 | **0,43** | 0,47 | 0,39 | 32 | 0,26 | 0,25 | 0,26 | 0,17 [0,06; 0,29] |
| Ukjent markedsverdi (ikke i SEC) | 195 | 21 | **0,40** | 0,34 | 0,48 | 29 | 0,29 | 0,26 | 0,33 | 0,11 [-0,05; 0,27] |
| Med NBIM-historikk | 1137 | 110 | **0,49** | 0,46 | 0,53 | 125 | 0,41 | 0,35 | 0,50 | 0,08 [0,03; 0,14] |
| Uten NBIM-historikk | 109 | 19 | **0,49** | 0,50 | 0,47 | 18 | 0,00 | 0,00 | 0,00 | 0,49 [0,26; 0,67] |
| Årlig say-on-pay | 1200 | 114 | **0,50** | 0,48 | 0,54 | 128 | 0,39 | 0,34 | 0,46 | 0,11 [0,06; 0,17] |
| Golden parachute / fusjon | 46 | 15 | **0,40** | 0,40 | 0,40 | 15 | 0,30 | 0,60 | 0,20 | 0,10 [-0,10; 0,36] |

#### VAL 2025

| Gruppe | n | MOT | modell F1 | P | R | ant. MOT-varsler | gulv F1 | gulv P | gulv R | diff F1 [95 %] |
|---|---|---|---|---|---|---|---|---|---|---|
| Alle | 1506 | 136 | **0,40** | 0,36 | 0,46 | 172 | 0,36 | 0,39 | 0,34 | 0,04 [-0,05; 0,13] |
| USA (ISIN US) | 1411 | 132 | **0,41** | 0,37 | 0,46 | 165 | 0,37 | 0,40 | 0,34 | 0,04 [-0,05; 0,13] |
| Ikke-USA (ISIN ellers) | 95 | 4 | **0,18** | 0,14 | 0,25 | 7 | 0,20 | 0,17 | 0,25 | -0,02 [-0,16; 0,13] |
| Stor (float ≥ median 5.7 mrd USD) | 639 | 67 | **0,41** | 0,37 | 0,46 | 84 | 0,41 | 0,41 | 0,40 | 0,00 [-0,11; 0,12] |
| Liten (float < median) | 647 | 46 | **0,36** | 0,31 | 0,41 | 61 | 0,31 | 0,33 | 0,28 | 0,05 [-0,10; 0,19] |
| Ukjent markedsverdi (ikke i SEC) | 220 | 23 | **0,48** | 0,44 | 0,52 | 27 | 0,32 | 0,43 | 0,26 | 0,16 [-0,04; 0,36] |
| Med NBIM-historikk | 1387 | 119 | **0,40** | 0,36 | 0,46 | 154 | 0,39 | 0,39 | 0,39 | 0,02 [-0,07; 0,10] |
| Uten NBIM-historikk | 119 | 17 | **0,40** | 0,39 | 0,41 | 18 | 0,00 | 0,00 | 0,00 | 0,40 [0,17; 0,59] |
| Årlig say-on-pay | 1472 | 129 | **0,40** | 0,38 | 0,43 | 148 | 0,37 | 0,39 | 0,36 | 0,03 [-0,05; 0,12] |
| Golden parachute / fusjon | 34 | 7 | **0,39** | 0,25 | 0,86 | 24 | 0,00 | 0,00 | 0,00 | 0,39 [0,15; 0,61] |

| Sett | saker til menneske | MOT blant dem | automatisk n | auto MOT | modell F1 auto | gulv F1 auto |
|---|---|---|---|---|---|---|
| TEST 2026 | 146 (12 %) | 31 | 1100 | 98 | 0,51 | 0,41 |
| VAL 2025 | 148 (10 %) | 24 | 1358 | 112 | 0,40 | 0,40 |

---
*Den tidligere versjonen (#1989, full med lekkasje) ligger i `arbeid/oppgave_1992/gammel_1989.md`.*
