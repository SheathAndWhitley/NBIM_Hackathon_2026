# Case 1: jury-zipen kjørt med annen Python enn landsbyens (#2353)

Zip: `/tmp/jurypakke_c1.zip` (15:07, sha256 96fa49c3…1078), uendret. Landsbyen kjører Python 3.12.14.
Hver kjøring: tom mappe, `env -i` (ingen landsby-.venv i PATH), tom uv-buffer `UV_CACHE_DIR=/tmp/uvcache2353`.

## Kommandoer (README ord for ord, pluss valg av Python)
    mkdir /tmp/zip2353 && cd /tmp/zip2353 && unzip -q /tmp/jurypakke_c1.zip && cd c1_stemmeagent
    env -i HOME=/tmp/home2353 PATH=~/.local/bin:/opt/homebrew/bin:/usr/bin:/bin \
        UV_PYTHON=3.13 UV_CACHE_DIR=/tmp/uvcache2353 sh KJOR.sh
    (samme i /tmp/zip2353b med UV_PYTHON=3.14)
    sh arbeid/hack/levering/sjekk_treffsikkerhet.sh /tmp/c1_sjekk2353   # README steg 4, på 3.13-kopien

## Resultat
| Python | utgang | FRYSVAKT | **HOVEDTALL F1 MOT** | TALLVAKT | tid (sync + kjøring) |
|---|---|---|---|---|---|
| 3.13.15 (tom buffer) | 0 | GRØNN (15) | **0.476190** (P 0.4412 R 0.5172, TP 30 FP 38 FN 28) | GRØNN (165 påstander, 0 avvik) | 23 s + 87 s |
| 3.14.7 | 0 | GRØNN | **0.476190** | GRØNN | 14 s + 60 s |

- Steg 4 (3.13): `TP 30 FP 38 FN 28 TN 1443: STEMMER`, sha256 = frossen fil (b113b545…): LIK.
- `ut/pred_maaler.csv` og `ut/agent.csv` er bit-like mellom 3.13 og 3.14 (b113b545…, 1543706f…).
- Ingen feil eller tracebacks i loggene. KP: forventet 0.476190, fikk 0.476190.

## Funn til smed (ingenting feilet, men juryen vil se dette)
1. **pyproject.toml i zipen er landsbyens egen**: `name = "landsby"`, «En landsby av agenter som tjener guden», kommentar om at
   landsbyen ble lammet 28.10, og avhengigheter agenten ikke bruker (torch, claude-agent-sdk, catboost, xgboost, interpret, pytabkit).
   Koden i zipen importerer bare lightgbm av disse. Følge: **.venv 1,4 GB, nedlasting 1,5 GB**; README lover «ca. 1 min»,
   på vanlig hotell-nett blir det mange minutter. Forslag: egen slank pyproject/uv.lock for zipen (sklearn, pandas, numpy, lightgbm).
2. README sier «python3 (3.10+)», men `requires-python = ">=3.11"`. Ufarlig fordi uv henter egen Python, men teksten bør si 3.11+.
3. Ikke prøvd: Linux og Python 3.11 (xgboost er kun ≥3.12 i lockfila, men ikke importert, så ventet OK).
