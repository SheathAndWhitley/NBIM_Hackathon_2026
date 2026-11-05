# Case 1 natt #2903: frø-spredning for v2 + av-regel. +0,043 står seg mot frøstøyen (smed3)

Samme oppsett som #2886 (`abl_seed.py`), men på BYTT-kandidaten fra #2887: `arbeid/c1_natt/v2/v2_rull.py` + `--seed` til LightGBM
(SVD-frøet står på 0 som i v2). k låst fra #2882: 2024 k=32, 2025 k=64, 2026 k=48. 2023-vakt = val-fila for T=2024, historikk < 2023.
Av-regelen er koden fra #2701 uendret. Målt med dommerens måler (`oppgave_2567/maaler_aar.py --score mot`, F1 MOT), samme som #2886 og #2887.
Frø 0–4, 15 treningskjøringer. Kode og tall: `arbeid/oppgave_2903/` (v2_seed.py, kjor_fro.sh, maal_fro.py, maal_fro.txt, s*_*.log).

## v2 + av (kandidaten), 5 frø

| | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 |
|---|---|---|---|---|---|
| #2887 (standardfrø, det som er målt i DOM.md) | 0,3723 | 0,5731 | 0,5667 | 0,5391 | 0,5596 |
| frø 0 | 0,3704 | 0,5509 | 0,5574 | 0,5714 | 0,5599 |
| frø 1 | 0,3723 | 0,5542 | 0,5667 | 0,5586 | 0,5598 |
| frø 2 | 0,3763 | 0,5714 | 0,5574 | 0,5565 | 0,5618 |
| frø 3 | 0,3723 | 0,5576 | 0,5495 | 0,5487 | 0,5519 |
| frø 4 | 0,3763 | 0,5614 | 0,5340 | 0,5614 | 0,5523 |
| **snitt 5 frø** | 0,3735 | 0,5591 | 0,5530 | 0,5593 | **0,5571** |
| **sd 5 frø** | 0,0027 | 0,0079 | 0,0122 | 0,0083 | **0,0047** |
| min–maks | 0,3704–0,3763 | 0,5509–0,5714 | 0,5340–0,5667 | 0,5487–0,5714 | 0,5519–0,5618 |

## Mot frossen (repo4, pakka kl. 20)

| | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 |
|---|---|---|---|---|---|
| frossen, pinnet tall (standardfrø) | 0,3350* | 0,5057 | 0,5309 | 0,5120 | 0,5162 |
| frossen, snitt 5 frø (#2886) | 0,3373 | 0,4945 | 0,5128 | 0,5354 | 0,5143 |
| frossen, sd 5 frø (#2886) | 0,0079 | 0,0114 | 0,0124 | 0,0210 | 0,0136 |
| frossen, beste frø (#2886) | 0,3431 | 0,5057 | 0,5342 | 0,5714 | 0,5371 |
| **v2+av verste frø minus frossen pinnet** | +0,035 | +0,045 | +0,003 | +0,037 | **+0,036** |
| **v2+av snitt minus frossen snitt** | +0,036 | +0,065 | +0,040 | +0,024 | **+0,043** |

*2023 for frossen er 0,3350 med maaler_aar og 0,3535 med natt-måleren (ulik id-avrunding i 2023-fila, se #2886); begge ligger godt under alle v2+av-frø.

**Svar: +0,043 står seg.** Snitt-til-snitt over frø er gevinsten den samme som i #2887 (+0,043). Det dårligste v2+av-frøet (0,5519) ligger
+0,036 over frossens pinnede tall og +0,015 over frossens *beste* frø (0,5371). Alle 5 frø klarer bytteregelen alene
(snitt ≥ +0,02 over 0,5162, intet år under -0,02; svakeste år er 2025 for frø 4 med +0,003). Vakt-året 2023 er pluss for alle frø.
#2887-tallet 0,5596 er ikke et heldig frø: det ligger 0,0025 over frø-snittet, godt innenfor én sd. Per år er det derimot frø-flaks i begge retninger:
#2887 har 2024 i toppen av spennet (0,5731 mot frø 0,551–0,571) og 2026 i bunnen (0,5391 mot frø 0,549–0,571). Det jevner seg ut i snittet.

## Mot frossen + av (ikke pakka, men den rettferdige sammenligningen for v2-delen)

| | 2023 | 2024 | 2025 | 2026 | snitt 24-26 |
|---|---|---|---|---|---|
| frossen+av, snitt 5 frø (#2886) | 0,3496 | 0,5221 | 0,5228 | 0,5485 | 0,5311 (sd 0,0123) |
| v2+av, snitt 5 frø | 0,3735 | 0,5591 | 0,5530 | 0,5593 | 0,5571 (sd 0,0047) |
| diff | +0,024 | +0,037 | +0,030 | +0,011 | **+0,026**, diff/sd = 2,8 |

Verste v2+av-frø (0,5519) slår beste frossen+av-frø (0,5506). Så v2-delen (SVD i LGBM) gir ekte gevinst også oppå av-regelen, ikke bare av-regelen alene.
2026 er det svakeste året: der er v2-gevinsten +0,011 i snitt, og frossen+av frø 3 (0,5818) slår alle v2+av-frø. Det er ett frø av fem og står ikke i pakka.

## Rå v2 uten av (samme kjøringer)

| | 2023 | 2024 | 2025 | 2026 | snitt 24-26 |
|---|---|---|---|---|---|
| snitt 5 frø | 0,3639 | 0,5258 | 0,5277 | 0,5412 | 0,5316 (sd 0,0059) |
| frossen rå, snitt 5 frø | 0,3373 | 0,4945 | 0,5128 | 0,5354 | 0,5143 (sd 0,0136) |

Gevinsten deler seg i ca. +0,017 fra v2 (SVD) og +0,026 fra av-regelen, og delene er nesten additive over frø (sum 0,043).
Bifunn: v2 har under halve frøspredningen til frossen (sd 0,005 mot 0,014 på snittet, 0,008 mot 0,021 i 2026). SVD-trekkene gjør LGBM-halvdelen mer stabil, ikke bare bedre.

## Forbehold
- Bare LightGBM-frøet varieres. SVD-frø (random_state=0) og LR er deterministiske og ikke rørt, samme avgrensing som #2886.
- Frø-til-frø er ikke parvis sammenlignbare mellom frossen og v2+av (ulike modeller). Jeg sammenligner fordelinger: snitt, sd, verste mot beste.
- Dette er fem frø. sd-ene på 0,005–0,014 er selv usikre, men svaret (alle fem frø over bytteregelen, verste frø over frossens beste) henger ikke på sd-estimatet.
- Ingen ny variant er valgt eller målt etter at tallene var kjent. Kandidaten er uendret #2887.
