# Case 1: dom over STÅR-reserven etter ærlighetssetningene (#2633) — GRØNN med to vilkår

Dommer, 05.11 kl. 17:2x. Lest `arbeid/hack/c1/reserve_staar/` (README, kravrespons, ERLIG_EVALUERING, JURY_SPORSMAL)
slik de står etter commit 3ceaac0 (uendret av 84d63e8, som bare la til MUNTLIG/LES). Sammenlignet mot BYTT-utgaven i
`leveranse/`, mot den frosne jury-zipen `/tmp/jurypakke_c1_2587.zip` og mot dommerrapportene c1_byttedom_265, c1_byttregel_forhand
og c1_dom_aerlighet. `lag_staar.py --sjekk`: README LIK, kravrespons LIK.

## Dom: GRØNN

| krav | funn | status |
|---|---|---|
| (1) forbehold om tidspunkt + lekkasjesjekk står og er sant for STÅR | ERLIG_EVALUERING.md:106 (tidspunkt: regel 16:49, 2026-tall kjent 16:13, 2024/25 målt 16:49–16:51, +0,051/+0,017, snitt +0,034) og :108 (lekkasje: #2575 seks punkter, brute force 400 rader ikke kjørt for repo4). JURY_SPORSMAL.md:87–88 sier det samme. Alle klokkeslett og tall stemmer med c1_dom_aerlighet.md:9–12 og c1_byttedom_265.md:22–29. Slutten er sluttført STÅR: «Den frosne modellen (0,476) står» (E:106), «Den frosne agenten (0,476) står» (J:87), README.md:12 og kravrespons.md:7 «så den frosne agenten står med 0,476». | GRØNN |
| (2) ingen BYTT-tall som hovedtall | Hovedtall 0,476 i README.md:8, :29, :46, :50, :62; kravrespons.md:4, :10; ERLIG_EVALUERING.md:6, :29, :34, :43, :53, :71; JURY_SPORSMAL.md:6, :11 (95,7 %, 30 funnet, 38 flagg), :15 (KI [0,36; 0,59], +0,11), :46, :52, :60–61, :81. Eneste treff på 0,512/repo4 utenfor § 7 og sp. 20 er README.md:12 og kravrespons.md:7, begge merket «byttedom, ikke hovedtall» og sluttført med 0,476. «fire historikktrekk» er borte fra modellbeskrivelsen (README.md:77 sier «miks h2»). Ingen rest av TP 32/FP 35/FN 26, 164 av 1578, 10,4 %, 96,0 %, [0,40; 0,62] eller `c1_repo4_tall_2592.md`. | GRØNN |
| (3) ingen henvisning til filer som ikke finnes | Alle 130 fil-henvisninger i de fire filene løst mot zip 2587 (`arbeid/hack/c1/leveranse/`, `kilder/`, `arbeid/hack/c1/`): alle finnes, unntatt `utviklingsrapport:`-pekerne, som zipens rot-README.md:66 forklarer som utviklingsrapporter utenfor zipen. De to nye i sp. 20 (`utviklingsrapport:c1_byttregel_forhand.md`, `utviklingsrapport:c1_byttedom_265.md`) finnes i `state/rapporter/`. Den usanne NESTE_VERSJON-pekeren fra #2618 er strøket i sp. 20 (JURY_SPORSMAL.md:90 peker bare på ERLIG § 7 og de to rapportene). NESTE_VERSJON.md:35-36/89-96/100-102 i sp. 19 stemmer med HEAD-utgaven (V2-avsnittene). | GRØNN |

Diff frossen zip 2587 → STÅR er bare: README.md:12 (byttedom-linja), kravrespons.md:7 (byttedom-setningene),
ERLIG_EVALUERING.md:78 (overskrift), :79 (status + «gjenskapt byte-likt av kontrollagenten», sant per c1_byttregel_forhand.md:22),
:86 (regel-kolonne), :105–108 (forbeholdet), JURY_SPORSMAL.md:86–90 (sp. 20). Ingenting annet er rørt.

## Vilkår (må gjøres ved STÅR, ellers blir to setninger usanne)
1. **c1_byttedom_265.md «Endelig» (linje 67–68) må fylles med STÅR** av den som tar #2603 kl. 18:45. Sp. 20 (J:90) siterer rapporten, og i dag slutter den med «BYTT på vilkår». Uten STÅR-linja motsier kilden svaret.
2. Setningene «pakken med repo4 ble ikke grønn i tide» (README:12, kravrespons:7, E:79, :86, :106, J:87) er bare sanne hvis dommen kl. 18:45 blir STÅR. Blir det BYTT, skal ikke en linje herfra brukes (LES.md sier det samme).

## Merknader, ikke blokkerende
- README.md:12 og kravrespons.md:7 sier «regel satt før måling» uten 2026-forbeholdet i samme setning; README peker til § 7 der det står. Kravresponsen peker ikke dit. Akseptabelt, men et jurymedlem som bare leser kravresponsen får ikke forbeholdet.
- JURY_SPORSMAL.md:1 sier «de atten vanskeligste», men fila har 20 spørsmål. Arvet fra frossen tekst (sp. 19 var der alt). Kosmetisk.
- ERLIG_EVALUERING.md:104 «(benk A, `kilder/`-kopi hvis dommen tar den inn)» er en intern formulering i jurytekst; ingen fil er lovet, så ikke brudd på krav 3.
