# Case 1 (#2614): tre harde jury-spørsmål om metoden, med svar fra pakken

Kilder er filer i `arbeid/hack/c1/leveranse/`. Tallene står der, med mindre noe er merket **HULL** (da står tallet bare i `state/rapporter/`, ikke i pakken).
KP: forventet repo4 0,5057/0,5309/0,5120 og frossen snitt 0,4817 likt i README:12 og byttedommen. Fikk likt (OK).

## 1. «Repo4 legger til fire historikktrekk. Lekker de fasit fra samme møte eller fra teståret?»
**Svar:** Historikken bruker bare møter som er strengt før saken. 400 tilfeldige rader er sjekket med brute force, med 0 avvik (`ERLIG_EVALUERING.md` § 2, `JURY_SPORSMAL.md` sp. 5). Kolonner som avslører svaret stoppes med assert (sp. 5). Vi fant og fjernet selv lekkasjen i `managementRecommendation` (README:75). Det er én antakelse: at NBIMs egne stemmer er kjent løpende gjennom sesongen. Uten den faller F1 MOT fra 0,512 til 0,415 [0,30; 0,53]. Det golvet oppgir vi (§ 2, sp. 18).
**Svakhet:** Brute force-sjekken på 400 rader ble kjørt på den frosne h2. For de fire nye repo4-trekkene er sjekken gjort i dommerens protokollsjekk #2575 (punkt 1 og 6). Repoets `add_history` oppdaterer først etter hele møtet, og ingen forbudte kolonner er med. **HULL:** dette står ikke i pakken. Én setning bør inn i § 7.

## 2. «Tre rullende testår, men trener dere på data etter teståret, eller velger dere noe på test?»
**Svar:** Nei. Hvert testår T trenes bare på årene før T−1, og grense og rutingsbånd velges på val T−1. Hvert testår kjøres én gang (README:12, § 7). Hovedåret 2026 er trent på 2019–2025 (11 785 saker), med grense valgt på val 2025 (§ 1, ingress). Data er låst med sha256 `71ba5135…` (README:24). Testårene har 88, 99 og 58 MOT (§ 7). Det er derfor vi ikke bytter på ett år: nesten alle kandidater som ser bedre ut på 2026, taper på 2024. V2 får for eksempel 0,516 på 2026, men 0,407 på 2024 (§ 7, benk A).
**Svakhet:** Med 58 MOT på test flytter én sak F1 omtrent ±0,01 (§ 3). Repo4s verste år, +0,017, ligger innenfor støyen.

## 3. «Regelen ble satt før måling. Men kjente dere tallene allerede, og hvor mange kandidater prøvde dere?» (det vanskeligste)
**Svar i pakken:** Regelen er snitt minst +0,02 og intet år under −0,02. Repo4 ga +0,0345, med verste år +0,017. Kontrollagenten dømte, ikke den som målte (README:12, kravrespons:7). KI for snittet er [−0,005; +0,078], altså ikke tydelig over null, og det sier vi selv (§ 7). Benk A og B viser 12 kandidatrader, og alle utenom repo4 stryker (§ 7).
**Det ærlige tilleggssvaret (HULL, står bare i `c1_byttedom_265.md` og `c1_byttregel_forhand.md`):** Repo4s 2026-tall (0,5120) var kjent kl. 16:13. Regelen kom 16:49. Tallene som avgjorde, 2024 (+0,051) og 2025 (+0,017), ble målt etter regelen, 16:49–16:50. Ser vi bare på de to årene, blir snittet +0,034. I 4 % av bootstrap-trekkene ligger repo4 under frossen. På det fjerde året, 2023, ligger repo4 0,005 over frossen (§ 7 nevner dette).
**Anbefaling:** Før tekststoppen kl. 19 bør smed3/smed legge to setninger inn i § 7 og som svar i `JURY_SPORSMAL.md`: (a) at «2026 var kjent da regelen ble skrevet, 2024 og 2025 var ukjente» med klokkeslett, og (b) at 4-trekkssjekken mot lekkasje er gjort i #2575. Ellers kan juryen finne forbeholdet selv, og da ser det ut som vi har skjult det.

## Funn i pakken nå (17:2x)
§ 7 i `ERLIG_EVALUERING.md` sier fortsatt «ingen kandidat er godkjent, den frosne modellen står». Samtidig sier ingressen at hovedtallet er 0,512, og README:12 sier BYTT. Det må samkjøres når dommen kl. 18:45 er klar (#2592 og #2598 eier tekstene). Juryen vil stille spørsmålet «hvilken modell leverte dere?» hvis dette står motstridende.
