# Måler for nye arrangørfiler (#2035, dommer2) – sjekket, ikke satt (oppgaven droppet)

- De to npx-filene 11:42:40 og 11:43:01 er identiske (md5 7c641ded...). Bruk 114240.
- maaler_ny.py reproduserer smed2s tall: npx aksjonærforslag=MOT 0,6453, npx t1 0,9034, real t2 0,4810, real aksjonær=MOT 0,1951. Følg styret 0.
- npx test 2026: 16455 rader, 634 MOT. 1021 rader har tom against_board. NB: 297 av 634 MOT er AVSTÅ, 292 MOT, 45 FOR (aksjonærforslag). Ekte uenighet med styret er få.
- LEKKASJE-RISIKO: fila har nbim_vote, nbim_vote_raw, rationale_text, rationale_section, funds_disagree. Måleren kan ikke hindre at modellen bruker dem. Hver kandidat må vise featureliste uten disse. t1 0,90 må sjekkes for dette før den godtas.
- split_year != year (split_year 2026 inneholder 2018 rader fra 2025). Bruk split_year som arrangøren gir.
- real_votes: 13757 rader 2019–2026, test year 2026 = 1539 rader, 66 MOT. Mer ærlig mål enn npx.
- Forslag til måler: kommandoen i oppgaveteksten er gyldig for npx. Anbefaler også egen måler på real_votes (year 2026).
