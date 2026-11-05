# Case 1: jurylesning av jurypakke_c1_1739_530ffd7.zip (#2677, arkitekt, 05.11 17:50)

Zipen er pakket ut i en tom mappe (/tmp/jury2677.zVWI). Jeg leste README.md, leveranse/JURY.md og ERLIG_EVALUERING.md slik et jurymedlem ville gjort, i 10 min.
Linjenumrene gjelder filene i zipen (`c1_stemmeagent/arbeid/hack/c1/leveranse/`). Jeg har ikke lagt inn noen nye tall: hver retting bruker tall som alt står i samme fil.

## 1. «Test 2026 brukes aldri til å velge» sier imot at 2026 ble brukt til å velge (alvorligst, gjelder ærligheten)
- `JURY.md:63`: «Test 2026 brukes aldri til å velge. Den kjøres på den frosne agenten …». Men `JURY.md:4` sier selv at «2026 ble brukt til å finne kandidaten», og ERLIG § 7 (`ERLIG_EVALUERING.md:79,86`) har 2026 som ett av de tre testårene i BYTT-regelen. `ERLIG_EVALUERING.md:62` sier også at «test 2026 kjøres én gang med lås».
- **Retting JURY.md:63:** «Fram til frysen kl. 16 ble test 2026 aldri brukt til å velge; repo4 er valgt etter en regel satt før måling, på tre testår der 2026 er ett av dem, så 2026 er ikke friskt for repo4 (ERLIG § 7).»
- **Retting ERLIG:62:** legg til «(fram til frysen; om valget av repo4 etterpå, se § 7)».

## 2. Sorteringsavsnittet bruker frosne tall, men tabellen rett under viser repo4
- `JURY.md:34` sier «… med 21 av treffene og **alle de 35** falske flaggene. Blant sakene agenten tar selv, er **alle 9** MOT-flagg riktige». Raden for levert repo4 på `JURY.md:47` viser 11 ekte MOT og 3 falske flagg som agenten tar selv (11 / 29 / 18 og 3 / 32). Tallene 9 og «alle falske» hører til frossen modell (`:46`).
- **Retting JURY.md:34:** «… med 21 av treffene og 32 av de 35 falske flaggene. Blant sakene agenten tar selv, er 11 av 14 MOT-flagg riktige (`kilder/c1_mennesket_arbeid.md`, rad repo4).»
- Litt mindre viktig: på `:46` står frossen modell i fet skrift som «Standard», mens den leverte modellen står i kursiv på `:47`. Et jurymedlem tror lett at 183 er tallet for den leverte agenten. Retting: gjør `:47` fet og merk `:46` med «(eldre frossen)».

## 3. «Les dette først» oppgir bommene til den frosne modellen
- `JURY.md:6`: «17 av de 28 bommene får P(MOT) ≤ 0,09 og rutes ikke». Pkt. 3 (`JURY.md:73`) og `JURY.md:35` gjelder levert repo4: 18 av 26 bommer, P(MOT) ≤ 0,11. Det første juryen leser, passer altså ikke med hovedtallet (FN 26).
- **Retting JURY.md:6:** «Svakheten: 18 av de 26 bommene får P(MOT) ≤ 0,11 og rutes ikke (pkt. 3).»
- Det samme gjelder `JURY.md:24` (overskriften «den frosne modellen», 30/58 og 28 bommer). Retting: legg til «(eldre frossen, 0,476; repo4: 32 av 58, se pkt. 3)» i overskriften.

## Sett, men ikke tatt med (under grensen på tre)
- `JURY.md:78`: 127 + 60 + 1 = 188, men totalen er 164. Gruppene overlapper sikkert, men teksten sier det ikke.
- `JURY.md:82`: «26 av de 38 falske MOT» bruker tallet for frossen modell (38); repo4 har 35 falske flagg.
- README og kjøreoppskriften var greie å følge. Hovedtallet 0,512 og TP 32 / FP 35 / FN 26 er like i README, JURY og ERLIG.
