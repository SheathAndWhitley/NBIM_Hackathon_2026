# Case 1: kald start av levert agent (#2044) etter at HF-cachen ble slettet, #2403

Dato: 2026-11-05 15:28. Kjørt av dommer med `sh arbeid/hack/levering/fremmed.sh /tmp/fremmed_2403`
(ren kopi, eget uv-miljø, `env -i`), ETTER at speideren (#2400) slettet 19 GB fra ~/.cache/huggingface
(218 MB igjen: bare bge-small og all-MiniLM-L6-v2).

## Resultat: GRØNN, identisk med #2402 (før slettingen)
| Tall | #2402 (før) | #2403 (etter) |
|---|---|---|
| HOVEDTALL F1 MOT mot styret (v3 --score mot) | 0,476190 | 0,476190 (TP 30, FP 38, FN 28; 58 MOT i fasit) |
| v2 avvik fra styret | 0,481752 | 0,481752 |
| Til menneske | 188 av 1578 (11,9 %) | 188 av 1578 (11,9 %) |
| Tid | 43 s | 46 s (uv sync 0 s, kjøring 46 s) |
| Tallvakt | GRØNN, 169/0 | GRØNN, 169 påstander stemmer, 0 avviker |
| Frysvakt | ikke frosset ennå | ikke frosset ennå (frys kl. 16) |
| Ledig disk | 7,0 GB | 26 GB |

Akseptkrav oppfylt: F1 mot = 0,476190 uendret, ingen manglende modellfiler, ingen feilmeldinger
om filer som ikke finnes.

## Hvorfor slettingen ikke kunne påvirke pakka
- Ingen av de 15 .py/.sh-filene i arbeid/hack/levering nevner huggingface, from_pretrained,
  SentenceTransformer, torch, HF_HOME eller .cache.
- Modellen er en tfidf/lineær pipeline som trenes på nytt i kjøringen (train.py #2044), ingen
  lagret modellfil lastes.
- Kopien er 269 MB, nesten alt .venv; ut/ inneholder bare agent.csv, pred_maaler.csv og KJORING.txt.

Kopien /tmp/fremmed_2403 er slettet etter kjøringen. Neste kaldstart: #2285 (smed3, etter frys kl. 16)
og #1972 (dommer, endelig pakke 18:30).
