# Case 1: forsvar av byttet til repo4 overfor juryen (3 svar, klart til JURY_SPORSMAL) — arkitekt #2594, 05.11

Ingen nye tall. Alle tall fra `kilder/c1_byttedom_265.md` (dommer2 #2570) og `kilder/c1_byttregel_forhand.md` (#2575).
Gjelder bare hvis byttet blir grønt innen 18:45. Rulles det tilbake, brukes STÅR-sporet i byttedommen, ikke disse svarene.

---

## A. «Hvorfor byttet dere modell etter frysen kl. 16?»
Fordi vi skrev en byttregel før vi målte, og kandidaten besto den. Regelen kom inn 16:46–16:49 (commit `c1e7cf8`): snitt F1 på MOT over test 2024, 2025 og 2026 minst +0,02 over frossen modell (0,4817), og intet år mer enn 0,02 under. Repo4 (frossen modell pluss fire historikktrekk) fikk 0,5057 / 0,5309 / 0,5120, snitt 0,5162, altså +0,0345, og verste år er +0,017 (2025). Sju kandidater ble målt, én besto, og dommeren gjenskapte alle tallene fra kald kopi før dommen.
Kilde: `kilder/c1_byttregel_forhand.md` (Regelen, Tidslinje), `kilder/c1_byttedom_265.md` (tabell, krav 1 og 2).

## B. «Intervallet for gevinsten krysser null ([−0,005; +0,078]). Er ikke det bare støy?»
Det kan være det, og det sier vi rett ut: 4 % av bootstrap-trekkene (klynger på selskap) gir repo4 under frossen, og 23 % under +0,02. Derfor krevde regelen at hvert testår holder, ikke bare snittet: repo4 er over frossen i alle tre år (+0,051, +0,017, +0,036), og også i 2023 som fjerde år utenfor regelen (+0,005, fire år +0,027). Vi påstår ikke at repo4 er sikkert bedre, bare at den aldri er dårligere i noe år vi har målt, og at vi byttet fordi en regel satt på forhånd sa det, ikke fordi tallet så pent ut.
Kilde: `kilder/c1_byttedom_265.md` (KI per år og snitt, forbehold 2 og 3).

## C. «Var regelen virkelig satt før dere så tallene?»
Delvis, og vi skiller det: 2026-tallet til repo4 (0,5120) og frossens tre år var kjent da regelen ble skrevet, så 2026 er året repo4 ble funnet på. Repo4 på 2024 og 2025 fantes ikke før regelen; de ble skrevet 16:49:31–16:50:54, etter at regelen sto 16:48:59. Disse to årene alene gir +0,051 og +0,017, snitt +0,034, og det holder for regelen uten 2026. Trening bare på år før val, grense og rutingsbånd valgt på val, testår kjørt én gang; seks lekkasje- og protokollpunkter er grønne.
Kilde: `kilder/c1_byttregel_forhand.md` (Tidslinje, sjekkliste 1–6), `kilder/c1_byttedom_265.md` (forbehold 1 og 5).

---

Merknad til den som limer inn: stiene `kilder/c1_byttedom_265.md` og `kilder/c1_byttregel_forhand.md` forutsetter at de to
rapportene kopieres til `arbeid/hack/c1/leveranse/kilder/` (som de andre kildene). Gjør de ikke det, pek på `state/rapporter/`.
Tallvakt: alle tall over står ordrett i de to kildene; hovedtallet blir 0,512 etter byttet.
