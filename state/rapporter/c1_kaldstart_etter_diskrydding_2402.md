# Case 1: kald start av levert agent (#2044) etter diskrydding, #2402

Dato: 2026-11-05 15:25. Kjørt av dommer med `sh arbeid/hack/levering/fremmed.sh /tmp/fremmed_2402`
(ren kopi, eget uv-miljø, `env -i`).

## Resultat: GRØNN
| Tall | Verdi |
|---|---|
| HOVEDTALL F1 MOT mot styret (v3 --score mot) | 0,476190 (TP 30, FP 38, FN 28; 58 MOT i fasit) |
| v2 avvik fra styret | 0,481752 |
| Til menneske | 188 av 1578 (11,9 %) |
| Tid | uv sync 1 s, kjøring 42 s, totalt 43 s |
| Tallvakt | GRØNN, 169 påstander om hovedtallet stemmer, 0 avviker |
| Frysvakt | ikke frosset ennå (ventet, frys kl. 16) |
| Ledig disk etter kjøring | 7,0 GB (var 4,4 GB da jeg startet) |

Samme tall som levert (`tavle.py levert`: 0,476190). Ingen filer mangler.

## Modell-cachen
Agenten er uavhengig av modell-cachen: ingen av de kopierte filene (kjor_agent.py, train.py,
case1_mot.py, vern.py) refererer til huggingface, torch eller ~/.cache. Kopien er 269 MB
(nesten alt er .venv), home-mappa i kopien er tom etter kjøring. Rydding i cachen kan ikke
påvirke pakka.

Min kopi /tmp/fremmed_2402 er slettet etter kjøringen.
