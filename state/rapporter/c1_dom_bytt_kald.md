# Case 1: dom på BYTT til repo4 fra kald start (#2649), GRØNN 17:29

**Dom: GRØNN.** Jury-zipen etter #2592/#2639 reproduserer F1 MOT 0,5120 (TP 32, FP 35, FN 26, TN 1446) i tom mappe uten landsbyens .venv. Alle fire akseptkrav oppfylt.

| Krav | Resultat |
|---|---|
| F1 MOT 0,5120, TP32 FP35 FN26 | `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000`, 2x2 fra rådata: TP 32 FP 35 FN 26 TN 1446 |
| sjekk_treffsikkerhet.sh | `forventet TP 32 FP 35 FN 26 TN 1446: STEMMER`, ny prediksjonsfil = frossen d02cf884…4a0c: LIK |
| frysvakt, frys 17:18 | landsby: `FRYSVAKT GRØNN: 21 filer like som ved frys 2026-11-05T17:18:18`; i zipen: 19 frosne filer samme sha256 som ved pakking |
| tallvakt 0 avvik | `20 filer, 157 påstander om hovedtallet stemmer, 0 avviker`, TALLVAKT GRØNN; tallsjekk i landsby: 0 tall uten kilde |

Zip: `state/levering/c1_gronn/jurypakke_c1_1724_5514792.zip` (= SISTE_GRONNE.zip), sha256 `fc0dbc5552989f447847e7d7c383f1cc58045db3ba9fdd5a5d7b0b2f1daffedc`, bygget på commit 5514792. HEAD 9ffe88c skiller seg fra 5514792 bare i `frys_fasit_1600.sha256` (frys regenerert for 8 tekster), frysvakta i landsby er grønn på HEAD.

Kald kjøring: tom mappe `/tmp/c1_dom_2649/zt`, `env -i` med tom HOME, sandbox som nekter lesing av landsbymappa. Kopien laget egen `.venv` fra uv.lock. Loggen nevner aldri «landsby». Agenten på test 2026: 1578 saker inn, 1539 med fasit, 164 til menneske (10,4 %). Tid: ziptest ca. 3 min, selve agenten 12 s.

Kommandoer kjørt (fra <repo>):
```
shasum -a 256 state/levering/c1_gronn/jurypakke_c1_1724_5514792.zip
python3 -I arbeid/verktoy/c1_frys.py sjekk --krev
python3 -I arbeid/verktoy/c1_tallsjekk.py --bare-ikke --feil
sh arbeid/hack/levering/test_jury_zip.sh state/levering/c1_gronn/jurypakke_c1_1724_5514792.zip /tmp/c1_dom_2649/zt
   (= unzip, cd c1_stemmeagent, sh KJOR.sh, sh arbeid/hack/levering/sjekk_treffsikkerhet.sh)
```
Logger: `/tmp/c1_dom_2649/ziptest.out`, `/tmp/c1_dom_2649/zt.logg`, `/tmp/c1_dom_2649/zt/sjekk.logg`.

Merk til #1972 (19:30): kommer det nye commits i leveranse/ etter 5514792 (tekststopp #2549 kl. 19), må `bash arbeid/hack/levering/sluttsjekk.sh` kjøres på nytt på den nye zipen. Denne dommen gjelder sha fc0dbc55.
