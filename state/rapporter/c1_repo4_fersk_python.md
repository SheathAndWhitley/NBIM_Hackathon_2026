# GRØNN: repo4-zipen kjørt i et helt nytt miljø med Python 3.14 (#2607)

- Zip: `state/levering/c1_gronn/SISTE_GRONNE.zip` = `jurypakke_c1_1724_5514792.zip`, sha256 `fc0dbc55…affedc` (stemmer med c1_zip_repo4.md)
- Pakket ut i tom `/tmp/smed4_2607`, kjørt som README sier: `cd c1_stemmeagent && sh KJOR.sh`, med `UV_PYTHON=3.14` og tom `UV_CACHE_DIR=/tmp/smed4_2607/uvcache`
- Python i .venv: **3.14.7** (landsbyen bruker 3.12.14, og pakka krever >=3.13). uv.lock har hjul for 3.14, og `uv sync --frozen` gikk uten feil.
- Merk: zipen har ingen `jury_kjor.sh`. Inngangen er `KJOR.sh`, så det var den jeg kjørte.

| sjekk | resultat |
|---|---|
| FRYSVAKT | GRØNN, 19 frosne filer |
| HOVEDTALL | `0.512000`, byte-likt README linje 24 (`[ "$a" = "$b" ]` sant) |
| TP/FP/FN | 32/35/26, P 0,4776, R 0,5517 |
| pred_maaler.csv sha256 | `d02cf884…` = den frosne |
| TALLVAKT | GRØNN, 157 påstander, 0 avvik |
| sidetall SCORE | 0.529412 |
| exit-kode | 0 |

**Kjøretid:** 35 s totalt (uv sync 3 s, agent 31 s). Python 3.14 fantes alt lokalt (brew), så den ble ikke lastet ned. Pakkene ble hentet på nytt til tom cache (233 MB pakket ut). Logg: `/tmp/smed4_2607/kjor.log`.
