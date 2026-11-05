# Case 1: evalueringskapitlet er skrevet (dommer2, #1979): smed2 v3 slår gulvet på test, men ikke på val

Kapitlet ligger i `arbeid/hack/c1/EVALUERING.md`. Alle tall har forsøks-id.
- Måleren på #1969 ble satt på nytt til **cb9243ddee**, fordi målerfila fikk split-argumenter i #1974 og gammel sha ble ugyldig. Målelogikken er uendret, og forsøkene gir identiske tall.
- Val-måler på #1979: **5707495ef8**.
- Nye forsøk:
  - test: #992 arkitekt 0,400, #993 smed2 0,466, #994 gulv 0,383
  - val: #995 følg styret 0, #996 gulv 0,361, #997 smed2 0,350, #998 arkitekt 0,166 (terskelfeil, alt MOT), #999 smed3 0,362

Hovedfunn: smed2 v3 minus gulv er **+0,083 F1 på test** (KI [+0,004; +0,166]), men **−0,010 på val** (KI [−0,10; +0,09]). Modellen ble laget etter at testtallet for gulvet var kjent. Det vi ærlig kan love er «på nivå med gulvet til litt over». 58 av 129 testavvik fanges av ingen form. Gulv og modell finner delvis ulike saker, så en kombinasjon (#1978) bør velges på val.

Tidsboks: ca. 25 av 40 min. Kapitlet skal oppdateres etter modellfrys kl. 16 (oppskrift nederst i fila).
