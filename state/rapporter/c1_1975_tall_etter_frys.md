# Case 1 (#1975): tallene i JURY.md og demo-manus etter modellfrysen kl. 16

Kald kopi av den frosne pakka 05.11 kl. 16.05 (`sh arbeid/hack/levering/fremmed.sh /tmp/c1_kald_1975`, 56 s):
- FRYSVAKT GRØNN (17 filer like som ved frysen 16:00:01), TALLVAKT GRØNN.
- F1 MOT 0,476190 (måler v3 sha 418a937e57). TP 30, FP 38, FN 28, P 0,4412, R 0,5172. 58 MOT i fasit, 66 avvik, avvik-F1 0,481752.
- Ruting: 188 av 1578 (127 usikre, 60 ukjent selskap, 1 instruks), 183 av 1539 med fasit (11,9 %).
- Delt på maskin/menneske: TP 9/21, FP 0/38, FN 17/11.
- `pred_maaler.csv` sha b113b545dd86, samme som før frysen. `agent.csv` sha 1543706f…, samme som i alle 8 kalde kopier siden #2329 (byggemappa har f0444a47…).

**JURY.md:** ingen endring trengs. Alle tallene over står der allerede: 0,476, 30/58, 38/68, 183/1539, 17 av 28, 9 riktige auto-MOT, 127/60/1. Tallvakta med kildemappa som rot: 18 filer, 168 påstander om hovedtallet, 0 avvik. Tallsjekken: alle tall har kilde.
Oppgaveteksten nevner #1959 (smed3 v3), #1970 (møtenivå) og DEF 14A v6. Det er tall fra N-PX-tiden. De er erstattet av NBIMs egne stemmer og hører ikke hjemme i JURY.md.

**Demo-manus:** Garmin, Dell og T-Mobile var N-PX-eksempler og er byttet ut for lenge siden. Manuset bruker nå Mobimo (treff, linje 276), LOTTE Chemical (bom, linje 89) og Kura Sushi (til menneske, linje 15). `vis_manussaker.py` på den frosne kjøringen gir MANUS OK: samme saker, samme p_mot (1,0 / 0,0896 / 0,5833) og samme ruting. Sitatene er uendret.
Eneste endring: avsnittet «Etter modellfrys» i `arbeid/hack/c1/DEMO_MANUS.md`. Det ba om agent.csv sha f0444a47, men kalde kopier gir 1543706f. Avsnittet viser nå resultatet av sjekken etter frysen. Ingen saker eller tall i selve manuset er endret.

**Til #1972 og #2440:** DEMO_MANUS.md er med i jury-zipen. Frys-fasiten (113 filer) og zipen må derfor bygges på nytt (`pakk_jury.sh`, `frys_fasit.py`), ellers viser frys_diff ENDRET DEMO_MANUS.md. Jeg har ikke rørt fasiten eller zipen.
