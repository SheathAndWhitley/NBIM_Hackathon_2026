# Case 1: lim-inn-fanen logger hver kjøring (#2362, krav 29)

Hvert klikk på Anbefal i lim-inn-fanen skriver nå én fil `arbeid/hack/levering/demo/logg/lim_<tid>_<kjoring>.json`.
Agent, modell og målere er urørt; bare `demo/app.py`, `demo/ekte_agent.py` og `demo/README.md` er endret.

## Hva fila inneholder
- `tid`, `kjoring` (samme id som vises i fanen), `fane`, `modell`
- `tekst_sha256` og `tekst_tegn` for den innlimte teksten, pluss `saker` (meeting_id|item_no)
- `agentkall`: kommandoen (landsbysti erstattet med `<rot>`, midlertidig mappe med `<tmp>`), cwd, utgangskode,
  varighet i sekunder, agentens stdout og halen av stderr
- `svar`: de 19 feltene fra agent.csv per sak, nøyaktig det fanen viser
- `feil`: null, eller feilmeldingen. Feiler innlimingen (manglende felt) eller agenten, skrives fila likevel.

Møte-fanen (stubben) logger som før én linje per forslag til `logg/demo_logg.jsonl`.

## Måling (arbeid/oppgave_2362/test_fane_logg.py, Streamlit AppTest)
| sjekk | resultat |
|---|---|
| de tre demo.sh-sakene (#2335 tre_saker.csv) | 3 rader, 19 felt, 0 avvik mot #2335/#2344 |
| nye filer i logg/ per klikk | 1 (gyldig) og 1 (feilklikk med `feil` satt) |
| sha256 i loggen = sha256 av innlimt tekst | ja |
| svar i loggen = svar i session_state | ja |
| landsbysti i logg/ (jurypakke.finn_lekk med <repo>) | ingen |
| agentkjøring | kode 0, 5,0 s |

Kjør testen: `arbeid/hack/levering/demo/.venv/bin/python arbeid/oppgave_2362/test_fane_logg.py` (ca. 10 s).

## Merk
- `ekte_agent.kjor()` har samme signatur som før (#2335); det nye er `kjor_sporbar()` som alltid returnerer en dict.
- `logg/` er i `levering/.gitignore`, så loggfilene committes ikke; de følger heller ikke jurypakka.
- Kravdekningen (krav 29) har fått én oppdateringslinje.
