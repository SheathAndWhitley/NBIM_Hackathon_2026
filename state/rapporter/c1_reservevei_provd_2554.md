# Case 1: reserveveien i kjøreplanen prøvd på kald kopi (#2554)

Kjørt 16:45 som om hovedkaldstarten feilet kl. 19:30. Reserven var 16:42-zipen, `jurypakke_c1_1642_bf0d3f8.zip`.

| Steg | Resultat |
|---|---|
| `shasum -a 256` mot planen | `83c3fdb6…62d3f8`: stemmer |
| `test_jury_zip.sh <reserve> /tmp/reserve_2554_*` (tom mappe, tom HOME, sandbox) | **ZIPTEST GRØNN**, F1 MOT **0.476190**, TP 30 FP 38 FN 28 TN 1443, frysvakt og tallvakt grønne, prediksjonsfil LIK |
| Tid fra start til grønn zip | **57 s** (planen anslo 5 min) |
| Samme kjøring med nettet sperret | RØD etter 6 s: `Failed to download pandas` (tom uv-buffer) |
| Nettfri variant `arbeid/oppgave_2554/test_jury_zip_utennett.sh` (maskinens uv-buffer, UV_OFFLINE=1) | GRØNN, 0.476190, 68 s |

## Hull, rettet i `c1_kjoreplan_18_20.md`
1. **Kaldtesten trenger nett.** Ny rad i feiltabellen viser hvordan man skiller nettfeil fra zipfeil (nettfri variant).
2. **Pakka bygges fra arbeidstreet, ikke fra HEAD.** De to zipene fra bf0d3f8 (16:42 og 16:44) har 6 tekstfiler som er ulike. Planen krever nå at `git status --short arbeid/hack` er tom før byggingen kl. 18 og 19. Jeg har ikke endret `pakk_jury.sh`, fordi den er andres kode og ligger nær frysen. Forslag til #2549: legg til `-dirty` i navnet når treet ikke er rent.
3. Reservezipen ligger i `state/`, som git ignorerer, så den finnes bare på disk. Ikke rydd `state/levering/c1_gronn/`.

Ingen frosne filer er endret. Den eksakte kommandoen for reserven står nå i planen.
