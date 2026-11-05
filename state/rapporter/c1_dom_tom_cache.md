# Case 1: dom over installasjonen med tom uv-cache (#2421, dømmer #2417)

**Dom: GRØNN.** F1 MOT 0,476190 gjenfunnet i egen kjøring fra tom uv-cache og tom Python-katalog. Tallvakta grønn, utgang 0.

## Hva jeg gjorde
Gjentok smedens strengeste variant (B) selv, i egne tomme mapper, 15:39:

```
UV_CACHE_DIR=/tmp/tomcache_dommer2421 UV_PYTHON_INSTALL_DIR=/tmp/tompy_dommer2421 \
UV_PYTHON_PREFERENCE=only-managed sh arbeid/hack/levering/fremmed.sh /tmp/fremmed_tomcache_dommer2421
```
Begge mappene var tomme før start (sjekket med `ls -A`). Logg: `arbeid/oppgave_2421/tomcache_dommer.log`.

## Resultat
| | smed A | smed B | dommer (som B) |
|---|---|---|---|
| uv-cache etter | 232 MB | 233 MB | 235 MB |
| Python | 3.13 fra før | 3.14.7 lastet ned, 73 MB | 3.14.7 lastet ned, 74 MB |
| uv sync | 3 s | 4 s | 20 s |
| kjøring | 37 s | 52 s | 69 s |
| totalt fremmed.sh | 41 s | 58 s | 89 s |
| HOVEDTALL F1 MOT | 0.476190 | 0.476190 | 0.476190 |
| TALLVAKT | GRØNN | GRØNN | GRØNN |

Kontroller utover smedens:
- Kopiens `.venv/bin/python` peker til `/tmp/tompy_dommer2421/cpython-3.14.7-...`, altså den nedlastede Python-en, ikke systemets. sklearn 1.9.1, numpy 2.5.4 (låst i uv.lock).
- `ut/pred_maaler.csv` er byte for byte identisk med pakkas referanse `arbeid/hack/levering/kjor_agent_real_pred_maaler.csv` (sha256 b113b545dd86b263…), 1578 svarrader + overskrift.
- Måler v3: TP 30, FP 38, FN 28, P 0,4412, R 0,5172, 58 MOT i fasit. Samme som leveransen.

## Avvik å rette (ikke rødt)
Tidsbruken. Smedens setning til README (#2416) sier «3–4 sekunder» og «hele kjøringen fra tom cache ferdig på under ett minutt». Min kjøring tok 20 s nedlasting og 89 s totalt, med andre agenter som belaster maskinen samtidig. Tallet er stabilt, tida er det ikke. README bør si «ett til to minutter på vår maskin, lengre på treg linje», ikke «under ett minutt». Meldt til speider (#2430).
