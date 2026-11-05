# Dom #2476: jury-zipen har kandidatens pyproject/uv.lock og gir 0,476190 (GODKJENT, zipen må bygges på nytt)

Dømt 2026-11-05 16:20 av dommer. Grunnlag: smed4 sin retting #2475 (state/rapporter/c1_zip_pyproject.md),
zip /tmp/s4_2475/jurypakke_c1.zip (bygd 16:08:25, sha256 c14a4636…3218).

## Hva jeg gjorde selv
1. Pakket zipen ut i ny tom mappe (/tmp/dommer_2476/ut): 117 filer.
2. sha256 i zip-rota mot arbeid/kandidater/smed2_c1_mot:
   - pyproject.toml 96fcf3b1…07d50, name «smed2-c1-mot»: LIK kandidatens.
   - uv.lock ed54fd6c…21a6: LIK kandidatens.
3. Kaldstart med test_jury_zip.sh (tom HOME, tom uv-cache, sandkasse nekter landsbymappa), egen testmappe:
   FRYSVAKT GRØNN (15 frosne filer), HOVEDTALL F1 MOT 0.476190, TP 30 FP 38 FN 28 TN 1443 STEMMER,
   prediksjonsfil = frossen (b113b545…3653) LIK, TALLVAKT GRØNN, ZIPTEST GRØNN. 64 s totalt.
   Miljøet kjøringen brukte var kandidatens: uv.lock i testmappa ed54fd6c…, 19 pakker i .venv,
   ingen torch/catboost/claude-agent-sdk (det landsbyens lås ville gitt).
4. c1_frys.py sjekk --krev: FRYSVAKT GRØNN, 17 filer like som ved frys 16:00:01.
5. frys_diff.sh --kilde: FRYS LIK, 0 avvik (fasit 117 filer, regenerert 16:13:51 i 7a5d892).
6. frys_diff.sh mot zipen: FRYS AVVIK 3: DEMO_MANUS.md, JURY_SPORSMAL.md, NESTE_VERSJON.md er ENDRET.
7. pakk_jury.sh i HEAD: `sh -n` OK (syntaksfeilen fra bb8289f er rettet).

## Dom
- Rettingen #2475 er GODKJENT: zip-rota har kandidatens pyproject.toml og uv.lock, kaldstarten fra zipen gir
  F1 MOT 0,476190 med kandidatens låste miljø, frysvakta er grønn, og fasiten stemmer med kilden.
- Zipen /tmp/s4_2475/jurypakke_c1.zip er IKKE endelig. De 3 avvikene er jurytekster endret etter 16:08
  (#2480 og #2487 i JURY_SPORSMAL.md 16:13, arkitekt #2481 i NESTE_VERSJON.md 16:15, DEMO_MANUS.md).
  Ingen av dem er frosne modellfiler, så tallene er uberørt. Det er ventet drift, ikke en feil i rettingen.
- Konsekvens: endelig zip bygges på nytt i sluttsjekken (#1972, 18:30) ETTER at alle tekstoppgaver (#2481,
  #2487, #2494, #2470) er lukket, og frys_diff mot den nye zipen skal da gi LIK. Bygges zipen før tekstene
  er ferdige, blir det avvik igjen.

## Rydding
Testmappene /tmp/dommer_2476/ut og /tmp/dommer_2476/ziptest er slettet (disk var 2,7 GB ledig før, 6,5 GB etter).
