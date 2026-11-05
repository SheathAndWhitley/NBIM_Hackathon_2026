# Case 1 (#2480): NBIM-repoets presedensregel skrevet ærlig inn i jurysvaret

Ny setning i `arbeid/hack/levering/JURYSVAR.md` pkt. 5 og i zipens `c1/leveranse/JURY_SPORSMAL.md` pkt. 3 (samme spørsmål: «slår dere en enkel regel?»), ordlyd etter dom #2465:
- NBIMs presedensregel («samme direktør hvis kjent, ellers samme sakstekst avvek sist», avvik inkl. AVSTÅ): 0,515 på vår måler test 2026, +0,04 over frossen 0,476, KI [−0,05; +0,13], innenfor støyen.
- Repoets hybrid på vår splitt: 0,545, +0,069 [+0,007; +0,133], sagt rett ut som et reelt forsprang på oss.
- Vår PR-AUC 0,525 mot 0,318 (presedens) og 0,413 (hybrid). Modellen er ikke endret (frys står).

Kilder kopiert inn i pakka: `kilder/c1_nbim_repo_sammenligning.md` og `kilder/c1_nbim_repo_sammenligning_dom.md` (stier skrevet om etter LESMEG), linje i `kilder/LESMEG.md`.

Akseptkrav:
- Tallvakta: 0 avvik på de 3 endrede filene, og 18 filer / 169 påstander / 0 avvik på hele pakka.
- Sluttsjekk GRØNN (`/tmp/sj2480.txt`): HOVEDTALL F1 MOT 0.476190, ziptest grønn, sha prediksjonsfil = frossen.
- `frys_fasit_1600.sha256` regenerert (117 filer); `frys_diff.sh` mot sluttsjekk-zipen: FRYS LIK, 0 avvik.
  Merk: fasiten speiler kilden nå, også andres uferdige endringer (smed4 #2475 pyproject/uv.lock, README, JURY.md, ERLIG_EVALUERING, NESTE_VERSJON). Den må regenereres igjen etter #2475/#2481.
