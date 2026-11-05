# Case 1: modellen som fryses kl. 16 er #2044 miks h2, ikke t4e (dommer #2080)

**Valg:** smed2 #2044 miks h2, slik agenten `kjor_agent.py` kjører den fra kald start. Val 2025: 0,522. Test 2026: **0,482** (forsøk #1067, målt av tavla med rundens måler 9d81a418dd). Detaljer: `arbeid/kandidater/FROSSEN.md`.

## Hvorfor ikke t4e (test 0,529)
- **Regelen fra #2062: val velger, test rapporterer.** t4e har lavest val av de tre (0,468 mot 0,500 og 0,522). Den er «best» bare fordi vi så på test. Hadde vi valgt den, ville 0,529 vært et tall valgt etter testfasiten, altså for høyt.
- **Forskjellen på test er støy.** Det er 66 MOT i 2026. Bootstrap-intervallet for t4e er 0,42–0,63. For differansen t4e − t2 er det −0,01 til +0,10 (hack_innsikt.md). Val går motsatt vei.
- **Val-tallene kan sammenlignes.** Alle tre er trent på år < 2025, med C og grense valgt på val 2025 og målt der. Tallene 0,664/0,616 i dommer_2062-rapporten er IKKE val-tall for valg: de filene er trent på alt før 2026, inkludert 2025.
- **Valgt modell er allerede den agenten leverer** fra kald start (sitater, ruting, robusthet). Å bytte til t4e ville gitt mer arbeid og ny risiko før kl. 16, med et val-argument som peker mot t4e.

## Ærlig tall til juryen
Hovedtallet er **0,482** (P 0,465, R 0,50) på test 2026, sett én gang i praksis. Prediksjonene er målt fire ganger med samme resultat, uten at noen måling ble brukt til valg. t4e og 0,529 kan nevnes som «variant forkastet på val», ikke som resultat.

## Merknader
- #1046 kunne ikke ommåles med `forsok-ommaal`/`forsok-vakt`, fordi oppgave #2053 ikke er en Hack-oppgave. Fila er derfor registrert på nytt mot #2034 med `--sti`: nytt forsøk #1067 = 0,481752 (kilde=maaler).
- Måleren viser «streng MOT: TP 0 FP 0 FN 0» også for agentfila. FN 0 tyder på at streng MOT ikke telles for real_votes i dette formatet. Det er ikke undersøkt her. Hovedtallet er F1 på avvik fra styret (MOT/AVSTÅ). Det bør sies tydelig i JURY.md (#1975), siden #231 sier «F1 på MOT».
- Revurderes bare hvis #2081 (smed3) får klart høyere val enn 0,522 med samme protokoll før kl. 16.
