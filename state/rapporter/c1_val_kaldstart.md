# Case 1: kald start av den frosne agenten på val 2025 og test 2026 (#2282, smed3)

Kjørt 2026-11-05 14:16 med `BEHOLD=1 bash arbeid/hack/c1/kaldstart.sh` (ren kopi i /tmp, egen .venv fra uv.lock:
lightgbm 4.7.0, sklearn 1.9.1, pandas 3.1.1), deretter samme kopi på `data_off/real_val_input.csv --vindu val`.
Måler: `maaler_offisiell_v3.py --score mot`, sha256[:10] **418a937e57** (oppgaven sa 8b09c36e01; det er sha fra
commit 58f2bd1, måleren fikk v3-endring kl. 13:31 og tall_tabell.md bruker 418a937e57). Ingen agentfiler er endret.
Frysvakta sa «ikke frosset ennå» (kl. 14:16, frys er kl. 16).

## Test 2026: stemmer med c1/tall_tabell.md til alle desimaler
| tall | kald start | tall_tabell / commit b808382 | avvik |
|---|---|---|---|
| F1 MOT mot styret | 0.4762 (SCORE 0.476190) | 0.476 | 0 |
| P / R | 0.4412 / 0.5172 | 0.44 / 0.52 | 0 |
| flagget MOT (TP+FP) | 30+38 = 68 | 68 | 0 |
| PR-AUC avvik | 0.5245 | 0.524 | 0 |
| accuracy (avvik, 1539 rader) | 95.39 % | 95.39 % | 0 |
| følg styret-accuracy | 95.71 % | 95.71 % | 0 |
| ruting til menneske | 188 av 1578 (11.9 %); måleren: 183 av 1539 vurderte | ikke i tabellen | – |
| agentens MOT-forslag | 74 (alle med NBIM-sitat) | – | – |
kaldstart.sh: GRØNN, AVVIK +0.000000, 30 s. Logg: arbeid/oppgave_2282/kaldstart_test.log.

## Val 2025: tabellen har ikke noe tall («ikke målt (ingen fil)»), så her er to tall
1. **Ærlig val (modell trent <2025, slik train.py velger C og grense):** F1 MOT mot styret **0.5202**
   (TP 45 FP 29 FN 54, P 0.608, R 0.455, 99 MOT i fasit). Avvik-F1 0.5217 (TP 48 FP 33 FN 55, PR-AUC 0.4732) er
   nøyaktig det train.py selv logger («val-F1 0.5217»). Accuracy 95.39 %, følg styret 94.60 %.
   Fil: arbeid/oppgave_2282/val2025_aerlig_radp.csv, laget av val_pred.py (kjører train.py uendret via runpy som
   c1_real gjør, skriver pv for val-radene i rad,p-format; 61 val-rader uten fasit får «følg styret»).
   Merk: grensa er valgt på val, så tallet er optimistisk for val, ikke et holdout-tall.
2. **Agenten kjørt rett på val-saker (--csv real_val_input.csv):** F1 MOT 0.7547, ruting 287 av 1970 (14.6 %).
   Dette er IKKE et ærlig tall: agenten bruker modellen trent <2026, og sier selv «saker fra før 2026 (i treningen,
   ikke ærlig målt): 1970». Tallet skal ikke brukes i pakka.

## Konklusjon
Frossen agent (#2044 miks h2 + vakter) gir fra kald start nøyaktig tallene i tall_tabell.md og på dashbordet for
test 2026. For val 2025 finnes det ikke noe referansetall i tabellen; det ærlige tallet er 0.520 (MOT) / 0.522 (avvik),
og det stemmer med train.py sin egen logg. Anbefaling: skriv VAL F1 = 0.520 inn i tall_tabell for #2044 med
fila over som kilde, slik at «ikke målt (ingen fil)» forsvinner. Måler-sha i oppgaver bør være 418a937e57.

Filer: arbeid/oppgave_2282/ (målerutskrifter maaler_v3_ut.txt, KJORING_*.txt, prediksjonsfiler, val_pred.py).
