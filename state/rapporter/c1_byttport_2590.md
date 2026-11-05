# Case 1: hard port for byttet til repo4 (ordre #266 hull 2, oppgave #2590) — dommer2, 05.11 17:05

Porten er skrevet som én linje i dommen `state/rapporter/c1_byttedom_265.md` (avsnittet «Porten»). Kort:

BYTT står bare hvis alle fem ledd er grønne kl. 19:00; ellers tilbakerulling etter byttplanen (#2572), og frossen 0,476 står.
1. Byttregelen holder (gjort i #2570: snitt +0,0345, verste år +0,017, kald kopi).
2. `bytt.sh --utfor` → `sluttsjekk.sh` → `pakk_jury.sh` + `test_jury_zip.sh` → generalprøve av demoen fra kald kopi (F1 MOT 0,5120, TP 32 FP 35 FN 26).
3. `DEMO_MANUS.md`, `JURY_SPORSMAL.md` sp. 13 og 19 og `ERLIG_EVALUERING.md` §7 oppdatert til repo4. Sp. 13/19 og §7 sier i dag «frossen står / avventer dom»; etter byttet må de si at repo4 besto en regel satt før måling.
4. README krediterer lagkameratenes `stemmeagent/ballot.py` (R pkt. 5, «credit any copied code»).
5. Grønt verifiseres av dommer (#2596), ikke av smeden som byttet.

Funn underveis: `arbeid/hack/c1/bytte/modell_repo4.py:71` kaller hybridrepoet «arrangørens repo». Det er lagkameratenes (jf. #266-gjennomgangen). Må rettes i byttet, ellers stemmer ikke krediteringen med koden.

Tid: smedens mål er 18:45 (#2592), porten er 19:00. Det gir 15 min til tilbakerulling før tekststopp (#2549).
