# Case 1: kald start fra jury-zip med tom HOME og tom uv-cache (#2492): GRØNN

**Resultat:** Zipen fungerer på en «jurymaskin» som aldri har sett uv-cachen eller Python-installasjonene våre. Den gir F1 MOT **0.476190** og TP 30 FP 38 FN 28 TN 1443 (STEMMER), og prediksjonsfila har samme sha256 som den frosne (b113b545…3653, LIK). Det ble testet med begge Python-versjonene under.

## Oppsett
- Zip: bygget fersk med `pakk_jury.sh` fra HEAD 7a5d892 (16:13) kl. 16:16, 900K, 117 filer, sha256 68b8ee232b9fbaf5…, «sha256 i pakka = frysfila». NB: arbeidstreet hadde en ukommittert endring i `c1/leveranse/NESTE_VERSJON.md` (tekst, ikke frosset), og den kom med i zipen.
- Strengere enn `test_jury_zip.sh`: `env -i`, tom `HOME` og tom `UV_CACHE_DIR` i /tmp, og PATH = bare en kopi av uv-binæren + /usr/bin:/bin (systemets python3 er 3.9, så den kan ikke brukes). Sandbox-exec nektet lesing av landsbymappen, ~/.cache, ~/.local (uv-pythonene våre), ~/.config og Homebrews python@3.13. Profilen ligger i `arbeid/oppgave_2492/sandbox.sb`.
- Uv måtte altså laste ned både Python og alle pakkene selv.

## Tall
| Variant | Python (lastet ned av uv) | uv sync | agent + målere | totalt inkl. unzip og sjekk | F1 MOT | tallvakt | ny prediksjonsfil = frossen |
|---|---|---|---|---|---|---|---|
| standard | 3.14.7 (uv velger nyeste ut fra `>=3.13`) | 7 s | 32 s | 47 s | 0.476190 | GRØNN | LIK |
| `UV_PYTHON=3.13` | 3.13.15 | 5 s | 42 s | 54 s | 0.476190 | GRØNN | LIK |

Plassbruk per kjøring: uv-cache 233 MB, Python 73 MB, .venv 265 MB. Til sammen ca. 0,6 GB, som juryen bør ha ledig.

## Funn
1. Første kjøring på en ren maskin tar under ett minutt. «uv sync» på 5–7 s gjelder med rask linje (nedlasting av ca. 300 MB). README kan trygt si «ca. 1 minutt + nedlasting».
2. Pakka låser ikke Python-versjonen (ingen `.python-version`), så en ren maskin får 3.14. Vi har nå målt at både 3.13 og 3.14 gir byte-lik prediksjon. Ingen endring er nødvendig, men en `.python-version` med 3.13 ville gjøre kjøringen helt deterministisk. Det hører til neste versjon, ikke frysen.
3. Ingen linjer i loggen nevner «landsby».

Logger: `arbeid/oppgave_2492/kald_py314.logg`, `kald_py313.logg`. Tmp-mappa /tmp/smed4_2492 (850 MB) er slettet.
