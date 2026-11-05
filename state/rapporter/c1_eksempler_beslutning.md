# Case 1: ett eksempel per beslutningstype fra den frosne agenten (#2411, smed3 05.11)

Generert av `arbeid/oppgave_2411/eksempler.py` fra `/tmp/k2377_0.15_0.85/ut` (kald kjøring med `levering/fremmed.sh`, frossen #2044 miks h2, bånd [0,15; 0,85)).
Kontroll: `_pred_uten_ruting.csv` er byte-identisk med levert `kjor_agent_real_maskin_alene.csv` (sha256 22ac6717e128…).
Måler v3 (`--score mot`, test 2026): **F1 MOT 0.476190** (TP 30, FP 38, FN 28); 1539 saker med fasit, 58 ekte MOT, 183 til menneske (11.9 %).
Utvalget er deterministisk, ikke håndplukket: følg styret = lavest P(MOT); MOT = auto-MOT med høyest sitatlikhet; til menneske = P(MOT) nærmest 0,5.
Kandidater: følg styret 1338, auto-MOT med sitat 9, til menneske pga. bånd 122.

## 1. Følg styret

- Sak: `2009896|1`, Electrolux AB, møte 2026-03-25: «Elect Chair of Meeting»
- Styret anbefaler FOR. Agenten sier **FOR**, kalibrert P(MOT) 0.0, til menneske: nei.
- Retningslinje NBIM 0.0.3 (NBIM Global Voting Guidelines): «Our starting point when deciding how to vote is to support the board. We participate in electing the board and entrust it with running the company.»
  Grunnlag: følger styret: NBIMs utgangspunkt er å støtte styret.
- Fasit 2026 (ikke sett av agenten): NBIM stemte FOR, med styret → agenten traff.

## 2. MOT (agenten stemmer mot styret selv)

- Sak: `2040395|11`, Global Power Synergy Public Company Limited, møte 2026-04-01: «Other Business»
- Styret anbefaler FOR. Agenten sier **MOT**, kalibrert P(MOT) 1.0, til menneske: nei.
- Retningslinje NBIM 5.2.1 (NBIM Global Voting Guidelines): «The board should use the annual report to present a fair, sensible and clear assessment of the company. The report should be reflective of the prior year, and include material risk factors.»
  Grunnlag: BM25 1012.0; type OTHER_BUSINESS: 33/33 tidligere MOT-begrunnelser i 5.2; nabo-begrunnelsen i 5.2; regler i seksjonen et menneske bør sjekke: 5.2.3, 5.2.4.
- Tidligere NBIM-begrunnelse (bare sitat, aldri feature; likhet 1.4): «We will not support an agenda item if the information disclosed is insufficient to make an informed decision.» (NBIMs begrunnelse 2020, Global Power Synergy Public Company Limited: «Other Business»).
- Fasit 2026 (ikke sett av agenten): NBIM stemte MOT, mot styret → agenten traff.

## 3. Til menneske

- Sak: `2033896|36`, Volkswagen AG, møte 2026-06-18: «Elect Hans Dieter Poetsch to the Supervisory Board»
- Styret anbefaler FOR. Agenten sier **MOT**, kalibrert P(MOT) 0.5217, til menneske: ja (usikker: kalibrert P(MOT) 0.52 i båndet [0.15, 0.85)).
- Retningslinje NBIM 1.1.1 (NBIM Global Voting Guidelines): «The board should guide company strategy and monitor management performance without conflicts of interest.»
  Grunnlag: BM25 43.7; type DIRECTOR_ELECTION: 74/277 tidligere MOT-begrunnelser i 1.1; nabo-begrunnelsen i 1.1; posisjonsnotat (fra nabo-begrunnelsen): Board independence (NBIM-PP2).
- Tidligere NBIM-begrunnelse (bare sitat, aldri feature; likhet 1.123): «The board should guide company strategy and monitor management performance without conflicts of interest. A majority of shareholder-elected board members in a non-controlled company should be independent of management, dominant shareholders, and related third parties. In a majority-controlled company, at least a third of board members should be independent.» (NBIMs begrunnelse 2021, Volkswagen AG: «Elect Hans Poetsch to the Supervisory Board»).
- Fasit 2026 (ikke sett av agenten): NBIM stemte MOT, mot styret.

## Slik gjenskapes fila
```
sh arbeid/hack/levering/fremmed.sh /tmp/k2411
python3 -I arbeid/oppgave_2411/eksempler.py /tmp/k2411/ut
```
