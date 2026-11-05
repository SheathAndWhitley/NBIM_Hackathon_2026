# Case 1: README-tida for tom cache rettet (#2434, dom #2421)

- Fil: arbeid/hack/levering/JURY_README.md, avsnittet «Det du trenger».
- Før: «3–4 sekunder på vår linje … Selve kjøringen tar under ett minutt.»
- Nå: nedlasting ca. 230 MB (+70 MB Python om 3.13+ mangler), hele kjøringen ett til to
  minutter på vår maskin (nedlasting 3–20 s, totalt 41–89 s, varierer med last), alltid samme
  hovedtall (0,476190); lengre på treg linje. Kilder: #2417 (smed), #2421 (state/rapporter/c1_dom_tom_cache.md).
- Sjekket: ingen andre «under ett minutt» i levering/ eller c1/leveranse/. «Et par minutter» under Kjør er i tråd.
- #2438 (speider): leveranse/README:53 «ca. 12 s» → «4,8 s for agenten alene på test 2026, `kilder/c1_kjoretid.md`»; ny README:40 «29–52 s med pakkene i uv-cachen (BEGRENSNINGER pkt. 8), med tom uv-cache 41–89 s (README i jury-zipen)», i tråd med #2434. Sluttsjekk med prøvefrys: steg 1–3 grønne, 3b RØD bare på NESTE_VERSJON:21 «2366» (internt #-nummer, ryddes i #2435), ingen README-tall uten kilde; steg 4–6 ikke nådd.
