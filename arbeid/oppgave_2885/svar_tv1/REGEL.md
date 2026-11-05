# REGEL for vinkel 3, tidsvekt på treningsrader (smed3, #2885, ordre #265/#281), skrevet FØR måling

Kandidat: frossen repo4 (tv_rull.py = abl_rull.py + sample_weight, --variant miks --hist 2
--repo prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate) med
sample_weight = tv^(T-1-år) i både LR og LGBM, pluss lederens av-regel #2701 oppå
(fjern MOT-flagg når NBIMs siste stemme på samme selskap+tekst var FOR, historikk < året som måles).

Valg av tv: per testår T prøves tv i {1.0, 0.9, 0.8, 0.7, 0.6}. tv velges som den med høyest
val-F1 (år T-1, trent <T-1, etter av-regel på val-fila) i tv_rull-kjøringen. Ved likhet velges tv nærmest 1.0.
Test T måles én gang med valgt tv. Ingen valg på testtall.

Svarfiler: tv_t2023.csv = val-fila fra T=2024-kjøringen (trent <2023) med T=2024s valgte tv,
tv_t2024/2025/2026.csv = testfilene. Alle med av-regel.
Kontroll (ikke kandidat): tv=1.0 + av skal gi lederens 0,5297 (natt-referanse). Måles i egen mappe svar_tv1.
Dom: arbeid/c1_natt/mal_kandidat.sh. BYTT bare hvis snitt(2024,2025,2026) - frossen >= +0,02
OG intet år (2023 medregnet) under -0,02. Ellers STÅR. Ingen ny variant måles i samme mappe etterpå.
(kontrollmappe: tv låst til 1.0)
