# Case 1: forbudte kolonner og lekkasjevakt (dommer2 #2055)

Til #2036, #2037 (smed3) og alle smeder. Full liste: `arbeid/hack/c1/FORBUDT.md`.

- Aldri input: nbim_vote, nbim_vote_raw, against_board, rationale_text, rationale_section, position_paper,
  funds_disagree, n_funds, injection_flag (og split_year bare til deling).
- n_funds er etter-stemmen-info (N-PX) og bærer signal (MOT 3 % → 26 %): forbudt. injection_flag = motstandstesten.
- Fasit i forkledning: på real 2026 gir «begrunnelse finnes» F1 ≈ 0,95 (63 TP, 2 FP, 3 FN). Det er nok
  der «over 94 %» kommer fra. Ærlig nivå nå: ~0,47–0,48.
- #2037: begrunnelser er lov som SITAT fra tidligere år, aldri feature for samme sak/år.
- Sjekk før du melder tall: `python3 -I arbeid/hack/c1/sjekk_lekkasje.py svar SVAR.csv --data real --vindu test`
  (forbudt kolonne → AVVIST; Jaccard ≥ 0,75 mot begrunnelsesradene → MISTANKE). Testet: lekk-regel 1,00 = MISTANKE,
  smed2 `oppgave_2046/pred_real_votes_2026.csv` 0,26 = OK, `oppgave_2049/typerate_val.csv` 0,05 = OK.
- Svakhet: signaturen fanger direkte bruk av begrunnelsene, ikke en modell som lekker litt. Kodesjekken
  (`sjekk_lekkasje.py kode <mappe>`) lister hver linje som nevner forbudte kolonner; dommeren leser dem.
- Funnet underveis: i val 2025 har ALLE 103 MOT begrunnelse, så recall på «med/uten begrunnelse» kan ikke skille der.
