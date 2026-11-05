# Case 1: jurylesning av kravrespons, README, JURY.md og demo-manus (#2662)

Lest 17:35–17:50 som jurymedlem, i lesevegen kravrespons → leveranse/README → JURY.md → DEMO_MANUS.
NB: lest FØR #2653/#2659 er lukket (oppgaven sa 18:30). Punkt 2 overlapper #2659, de andre er utenfor
det #2653/#2659/#2665 står oppført med. Alt er kontrollert mot repo4-kjøringen (TP32 FP35 FN26, tall_tabell.md:4,10)
og mot `/tmp/c1_kald/ut/agent.csv` (17:18).

## 1. Teksten sier fortsatt «test 2026 velger aldri, den frosne står», mens vi leverer repo4 (verst)
Juryen leser i JURY.md:4 og :9 at 2026 ble brukt til å finne repo4, og så motsatt lenger ned:
- `leveranse/JURY.md:63` «Test 2026 brukes aldri til å velge. Den kjøres på den frosne agenten og rapporteres som den er.»
- `leveranse/JURY.md:58` «Det lå under målet 0,5 … Vi la dem ikke inn», og `:61` og `:82` «den frosne agenten står».
- `leveranse/kravrespons.md:7` «Modell og grense er valgt på 2025 og kjørt én gang på 2026». `leveranse/README.md:9` «kjørt én gang på test».
- `leveranse/README.md:13` «besto en regel … på 2024 og 2025» mot `:12` «tre rullende testår 2024–2026».
**Forslag:** JURY.md:63 → «Test 2026 brukes ikke til å avgjøre: repo4 ble funnet med 2026 i blikket, men byttet ble avgjort på 2024 og 2025 etter en regel satt før måling. 2026-tallet 0,512 er derfor ikke friskt.» :58 → «Den eldre frosne agenten (#2044) hadde 0,476 … Disse endringene la vi ikke inn» (behold), og stryk «den frosne agenten står» i :61/:82 (skriv «ble ikke lagt inn»). Kravrespons:7 og README:9: «valgt på 2025; repo4-byttet avgjort på 2024–2025 (2026 ikke friskt, se JURY sp. 20)». README:12 og :13 må si det samme om hvilke år som avgjorde.

## 2. Demo-manuset: sakene på skjermen er ikke lenger de samme med repo4 (#2659 må vite det)
`vis_manussaker.py` på kald repo4-kopi (17:18) melder AVVIK FRA MANUS: Kura Sushi (linje 15, `DEMO_MANUS.md:39-44`) rutes ikke lenger, den tas nå av maskinen alene; første sak til menneske er H. Lundbeck (linje 39), der agenten sier MOT med p 0,23 og fasit er FOR. Historien «mennesket fikk riktig forslag» (`DEMO_MANUS.md:44`) holder ikke for første rutede sak. I tillegg frossen-tall: `:1`, `:3` («frossen sak 2044»), `:15` (0,476, 30 av 58, 44 %), `:44`/`:57` (183 av 1539), `:63` og `:67` («frysen står; 0,476 mot …»).
**Forslag:** bytt tekst, ikke saker (verktøyet sier det): treff_maskin = linje 15 (Kura Sushi), til_menneske = velg en rutet sak med fasit MOT, eller vis Lundbeck ærlig som falskt flagg som mennesket fanger. Tall: 0,512, 32 av 58, 48 % av flaggene ekte, 164 av 1578 (161 av 1539). Kjør `vis_manussaker.py` til «MANUS OK» før tekststopp.

## 3. Gammelt KI og «under målet» står igjen
- `leveranse/kravrespons.md:7` KI [0,36; 0,59] er klynge-KI for frossen #2044 (tall_tabell.md:4). repo4 har [0,40; 0,62].
- `leveranse/kravrespons.md:10` «0,512 ligger under målet vårt på 0,5» er feil.
- `leveranse/JURY.md:72` hele pkt. 2 er frossen: KI [0,36; 0,59] / [0,37; 0,59], «punktestimatet er under», val 0,520 (repo4: 0,530 jf. README:9), «0,476 er et typisk seed-utfall».
**Forslag:** kravrespons:7 → [0,40; 0,62]; kravrespons:10 → «0,512 ligger like over målet 0,5, men intervallet går godt under». JURY:72 → «95 % KI [0,40; 0,62] (klynge per selskap; rader gir det samme). Målet 0,5 ligger inne i intervallet, punktestimatet like over. Seed-spredningen (0,462–0,522, snitt 0,483) er målt på den frosne #2044, ikke repo4.»

## 4. Ruting- og bunketall er fra frossen, og motsier repo4-raden i samme tabell
- `leveranse/JURY.md:34` «21 av treffene og alle de 35 falske flaggene … alle 9 MOT-flagg riktige»: repo4-raden `:47` sier 11 auto-MOT og 3 falske flagg tatt av maskinen. Altså ikke «alle» og ikke «9 av 9».
- `:46` fet «Standard»-rad (183, 9/32/17, 0/38) er frossen, mens den leverte repo4 står kursiv under. `:50` («12 av 100», «32 av de 58») er frossen.
- `:78` «127 usikre, 60 ukjent, 1 instruks» = 188, ikke 164. README:17 sier 101 + 61 + 1 + 1 = 164.
- `:29` «F1 0,482 på avvik» er frossen; repo4 gir 0,529 (README:17).
**Forslag:** :34 → «161 av 1539 til menneske, med 29 av MOT-ene og 32 av de 35 falske flaggene. Maskinen tar selv 14 MOT-flagg, 11 riktige og 3 falske.» Gjør repo4-raden fet og merk den gamle «frossen #2044». :50 → «leser 10–11 av 100 saker og får 29 av 58 MOT der». :78 → «101 usikre, 61 ukjent selskap, 1 instruks, 1 annen vakt». :29 → 0,529 (frossen 0,482).

## 5. Det største forbeholdet er undervurdert for repo4 (overselger)
`leveranse/README.md:14` og `kravrespons.md:10` sier at «omtrent 0,06 av F1» kommer fra stemmer i samme sesong. Men 0,06 er 0,476 − 0,415, altså målt på den frosne modellen. For repo4 er det 0,512 − 0,415 ≈ 0,10. Og repo4 legger til fire historikktrekk, så avhengigheten er trolig større, men golvet er ikke målt for repo4 (`JURY.md:21` sier selv «frossen»). Samme gjelder motstandstesten (`JURY.md:81`), som er kjørt på frossen og ikke på repo4.
**Forslag:** README:14 og kravrespons:10 → «Minst 0,10 av F1 hviler på NBIMs stemmer fra samme sesong (repo4 0,512 mot 0,415 for den frosne modellen uten dem; golvet for repo4 er ikke målt).» JURY:81: én setning om at angrepstallene er fra frossen #2044, og at repo4 har samme vakt, men ikke er angrepstestet.

Mindre: `kravrespons.md:7` og `README.md:10` sier `sh KJOR.sh`, mens fila i leveranse/ heter `kjor.sh`. Det er riktig for zipen, men ordet «zip» står ikke i kravresponsen. Skriv «`sh KJOR.sh` i jury-zipen».
