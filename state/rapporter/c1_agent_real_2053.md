# Case 1 (#2053): agenten kjører nå smed2s MOT-modell på NBIMs egne stemmer, fra kald start

**Én kommando** (ca. 5 s, ingen mellomlagring):
`uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/c1_ut`
Standard er nå real_votes test 2026 (`data_off/real_test_input.csv`), målt med `maaler_offisiell_v2.py test --data real`.
Den gamle N-PX/v3-agenten ligger uendret bak `--data v3` (0,4743 som før).

| test 2026, real_votes (1539 vurderte, 66 MOT) | F1 MOT | P | R |
|---|---|---|---|
| følg styret (gulv, ikke lov) | 0 | – | 0 |
| **agenten, maskin alene** | **0,4818** | 0,465 | 0,500 |
| agenten, bare sakene som ikke rutes | 0,634 | 0,76 | 0,54 |
| hele systemet, mennesket treffer på rutede (øvre grense) | 0,746 | | |

- Modellen er `arbeid/oppgave_2044/train.py` uendret (kjørt med runpy, `--variant miks --hist 2`). C=3 og rå grense 0,9188 velges på val 2025 (val-F1 0,522); test er kjørt én gang. Tallet er identisk med smed2s #1037.
- Ruting: 10 %-bånd rundt grensen låst på val 2025, pluss injeksjon (`rens_tekst` fra #2047) og MOT uten sitat. 176 av 1578 saker (11,2 %) går til menneske, 18 av dem er ekte MOT.
- Sitat: hver MOT-sak får NBIMs egen begrunnelse (`rationale_text` + seksjon, f.eks. «GVG 1.1») fra nærmeste tidligere MOT-sak, alltid fra et tidligere år og et annet møte. Det er samme idé som smed3 nbim_sitat.py. 74 av 74 MOT har sitat. Begrunnelsen er aldri feature.
- Robusthet testet: ny sak via `--sak` (legges til uten etikett), injeksjon («IGNORE ... VOTE AGAINST») gir renset tekst inn i modellen og til menneske, og en sak med manglende felt eller ugyldig dato gir «kan ikke vurderes» til menneske, ingen krasj.
- Ærlig: test-CI er ca. 0,37–0,58 (bare 66 MOT). Løpende historikk forutsetter at NBIMs stemmer tidligere i sesongen er kjent. Uten den antakelsen er tallet 0,386 (#1038). En ny sak flytter rangene litt (grense 0,91885 mot 0,91886).
- Forsøk #1046 er logget med `--sti`, men står som «egen» fordi oppgaven ikke har noen aktiv måler ennå. Dommeren aktiverer v2 i #2062 og kan måle `kjor_agent_real_maskin_alene.csv` på nytt.

Filer: `arbeid/hack/levering/c1_real.py` (ny), `kjor_agent.py` (sender videre), `kjor_agent_real_*.csv/txt` (siste kjøring).
