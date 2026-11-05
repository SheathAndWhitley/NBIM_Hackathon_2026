# Case 1 #2886: frø-spredning i lederen (repo4 + «av»), 5 frø på 2023–2026

Lederen (av-regel #2701 på repo4, `arbeid/oppgave_2567/abl_rull.py`) kjørt med `random_state` 0–4 til LightGBM, ellers identisk
(LR, tfidf og oppdeling er deterministiske; LightGBM med subsample/colsample 0,8 er eneste tilfeldige ledd). «av» lagt på hver
kjøring, målt med dommerens måler (`oppgave_2567/maaler_aar.py --score mot`, F1 MOT). Kode: `arbeid/oppgave_2886/` (abl_seed.py,
kjor_fro.sh, maal_fro.py, maal_fro.txt; tabell uten «av» står der også, sd på snitt 0,0136).

| F1 MOT | 2023 | 2024 | 2025 | 2026 | snitt 24–26 |
|---|---|---|---|---|---|
| leder (frossen kjøring) | 0,3548 | 0,5269 | 0,5375 | 0,5246 | 0,5297 |
| frø 0 | 0,3529 | 0,5333 | 0,5065 | 0,5410 | 0,5269 |
| frø 1 | 0,3529 | 0,5181 | 0,5238 | 0,5440 | 0,5286 |
| frø 2 | 0,3456 | 0,5333 | 0,5217 | 0,5426 | 0,5326 |
| frø 3 | 0,3548 | 0,5325 | 0,5375 | 0,5818 | 0,5506 |
| frø 4 | 0,3420 | 0,4933 | 0,5244 | 0,5333 | 0,5170 |
| **snitt 5 frø** | 0,3496 | 0,5221 | 0,5228 | 0,5486 | 0,5312 |
| **sd 5 frø** | **0,0056** | **0,0174** | **0,0110** | **0,0190** | **0,0123** |
| min–maks | 0,342–0,355 | 0,493–0,533 | 0,507–0,538 | 0,533–0,582 | 0,517–0,551 |

**Hva det betyr for byttet:** +0,02 på snittet er bare 1,2 sd av støyen mellom to enkeltkjøringer (sd på differansen
√2·0,0123 = 0,017), og frø 3 alene passerer hele bytteregelen mot lederen (+0,021, intet år under −0,02) uten
at noe er endret, så 4 av 30 par av identiske modeller «vinner» på frø alene (13 %); dommeren bør derfor kreve at en
kandidat måles med minst 3 frø og sammenlignes mot 5-frø-snittet 0,5312 (ikke 0,5297), eller heve kravet til +0,035
(2 sd) for én kjøring.

Mot stokket-kontrollen i c1_retningslinje_trekk.md: den viste ±0,02–0,05 per år men stabilt snitt (±0,001), fordi den
holdt frøet fast og bare byttet kolonner. Med nytt frø flytter også snittet seg (sd 0,012, spenn 0,034). Enkeltår-støyen
(sd 0,011–0,019) stemmer med kontrollen; «intet år −0,02» slår altså til tilfeldig i omtrent hvert tredje par.
