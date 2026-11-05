# Case 1: hva landsbyen ville gjort med én dag til (#2409)

> **Eldre tall:** linjer merket «eldre frossen modell #2044» gjelder modellen som var frossen før byttet til repo4 (#2572). Målte tall er ikke endret. Dagens hovedtall står i `arbeid/hack/c1/tall_tabell.md`.

Arkitekt, 05.11 kl. 15.40. Ingen nye tall: hvert tall under er målt før og har kilde. Levert agent er frossen #2044 miks h2,
F1 MOT **0,476 på test 2026 / 0,520 på val 2025** (måler v3 `--score mot`). Valgregelen står: alt velges på val, aldri på test. <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->

## 1. Historikk som foreldes på styrevalg (største feilgruppe)
- **Målt grunnlag:** 26 av 38 falske MOT på test er styrevalg. Alle 9 falske MOT i USA er saker der NBIM stemte MOT før
  og snudde til FOR i 2026. Samme person MOT året etter i USA: 4 av 4 (2024→2025), 0 av 5 (2025→2026) (`c1_falske_mot.md`).
- **Tak, ikke gevinst:** retter vi alle styrevalg-FP, blir F1 høyst 0,600 test / 0,596 val (`arkitekt_c1_neste_versjon.md`).
- **Hvorfor ikke levert:** Det enkle forsøket (nyeste historikk A+B, #2363) vant på val, 2025 +0,021 og 2024 +0,028, men paret bootstrap
  dekker null begge år. PR-AUC gikk ned (0,509 mot 0,525) og USA hadde fortsatt 9 falske MOT. Dom #2366: ikke inn (`c1_beslutning_nyeste_historikk.md`).
  Neste dag: bruk NBIMs egne begrunnelser fra tidligere år (`rationale_section`, finnes i dataene) til å se *hvilken regel* som ga MOT.
  Historikken skal foreldes når regelen endres, ikke bare med alderen.

## 2. Flere val-år, så små gevinster kan avgjøres
- **Målt grunnlag:** Kandidatene vi har er på 0,01–0,04 F1, mens støyen er større. India-regelen ga +0,042 på val 2025, men det var året
  regelen ble funnet (p ≈ 0,06). På 2024 ga den +0,008, og det er én sak (p = 1,0) (`c1_india_paret.md`). Seed-støyen i grunnmodellen alene
  spenner 0,030 på 2024 (`c1_india_seeds.md`). Bootstrap-intervallet på test er ca. ±0,1 (`c1_bootstrap_f1.md`).
- **Hvorfor ikke levert:** Med to val-år kan vi verken ta inn eller avvise disse kandidatene. Rullerende val på 2022–2025 (trene < år, måle år)
  krever omtrening per år og nye lekkasjesjekker. Det rakk vi ikke før frysen kl. 16. Dette steget gir ingen F1 alene, men
  avgjør tiltak 1 og India ærlig.

## 3. Revisor og «annet fra ledelsen» til menneske med sjekkliste
- **Målt grunnlag:** Savnede MOT der grunnen ikke står i saksteksten: 9 FN på test, 10 på val. Tak hvis alle rettes: 0,578 test / 0,601 val
  (`arkitekt_c1_neste_versjon.md`, kilder i `c1_feil_per_gruppe.md`). Rutingen fanger allerede noe: av 58 MOT på test havner 32 hos menneske (smed3 #2323, forsøk #1171).
- **Hvorfor ikke levert:** Revisorens år og honorar finnes ikke i arrangørens data. Å hente dem er nytt datainnsamlingsarbeid (DEF 14A).
  Tidligere DEF 14A-fakta i sitatagenten (#1950, #1959) ble målt med en annen måler og er ikke sammenlignbare. Gevinsten må vises på val først.

## Det vi bevisst *ikke* ville brukt dagen på
- **t4e (+samme-tekst-historikk +NPX), 0,529 på test** (forsøk #1033, måler v2, gruppe #2399 på tavla). Det er det høyeste testtallet vi har sett, men
  det tapte på val: 0,468 mot 0,522. Å ta det inn nå ville vært å velge på test (`c1_valgt_bort.md`).
- **Fast budsjett k=50 til menneske**, med F1 0,517. Det er valgt i etterkant på test og blir ikke hovedtall. Som beslutningsstøtte står
  målingen: 30 av 66 MOT i topp 50, presisjon 0,60, mot 0,03 recall ved tilfeldig utvalg (`speider_2399_recall_budsjett.md`).

**Rekkefølge:** 2 først (formiddag, gjør 1 og India målbare), så 1 (ettermiddag), og 3 bare hvis revisordata kan hentes lovlig og lokalt.
Trukket vinkel («finn den nedre grensen først»): takene over er øvre grenser. Ingen av dem er lovet som gevinst.
