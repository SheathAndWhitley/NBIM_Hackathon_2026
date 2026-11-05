# Case 1, #2068: kaldstartmodellen inn i agenten? Nei. Val viser ingen gevinst (nullfunn)

**Hva jeg prøvde:** smed3s selskapsblinde kaldstartmodell (#2065, `smed3_utf_kald/kald.py`) for selskaper uten historikk (ingen rad i real_votes fra tidligere år), og smed2s #2044-modell (agentens standard) ellers. Kaldgrensen ble valgt på val 2025 (begge modellene trent på data før 2025) som den grensen som gir best F1 på hele val.

**Val 2025 (avgjør):** 1909 saker og 103 MOT. Uten historikk: 98 saker, men bare **3 MOT**.
| | F1 hele val | uten hist |
|---|---|---|
| smed2 alene | **0,522** | 0,57 (tp2 fp2 fn1) |
| kombinert, beste kaldgrense (0,854) | 0,514 | 0,33 (tp1 fp2 fn2) |
| kombinert, kaldmodellens egen grense | 0,505 | – |
Hist-varianten av kald.py gir det samme (0,514). **Beslutning: smed2 står alene, og kombinasjonen går ikke inn i agenten.**

**Test 2026, målt én gang med `maaler_offisiell.py test --data real`:** helhet **F1 0,4818** (TP 33, FP 38, FN 33). Det er identisk med standardagenten.
Uten historikk (69 saker, 8 MOT): smed2 0,364 (tp2 fp1 fn6). Kaldmodellen alene fikk også 0,364 (tp2 fp1) i #2065. Heller ikke test viser noen gevinst.
Med historikk: 0,492.

**Hvorfor:** Delmengden uten historikk er for liten til å velge noe på (3 MOT på val, 8 på test). smed2s modell klarer seg heller ikke dårligere der enn den selskapsblinde. Fallet på delmengden (0,49 → 0,36) skyldes sakene selv, ikke at historikken mangler (samme funn som i #2065).

**Kjør (kald start, ca. 7 s):** `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2068/kombiner.py --kald plain`
Svarfil: `arbeid/oppgave_2068/ut/svar_test_plain.csv`, logg: `arbeid/oppgave_2068/kjoring.txt`. `--bare-val` stopper før test.

**Tavla:** Forsøket ble avvist: «måleren er endret på disk (8733327407 -> 474eae7bc8)». Dommeren må sette måleren for #2068 på nytt (`tavle maaler --oppgave 2068 --kmd ...`), og så kan svarfila over måles.
