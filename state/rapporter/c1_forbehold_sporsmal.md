# Case 1 (#2626): tre harde juryspørsmål om forbeholdet og F1 på MOT, BYTT og STÅR

KP: Jeg forventet repo4 2026 TP 32 FP 35 FN 26 og F1 0,5120. Tallvakten målte det samme (`c1_tallvakt.py`: OK, 174 påstander, 0 avvik). Frossen: TP 30 FP 38 FN 28, F1 = 60/126 = 0,476, fra `reserve_staar/LES.md`.
Sp. 20 (tidspunkt og lekkasje, #2616) står allerede i pakken. Disse tre spørsmålene tar nye vinkler: tilpasning til teståret, støy, og målet sammen med hva F1 betyr.

## Hvor tekstene står
- **BYTT:** sp. 21–23 er lagt inn i `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md`, før «## Hull vi kjenner». Filen er ikke frosset, og frysvakten viser fortsatt 21 filer uendret.
- **STÅR:** teksten står bare her. `c1/reserve_staar/` har ingen JURY_SPORSMAL.md, så **hvis dommen blir STÅR, sendes BYTT-svarene på sp. 20–23 med som de er.** Det gjelder #2625 (smed2): bytt inn STÅR-svarene under, og STÅR-varianten av sp. 20 fra `arbeid/oppgave_2616/innliming.md`.

## 21. «Dere fant repo4 ved å se på 2026 og skrev regelen etterpå. Er ikke 0,512 bare tilpasset teståret?»
**BYTT:** Delvis: vi så 0,512 kl. 16:13 og skrev regelen kl. 16:49, så 2026 er ikke et friskt år for repo4. Byttet bygger på 2024 og 2025, som ble målt etter regelen: 0,506 og 0,531 mot frossen 0,455 og 0,514, i snitt +0,034, og det holder alene for kravet om +0,02. Les derfor 0,512 som et optimistisk punkt og gevinsten på de friske årene som beviset.
**STÅR:** Delvis, og det er også en grunn til at vi ikke kaller 0,512 vårt resultat: tallet var kjent kl. 16:13, og regelen ble skrevet kl. 16:49. På de to årene som ble målt etter regelen, lå repo4 +0,051 og +0,017 over frossen, så den besto regelen, men pakken ble ikke grønn før fristen. Hovedtallet 0,476 kommer fra en modell valgt helt uten test, og repo4 står først i `NESTE_VERSJON.md`.

## 22. «0,476 mot 0,512 er noen få saker av 58 MOT. Er det mer enn støy?»
**BYTT:** Det er ikke bevist: på 2026 er forskjellen 2 flere riktige MOT (TP 30→32) og 3 færre falske alarmer (FP 38→35). KI for snittet over tre år er [−0,005; +0,078], og 4 % av bootstrap-trekkene havner under frossen. Vi byttet fordi en regel satt før måling ble fulgt og dømt av en annen agent, ikke fordi gevinsten er sikker, så vi kaller den sannsynlig.
**STÅR:** Nei, det er ikke bevist: forskjellen er 2 TP og 3 FP på 2026, og KI for snittet over tre år krysser null ([−0,005; +0,078]). Byttet stoppet på tidsfristen, ikke på støyen. Men fordi gevinsten er så liten, var det ikke verdt å levere en pakke som ikke var bekreftet fra kald start.

## 23. «Målet var 0,5. Nådde dere det bare fordi dere byttet etter frysen? Og hva betyr F1 for forvalteren?»
**BYTT:** Ja: den frosne modellen, valgt helt uten test, ga 0,476 og nådde ikke målet, og begge tallene står i pakken. F1 0,512 betyr at agenten finner 32 av 58 MOT-stemmer (R 0,55), og at 32 av 67 MOT-varsler er riktige (P 0,48). Derfor er agenten beslutningsstøtte som sender usikre saker til et menneske, ikke en erstatning for analytikeren.
**STÅR:** Nei, vi nådde ikke målet: 0,476 betyr at agenten finner 30 av 58 MOT-stemmer (R 0,52), og at 30 av 68 MOT-varsler er riktige (P 0,44). Repo4 ville gitt 0,512, men vi oppgir den som kandidat og ikke som resultat. Derfor er agenten beslutningsstøtte som sender usikre saker til et menneske, ikke en erstatning for analytikeren.

## Kilder
`leveranse/README.md:9` (P/R/TP/FP/FN for repo4) og `:12` (per år og KI), `reserve_staar/LES.md` (frosne tall), `c1_byttedom_265.md` (4 %, per år), `c1_byttregel_forhand.md` (klokkeslett).
