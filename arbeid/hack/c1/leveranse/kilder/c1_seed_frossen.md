# Case 1: seed-spredning på den frosne agenten (#2326, smed2)

Kopi av frossen #2044 «miks h2» uten India (via #2320, `arbeid/oppgave_2326/train.py`, India av).
Levert mappe og frysfiler er ikke rørt. Bare LightGBM `random_state` endres; LR, C, grensevalg på val 2025 og
trening/test er som frossen. Grensen velges på nytt på val 2025 for hver seed (som i frossen protokoll).
Måler: `maaler_offisiell_v3.py <fil> val|test --data real --score mot` (uendret). Kjør: `bash arbeid/oppgave_2326/kjor.sh` (8 s).

| seed | val 2025 F1 MOT | TP | FP | FN | test 2026 F1 MOT | TP | FP | FN |
|---|---|---|---|---|---|---|---|---|
| std (= frossen) | 0,520231 | 45 | 29 | 54 | **0,476190** | 30 | 38 | 28 |
| 1 | 0,523810 | 44 | 25 | 55 | 0,495868 | 30 | 33 | 28 |
| 2 | 0,511364 | 45 | 32 | 54 | 0,468750 | 30 | 40 | 28 |
| 3 | 0,514286 | 45 | 31 | 54 | 0,461538 | 30 | 42 | 28 |
| 4 | 0,511905 | 43 | 26 | 56 | 0,521739 | 30 | 27 | 28 |
| 5 | 0,517241 | 45 | 30 | 54 | 0,465116 | 30 | 41 | 28 |
| **5 seed snitt** | 0,5157 (sd 0,005) | | | | **0,4826** (sd 0,026) | | | |
| **min / maks (5 seed)** | 0,5114 / 0,5238 | | | | **0,4615 / 0,5217** | | | |

Funn:
- Kontroll: std-kjøringen gir nøyaktig levert tall (0,476190, TP 30 FP 38 FN 28). Fila skiller seg fra levert
  `kjor_agent_real_maskin_alene.csv` bare på rader uten fasit/vurdering (3 anbefalinger, p_avvik på 39 rader);
  målt tall og TP/FP/FN er identiske.
- 0,476 er et typisk seed-utfall: 4. av 6 sortert, 0,007 under snittet av 5 andre seed (0,483). Ikke heldig.
- På test er TP 30 og FN 28 like for alle seed; seed flytter bare antall falske flagg (27–42). Altså endrer seed
  hvor mange svake MOT-flagg som slipper over grensen, ikke hvilke ekte MOT som finnes.
- Spredningen på test (bredde 0,060, sd 0,026) er mye mindre enn bootstrap-KI-et [0,36; 0,59] (bredde 0,23).
  Seed-støy er derfor ikke hovedusikkerheten; utvalget (58 MOT) er det. Ingen varsel på tavla nødvendig.
- Seed 4 ville gitt 0,522 på test, men det er ikke synlig på val (0,512, nest lavest), så å velge seed etter test
  ville vært juks. Snittet av seeds kunne vært en stabilisering etter fristen, ikke nå (frys kl. 16).
