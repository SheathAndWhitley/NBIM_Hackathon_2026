# Case 1: uavhengig gjentakelse av robusthetstesten (dommer2 sak 2154)

> **Eldre tall:** linjer merket «eldre frossen modell #2044» gjelder modellen som var frossen før byttet til repo4 (#2572). Målte tall er ikke endret. Dagens hovedtall står i `arbeid/hack/c1/tall_tabell.md`.

**Dom: GODKJENT.** smed2s tabell i `c1_robusthet_frossen.md` (sak 2144) er reprodusert eksakt.

- Kommando: `python3 -I <arbeidsmappe>/oppgave_2144/robusthet_frossen.py --ut /tmp/rob_d2.md` fra rotmappa i repoet, 05.11 ca. 13:02. Tid: 43 s, ingen krasj.
- Basis: F1 MOT **0,4762** (TP 30, FP 38, FN 28, 58 i fasit), som krevd. <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->
- Alle 8 tabellrader (basis, nye_selskaper, tom_tekst, tomme_felt, ukjent_type, ukjent_type_inn, tomme_valgfri, uten_styret) og alle 8 målerlinjer (TP/FP/FN/P/R/F1 med 4 desimaler) er **tegn for tegn identiske** med rapporten (`diff` tom). Avvik 0,000, godt innenfor 0,001.
- Fasitfila `state/opplastet/20261105_114241_real_votes.csv` (den måleren leser) er uendret: sha256 `71ba5135…19e525e6` før og etter.

Merknad: dette bekrefter tallene, ikke tolkningen. Svakhetene smed2 peker på (tom `mgmt_rec`, `country`, `market` gir ingen ruting) står ved lag og dekkes av sak 2152.
