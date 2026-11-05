# Case 1: tørrkjøring av kald kopi (#2118, dommer, 05.11 12:50)

**Konklusjon:** På standardstien (`kjor.sh` → `fremmed.sh` → `kjor_agent.py` → `c1_real.py`, `--data real`)
mangler kopien **bare de to filene som #2116 allerede retter**. Ingen nye blokkerende funn.

## Hva jeg gjorde
1. `fremmed.sh` kjørt til tom mappe `/tmp/torr2118`, kuttet før `kjor_agent.py` (kopi + `uv sync --frozen`, 162 MB).
   Skript: `arbeid/oppgave_2118/fremmed_kopi.sh`.
2. Statisk skann av alle 12 .py i kopien: importer og filstier (`arbeid/oppgave_2118/skann.py`, utdata `skann.txt`),
   sjekket mot kopi og kilde.
3. Importsteget dynamisk under `env -i` med kopiens .venv: `import c1_real`, exec av `vern.py` (som laster
   `case1_mot.py`), `import fakta`, og alle tredjepartspakker (numpy, pandas, scipy, sklearn, lightgbm).

## Funn
| Fil | I kopien | Brukes på standardstien | Virkning |
|---|---|---|---|
| `arbeid/hack/levering/retningslinje_oppslag.py` | NEI | ja (`c1_real.py:162`) | **ModuleNotFoundError**, krasj (kjent, #2116) |
| `arbeid/hack/c1/retningslinjer/punkter.jsonl` | NEI | ja (leses av `Oppslag`) | krasj (kjent, #2116) |
| `arbeid/kandidater/smed2_c1_mot/forklaring.csv` | NEI | nei, bare `--data v3` (`kjor_agent.py:214`) | stille: MOT-sitatenes grunn blir tom, ingen krasj |
| `state/opplastet/20261105_114240_npx_votes.csv` | NEI | nei, bare målerne med `--data npx` | krasj hvis noen måler npx i kopien |
| `arbeid/hack/CASE/*_real_votes.csv`, `*_npx_votes.csv` | NEI | nei, bare når `case1_mot.py` kjøres som skript | ingen ved import |
| `arbeid/hack/c1/data_off/npx_inj_input.csv` | NEI | nei, bare `vern.py` som skript | ingen ved import |

Kontroll: med de to #2116-filene lagt inn for hånd i kopien går `import c1_real, retningslinje_oppslag` og
`Oppslag(real_votes)` rent under `env -i`. `fremmed.sh` inneholder fortsatt ingen av de to (grep 12:50), så #2116 er ikke gjort ennå.

## Ikke dekket
Ikke kjørt hele pipelinen (det er #1952 kl. 13), ikke sjekket `demo/` eller `maaler.sh` (de kjører fra landsbymappen, ikke fra kopien).
Rad 3 (`forklaring.csv`) er verdt å ta med i #2116 hvis v3-sporet skal vises i demoen; ellers ikke nødvendig.
