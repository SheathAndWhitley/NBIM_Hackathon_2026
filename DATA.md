# Data: arrangørens casedata

NBIMs stemmer (casedata fra arrangøren av FinTech-hackathonet, Case 1) ligger i `ny_data/` i denne repoen:
`real_votes.csv` (fasiten agenten måles mot) og `npx_votes.csv` (brukes ikke i hovedtallet). `sh KJOR.sh` trenger
bare `ny_data/real_votes.csv`. Bruker du en kopi uten dataene, legg arrangørens fil der først:

    mkdir -p ny_data && cp <casepakka>/real_votes.csv ny_data/
    sh KJOR.sh

`sh KJOR.sh` gjør resten selv:

| hva | sti i repoen | laget av |
|---|---|---|
| real_votes.csv | `state/opplastet/20261105_114241_real_votes.csv` | kopiert fra `ny_data/` |
| testinndata 2026 (uten fasitfelt) | `arbeid/hack/c1/data_off/real_test_input.csv` | `arbeid/hack/c1/lag_inndata.py` |
| valideringsinndata 2025 (uten fasitfelt) | `arbeid/hack/c1/data_off/real_val_input.csv` | `arbeid/hack/c1/lag_inndata.py` |

Stien med tidsstempel er fast fordi målerne og agenten sjekker akkurat den og fila sin sha256: en annen versjon av
real_votes.csv stopper agenten med en tydelig feil. `lag_inndata.py` tar årene 2026 og 2025, setter `id = meeting_id|item_no`
og dropper fasitfeltene; resultatet er byte-likt med filene modellen ble frosset mot. For hånd: `python3 arbeid/hack/c1/lag_inndata.py`.

`FROSNE_SHA256.txt` gjelder filene som ligger i repoen. Agentens egne prediksjoner (csv med id og sannsynlighet) er med.

## Rådata vi selv lastet ned (ikke i repoen, kan hentes på nytt)

| hva | hvordan hente |
|---|---|
| N-PX-stemmefiler fra SEC EDGAR (`arbeid/hack/c1/arkiv/gammel_data/`, flere GB) | `arbeid/hack/c1/hent_npx.py` og `arbeid/hack/c1/hent_votes.py` (sett først `SEC_USER_AGENT="Navn e-post"`: SEC krever kontaktinfo i User-Agent) |
| NBIMs offentlige stemmebegrunnelser (`arbeid/hack/c1/kilder/nbim_begrunnelser*.csv`) | `arbeid/hack/c1/hent_nbim.py` (samme `SEC_USER_AGENT`) |
| csv-er med fasitkolonne eller arrangørens forslagstekst (testinndata, agent.csv m.fl.) | lages på nytt av skriptene i `arbeid/hack/` fra casedataene over, f.eks. `sh KJOR.sh` |
| `arbeid/hack/levering/demo/.venv` | `uv sync` i `arbeid/hack/levering/demo` |

Full liste over utelatte filer med grunn: `python3 arbeid/verktoy/c1_github_alt.py utelatt` (krever landsbyens mappe), og `state/rapporter/c1_github_alt.md`.
