# Case 1 tallsjekk: tall i pakka uten kilde

> **Oppdatering 14:20 (dommer, #2276):** alle 17 er funnet eller rettet (574 → 575 i METODE.md). Ny kjøring gir IKKE FUNNET 0. Kilde: `arbeid/hack/c1/tall_kilder_ut.txt` (lages av `lag_tall_kilder.py`). Detaljer i `state/rapporter/c1_tall_uten_kilde.md`.

Generert 2026-11-05 14:08 med `python3 -I arbeid/verktoy/c1_tallsjekk.py --rapport state/rapporter/c1_tallsjekk.md`.

1958 tall i 14 filer: IKKE FUNNET 17, avledet A 34, funnet A 1487, funnet B 420. Kilder A 367 tall, B 12489 tall. 0.1 s.

Kilde A = tall_tabell.md, maaling.txt (#2267), terskeltabell_ut.md. Kilde B = andre målerutskrifter (oppgave_2xxx/*.txt/log/json, c1/*.md/txt). Funnet B betyr bare at tallet står i en logg et sted: stikkprøv dem. Små heltall (16 instrukser, 15 av 20) finnes nesten alltid i B.

## Ikke funnet (17)

| fil:linje | tall | type | linje |
|---|---|---|---|
| arbeid/hack/c1/leveranse/JURY.md:45 | 0,252 | KI | / Regel b2: samme selskap + samme forslagstekst fikk MOT før / 0,365 / [0,252; 0,492] / |
| arbeid/hack/levering/BESLUTNINGSSTOTTE.md:25 | 0,779 | desimal | / bare båndet: kalibrert P(MOT) i [0,15; 0,85) / 122 av 1539 (7,9 %) / 27 av 58 / P 0,44 / R 0,52 / F1 0,476 ( |
| arbeid/hack/levering/BESLUTNINGSSTOTTE.md:26 | 0,269 | desimal | / **standard** (bånd + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat) / 183 av 1539 (11,9 %) / 32 a |
| arbeid/hack/levering/BESLUTNINGSSTOTTE.md:46 | 571 | heltall | / øvrige (styret): vedtekter 3, say-on-pay 3, emisjon 2, nærstående 1, aksjeprogram 1, regnskap 1 / 11 / 571 / |
| arbeid/hack/levering/EN_SIDE.md:38 | 0,269 | desimal | / MOT funnet, maskin + menneske / 41 av 58, F1 0,828 hvis mennesket avgjør riktig (øvre grense); 0,269 hvis me |
| arbeid/hack/levering/JURYSVAR.md:30 | 0,269 | desimal | Den gjør ikke maskinen flinkere: maskinens egne svar er de samme (F1 0,476). Den flytter de usikre MOT-sakene  |
| arbeid/hack/levering/JURYSVAR.md:37 | 0,779 | desimal | / bare båndet: kalibrert P(MOT) i [0,15; 0,85) / 122 av 1539 (7,9 %) / 27 av 58 / P 0,44 / R 0,52 / F1 0,476 ( |
| arbeid/hack/levering/JURYSVAR.md:38 | 0,269 | desimal | / **standard** (bånd + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat) / 183 av 1539 (11,9 %) / 32 a |
| arbeid/hack/levering/JURY_SPORSMAL.md:61 | 367 | heltall | `position_paper` var lekkasje: 97,5 % av de 367 radene der feltet er satt, er MOT. Sakstypen lekker ikke svare |
| arbeid/hack/levering/METODE.md:15 | 9876 | heltall | / train / 2019–2024 / 9876 / 504 / 574 / |
| arbeid/hack/levering/METODE.md:15 | 504 | heltall | / train / 2019–2024 / 9876 / 504 / 574 / |
| arbeid/hack/levering/METODE.md:15 | 574 | heltall | / train / 2019–2024 / 9876 / 504 / 574 / |
| arbeid/hack/levering/README.md:63 | 0,779 | desimal | / bare båndet: kalibrert P(MOT) i [0,15; 0,85) / 122 av 1539 (7,9 %) / 27 av 58 / P 0,44 / R 0,52 / F1 0,476 ( |
| arbeid/hack/levering/README.md:64 | 0,269 | desimal | / **standard** (bånd + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat) / 183 av 1539 (11,9 %) / 32 a |
| arbeid/hack/levering/TREFFSIKKERHET.md:31 | 98,75 % | prosent | - Accuracy 98,75 % (følg styret på de samme sakene: 98,1 %). |
| arbeid/hack/levering/TREFFSIKKERHET.md:45 | 55,7 % | prosent | / Konfidens ≥ 0,6 (1356 saker) / recall MOT / 34,6 % / 15,8–55,0 % / 17,2–55,7 % / |
| arbeid/hack/levering/TREFFSIKKERHET.md:72 | 0,189 | desimal | / 0,80 / 0,262 / 0,646 / 0,373 / 0,189 / 0,707 / 0,298 / 41/176 / |

## Avledet (34): bare regnet frem fra kilde A, kan være tilfeldig

Sum og differanse av tellinger (1443 = 113+1330) er som regel ekte. Brøker for tall med tre desimaler (0,097 = 10/103) er ofte tilfeldige: les dem som ikke funnet.

| fil:linje | tall | regnet som | linje |
|---|---|---|---|
| arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md:28 | 400 | 24+276 | h2 bruker NBIMs stemmer fra møter **strengt før** sakens dato i samme sesong. Dommeren fan |
| arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md:43 | 0,097 | 0/103 | - **Historikkregel «selskapet hadde MOT før»:** under står 0,091 (gammelt skript `hist_reg |
| arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md:43 | 0,124 | 1/89 | - **Historikkregel «selskapet hadde MOT før»:** under står 0,091 (gammelt skript `hist_reg |
| arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md:54 | 400 | 24+276 | Fasiten er NBIMs egne stemmer (real_votes fra arrangøren). Målvariabelen er *MOT styret* ( |
| arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md:59 | 0,845 | 909/2260 | / historikkregel: MOT hvis selskapet hadde MOT før / 0,048 / 0,845 / 0,091 / |
| arbeid/hack/c1/leveranse/JURY.md:44 | 0,359 | 3/64 | / **Hovedmodell #2044 miks (løpende historikk)** / **0,476** / [0,359; 0,590] / |
| arbeid/hack/c1/leveranse/JURY.md:47 | 0,097 | 0/103 | / Regel a: NBIM stemte MOT mot styret i selskapet før / 0,097 / [0,072; 0,124] / |
| arbeid/hack/c1/leveranse/JURY.md:47 | 0,124 | 1/89 | / Regel a: NBIM stemte MOT mot styret i selskapet før / 0,097 / [0,072; 0,124] / |
| arbeid/hack/c1/leveranse/JURY.md:49 | 0,301 | 5/83 | / Golv: samme modell, bare historikk fra tidligere år / 0,415 / [0,301; 0,533] / |
| arbeid/hack/c1/leveranse/README.md:24 | 1443 | 13+1330 | Riktige tall fra kald start: TP 30 FP 38 FN 28 TN 1443, F1 MOT 0,476, accuracy 95,7 % (føl |
| arbeid/hack/levering/BESLUTNINGSSTOTTE.md:25 | 0,294 | 0/68 | / bare båndet: kalibrert P(MOT) i [0,15; 0,85) / 122 av 1539 (7,9 %) / 27 av 58 / P 0,44 / |
| arbeid/hack/levering/JURYSVAR.md:23 | 0,097 | 0/103 | Ja. Gulvet som er lov, «følg styret», gir F1 0. Den sterkeste enkle regelen vi har målt, « |
| arbeid/hack/levering/JURYSVAR.md:37 | 0,294 | 0/68 | / bare båndet: kalibrert P(MOT) i [0,15; 0,85) / 122 av 1539 (7,9 %) / 27 av 58 / P 0,44 / |
| arbeid/hack/levering/JURY_SPORSMAL.md:9 | 1481 | 539-58 | - Treffprosent (accuracy): **95,7 %** (1473 av 1539). Å alltid følge styret gir **96,2 %** |
| arbeid/hack/levering/JURY_SPORSMAL.md:10 | 1443 | 13+1330 | - Riktig på FOR-sakene: **97,4 %** (1443 av 1481). Det er her «97 %» kommer fra, men det e |
| arbeid/hack/levering/JURY_SPORSMAL.md:10 | 1481 | 539-58 | - Riktig på FOR-sakene: **97,4 %** (1443 av 1481). Det er her «97 %» kommer fra, men det e |
| arbeid/hack/levering/JURY_SPORSMAL.md:62 | 400 | 24+276 | 0,500 [0,38; 0,61] mot 0,476. Historikk fra samme møte er sjekket på 400 rader, og den ga  |
| arbeid/hack/levering/KRAVRESPONS.md:70 | 395 | 18-23 | / 20 / Kravrespons maks 1 side, malens overskrifter (B §2–3) / `c1/leveranse/kravrespons.m |
| arbeid/hack/levering/METODE.md:20 | 400 | 24+276 | - **Trekk:** TF-IDF på forslagsteksten; kategorier `proposal_type`, `proponent`, `mgmt_rec |
| arbeid/hack/levering/METODE.md:31 | 2115 | 1+2044 | - *Stikkprøve (#2115, 20 av 63 MOT-saker, seed 2115):* 20/20 ordrett, **15/20 er regelen s |
| arbeid/hack/levering/README.md:10 | 1443 | 13+1330 | > saker (3,8 %) er MOT og følg styret aldri sier MOT. 2x2 (TP 30 FP 38 FN 28 TN 1443), R 0 |
| arbeid/hack/levering/README.md:50 | 1443 | 13+1330 | Forventet: TP 30 FP 38 FN 28 TN 1443, accuracy 95,7 % (følg styret 96,2 %), F1 0,476 på MO |
| arbeid/hack/levering/README.md:63 | 0,294 | 0/68 | / bare båndet: kalibrert P(MOT) i [0,15; 0,85) / 122 av 1539 (7,9 %) / 27 av 58 / P 0,44 / |
| arbeid/hack/levering/TREFFSIKKERHET.md:12 | 1443 | 13+1330 | / **Agenten: ikke MOT**   / FN **28**         / TN **1443**     / |
| arbeid/hack/levering/TREFFSIKKERHET.md:14 | 1481 | 539-58 | - Accuracy: **95,7 %** (1473 av 1539). Følg styret: **96,2 %** (1481 av 1539). |
| arbeid/hack/levering/TREFFSIKKERHET.md:17 | 1443 | 13+1330 | - Riktig på FOR (ikke-MOT-saker): **97,4 %** (1443 av 1481). |
| arbeid/hack/levering/TREFFSIKKERHET.md:17 | 1481 | 539-58 | - Riktig på FOR (ikke-MOT-saker): **97,4 %** (1443 av 1481). |
| arbeid/hack/levering/TREFFSIKKERHET.md:38 | 2185 | 76+1909 | tilbakelegging, fast frø 2185, 2,5- og 97,5-persentil. Clopper-Pearson (eksakt binomial) s |
| arbeid/hack/levering/TREFFSIKKERHET.md:43 | 65,2 % | 8/89 | / Alle 1539 saker / recall MOT / 51,7 % / 39,1–65,2 % / 38,2–65,0 % / |
| arbeid/hack/levering/TREFFSIKKERHET.md:72 | 0,262 | 8/107 | / 0,80 / 0,262 / 0,646 / 0,373 / 0,189 / 0,707 / 0,298 / 41/176 / |
| arbeid/hack/levering/TREFFSIKKERHET.md:77 | 0,735 | 3/113 | / 0,97 / 0,735 / 0,253 / 0,376 / 0,742 / 0,397 / 0,517 / 23/8 / |
| arbeid/hack/levering/TREFFSIKKERHET.md:77 | 0,742 | 6/89 | / 0,97 / 0,735 / 0,253 / 0,376 / 0,742 / 0,397 / 0,517 / 23/8 / |
| arbeid/hack/levering/TREFFSIKKERHET.md:97 | 2185 | 76+1909 | #  -> 95 %-intervall (bootstrap 2000 trekk, frø 2185, og Clopper-Pearson) for P og R, alle |
| arbeid/hack/levering/TREFFSIKKERHET.md:100 | 1443 | 13+1330 | TN = 1539 − 30 − 38 − 28 = 1443. Sjekket 05.11 av smed3 (#2175). |

## Kontrollpunkt og grenser (arkitekt, #2271)
- KP: hovedtallet 0,476 i EN_SIDE.md:19 skulle gi «funnet A (tall_tabell.md)», og det gjorde det. 0,4818 (avvik inkl. AVSTÅ) skulle gi «funnet A (maaling.txt)», og det gjorde det også. Med `--streng` (bare kilde A) blir 313 av 1958 tall stående som ikke funnet. Tall-tabellen og målerutskriften dekker altså ikke pakka alene.
- «Funnet» betyr at tallet står i en kilde, ikke at det betyr det samme der. Små heltall (15, 16, 20) og tall fra gamle logger (0,415 kom fra oppgave_2017) må stikkprøves. Kolonnen med kildefil gjør det raskt.
- De 17 som ikke ble funnet, sortert: 0,779 og 0,269 (F1 for maskin og menneske i rutingstabellen, 7 steder) og 0,252 (KI-grense for regel b2). Disse finnes ikke i noen måleutskrift. Videre 9876, 504 og 574 (train-tellinger i METODE.md), 571, 367, 98,75 %, 55,7 % og 0,189 (TREFFSIKKERHET.md). Dommer2 (#2255) bør enten finne kilden eller få speideren til å lagre utskriften de kommer fra.
- Kjøretid er 0,2 s. Verktøyet bare leser og rører ingen leveransefiler eller modellen. `--feil` gir utgang 1 ved ikke-funnet, til kaldstarten (#2273).
