# Case 1: limelapp for jurysvar sp. 13 og 19 og ERLIG_EVALUERING §7, utgave BYTT og STÅR — arkitekt #2602, 05.11

Til smed3 (#2598) og den som lager BYTT-pakken (#2592). Lim inn **én** blokk, etter dommen 18:45 (#2603).
Ingen nye tall. Hvert tall står ordrett i en av disse kildene:
- `kilder/c1_byttedom_265.md` (dommer2 #2570, tabell, KI, forbehold 1–5, STÅR-sporet)
- `kilder/c1_byttregel_forhand.md` (#2575, regelen, tidslinje, sjekkliste 1–6)
- `ERLIG_EVALUERING.md` §7 benk A (tre-års-tabellen; står allerede i pakken)
- forsvaret selv: `state/rapporter/c1_forsvar_bytte.md` (#2594), svar A–C

De to første må kopieres til `arbeid/hack/c1/leveranse/kilder/` fra `state/rapporter/`. Mangler de der, bytt stiene til
`utviklingsrapport:c1_byttedom_265.md` og `utviklingsrapport:c1_byttregel_forhand.md` (samme form som sp. 19 bruker i dag).
Tallvakt-markørene (`<!-- tallvakt: ignorer ... -->`) er med der linjer har tall som ikke er hovedtall.

====================================================================
# BLOKK BYTT (hovedtall 0,512, repo4 levert)
====================================================================

### JURY_SPORSMAL.md, erstatt hele sp. 13 (overskrift og tekst)

## 13. «Den parallelle hybridløsningen slår dere på 2026. Hvorfor byttet dere til repo4 og ikke til den?»
Fordi vi byttet etter en regel skrevet før målingen, ikke etter det beste tallet på ett testår. Regelen: snitt F1 på MOT over test 2024, 2025 og 2026 minst +0,02 over den frosne modellen (0,4817), og intet år mer enn 0,02 under. Hybridløsningen (laget av andre i teamet, parallelt med agenten, ikke fra NBIM) gir 0,545 på 2026, men 0,407 på 2024, snitt 0,487 og verste år −0,047 mot frossen, så den feiler regelen. Repo4 (frossen modell pluss fire historikktrekk) gir 0,506 / 0,531 / 0,512, snitt 0,516, +0,035 mot frossen og verste år +0,017; den er eneste av sju kandidater som består. At hybriden er høyest på 2026 og lavest på 2024, er nettopp mønsteret regelen skal fange: nesten alle kandidater som ser bedre ut på 2026, faller under frossen på 2024. <!-- tallvakt: ignorer: hybriden og tre testår, bare 0,512 er hovedtall -->
Kilde: `ERLIG_EVALUERING.md` §7 (benk A), `kilder/c1_byttregel_forhand.md` (Regelen), `kilder/c1_byttedom_265.md` (tabell, krav 1 og 2).

### JURY_SPORSMAL.md, erstatt hele sp. 19 (overskrift og tekst)

## 19. «Hvorfor byttet dere modell etter frysen kl. 16, og er gevinsten mer enn støy?»
Fordi en regel satt før målingen sa det. Regelen (snitt over test 2024–2026 minst +0,02 over frossen 0,4817, intet år under −0,02) kom inn 16:46–16:49. Repo4 fikk 0,5057 / 0,5309 / 0,5120, snitt 0,5162, altså +0,0345, og verste år +0,017 (2025). Sju kandidater ble målt, én besto, og kontrollagenten (dommeren) gjenskapte alle tallene fra kald kopi før dommen. <!-- tallvakt: ignorer: tre testår og frossen, bare 0,512 er hovedtall -->
Gevinsten kan være støy, og vi sier det: klyngebootstrap på selskap gir snittet +0,0345 med KI [−0,005; +0,078]; 4 % av trekkene gir repo4 under frossen, 23 % under +0,02. Derfor krevde regelen hvert år, ikke bare snittet: repo4 er over frossen alle tre år (+0,051, +0,017, +0,036), og også i 2023 som fjerde år utenfor regelen (+0,005; fire år +0,027). Vi påstår ikke at repo4 er sikkert bedre, bare at den ikke er dårligere i noe år vi har målt. <!-- tallvakt: ignorer: differanser og KI, ikke hovedtall -->
Var regelen satt før tallene? Delvis, og vi skiller det: repo4 sitt 2026-tall (0,5120) og frossens tre år var kjent da regelen ble skrevet, så 2026 er året repo4 ble funnet på. Repo4 på 2024 og 2025 ble målt 16:49:31–16:50:54, etter at regelen sto 16:48:59; de to årene alene gir +0,051 og +0,017, snitt +0,034, og holder for regelen uten 2026. Trening bare på år før val, grense og rutingsbånd valgt på val, hvert testår kjørt én gang; seks lekkasje- og protokollpunkter er grønne. <!-- tallvakt: ignorer: klokkeslett og differanser, ikke hovedtall -->
Kilde: `kilder/c1_byttregel_forhand.md` (Regelen, Tidslinje, sjekkliste 1–6), `kilder/c1_byttedom_265.md` (tabell, KI per år og snitt, forbehold 1–5).

### ERLIG_EVALUERING.md §7, to endringer

1. Overskrift: `## 7. Forsøkt etter ordre om bedre treff: tre testår, repo4 valgt (05.11 kl. 16–18)`
2. Erstatt setningen som begynner «**Status når dette skrives (kl. 17)** …» til og med «… det leverte teståret).» med:

**Status: repo4 er godkjent og levert.** Kontrollagenten dømte BYTT kl. 17:02 etter å ha gjenskapt alle seks prediksjonsfilene fra kald kopi (byte-like), og pakken ble grønn innen fristen 18:45. Tallene i benk A under er dermed dommergodkjente; benk B er ikke dømt og var ikke med i byttet. 2024 har 88 MOT, 2025 har 99 og 2026 har 58 (det leverte teståret). <!-- tallvakt: ignorer: tre testår, bare 2026-kolonnen er hovedtallet -->

3. I benk A, repo4-raden: endre siste kolonne `oppfyller på papiret, avventer dom` til `**ja, levert** (dom c1_byttedom_265.md)`.
4. Erstatt siste setning i §7 («Blir en kandidat godkjent før innlevering, … levert uendret.») med:

Med parret klyngebootstrap per år er differansen +0,051 [−0,065; +0,160] i 2024, +0,017 [−0,031; +0,068] i 2025 og +0,036 [−0,008; +0,085] i 2026; snittet +0,0345 [−0,005; +0,078] krysser null. Byttet hviler altså på regelen satt før måling og på at repo4 aldri er under frossen, ikke på et sikkert tall. Kilde: `kilder/c1_byttedom_265.md`, `kilder/c1_byttregel_forhand.md`. <!-- tallvakt: ignorer: differanser og KI, ikke hovedtall -->

====================================================================
# BLOKK STÅR (hovedtall 0,476, frossen levert, repo4 rullet tilbake)
====================================================================

### JURY_SPORSMAL.md sp. 13: behold dagens tekst, legg til ett avsnitt til slutt (før Kilde-linja)

Etter frysen målte vi også sju kandidater på tre testår (2024–2026) mot en regel satt før målingen (snitt +0,02 over frossen, intet år under −0,02). Hybridløsningen gir der 0,407 på 2024, snitt 0,487 og verste år −0,047 mot frossen, og feiler regelen; den ser bare bedre ut på 2026. Se sp. 19 og `ERLIG_EVALUERING.md` §7. <!-- tallvakt: ignorer: hybriden og tre testår, ikke hovedtall -->

### JURY_SPORSMAL.md sp. 19: behold dagens tekst, legg til ett avsnitt før Kilde-linja

Etter ordren om bedre treff besto én kandidat, repo4 (frossen modell pluss fire historikktrekk), regelen satt før måling: 0,5057 / 0,5309 / 0,5120, snitt +0,0345 over frossen og verste år +0,017, gjenskapt av kontrollagenten fra kald kopi. Kontrollagenten dømte BYTT på vilkår om grønn pakke innen 18:45. Pakken ble ikke grønn i tide, så vi rullet tilbake etter planen, og **den frosne agenten står med 0,476**. Repo4 er altså forsøkt og avvist av tid, ikke av regelen, og er kandidaten for neste versjon. Gevinsten var heller ikke sikker: KI for snittet er [−0,005; +0,078]. <!-- tallvakt: ignorer: repo4 og differanser, ikke hovedtall -->
(Legg `kilder/c1_byttedom_265.md` (dommen og STÅR-sporet) til i Kilde-linja.)

### ERLIG_EVALUERING.md §7, to endringer

1. Overskriften står: `## 7. Forsøkt etter ordre om bedre treff: tre testår, ikke valgt (05.11 kl. 16–18)`
2. Erstatt setningen «**Status når dette skrives (kl. 17)** …» til og med «… det leverte teståret).» med:

**Status: den frosne modellen står.** Repo4 besto regelen (snitt +0,0345, verste år +0,017), og kontrollagenten dømte BYTT kl. 17:02 på vilkår om grønn pakke innen 18:45. Pakken ble ikke grønn i tide, så byttet ble rullet tilbake etter planen: repo4 er forsøkt og avvist av tid, ikke av regelen. Tallene i benk A er gjenskapt av kontrollagenten fra kald kopi; benk B er ikke dømt. 2024 har 88 MOT, 2025 har 99 og 2026 har 58 (det leverte teståret). <!-- tallvakt: ignorer: tre testår, bare 2026-kolonnen er hovedtallet -->

3. I benk A, repo4-raden: endre siste kolonne `oppfyller på papiret, avventer dom` til `ja, men ikke grønn pakke før 18:45; neste versjon`.
4. Erstatt siste setning i §7 («Blir en kandidat godkjent før innlevering, … levert uendret.») med:

Den frosne modellen er levert uendret. Repo4 går inn i `NESTE_VERSJON.md` som første kandidat. Kilde: `kilder/c1_byttedom_265.md` (dommen og STÅR-sporet).

====================================================================
Kontroll gjort av arkitekt: alle tall over finnes ordrett i `state/rapporter/c1_byttedom_265.md`,
`state/rapporter/c1_forsvar_bytte.md` eller §7 benk A i `arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md` (lest 17:05).
Ikke gjort: tallvakt-kjøring på innlimt tekst; det gjør #2597 etter innliming. STÅR-teksten forutsetter at grunnen til
tilbakerulling er «ikke grønn i tide»; er grunnen en annen, bytt den ene setningen.
