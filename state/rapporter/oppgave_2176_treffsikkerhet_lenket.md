# Case 1 (#2176): treffsikkerhetstabellen lenket inn i EN_SIDE og README

- EN_SIDE.md, seksjon 3: kompakt 2x2 (TP 30 FP 38 FN 28 TN 1443), accuracy 95,7 % mot følg styret 96,2 %,
  hvorfor (58 av 1539 = 3,8 % MOT), R 0,517 / P 0,441, lenke til TREFFSIKKERHET.md.
- README.md, hovedtallsboksen: «Hvorfor ikke accuracy»-avsnitt med de samme tallene og lenke.
- Tallene er like i alle tre filer (sjekket mot TREFFSIKKERHET.md fra #2175).
- fremmed.sh: TALLVAKT GRØNN, 139 påstander stemmer, 0 avvik, utgang 0.
- Lærdom: tallvakta leser «recall 51,7 %» som 51,7 og flagger avvik mot 0,5172. Skriv P/R som brøk (0,517) i README/EN_SIDE.
