# Case 1: byttetabell for 02-dommen (#2874), ført av dommer2 (#2911, 2026-11-05 20:05)

Regel (REGEL.md i hver kandidatmappe, ordre #265/#281): BYTT bare hvis snitt(2024,2025,2026) − frossen ≥ +0,02 OG intet år
(2023 medregnet) under −0,02. Frossen = repo4 (oppgave_2575): 2023 0,3535 (vakt) | 2024 0,5057 | 2025 0,5309 | 2026 0,5120 | snitt **0,5162**.
Måler: `arbeid/c1_natt/mal_kandidat.sh` / `oppgave_2567/maaler_aar.py --score mot` (F1 MOT). Alle tall er dommer-verifiserte der det står slik.

## Hovedtabell

| kandidat | snitt 24-26 | diff frossen | 2023 (vakt) | 2024 | 2025 | 2026 | frøspredning (sd snitt, min–maks) | regel oppfylt | verifisert |
|---|---|---|---|---|---|---|---|---|---|
| frossen repo4 (oppgave_2575) | 0,5162 | 0 | 0,3535 | 0,5057 | 0,5309 | 0,5120 | ikke målt med frø (rå repo4-frø i #2886: sd 0,0136, 0,5008–0,5371) | – (referanse) | ja, #1243 |
| #2701 av-regel på repo4 (leder før natta) | 0,5297 | +0,0135 | 0,3736 | 0,5269 | 0,5375 | 0,5246 | 5 frø (#2886): snitt 0,5312, sd 0,0123, 0,5170–0,5506 | **nei** (snitt < +0,02; frø 3 alene 0,5506 ville passert) | ja, #1238 |
| #2703 midt-terskel + av | 0,5261 | +0,0099 | 0,3556 | 0,5083 | 0,5276 | 0,5424 | ikke målt | nei | ja, #1246 |
| #2882 v2 SVD-tekst i LGBM, k på val | 0,5354 | +0,0192 | 0,3592 | 0,5326 | 0,5436 | 0,5299 | 5 frø (#2903/#2911): snitt 0,5316, sd 0,0059, 0,5242–0,5375 | **nei** (0,0008 under, frø-snitt +0,0154) | ja, #1258 |
| **#2887 v2 + av-regel (smed)** | **0,5596** | **+0,0434** | 0,3723 | 0,5731 | 0,5667 | 0,5391 | 5 frø (#2903/#2911): snitt **0,5571**, sd **0,0047**, 0,5519–0,5618 | **ja**, alle 6 kjøringer hver for seg (se under) | ja, kald kopi byte-lik #2895 og #2911, forsøk #1266 |
| #2881b av + regimeskifte (smed2) | 0,5349 | +0,0187 | 0,3736 | – | – | – | ikke målt | nei (0,0013 under) | ja, #1256 |
| #2885 tidsvekt + arvet flaggtall + av (smed3) | 0,5401 | +0,0239 | – | – | 2025 +0,0033 | – | ikke målt | ja på tall, men regel testinformert (#2902) og under v2+av | ja, #1265/#1268 |

Per-år-tall for #2881b og #2885 står i leaderboard.md / c1_natt_maaling.md; de er ikke bytte-kandidater etter v2+av.

## Frø-spredning v2 + av, dommer-omkjøring fra kald kopi (#2911)

Kald kopi: `arbeid/oppgave_2911/kald/` (v2_seed.py = v2_rull.py + `--seed` til LightGBM, md5-lik smed3s; kjor_fro.sh med absolutt
prosjektsti; ingen av smed3s utdata). 15 kjøringer (frø 0–4 × testår 2024/2025/2026, k låst 32/64/48 fra #2882), «av»-regel og
måling med `maal_fro.py`. Alle 45 csv-er er **byte-identiske** med `arbeid/oppgave_2903/`, og `maal_fro.txt` er identisk linje for linje.
Selvrapportert 0,5571 / sd 0,0047 er dermed bekreftet.

| F1 MOT, v2+av | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 | diff frossen | verste år mot frossen | regel |
|---|---|---|---|---|---|---|---|---|
| frø std (#2887, den som ligger i svar/) | 0,3723 | 0,5731 | 0,5667 | 0,5391 | 0,5596 | +0,0434 | 2023 +0,0188 | ja |
| frø 0 | 0,3704 | 0,5509 | 0,5574 | 0,5714 | 0,5599 | +0,0437 | 2023 +0,0169 | ja |
| frø 1 | 0,3723 | 0,5542 | 0,5667 | 0,5586 | 0,5598 | +0,0436 | 2023 +0,0188 | ja |
| frø 2 | 0,3763 | 0,5714 | 0,5574 | 0,5565 | 0,5618 | +0,0456 | 2023 +0,0228 | ja |
| frø 3 | 0,3723 | 0,5576 | 0,5495 | 0,5487 | 0,5519 | +0,0357 | 2025 +0,0186 | ja |
| frø 4 | 0,3763 | 0,5614 | 0,5340 | 0,5614 | 0,5523 | +0,0361 | 2025 +0,0031 | ja |
| **snitt 5 frø** | 0,3735 | 0,5591 | 0,5530 | 0,5593 | **0,5571** | **+0,0409** | 2023 +0,0200 | **ja** |
| sd 5 frø | 0,0027 | 0,0079 | 0,0122 | 0,0083 | 0,0047 | | | |

Mot lederen #2701 sitt 5-frø-snitt (0,5312, sd 0,0123): +0,0259, og **verste** v2+av-frø (0,5519) ligger over **beste** leder-frø (0,5506).
Samlet sd 0,0093, diff/sd = 2,8. Per år mot leder-frøsnitt: 2023 +0,024, 2024 +0,037, 2025 +0,030, 2026 +0,011; ingen år negativt.
Rå v2 uten «av» har frø-snitt 0,5316 (sd 0,0059), så «av»-regelen bidrar stabilt +0,026 på alle frø.

## Hva 02-dommen kan lese rett ut
- v2+av er den eneste kandidaten som oppfyller regelen, og den gjør det med alle 5 frø hver for seg og med frø-snittet; løftet er ikke frø-flaks
  (sd 0,0047 mot kravet +0,02). Kaldt reprodusert to ganger (#2895 svarfiler, #2911 frø).
- Forbehold som før (c1_natt_referanse.md): k-valget og «av»-regelen er ledd som var sett på test i tidligere oppgaver (#2701, #2882), så
  +0,043 er et øvre anslag; frø-snittet +0,041 er det ærligste enkelttallet.
- Nye kandidater i natt (#2907 forklaringstrekk, #2910 tidsvekt+v2+av, #2912 trekk A) må slå **v2+av**, ikke frossen, for å bytte igjen, og bør
  måles med minst 3 frø mot 0,5571 (anbefaling fra #2886). Fyll inn under når de kommer.

## Nye kandidater (fylles av dommer ved måling)

| kandidat | snitt 24-26 | diff v2+av (0,5571 frøsnitt / 0,5596 std) | 2023 | 2024 | 2025 | 2026 | frøspredning | regel oppfylt | verifisert |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
