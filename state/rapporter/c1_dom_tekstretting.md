# Case 1: dom over tekstrettingene i siste grønne zip (dommer, #2667, 05.11 kl. 17.45)

**Dom: RØD.** Zipen har riktig hovedtall overalt der tallvakta ser (0,512, 157 påstander, 0 avvik), men
0,512 omtales fortsatt som «under målet» i tre jurytekster, og 0,476 står som hovedtall/agenttall uten
merkelappen eldre/frossen i demo-manusene, JURY_METODE, SVAKHETER, kjor.sh og JURY_SPORSMAL sp. 20.
Alt under er på zipen; flere linjer er allerede rettet i arbeidstreet (merket «rettet i tre»), så neste
zip (#2549 kl. 19) blir grønn hvis resten tas.

- Zip: `state/levering/c1_gronn/jurypakke_c1_1724_5514792.zip` (= SISTE_GRONNE.zip, git 5514792, kl. 17.24)
- sha256: `fc0dbc5552989f447847e7d7c383f1cc58045db3ba9fdd5a5d7b0b2f1daffedc`
- Pakket ut i tom mappe, 150 filer. Tallvakt kjørt på zipens egen rot: måler v3 F1 0,5120 P 0,4776 R 0,5517 TP 32 FP 35 FN 26; **TALLVAKT GRØNN**, 20 filer, 157 påstander, 0 avvik.
- Grep: `0[.,]476` i 57 tekstfiler (+4 csv med rådata), `under målet` i 4 filer.

## RØDE linjer (fil:linje i zipen, eier)

**smed2, #2653 (BYTT-tekstene i c1/leveranse/):**
1. `c1/leveranse/kravrespons.md:10` «0,512 ligger under målet vårt på 0,5» → 0,512 er *over* 0,5. Står fortsatt i treet.
2. `c1/leveranse/JURY.md:5` «Tallet er under målet 0,5» rett etter 0,512. Rettet i tre.
3. `c1/leveranse/JURY.md:72` «95 % KI [0,36; 0,59] … punktestimatet er under» er den gamle KI-en for 0,476; for 0,512 er KI [0,40; 0,62] (som linje 5 sier) og punktestimatet er over. Står i treet.
4. `c1/leveranse/ERLIG_EVALUERING.md:53` «les 0,512 (0,40–0,62), under målet 0,5». Står i treet.
5. `c1/leveranse/JURY_SPORSMAL.md:81` (sp. 20) «Fordi hovedtallet 0,476 er det eneste som er valgt uten å se test» → hovedtallet er 0,512; 0,476 er den eldre frosne. Står i treet (alt kjent fra #2653).

**smed, #2659 (demo):**
6. `c1/DEMO_MANUS.md:15` «Agenten: F1 0,476 … 30 av 58 … 44 %», `:56` samme i tabell, `:63` «F1 MOT 0,4762 (0.476190), TP 30 FP 38 FN 28», `:4` «F1 0,4762 … uendret». Topplinja sier «frossen agent», men manuset leser opp 0,476 som agentens tall. 3 av 5 linjer igjen i treet.
7. `c1/DEMO_MANUS_5min_tilfeldige.md:24,25,91` «Agenten: F1 {F1_TEST} (0,476)», «Hovedtallet er F1 0,476 på MOT». 1 linje igjen i treet. Skal fila ut av zipen, er det også greit; si det i #2549.

**smed4, #2665 (resten av c1-tekstene):**
8. `c1/JURY_METODE.md:19` «Samme modell, F1 på MOT mot styret (hovedtall) | **0,476**», `:28` «vi ligger under det på test (0,476 på MOT)». Ingen eldre-merking. Står i treet.
9. `c1/SVAKHETER.md:3-4` «modellen og hovedtallet er de samme etter modellfrysen … **0,476 på test 2026**», `:75` engelsk «F1 on AGAINST is 0.476 on test 2026». Står i treet. Trenger én linje øverst: eldre frossen #2044, hovedtall nå repo4 0,512.
10. `c1/leveranse/kjor.sh:10` kommentar «Forventet SCORE 0.481752 (avvik), MOT mot styret F1 0.4762» i selve kjøreskriptet som gir 0,512. Står i treet.
11. `c1/tall_tabell.md:10,12` tabell generert 13:38 med #2044 som «modell»; topplinja sier ikke at den er eldre. Legg «eldre (før bytte 17:03)» i topplinja, eller generer på nytt.
12. `levering/JURY_SPORSMAL.md:117` «(0,476 mot 0,520)» uten eldre. Rettet i tre.

## GRØNT (merket eldre/frossen, eller tydelig om noe annet)
- `levering/README.md:12`, `GITHUB_README_UTKAST.md:32`, `JURYSVAR.md:23`: 0,476 som «frossen» i tre-års-tabellen.
- `c1/leveranse/README.md:12`, `BEGRENSNINGER.md:3,18`, `MUNTLIG.md:13`, `NESTE_VERSJON.md` (4), `ERLIG_EVALUERING.md:34,85,104`, `JURY.md:58,60`, `JURY_SPORSMAL.md:52,57,61,95,100`: alle sier eldre/frossen #2044 eller «forrige frosne modellen».
- `c1/leveranse/kilder/*` (26 filer, 104 treff): LESMEG.md sier kopier fra 14.15 med uendret innhold; målerapporter på den frosne modellen, datert. `kilder/hand_tall3.py` er selve rettingsskriptet (#2592) og inneholder gammel og ny streng; «under målet»-treffene der er fra-strengene.
- `state/rapporter/*` i zipen (6): daterte rapporter om den frosne modellen (#2188, #2272, #2280, #2358, #2399, #2406).
- `arbeid/verktoy/c1_tallvakt.py:6`: eksempel i docstring.
- csv-filer: rådata/prediksjoner, ikke tekst.

## Hva som må skje før 19:00
Punkt 1, 3, 4, 5 (smed2), 6, 7 (smed), 8, 9, 10, 11 (smed4). Punkt 2 og 12 er allerede ute av treet.
Dommer2 dømmer den nye zipen i #2668 etter #2549; tallvakta alene er ikke nok, grep «under målet» og «0,476» må gjøres på nytt.
