# Case 1: rester fra dom #2578 rettet (#2583)

- JURY_SPORSMAL.md:53 (svar 12): «prøves nå» er byttet ut med utfallet. Tom uv-cache og tom Python-katalog ga samme hovedtall, F1 MOT 0,476, og en svarfil som er byte for byte lik pakkas. Hele løpet tok ett til to minutter (tidsbruken er rettet som dommen ba om). Kilde lagt til: `landsbyrapport:c1_dom_tom_cache.md`. Seks desimaler (0,476190) ble avvist av tallvakta, så det står 0,476.
- NESTE_VERSJON.md:102: «Dommerens byttedom (#2529, 16:42)» er endret til «Kontrollagentens byttedom (16:42)».
- Saksnumre er fjernet fra prosa: JURY_SPORSMAL :53, :62 og :82. NESTE_VERSJON :3, :19, :21 og :102, og i tillegg :48 (sak 1950/1959). demo_vis.py docstring/kommentar (2093, 2127, og i tillegg 2132, 2114, 2106). Bare kommentarer, ingen kode. demo_vis.py er ikke frossen.
- Pkt. 4 (gammel kopi arbeid/hack/levering/JURY_SPORSMAL.md) er ikke rørt. Obs: den står i frys_fasit_1600.sha256:102, så den er med i fasiten. Dommeren bør sjekke om den havner i pakken.
- Fasit: bare tre sha-linjer er endret (JURY_SPORSMAL, NESTE_VERSJON, demo_vis). Tallvakt 0 avvik (170), frys_diff --kilde LIK, frysvakt grønn.
- Ikke med i commit: ERLIG_EVALUERING (smed3) og demo_utskrift.txt (annen agent).
