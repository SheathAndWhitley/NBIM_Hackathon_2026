# Case 1: én side om hvordan forvalteren bruker agenten (arkitekt #2004)

Levert: `arbeid/hack/levering/BESLUTNINGSSTOTTE.md` (652 ord, én side). Den beskriver arbeidsflyten med tre bunker (FOR / mulig MOT med sitat / usikker til menneske), tall per 100 forslag, hva som skjer ved feil, og hva agenten ikke skal brukes til.

Tall per 100 forslag (test 2026, variant b, regnet fra P/R i `arbeid/oppgave_1995/ruting_b.txt`):
- Anbefalt oppsett med 10 % symmetrisk ruting (#1026): et menneske ser 23,3 saker (9,6 usikre + 13,7 MOT-flagg) og fanger 7,3 av 10,4 MOT. 3,0 MOT går ikke gjennom noen. 7,9 flagg er falske. Dette er en øvre grense, siden mennesket antas å svare riktig.
- Uten ruting (#1023): 17,7 saker sett, 6,7 MOT fanget. Skjevt bånd (#1027): 17,7 saker sett, 6,7 fanget, bare 3,5 falske flagg.
- Ingen nye modeller er kjørt. Tallene er regnet om fra eksisterende linjer og kontrollert med et lite regnestykke.

Avvik andre bør rette: BEGRENSNINGER.md pkt. 6 og METODE.md pkt. 6 bruker fortsatt #1955-tallene (presisjon 0,38 → 0,50, 125 saker). For variant b er det riktige 0,38 → 0,43 og 119 saker (#1995). Dette gjelder dommer #2005 og speider #1975.
