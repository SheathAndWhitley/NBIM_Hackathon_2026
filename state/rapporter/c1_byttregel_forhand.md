# Case 1: byttregelen slik den gjaldt FØR måling, og sjekk av smed4s målebenk (#2567) — dommer2 #2575, 05.11 16:57

## Regelen (ordre #265, fastsatt før måling)
En kandidat erstatter frossen #2044 bare hvis, målt med den offisielle måleren (`maaler_aar.py --score mot`,
F1 på stemmer MOT styret) på tre rullende testår 2024/2025/2026 (val = året før, trening = år før val):
1. snittet over de tre årene er minst **+0,02** over frossen (frossen: 0,4545 / 0,5143 / 0,4762, snitt 0,4817), og
2. **intet år** er mer enn **0,02 under** frossen.
Dommeren avgjør (#2570, kl. 18). Ellers står frossen.

Tidslinje (tavla og git): ordre #265 inn 16:46:54; regelen i oppgaveteksten til #2567 16:48:59 og i mission.md
commit `c1e7cf8` 16:49:22; smed4 startet 16:49:00; de nye målingene (repo4 2024/2025, hybrider 2025, benk.txt)
er skrevet 16:49:31–16:50:54. Regelen sto altså før de avgjørende tallene fantes. Ærlig forbehold: 2026-tallene for
alle kandidater (repo4 0,5120 fra #2490, 16:13) og frossens tre år (#2496/#2503) var kjent da regelen ble skrevet.
Det som ikke fantes før regelen, og som avgjør, er repo4 på 2024 og 2025.

## Sjekkliste
| # | Punkt | Status | Grunnlag |
|---|---|---|---|
| 1 | Hvert testår trenes bare på år før; val = året rett før | **GRØNN** | `abl_rull.py`: val VA=TA−1 trent på år<VA, test trent på år<TA; TF-IDF/one-hot fittes bare på treningsrader. `rull3.py`: hybrid trent ≤T−2, valgt på T−1, test T. Repoets `add_history` oppdaterer først etter hele møtet (bare tidligere møter). |
| 2 | Terskel og rutingsbånd velges på val, ikke test | **GRØNN** | `abl_rull.py`: C og grense fra rutenett på val, testfila skrives med rå val-grense (linja «samme andel flagget» er bare utskrift). `rull3.py`: a/b/t fra rutenett på val, hybridens t_flag fra `fit_select(train, valid)`. Testår kjørt én gang. |
| 3 | Frossen i samme benk gir 0,4545 / 0,5143 / 0,4762 (dommer #2503) | **GRØNN** | Kjørt på nytt av meg fra `oppgave_2567/abl_rull.py` (arbeid/oppgave_2575/kjor.sh): byte-like 2496-filene, offisiell måler gir nøyaktig 0,4545 / 0,5143 / 0,4762. |
| 4 | Kandidaten som består (repo4) reproduserer | **GRØNN** | Mine repo4-filer byte-like smed4s (2024, 2025) og #2490 (2026). Måler: 0,5057 / 0,5309 / 0,5120, snitt 0,5162 (+0,035). KI snitt [−0,005; +0,078], 4 % av trekk under frossen, identisk med smed4. |
| 5 | Skript lik dommerens kalde kopi | **GRØNN** | `abl_rull.py`, `maaler_aar.py`, `diff_ki_aar.py` i 2567 er diff-like oppgave_2503 (og 2496). Datavakt: sha256 71ba5135, samme fil. |
| 6 | Forbudte kolonner | **GRØNN** | FEATURES-linja i loggene: ingen av nbim_vote, rationale_*, funds_disagree, position_paper. Repo-trekkene bygges av `against_board` fra tidligere møter. `prev_same_section` (rationale) er ikke blant de fire repo4-trekkene. |

Merknad (ikke rødt, gjelder frossen og kandidater likt): historikktrekkene er «løpende» (`--hist 2` og repoets
`add_history`): en sak i teståret ser etiketter fra tidligere møter samme år. Det er frossens egne konvensjon fra
#2044, og den gjelder alle kandidatene på samme vilkår. Repoets prior `base_rate` er én skalar fra 2019–2023.

## Konklusjon
Ingen røde punkter. Benken er ren, og tallene i `c1_tre_aar_kandidater.md` er reprodusert av meg. Etter regelen
består bare repo4 (snitt +0,035, verste år +0,017 i 2025); gevinsten er ikke statistisk sikker (KI krysser null).
Selve byttedommen tas i #2570. Rullende 2023 som fjerde år (#2573) bør leses før dommen hvis den er klar.

Gjenskap: `bash arbeid/oppgave_2575/kjor.sh`, deretter fra `arbeid/oppgave_2567/`:
`python3 -I maaler_aar.py ../oppgave_2575/<full|repo4>_<år>_test.csv y<år> --data real --score mot`.

Commit: rapporten ligger i 23135ba (regelen: c1e7cf8). Kjøringsfilene i arbeid/oppgave_2575/ er git-ignorert og ligger bare på disk.
