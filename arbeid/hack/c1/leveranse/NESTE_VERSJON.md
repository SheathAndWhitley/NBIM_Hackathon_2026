# Neste versjon av stemmeagenten: fire tiltak, regnet fra feilene og teamets parallelle hybridløsning

Tiltak 1–3 i samme rekkefølge som `kilder/c1_neste_steg.md`. Ingen nye tall: hvert tall
under er målt før og har kilde. Grunnlag: eldre frossen agent (miks h2), F1 på MOT 0,476 på test 2026
(eldre TP 30, FP 38, FN 28) [`utviklingsrapport:c1_feil_per_gruppe.md:4`] og 0,520 på val 2025 (TP 45, FP 29, FN 54)
[`<arbeidsmappe>/oppgave_2274/feil_val2025.md:1`], måler v3 `--score mot`. Valgregelen står: alt velges på val,
aldri på test. Ingenting her er bygd inn; dette er plan.
«Øvre grense» = F1 hvis tiltaket retter **alle** feilene i sin gruppe og ingen andre
[`utviklingsrapport:arkitekt_c1_neste_versjon.md`]. Den nås ikke i praksis; den sier bare hvor mye gruppa er verdt.

## Tiltak 1: historikk som foreldes på styrevalg (største feilgruppe)

- **Feilgruppe:** falske MOT på styrevalg. 26 av 38 FP på test [`c1_feil_per_gruppe.md:25`],
  22 av 29 på val [`feil_val2025.md:7`]. Alle 9 falske MOT i USA er saker der NBIM stemte MOT før og
  snudde til FOR i 2026. Samme person MOT året etter i USA: 4 av 4 (2024→2025), 0 av 5 (2025→2026)
  [`kilder/c1_falske_mot.md`].
- **Øvre grense:** retter maks 26 FP (test) / 22 FP (val), ingen FN. F1 0,512 → **0,600** (test) og
  0,520 → **0,596** (val) [`arkitekt_c1_neste_versjon.md`].
- **Hvorfor ikke levert:** nyeste historikk A+B vant på val, 2025 +0,021 og 2024 +0,028, men paret
  bootstrap dekker null begge år, PR-AUC gikk ned (0,509 mot 0,525) og USA hadde fortsatt 9 falske MOT.
  Kontrollagentens dom: ikke inn [`kilder/c1_beslutning_nyeste_historikk.md`]. Forfall med år:
  val 2025 0,520 → 0,551, men holdt-ut 2024 0,567 → 0,552 [`utviklingsrapport:arkitekt_tiltak1_malt.md`].
- **Neste dag:** bruk NBIMs egne begrunnelser fra tidligere år (`rationale_section`, finnes i dataene
  [`utviklingsrapport:opplastet_20261105_114241_real_votes.md:7`]) til å se *hvilken regel* som ga MOT.
  Historikken skal foreldes når regelen endres, ikke bare med alderen. Bare fjorårets og eldre
  begrunnelser, aldri årets (lekkasje).

## Tiltak 2: flere val-år, så små gevinster kan avgjøres

- **Problem:** kandidatene vi har er på 0,01–0,04 F1, mens støyen er større. India-regelen ga +0,042 på val
  2025, men det var året regelen ble funnet (p ≈ 0,06); på 2024 ga den +0,008, og det er én sak (p = 1,0)
  [`utviklingsrapport:c1_india_paret.md`]. Seed-støyen i grunnmodellen alene spenner 0,030 på 2024
  [`utviklingsrapport:c1_india_seeds.md`]. Bootstrap-intervallet på test er ca. ±0,1
  [`kilder/c1_bootstrap_f1.md`].
- **Hva:** rullerende val på 2022–2025 (trene på år før, måle på året). Krever omtrening per år og nye
  lekkasjesjekker; det rakk vi ikke før frysen kl. 16.
- **Gevinst:** ingen F1 alene, men avgjør tiltak 1 og India-regelen ærlig. Med to val-år kan vi verken ta
  dem inn eller avvise dem.

## Tiltak 3: revisor og «annet fra ledelsen» til menneske med sjekkliste

- **Feilgruppe:** savnede MOT der NBIMs grunn (GVG 4.3 og 5.1) ikke står i saksteksten: 9 FN på test,
  10 på val [`c1_feil_per_gruppe.md:26-27`, `feil_val2025.md:9-10`].
- **Øvre grense:** 0,578 test / 0,601 val hvis alle rettes [`arkitekt_c1_neste_versjon.md`]. Rutingen fanger
  allerede noe: av 58 MOT på test havner 32 hos menneske (kontrollagenten, forsøk 1171).
- **Hvorfor ikke levert:** revisorens år og honorar finnes ikke i arrangørens data
  [`utviklingsrapport:opplastet_20261105_114241_real_votes.md:7`]. Å hente dem er nytt datainnsamlingsarbeid (DEF 14A).
  Tidligere DEF 14A-fakta i sitatagenten ble målt med en annen måler og er ikke
  sammenlignbare. Gevinsten må vises på val først.

## Tiltak 4: presedens først, vår rangering etterpå (fra teamets parallelle hybridløsning, ikke fra NBIM)

- **Hva hybridløsningen gjør:** Teamets parallelle hybridløsning (laget av andre i teamet, parallelt med agenten, ikke fra NBIM) flagger en sak uansett modell når NBIM har avveket
  før hos samme selskap: på **samme direktør hvis navnet er kjent, ellers samme sakstekst** (tekst uten tall).
  «Avveket» teller alle avvik, også AVSTÅ. Saker uten presedens går til en kalibrert modell med terskel valgt
  for F1 i valideringsåret [`kilder/c1_nbim_repo_sammenligning_dom.md`].
- **Målt på vår måler og vår test 2026** (58 MOT i fasit, hybridløsningens kode uendret, gjenskapt av kontrollagenten med
  avvik 0; ikke hovedtall): presedensregelen alene gir F1 MOT **0,515** (P 0,605, R 0,448), +0,039
  [−0,051; +0,126] over vår frosne agent, innenfor støyen. Hybriden trent på vår splitt (til og med 2024,
  terskel valgt på 2025) gir **0,545**, **+0,069 [+0,007; +0,133]** (parret klyngebootstrap per selskap), det
  eneste intervallet som ligger helt over null [`kilder/c1_nbim_repo_sammenligning.md`].
- **Hvor gapet ligger:** i F1, ikke i PR-AUC. Vår PR-AUC på MOT er høyest: 0,525 mot 0,318 for presedensregelen
  og 0,413 for hybriden. Gapet er presedens som overstyring og færre, sikrere flagg: vi flagger 68 med
  presisjon 0,478, hybriden 52 med 0,577.
- **Kombinasjonen i neste versjon:** (1) presedensflagget først, med hybridløsningens definisjon (direktør, ellers sak),
  men bare med stemmer fra før møtedatoen; (2) saker uten presedens får vår P(MOT) som i dag; (3) terskelen
  settes på val for F1, ikke på test. Overlapp med tiltak 1: presedensregelen gir også falske MOT der NBIM
  snudde, så tiltak 1 (foreldelse når regelen endres) skal gjelde presedensflagget også.
- **Hvorfor vi ikke bytter etter frys:** målingen ble gjort etter at modellen var frosset og testen sett.
  Å bytte til regelen eller hybriden nå ville vært å velge på test, samme grunn som t4e ble valgt bort.
  Hybridløsningens egen test (2025-26) inneholder 2026, så utformingen kan være valgt med 2026 synlig. Bare én rad har
  et intervall over null, med 58 positive. Kombinasjonen skal vinne på val (rullerende, tiltak 2) før den
  tas inn.
- **Hybridløsningens personnøkkel som trekk i vår modell (målt etter frys, ikke hovedtall):** frossen modell
  pluss bare `prev_same_person` (forrige stemme på samme direktør i samme selskap), terskel valgt på val 2025
  (0,536). Resultat på test 2026, ikke hovedtall: F1 MOT 0,525, mot 0,476 frossen: +0,049 [+0,016; +0,090],
  parret klyngebootstrap per selskap. Gevinsten kommer fra presisjon (8 færre falske MOT), og bare 14 saker
  endrer prediksjon. Alle fire trekk fra hybridløsningen sammen hjelper ikke mer: ikke hovedtall 0,512, +0,036 [−0,008; +0,085].
  Som trekk virker presedens bedre enn som overstyring etter vår modell (ikke hovedtall 0,485).
  Personregexen er laget av hybridløsningens forfattere i teamet med 2026 synlig, og testen er sett. Derfor gjelder det samme
  som over: dette blir første test i neste versjon på rullerende val, ikke et bytte nå
  [`utviklingsrapport:c1_repotrekk_neste_versjon.md`].
- **Personnøkkelen på tidligere år (rullende tidssplitt, ikke hovedtall):** samme oppsett, C og terskel
  valgt på året før. Personnøkkel minus uten: 2024 −0,037 [−0,133; +0,058] (0,418 mot 0,455), 2025 +0,001
  [−0,042; +0,050] (0,516 mot 0,514), 2026 +0,049 [+0,016; +0,090]. Gevinsten holder ikke og finnes bare i 2026.
  KI dekker null i 2024 og 2025. Den tas derfor ikke inn som første tiltak, bare som et trekk som kan prøves igjen
  [`kilder/c1_personnokkel_rullende.md`, dom `kilder/c1_personnokkel_dom.md`].
  Figur (år på x, F1 MOT med og uten personnøkkel, KI-strek, «følg styret» = 0): `kilder/c1_personnokkel_rullende.png` (laget av `arbeid/oppgave_2497/lag_figur.py` i repoet, tallene lest rett fra tabellen i `kilder/c1_personnokkel_rullende.md`; dom `kilder/dom_2497_figur.md`).
- **Hybriden først, vår rangering i midten (ikke hovedtall, målt etter frys):** hybriden
  avgjør sakene den er sikker på (score ≥ 0,407 gir MOT, < 0,091 gir ikke MOT); resten avgjøres av frossen
  modell med p ≥ 0,919. a, b og t er valgt på val 2025 og brukt uendret på test 2026.
  Test 2026, ikke hovedtall: F1 MOT 0,516 (ikke hovedtall P 0,485, ikke hovedtall R 0,552). Mot 0,476 frossen: +0,040 [−0,007; +0,095]; mot hybriden
  0,545: −0,029 [−0,067; +0,010], parret klyngebootstrap per selskap, 2000 trekk. Ingen av delene er sikre.
  Det som hjelper er hybridens «sikker nei», som fjerner falske MOT fra vår modell (38 → 34). Hybridens
  terskel er også valgt på 2025, så val-tallet er litt optimistisk. Kombinasjonen slår ikke hybriden alene og
  tas ikke inn uten å vinne på rullerende val [`utviklingsrapport:c1_hybrid_pluss_rangering.md`].
- **Samme kombinasjon rullet til 2024 (tidligere år, ikke hovedtall, målt etter frys):** hybriden trent på
  årene til og med 2022, a, b og t valgt på val 2023 (a 0,625, b 0,269, t 0,96), testet én gang på 2024.
  F1 MOT 2024, ikke hovedtall: 0,407 mot 0,455 for frossen-oppsettet rullet til samme år: −0,047 [−0,173; +0,092],
  parret klyngebootstrap per selskap. Med t 0,96 bidrar vår rangering nesten ikke, og kombinasjonen blir i praksis
  hybriden alene. Den flagger flere saker, men presisjonen faller. Gevinsten fra 2026 (+0,040) følger ikke med til 2024.
  Kontrollagentens byttedom (16:42): frossen agent står som hovedtall, fordi KI-nedre for 2026 er under null og
  kombinasjonen ikke er lagt inn i pakken. Kombinasjonen må vinne på flere rullende år før den tas inn
  [`kilder/c1_v2_rullende_2024.md`].

## Det vi bevisst *ikke* ville brukt dagen på

- **t4e (+samme-tekst-historikk +NPX), 0,529 på test** (forsøk 1033, måler v2): det høyeste testtallet vi har
  sett, men det tapte på val: 0,468 mot 0,522. Å ta det inn nå ville vært å velge på test
  [`kilder/c1_valgt_bort.md`].
- **Fast budsjett k=50 til menneske**, F1 0,552: valgt i etterkant på test, blir ikke hovedtall. Som
  beslutningsstøtte står målingen: 30 av 66 MOT i topp 50, presisjon 0,60, mot 0,03 recall ved tilfeldig
  utvalg [`state/rapporter/speider_2399_recall_budsjett.md:16-23`].
- **«Styrevalg i USA → menneske»:** løfter test (eldre 0,476 → 0,504) men senker val (0,520 → 0,488)
  [`kilder/c1_feil_stabilitet.md:23`].

**Rekkefølge:** 2 først (formiddag, gjør 1 og India målbare), så 1 (ettermiddag), og 3 bare hvis revisordata
kan hentes lovlig og lokalt [`kilder/c1_neste_steg.md`]. Tiltak 4 (presedens først) måles i samme
rullerende val som tiltak 1, siden begge handler om historikk. Takene over er øvre grenser; ingen av dem er
lovet som gevinst.

## Små rettelser fra rare-inndata-testen (ikke hovedtall, endrer ingen stemme)

Fra `kilder/c1_rare_inndata.md` og dommen `kilder/dom_2499_rare_inndata.md` (svakhet 3 og 5; se også `BEGRENSNINGER.md` pkt. 9):
- **AI-saker:** fjern `ai` alene fra injeksjonsregexen (`levering/injeksjon_hoflig.py:21`), eller krev at ordet står i en instruks («the AI should»). I dag flagges aksjonærforslag om AI-risiko som instruks.
- **Uleste rader:** la `styret` og `anbefaling` stå tomme når styreanbefalingen mangler, i stedet for standardverdien FOR (`levering/c1_real.py:210`).
- I samme runde: sjekk hele fila før radene behandles. 0 byte eller manglende påkrevde kolonner gir én feilmelding (med skilletegnet som ble funnet) og utgang ≠ 0.
