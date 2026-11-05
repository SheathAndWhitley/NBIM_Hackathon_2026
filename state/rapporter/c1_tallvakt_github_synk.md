# Case 1: tallvakt mot GitHub-repoen etter tekststopp-synken (#2819, smed2, 05.11 ~19:15)

**Dom: 0 avvik. OK.** Commit: origin/main = `e844c6e` («Synk fra landsbyen 2026-11-05 19:12:06 (skanning 0 funn)», synk #2728).

| Sjekk | Filer | Påstander | Avvik | Utgang |
|---|---|---|---|---|
| c1_tallvakt.py, standardsettet (levering/*.md, c1/leveranse/*.md, c1/*.md) i ren worktree av origin/main, svarfil og KJORING fra repoen | 32 | 197 | **0** | 0 |
| c1_tallvakt.py på rot-filene README.md, DATA.md, LAGET.md i repoen | 3 | 4 | **0** | 0 |
| c1_tallsjekk.py --bare-ikke --feil (landsbykilden) | 23 | 3359 tall | 0 feil | 0 |

Måletall: F1 MOT 0,512 (P 0,4776, R 0,5517, TP 32 FP 35 FN 26), menneske 164 av 1578 (10,4 %).

Fil-for-fil mot landsbyen: alle filer finnes. To ULIK (JURY_README.md:73,91 og TREFFSIKKERHET.md) er bare stianonymisering fra synken (`~/...` → `~/...` / `<repo>`), ingen tall. Ventet.

Ingen avvik, så ingen melding til dommer (#2773). Ingen push. Kjøring: `bash arbeid/oppgave_2819/kjor.sh` (logg `arbeid/oppgave_2819/kjoring.txt`).
Forbehold: kilder/*.md (daterte øyeblikksbilder) er utenfor standardsettet, som i #2676/#2780.
