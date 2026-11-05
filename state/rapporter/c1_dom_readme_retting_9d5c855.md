# Dom: README-rettingen og synk-endringen i commit 9d5c855 (oppgave #2793)

**GODKJENT.** Alle fire akseptkrav står. Dømt av dommer2 2026-11-05 kl. 18:55, før synken 19:10.

| krav | resultat |
|---|---|
| (1) `bash -n arbeid/verktoy/github_synk.sh` | OK |
| (2) tørrkjør mot tom tmp-mappe, ingen push | GRØNN, 0 funn i hemmelighetsskanningen, 958 filer, commit lokalt i tmp. Ingen `real_votes.csv`, `real_test_input.csv`, `real_val_input.csv`, `pred_miks_h2.csv`, `.venv/`, `state/opplastet/` eller `data_off/` i repoen. Ingen `~` i noen fil. 48 filer fra ALT-lista flagget og utelatt (bl.a. hent_*.py med e-post i User-Agent), som designet i #2762. |
| (3) `git diff 9d5c855~1 9d5c855` | Bare tekst. Hovedtall 0,512, tre testår 0,5057 / 0,5309 / 0,5120, snitt 0,5162, KI [0,400; 0,621], 164 av 1578 (10,4 %), 39 uten styreanbefaling, 1539 med fasit: alle uendret. Ny setning i DATA.md i github_synk.sh forklarer bare den faste tidsstempelstien. README.md i tmp-repoen er identisk med GITHUB_README_UTKAST.md. |
| (4) frysvakt | GRØNN, 21 filer like som ved frys 17:18:18 |

Tallvakt kjørt i tillegg: 32 filer, 197 påstander, 0 avvik.

Tørrkjøringen brukte skriptets egne miljøvariabler (C1_GITHUB_REPO, C1_GITHUB_STAGE, C1_GITHUB_RAPPORT, C1_GITHUB_ROD, C1_GITHUB_VARSLE=0), så den rørte verken den ekte lokale repoen, synkrapporten eller tavla. tmp-mappa er slettet.

## Merknad (ikke avvisningsgrunn, gjelder ikke denne committen)
`state/rapporter/opplastet_20261105_114241_real_votes.md` følger med i repoen (ligger der allerede fra tidligere synker). Det er landsbyens egen rapport om opplastingen, men den viser header og de tre første radene av arrangørens real_votes.csv som eksempel. Vil vi være helt rene på «ingen casedata i repoen», bør smed (#2728) legge fila i utelatt-lista i c1_github_alt.py før 19:10-synken. Tre rader av 13757 uten fasit for testår er ikke lekkasje, så jeg stopper ikke synken for det.
