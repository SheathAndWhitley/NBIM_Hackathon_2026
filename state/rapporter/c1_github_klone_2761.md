# Case 1 #2761: ny GitHub-klone etter tekststopp-synken, README- og JURY-kommandoer grønne

- Klone: `git clone git@github.com:Martinkristofferhansen/nbim.git` med deploy-nøkkelen (repoen er fortsatt privat; anonym SSH/HTTPS avvises) til tom `/tmp/c1_gh_klone_1925`. HEAD = 4f148d1 (synk 19:16:06), lik `ls-remote` 19:26.
- Casedata lagt inn etter DATA.md. Skript: `arbeid/oppgave_2761/kjor_klone.sh` (40 s totalt).
- `sh KJOR.sh` (README): exit 0, FRYSVAKT GRØNN (14 filer), HOVEDTALL F1 MOT 0.512000, TALLVAKT GRØNN.
- `testaar.sh` og `testaar.sh --rask` (JURY.md): exit 0 begge, `2024 0.5057  2025 0.5309  2026 0.5120  snitt 0.5162`, lik fasit (#2713).
- Absolutte stier: 0 ekte. `git grep '/Users/|/home/'` gir 4 treff, alle ufarlige: `.gitignore` `/home/` (rotforankret ignorering), `pakk_jury.sh` `./home/*`, og to rapporter som nevner «/Users/…» og `/home/` uten brukernavn. 0 treff på `~`.
- `git status` i klonen etter kjøringene: 0 endringer i sporede filer.
- Avvik: ingen. Dommer trenger ikke varsles.
