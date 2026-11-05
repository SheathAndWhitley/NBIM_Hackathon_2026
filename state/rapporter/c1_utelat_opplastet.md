# Case 1 (#2795): opplastings-rapporten med real_votes-rader holdes ute av GitHub-synken

**Endring:** `arbeid/verktoy/c1_github_alt.py` har fått `MONSTER_UT = {"opplastet_*real_votes*": ...}` (fnmatch på filnavn), sjekket i `grunn()`. Fila `state/rapporter/opplastet_20261105_114241_real_votes.md` (header + 3 rader av arrangørens real_votes.csv, merknad fra dommer2 i #2793) står nå i `utelatt` med grunn «opplastings-rapport med rader fra arrangørens real_votes.csv (#2795)».

**Bevis:**
- `c1_github_alt.py liste`: 1006 linjer før, 1005 etter. `diff` viser bare den ene fila som forsvinner.
- Tørrkjøring av `github_synk.sh` mot tom tmp-repo (C1_GITHUB_REPO/STAGE/RAPPORT/ROD satt til tmp, C1_GITHUB_VARSLE=0, ingen push, den ekte repoen er ikke rørt): GRØNN, hemmelighetsskanning **0 funn**, 48 flaggede filer utelatt som før, **961 filer** i repoen, ingen `*real_votes*`-fil. tmp-mappa er slettet.
- Hvorfor 961 og ikke 957 (958 − 1): det er skrevet nye `c1_*`-rapporter etter dommer2 sin tørrkjøring. Sammenligningen før/etter på samme tidspunkt (lista over) viser at endringen fjerner nøyaktig én fil.
- Den ekte repoen: `rsync --delete` i steg 4 fjerner fila der ved neste synk (#2728, 19:10).
- Frysvakt GRØNN, 21 filer like som ved frys 17:18:18.

**Ikke gjort (utenfor oppgaven):** de to `opplastet_*npx_votes.md`, `startpakke` og `NBIM_Hackathon_2026-main` følger fortsatt med. Ta en titt på om de også viser rader fra data før synken, hvis noen har tid.

**Tillegg #2807 (smed2, før 19:10):** `opplastet_*npx_votes*` lagt i MONSTER_UT i `arbeid/verktoy/c1_github_alt.py` (dommer2 #2797: 4 rader av npx_votes.csv). Lista før/etter samme minutt: 1009 -> 1007, diff er nøyaktig de to `opplastet_20261105_114240_npx_votes.md` og `..._114301_npx_votes.md`. Commit cbae393 (18:58).
Den ekte repoen mister dem ved synken 19:10 (#2728, rsync --delete).

**Dommer-dom #2808 (dommer2, 19:01): GRØNN.** (1) `c1_github_alt.py liste` har 0 treff på `opplastet_*npx_votes*` og `opplastet_*real_votes*`; `utelatt` viser alle tre med grunn. (2) Lista før (cbae393^) og etter kjørt samme minutt: 1010 -> 1008, diff er nøyaktig `opplastet_20261105_114240_npx_votes.md` og `..._114301_npx_votes.md` (én fil mer enn smed2s 1009/1007 fordi en ny c1-rapport er skrevet siden, delta er fortsatt 2). (3) Tørrkjøring av `github_synk.sh` mot tom tmp-repo (PUSH=0, VARSLE=0): skanning 0 funn, 50 flaggede filer utelatt, 962 filer, 0 `opplastet_*votes*`-filer i repoen, GRØNN. Ekte repo urørt (53b0023), frysvakt GRØNN 21 filer. tmp slettet.
