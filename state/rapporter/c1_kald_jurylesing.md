# Case 1: kald jurylesing av jury-zipen (#2472)

Lest: `/tmp/jurypakke_c1_2457.zip` (15:57, 113 filer), pakket ut i tom mappe `/tmp/kald2472b`. Ikke kjørt, bare lest
som et jurymedlem i ca. 12 min: rot-README, så JURY.md, så ERLIG_EVALUERING.md, kravrespons.md og et tall-søk.
Tallsporing: `arbeid/speider/k2472/spor.py <mappe> <regex...>` (søker i md/txt utenom jurytekstene selv).

Rangert, viktigst først:

1. **Motsigelse om metoden, båndet [0,15; 0,85).** JURY.md (Spørsmål 2) og `kilder/c1_mennesket_arbeid.md:12,20` sier
   «låst på val 2025». ERLIG_EVALUERING.md:49 og :56 sier at båndet «ble valgt fra en tabell på test 2026 og bare
   sjekket på val». Juryen vekter ærlig evaluering 60 %, så de må si det samme. Forslag: skriv i JURY.md det
   ERLIG_EVALUERING sier (valgt fra fast rutenett på test-tabellen, sjekket på val), og rett `c1_mennesket_arbeid.md`
   eller legg en merknad i kilder/LESMEG.
2. **Død reproduksjonslenke.** ERLIG_EVALUERING.md:70 skriver «Alt over reproduseres med ett kall: `bash
   arbeid/hack/c1/kaldstart.sh`», og nevner også `fremmed.sh`. Ingen av dem ligger i zipen. Her stoppet jeg som
   jurymedlem. Forslag: bytt til `sh KJOR.sh` (rota).
3. **Var 2025 i treningen eller ikke?** JURY.md «Les dette først» sier «trent på 2019–2025», og samtidig er grense og
   kalibrering valgt på val 2025. Først i ERLIG_EVALUERING.md:3 står det at val-modellen er trent på 2019–2024 og
   test-modellen på 2019–2025. En setning i JURY.md øverst ville spart juryen for mistanken om at grensen er valgt i treningsdata.
4. **Tall uten kilde i pakka:** kalibrert MOT-grense **0,191** (README, kolonnetabellen) står ingen andre steder.
   Alle andre tall jeg sporet fra JURY.md fant jeg i `kilder/` (0,365 og +0,11 [0,01; 0,22], 0,415, 0,282, 0,457,
   0,375/99,4 %, 11 785, 95,7 %, 0,066 = 0,0656, seed 0,462 = 0,4615, 0,504/0,488, TP 30/FP 38/FN 28).
5. **Interne numre er fortsatt med:** rot-README «(#2417, #2421)», JURY.md pkt. 12 «forsøk 2363 … sak 2366»,
   `c1_mennesket_arbeid.md` «#2128». De sier ingenting til en jury.
6. **To «pkt.»-systemer.** JURY.md viser til «pkt. 3, 8, 11», som er JURY sine egne Begrensninger, og samtidig til
   «BEGRENSNINGER.md pkt. 4, 6, 7», som er en annen fil. Jeg måtte bla for å skjønne hvilken liste som menes.
   Forslag: «Begrensninger pkt. 3 (under)».
7. **To «16» i pkt. 11** («alle 16 instrukser fanges» og «av 16 nye tittel-instrukser slipper 6») er lett å lese
   som motsigelse. Forslag: «16 kjente» / «16 nye».
8. **Dobbeltfiler skaper tvil om hva som gjelder:** JURY_SPORSMAL.md, TREFFSIKKERHET.md og KRAVRESPONS/kravrespons.md
   finnes både i `c1/leveranse/` og `levering/`. Levering-versjonene er merket UTDATERT eller INTERN *inne* i fila,
   men en jury som åpner `levering/` først (JURY_README.md og JURYSVAR.md lokker) leser gamle tall. Forslag: ta ut
   UTDATERT/INTERN-filene av zipen, eller skriv tydelig i rot-README «les bare `c1/leveranse/`».
9. **Fire zipper i /tmp** (`jurypakke_c1.zip` 15:45, `_2457` 15:57, `_gp1545`, `_2349`). README sier `unzip
   jurypakke_c1.zip`, men den nyeste er `_2457`. Dommeren bør låse hvilken som er «den» før 19:30.
10. **Det som virket godt:** «Les dette først» svarer på metode, ærlighet og usikkerhet på ett minutt.
    Tabellen med enkle regler og KI, og «Hvorfor vi ikke jaget testtallet», er sterke. Rot-README forklarer
    hvorfor SCORE-linjene (0,481752) ikke er hovedtallet. TP/FP/FN går opp (F1 = 60/126 = 0,476).
