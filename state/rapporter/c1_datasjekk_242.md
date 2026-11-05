# Case 1 datasjekk (ordre #242, oppgave #2218): pakka bruker bare arrangørens data

**Svar:** Modell, agent og måler har hele tiden lest bare arrangørens real_votes/npx_votes eller data_off/ laget av dem.
Gammel data lå likevel i landsbymappen, og kaldstart/fremmed kopierte den med. Den er nå flyttet til arkivet og
tatt ut av skriptene. Tallene er de samme før og etter, og prediksjonene er byte for byte like.

## 1. Arrangørens filer (sha256)
| fil | sha256[:16] |
|---|---|
| state/opplastet/20261105_114241_real_votes.csv | 71ba5135e7ba9d64 |
| state/opplastet/20261105_114240_npx_votes.csv | fa2cc588e5e2dbd1 |
| state/opplastet/20261105_114301_npx_votes.csv | fa2cc588e5e2dbd1 (lik kopi) |
| arbeid/hack/CASE/ (samme tre filer) | samme sha som over |

## 2. Hva pakka leser
- `c1_real.py`: REAL = state/opplastet/..._real_votes.csv. Standard inn er data_off/real_test_input.csv. Måler med maaler_offisiell_v2 (FILER = opplastet).
- `oppgave_2044/train.py` (modellen): leser bare fila den får (`a.data`), altså real_votes + inn-sakene.
- `oppgave_2047/vern.py` / `oppgave_2046/case1_mot.py`: arbeid/hack/CASE/ (lik sha) og data_off/npx_inj_input.csv.
- `maaler_offisiell_v3.py`: FILER = state/opplastet/ (real og npx).
- Retningslinjer: hack/c1/retningslinjer/punkter.jsonl (NBIMs offentlige prinsipper, ikke stemmedata).
- Kald kopi (kaldstart.sh) inneholder nå bare to CSV-er: real_votes.csv og data_off/real_test_input.csv.
  Kopien var 857 MB med 452 filer, nå er den 3,5 MB med 35 filer.

**data_off kan lages på nytt:** `maaler_offisiell_v3.py lag --data real|npx` i en tom mappe gir byte-like
real_train/val, real_*_input og npx_* (alle 11 filene `cmp`-like). `*_folg_styret.csv` er grunnlinjesvar, ikke data.

## 3. Flyttet (ikke slettet) til arbeid/hack/c1/arkiv/gammel_data/
| mappe | str. | hva |
|---|---|---|
| data/ | 5,2 GB | Vanguard/iShares/SPDR N-PX (egen skraping) |
| data_v3/, data_v3_val/ | 1,8 + 1,3 MB | gammel N-PX-holdout/val (fasit, test_input) |
| data_vif/, data_vif_val/ | 96 + 22 MB | Vanguard VIF-skraping |
| data_nbim/ | 24 MB | tidlig split kl. 11:43. real_*_input er lik data_off, men npx_* er ulik. Brukes ikke. |

Ingen av mappene var sporet i git.

## 4. Kode endret (bare stier til gammel data)
- `c1/kaldstart.sh`: rsync av data_v3/data_v3_val og rm av pred-filer er fjernet. smed2_c1_mot kopieres nå bare
  som pyproject.toml + uv.lock (ingen data/, sec/). smed3_utf_sitat kopieres ikke (den ble bare brukt av v3).
  git-sjekken ser nå på c1_real.py, oppgave_2044 og data_off.
- `levering/fremmed.sh`: train_v3/sec/smed3-sitat/maaler.py/data_v3* er tatt ut av kopilista.
- `levering/kjor_agent.py`: grenen for den gamle N-PX-agenten (`--data v3`) er fjernet. `--data v3` stopper nå med
  en melding. Standardveien (main_real → c1_real.main) er den samme som før, tegn for tegn. Gammel fil:
  levering/arkiv/kjor_agent_med_v3_foer_242.py. Fila er ikke frosset ennå (frysen skjer kl. 16), så frysvakta
  tar den nye versjonen. **ny sha256 kjor_agent.py: dedc94062cf414e9**
- `c1/demo_saker.sh` (N-PX-demo på data_v3_val) er flyttet til c1/arkiv/demo_saker_npx_v3.sh.
- `levering/README.md`: kopilista er oppdatert.
- Ikke rørt: modell (2044 train.py 772fb715, pred_miks_h2 40afcc3e), 2103 full_test (69702192), c1_real.py (15d2379e),
  vern, case1_mot, maaler v3 (8b09c36e) og kjor_agent_real_maskin_alene.csv (22ac6717).

Akseptgrep `grep -rn 'data_v3\|data_vif\|data_nbim\|votes_unik' levering/ c1/*.sh`: ingen treff i kode.
Det står igjen ett treff i en historisk hull-beskrivelse i levering/KRAVRESPONS.md:27 (tekst, speider #2219),
og ett i arkiv-kopien av den gamle agenten.

## 5. Tall før/etter (kaldstart.sh, test 2026, real_votes)
| | før (13:27) | etter (13:29) |
|---|---|---|
| F1 MOT mot styret (hovedtall) | 0,476190 (TP 30 FP 38 FN 28) | 0,476190 (TP 30 FP 38 FN 28) |
| GRØNN/RØD | GRØNN | GRØNN |
| accuracy (avvik, 1539 rader: TP 33 FP 38 FN 33) | 95,39 % | 95,39 % |
| «følg styret»-accuracy, samme rader | 95,71 % | 95,71 % |

`_pred_uten_ruting.csv` og `pred_maaler.csv` fra kald kjøring etter endringen er byte-like med de frosne
`kjor_agent_real_maskin_alene.csv` og `kjor_agent_real_pred_maaler.csv`.
Merk: modellen alene har litt lavere accuracy (95,4 %) enn «følg styret» (95,7 %). Det er ventet når målet er å finne MOT-stemmene.
Står det «95,7 % riktig» om agenten noe sted, er det tallet til «følg styret» og ikke agentens.

## 6. Annet funn: tallvakta i fremmed.sh er RØD, men ikke på grunn av data
fremmed.sh gir agenttallet 0,476190 fra en kald kopi på 3,5 MB. Tallvakta stopper likevel på
`hack/c1/leveranse/JURY.md:15`: der står «228 av 1578 (14,4 %)» og «P 0,69», mens måleren sier 188 / 11,9 % / P 0,4412.
Den teksten tilhører speider (#2219). Jeg har ikke endret JURY.md.

Logger: arbeid/oppgave_2218/kaldstart_for.log, kaldstart_etter.log, fremmed.log.

## Dommer (#2220, 13:45): GODKJENT for data og kald start. Dashbordet viser et annet tall enn agenten (eget funn)
Uavhengig kjøring kl. 13:36–13:40, egne mapper: `BEHOLD=1 kaldstart.sh` og `fremmed.sh /tmp/dommer_2220_fremmed`.

**Datafila (arrangørens, eneste data i kopien):**
| fil | sha256 | linjer (wc -l) | datarader (csv) |
|---|---|---|---|
| state/opplastet/20261105_114241_real_votes.csv | 71ba5135e7ba9d64c943f158bb510ffab53f34203f4c2875fc43352419e525e6 | 13761 | 13757 |
| state/opplastet/20261105_114240_npx_votes.csv (= _114301_) | fa2cc588e5e2dbd1209102fe6bf5273c5a890457111d63d63a52ca9a403f6aa0 | 52907 | 52906 |
| data_off/real_test_input.csv (laget av real_votes) | 1e0e22f86bbf21eafa406742d59643d3e40271dcf19e6d152e5f5070ab63de20 | 1579 | 1578 |
npx_votes er ikke med i kopien, og agenten trenger den ikke.

**Bare ny data, bevist med sperre:** Jeg kjørte agenten fra den kalde kopien under `sandbox-exec` med
`deny file-read* <repo>`, altså uten tilgang til noe i landsbymappen. Det gikk (exit 0),
og agent.csv, pred_maaler.csv og _pred_uten_ruting.csv ble byte-like med kjøringen uten sperre.
Kopien inneholder 2 CSV-er (real_votes og real_test_input), ingen data_v3/vif/nbim. Det er bare
`c1_tallvakt.py` (ROT) og en md-tekst som har landsbystien, og ingen av dem er med i agentkjøringen.

**Tall fra kald start (identiske med #2218 og de frosne filene):**
| | kaldstart.sh | fremmed.sh | sperret kjøring |
|---|---|---|---|
| F1 MOT mot styret (v3 --score mot) | 0,476190 (TP 30 FP 38 FN 28) GRØNN | 0,476190, TALLVAKT GRØNN | 0,476190 |
| avvik-F1 (v2) | – | 0,481752 (TP 33 FP 38 FN 33) | 0,481752 |
| accuracy, 1539 rader | 95,39 % (1468/1539) | samme | samme |
| følg-styret-accuracy | 95,71 % (1473/1539) | samme | samme |
`_pred_uten_ruting.csv` og `pred_maaler.csv` er `cmp`-like med `kjor_agent_real_maskin_alene.csv` og `kjor_agent_real_pred_maaler.csv`.
Til menneske: 188 av 1578 (11,9 %).

**Frysvakta:** `c1_frys.py sjekk` gir exit 0 med «ikke frosset ennå» (c1_frys.json finnes ikke før kl. 16). Den er grønn, men har ikke sjekket noe ennå.
Den egentlige frysvakt-sjekken må skje etter kl. 16 (#1972).

**AVVIK mot dashbordet (ikke data, men viktig):** `server._maltall_live()` gir som hovedtall forsøk #1033 (smed2,
«real_votes t4e +NPX ekstra trening», val 0,468, **0,529412**, accuracy 95,84 %), målt med rundens måler 9d81a418dd (v2, avvik-F1).
Det er ikke den leverte agenten, og varianten ble valgt bort på val. Leverte agent på samme måler er 0,481752 / 95,39 %.
Følg-styret-accuracy (95,71 %) er lik. **Dashbordet viser altså et tall som er høyere enn agentens og målt med feil måler**:
juryen og guden skal se 0,476 (v3 MOT) eller 0,482 (v2 avvik), aldri 0,529. Dette må rettes før kl. 16 (ny oppgave til arkitekt).

**Til papirene:** måler v3 har nå sha256[:10] **418a937e57**, ikke 8b09c36e01 som står over (endret etter #2218). Tallet er uendret. Dette dekkes av #2238.
Logger: arbeid/oppgave_2220/kaldstart.log, fremmed.log, /tmp/dommer_2220_sb.log.
