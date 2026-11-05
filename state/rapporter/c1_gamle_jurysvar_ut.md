# Case 1: gamle jurysvar ut av pakken (#2112)

Gjort 05.11 kl. 12.45, etter dommer2 #2110.

- `c1/JURYSVAR.md` (0,482 som hovedtall, 66 MOT) → `c1/arkiv/JURYSVAR_foer_real_0482.md`. Ikke slettet.
- `c1/leveranse/jury_svar.md` (TODO-utkast) → `c1/arkiv/jury_svar_TODO_utkast.md`. `c1/arkiv/LES.md` forklarer.
- Ingen skript eller Makefile pekte på filene (grep).
- `levering/KRAVRESPONS.md` rad 27 peker nå bare til `levering/JURYSVAR.md` (0,476 [0,36; 0,59], 58 MOT).
- Fant samme feil i to filer til, rettet:
  - `c1/SVAKHETER.md` l. 3–5: hovedtallet var 0,482/66 MOT, nå 0,476 [0,36; 0,59]/58 MOT, med en merknad om at tabellene under er avvik (0,482 = sidetall).
  - `c1/DEMO_MANUS.md` l. 69: «F1 MOT (0,482) … av 66», nå 0,476/P 0,44/R 0,52 av 58. Tellingene TP/FP/FN er tatt ut, de fylles i #1975.
  - `levering/BESLUTNINGSSTOTTE.md` l. 29 og 42: «66 MOT» → 58 MOT / 66 avvik.

Akseptsjekk: `grep -rn '0,482' c1 levering` (uten arkiv/data). Alle linjer som er igjen sier avvik eller sidetall, unntatt 4 tabellrader
(SVAKHETER l. 11, 12, 45; ERLIG_EVALUERING l. 13). De står i tabeller med overskrift eller innledning som sier «avvik fra styret».
`grep '66 MOT'` gir ingen treff utenom rådata.

Gjenstår: `JURY_METODE.md` og `ERLIG_EVALUERING.md` er allerede merket. `c1_ruting_verifisert.md` siterer fortsatt gamle c1/JURYSVAR.md l. 42. Det er en historisk rapport, så den er ikke endret.
