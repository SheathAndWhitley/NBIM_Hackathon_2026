# REGEL 2 for vinkel 3, tidsvekt med arvet flaggtall (smed3, #2885), skrevet FØR måling 2 (19:5x)

Ærlig forbehold: dette er forsøk 2. Forsøk 1 (svar/, DOM STÅR -0,025) viste at den rå val-grensen ikke overføres
ved tv<1 (2024 fikk 37 flagg mot 90). Diagnosen (rang.py, låst flaggtall, BRUKTE TESTENS FLAGGTALL, ikke kandidat)
viste at rangeringen bedres. Regelen under er laget etter den diagnosen, så dommeren bør vekte resultatet som
et andregangsforsøk. tv velges likevel bare på val.

Kandidat: samme tv_rull-kjøringer (miks, hist 2, repo4-trekk) med sample_weight = tv^(T-1-år).
Grense: tidsvekten bare RANGERER. Antall rå flagg (før av) per år = antall rå flagg i tv=1,0-kjøringen
(= frossen repo4) på samme fil. Det tallet er etikettfritt (frossens val-grense brukt på årets p-fordeling).
Toppen k etter p_avvik flagges. Deretter av-regelen #2701.
Valg av tv: per T prøves tv i {0.9, 0.8, 0.7, 0.6} (1.0 = leder, ikke kandidat). tv velges som den med høyest
val-F1 (år T-1, trent <T-1, arvet flaggtall fra tv=1,0 sin val-fil, av oppå). Likhet: nærmest 1,0. Test T måles én gang.
Svarfiler: tv2_t2023.csv = val-fila fra T=2024 med T=2024s valgte tv; tv2_t2024/2025/2026.csv = testfilene.
Dom: arbeid/c1_natt/mal_kandidat.sh, bytteregel #265/#281 (snitt 24-26 >= +0,02 over frossen, intet år inkl. 2023 < -0,02).
Ingen ny variant måles i denne mappa etterpå.
