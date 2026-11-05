# Case 1: pakka installert med tom uv-cache og nett (#2417)

Forbeholdet fra #2412 (uv sync gikk uten nett fordi hjulene lå i cachen) er nå testet bort.

| Kjøring | uv-cache | Python | uv sync | kjøring | utgang | HOVEDTALL | TALLVAKT |
|---|---|---|---|---|---|---|---|
| A 15:32 | tom `/tmp/tomcache_153242` → 232 MB | uv-managed 3.13 fra før | 3 s | 37 s | 0 | 0.476190 | GRØNN |
| B 15:33 | tom `/tmp/tomcache_153331` → 233 MB | også tom (`UV_PYTHON_INSTALL_DIR` tom, `only-managed`): lastet ned 3.14.7, 73 MB | 4 s | 52 s | 0 | 0.476190 | GRØNN |

- Kommando: `UV_CACHE_DIR=/tmp/tomcache_<n> sh arbeid/hack/levering/fremmed.sh /tmp/fremmed_tomcache_<n>` (B i tillegg `UV_PYTHON_INSTALL_DIR=/tmp/tompy_<n> UV_PYTHON_PREFERENCE=only-managed`).
- Logger: `arbeid/oppgave_2417/tomcache_153242.log`, `tomcache_153331.log`.
- Merk: uv sync-tida (3–4 s) er målt på gudens linje her; en tregere linje bruker lengre tid på ~230 MB hjul (+ ~70 MB Python om den mangler). Veggtid hele fremmed.sh: 41 s (A) og 58 s (B).
- Funn: med fersk Python velger uv 3.14.7 (pyproject krever >=3.13); tallet er identisk, så ingen grunn til å endre noe før frys.

## Setning til README (smed2, #2416)
Første installasjon (`uv sync`) trenger nett én gang og laster ned ca. 230 MB pakker (pluss ca. 70 MB Python hvis uv ikke finner Python 3.13+); på vår linje tok det 3–4 sekunder, og hele kjøringen fra tom cache var ferdig på under ett minutt med samme hovedtall (F1 MOT 0,476).
