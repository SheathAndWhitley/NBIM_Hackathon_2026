# Case 1 #2236: gamle N-PX-filer ut av hovedveien, TEST 2026-linja merket

Regelsjekk punkt 6 og 9 (case1_regelsjekk.md) er rettet.

1. `run.sh`, `rapport.py`, `resultat.py`, `sporlogg.py`, `motstand_inj.py` og `utkast_1100/` er flyttet fra
   `arbeid/hack/c1/leveranse/` til `leveranse/spor_npx/` (ingenting slettet), med `spor_npx/LESMEG.md`:
   «Brukes bare av SPOR=npx». Stiene er rettet i `kjor.sh` (SPOR=npx-grenen), `spor_npx/run.sh` (cd ../.. og
   egne stier) og `c1/Makefile`.
2. `KJORING.txt`-linja «TEST 2026 (samme andel flagget som val …) F1 0.5» får nå prefikset
   «IKKE HOVEDTALL (bare sjekk, grensa satt med test-fordelingen; hovedtallet er måler v3 under):».
   Endringen er bare i loggteksten i `levering/c1_real.py` (`kjor_modell`). `train.py` er urørt.

Bevis (13:41, egen kald mappe `KALD=/tmp/c1_kald_smed2_2236`): `bash arbeid/hack/c1/leveranse/kjor.sh` gir rc 0,
`MOT mot styret: TP 30 FP 38 FN 28 P 0.4412 R 0.5172 F1 0.4762`, SCORE 0.481752, TALLVAKT GRØNN (153 påstander, 0 avvik).
`_pred_uten_ruting.csv` er byte-lik `kjor_agent_real_maskin_alene.csv`, så prediksjonene er uendret.
`SPOR=npx` (kjørt i kopi /tmp/npx_2236, så pakkemappa ikke får data/) gir rc 0, SCORE 0.383275.

NB 1: `c1_real.py` står på frysvaktens liste. Frysen er ikke tatt ennå (kl. 16), så sha-en tas med denne versjonen.
NB 2: Første kald kjøring med standard `/tmp/c1_kald` krasjet med en ImportError i scipy. Trolig kjørte en annen
agent (dommer2, #2240) i samme mappe samtidig. To verifikasjoner bør ikke dele `/tmp/c1_kald`. Bruk `KALD=/tmp/<eget>`.
