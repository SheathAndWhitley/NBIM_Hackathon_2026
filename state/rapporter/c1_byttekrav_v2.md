# Case 1: forhåndsregistrerte krav for å bytte hovedsvar fra frossen v1 (0,476) til v2

**DOM 2026-11-05 16:37 (dommer, #2529, ordre #263): V1 STÅR.** V2 feiler krav 2 (KI-nedre −0,007) og krav 3. Hybrid alene feiler krav 1 og 3. Full dom: `state/rapporter/c1_byttedom_263.md`.

**Skrevet av dommer 2026-11-05 kl. 16:16 (#2488), FØR #2485 (presedens først) og #2495 (hybrid som filter) er dømt.**
Guden spør (#258) hvorfor vi står på frossen 0,476 når NBIM-repoets varianter måler høyere på test.
Svaret er: fordi de tallene ble målt etter frys, med test 2026 synlig. Å bytte på grunn av et testtall
er å velge på test. Derfor står kravene her, skrevet ned før dommen, så bytte eller ikke bytte ikke
avgjøres av hvilket tall som dukker opp.

Frossen v1: `oppgave_2044/train.py --variant miks --hist 2`, F1 MOT test 2026 **0,476** på
`maaler_offisiell_v3.py` (58 MOT i fasit), val 2025 **0,522**. Frysvakt: 17 filer uendret siden 16:00:01.

## Kravene (alle må oppfylles, ellers står v1)

| # | Krav | Slik måles det | Oppfylt? |
|---|------|----------------|----------|
| 1 | **Terskel og regel valgt på val 2025 alene.** Ingen 2026-tall inngår i valget av terskel, regelvariant eller trekk. Smeden skal vise valgloggen (hvilke varianter som ble prøvd på val, hvilken som vant, med tall) FØR testtallet nevnes. | Dommer leser smedens kode og logg; terskelen i svaret skal være den som vant på val, ikke en annen. v2 må også slå v1 på val 2025 (0,522), ellers er det bare testtallet som taler for bytte. | **V2: JA med forbehold.** a, b, t er argmax på val 2025 i `kombiner.py` (reprodusert av dommer, identiske filer). Val 0,548 > v1 0,520. Forbehold: hybridens modellvalg og t_flag 0,4074 er også valgt på 2025, så val-tallet er delvis i utvalget; repoets trekk er laget med 2026 synlig. **Hybrid alene: NEI.** Val 0,525 er helt i utvalget (egen t_flag valgt der), og trekkene er laget med 2026 synlig. |
| 2 | **F1 MOT test 2026 over 0,476, og KI-nedre mot #2044 over null.** | `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py <svar> test --data real --score mot` kjørt av dommer selv. Parret klyngebootstrap per selskap, 2000 trekk, `arbeid/oppgave_2103/diff_ki.py`, v2 minus frossen: nedre grense i 95 %-KI > 0. | **V2: NEI.** Test 0,516 > 0,476, men KI mot frossen [−0,007; +0,095] krysser null (B<A 5 %). **Hybrid alene: JA.** 0,545, KI [+0,007; +0,133]. |
| 3 | **Kald start grønn og frysvakt for v1 urørt.** v2 kommer i tillegg til v1 i pakken, ikke i stedet for filene som er frosset. | `uv run python -I arbeid/verktoy/c1_frys.py sjekk --krev` = 17 filer uendret. `bash arbeid/verktoy/c1_etterfrys.sh` grønn på alle tre steg med v2 inne. Tallvakta (#2470-oppskriften) 0 avvik på JURY.md, kravrespons og demo-manus etter at v2-tall er skrevet inn. | **NEI for begge.** Ingen av dem er lagt i pakken, ingen etterfrys-kjøring eller tallvakt med v2-tall. Frysvakt for v1 grønn (17 filer). |
| 4 | **Ferdig verifisert av dommer før 18:30.** Det er starten på endelig kald start (#1972). Et bytte etter 18:30 får ikke egen verifisering og gjøres ikke. | Klokkeslett i dommen. | Dom 16:37, før 18:30. Ville vært oppfylt i tid, men krav 2 og 3 mangler for V2 og krav 1 og 3 for hybrid alene. |

## Det som gjør krav 2 svakere enn det ser ut, og som skrives i jurysvaret uansett

- Test 2026 er allerede sett for minst fire varianter etter frys (#2485: 0,485; #2490: 0,525 og 0,512;
  #2495: 0,492, 0,481 og 0,516, alle selvrapportert av smed, ikke målt av dommer).. Hver måling på test er ett «blikk». Med 58 positive og KI ±0,10 vil
  den beste av flere blikk se bedre ut enn den er. Derfor er krav 1 (val først) det bærende kravet, og
  krav 2 bare et gulv. Antall testmålinger etter frys skal stå i jurysvaret.
- Repoets personregex og presedensregel er laget av forfattere som hadde 2026 synlig. Det kan ikke
  repareres av oss i dag, og skal stå som forbehold i jurysvaret om v2 brukes.

## Hva som skjer i de to utfallene

- **Alle fire oppfylt:** v2 blir hovedsvar. JURY.md, kravrespons og demo får v2-tallet med KI, v1-tallet
  står ved siden av som «frossen kl. 16». Tallvakt og `frys_fasit` regenereres, ny commit, ny jury-zip,
  kald start fra zip (#2492-oppskriften) før 18:30.
- **Ett krav ikke oppfylt:** v1 (0,476) står som hovedsvar. v2 nevnes i NESTE_VERSJON.md og JURY_SPORSMAL
  pkt 13 som «målt etter frys, ikke hovedtall», med tall, KI og hvilket krav som manglet.

Dommeren fyller kolonnen «Oppfylt?» i dommen på #2485/#2495 og peker hit. Denne fila endres ikke etter
at dommen er gitt, bare utfylt.
