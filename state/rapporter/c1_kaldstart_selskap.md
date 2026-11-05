# Case 1: hvor godt treffer den frosne agenten på selskaper uten historikk? (#2302, smed3)

Frossen #2044 miks h2 (`arbeid/oppgave_2044/train.py`, kjørt uendret via runpy som c1_real.py gjør), målt som
«MOT mot styret» med definisjonen i måler v3. Gruppe = antall tidligere NBIM-stemmer (etiketterte saker) i samme
selskap med møtedato strengt før sakens dato, altså akkurat den historikken modellen selv får se (hist 2).
Totalene per vindu er kontrollert mot `maaler_offisiell_v3.py --score mot` og stemmer på TP/FP/FN
(val 2025 SCORE 0,520231, test 2026 SCORE 0,476190 = det leverte tallet).

Holdt-ut 2024 finnes ikke i den frosne pakka (2024 er treningsår). Det er laget med samme oppskrift flyttet ett år
(`arbeid/oppgave_2302/train_2024.py`: tren <2024, C og grense valgt på 2024 slik train.py gjør for 2025). Det er samme
prosedyre som val 2025 i pakka, og like optimistisk (grensa er valgt på samme år). Pakka er urørt.

## Tabell (MOT mot styret, måler v3-definisjon)

| vindu | tidl. stemmer i selskapet | saker | MOT i fasit | flagget MOT | TP | FP | FN | presisjon | recall | F1 |
|---|---|---|---|---|---|---|---|---|---|---|
| val 2025 (frossen) | 0 | 98 | 3 | 4 | 2 | 2 | 1 | 0,500 | 0,667 | 0,571 |
| val 2025 (frossen) | 1-3 | 17 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| val 2025 (frossen) | 4+ | 1794 | 95 | 70 | 43 | 27 | 52 | 0,614 | 0,453 | 0,521 |
| val 2025 (frossen) | alle | 1909 | 99 | 74 | 45 | 29 | 54 | 0,608 | 0,455 | 0,520 |
| holdt-ut 2026 (frossen, levert) | 0 | 69 | 6 | 3 | 2 | 1 | 4 | 0,667 | 0,333 | 0,444 |
| holdt-ut 2026 (frossen, levert) | 1-3 | 11 | 0 | 0 | 0 | 0 | 0 | – | – | – |
| holdt-ut 2026 (frossen, levert) | 4+ | 1459 | 52 | 65 | 28 | 37 | 24 | 0,431 | 0,538 | 0,479 |
| holdt-ut 2026 (frossen, levert) | alle | 1539 | 58 | 68 | 30 | 38 | 28 | 0,441 | 0,517 | 0,476 |
| holdt-ut 2024 (oppskrift flyttet ett år) | 0 | 112 | 8 | 5 | 2 | 3 | 6 | 0,400 | 0,250 | 0,308 |
| holdt-ut 2024 (oppskrift flyttet ett år) | 1-3 | 0 | 0 | 0 | 0 | 0 | 0 | – | – | – |
| holdt-ut 2024 (oppskrift flyttet ett år) | 4+ | 1771 | 80 | 86 | 46 | 40 | 34 | 0,535 | 0,575 | 0,554 |
| holdt-ut 2024 (oppskrift flyttet ett år) | alle | 1883 | 88 | 91 | 48 | 43 | 40 | 0,527 | 0,545 | 0,536 |

Slått sammen over de tre vinduene (2024, 2025, 2026):

| gruppe | saker | MOT i fasit | TP | FP | FN | presisjon | recall | F1 |
|---|---|---|---|---|---|---|---|---|
| 0 tidligere stemmer | 279 | 17 | 6 | 6 | 11 | 0,500 | 0,353 | 0,414 |
| 1-3 | 28 | 1 | 0 | 0 | 1 | – | 0 | 0 |
| 4+ | 5024 | 227 | 117 | 104 | 110 | 0,529 | 0,515 | 0,522 |

Biprodukt (oppskriften flyttet ett år, holdt-ut 2025 med grense fra 2024): F1 alle 0,514, 4+ 0,515, 0-gruppa 0,571
(2/4 flagget riktig, 1 tapt). Samme bilde som den frosne val 2025-kjøringen.

## Hva det betyr
- Gruppa 1-3 er nesten tom (28 saker, 1 MOT på tre år). NBIM stemmer på hele dagsordenen, så et selskaps første møte
  gir alle sakene 0 tidligere stemmer, og neste møte gir dem 4+. «Nytt selskap» betyr i praksis «første møte».
- Saker uten historikk er 4,5–6 % av sakene og 5–9 % av MOT-ene i hvert vindu, med 3–8 MOT per år. Med så få
  tilfeller er ingen av forskjellene mellom gruppene statistisk skillbare (et enkelt treff flytter F1 med 0,1–0,2).
- Mønsteret er likevel det samme i alle tre år: presisjonen holder seg (0,40–0,67, omtrent som for 4+), men recall
  faller (0,25–0,67, sammenlagt 0,35 mot 0,52), fordi modellen uten selskapshistorikk bare har tekst og kategorier
  å gå på og flagger færre saker.
- Én setning for porteføljen: for nye selskaper finner agenten rundt en tredjedel av NBIMs MOT-stemmer (6 av 17 over tre år)
  med omtrent samme presisjon som ellers, så første generalforsamling i et nytt selskap bør rutes til menneske
  i større grad enn resten; det er lite volum (ca. 5 % av sakene), så det koster lite.

## Filer
- `arbeid/oppgave_2302/analyse.py` (gruppering og tabell), `train_2024.py` (årsflyttet kopi, bare for 2024-raden)
- `arbeid/oppgave_2302/frossen_{val,test}_full.csv` (rad,p til måler v3), `frossen_grupper.csv` og `skift2024_grupper.csv`
  (gruppe, flagg og fasit per sak)
