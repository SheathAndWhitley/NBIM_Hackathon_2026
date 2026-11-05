# Dom #2527: hybridløsningen kalles ikke lenger NBIMs (ordre #262), GODKJENT med én stryking

Dømt av dommer2 05.11 kl. 16.45, på smed4s retting #2526 (rapport `c1_opphav_hybrid_2526.md`).

## Hva jeg sjekket, uavhengig av smed4
- **Restsøk** i `arbeid/hack/c1/leveranse/` og `arbeid/hack/levering/*.md` etter «NBIMs egen/eget repo|hybrid|presedens», «NBIM-repo», «opplastede repo», «repoet juryen», «fra NBIMs», «repo-hybrid»: 0 treff utenom filnavnene `kilder/c1_nbim_repo_sammenligning*.md` (beholdt så pekere ikke brekker, med merknad i fila og i LESMEG). «NBIMs egen» finnes tre steder i kilder/, alle om NBIMs retningslinjer og nummerering, ikke om løsningen. «repoet» ellers i pakka betyr vår egen rotmappe (README, ERLIG, kravrespons), riktig.
- **Diffen** mot HEAD: 8 filer, bare ordlyd. Svar 3 i JURY_SPORSMAL (som fortsatt sa «NBIMs egen presedensregel i det opplastede repoet» mens jeg leste) ble rettet før #2526 lukket.
- **Tallvakt** fra landsbymappa: 18 filer, 169 påstander, 0 avvik.
- **Frysvakt**: GRØNN, 17 filer like som ved frys 16:00:01. Frosne filer er ikke rørt.
- **Pekere**: alle backtick-stier i de 8 filene finnes. Eneste «døde» er plassholderen `kilder/<navn>.md` i LESMEG, som er med vilje.
- **Zip**: `pakk_jury.sh` i egen mappe, se nederst.

## Én stryking (oppgave #2542 til smed4)
Svar 19 sier hybriden er «ikke fra NBIM og ikke et offentlig repo». Ordre #262 sier bare at teamet laget den utenom landsbyen. Om den er offentlig vet vi ikke, og zip-navnet `NBIM_Hackathon_2026-main` ser ut som en GitHub-nedlasting. Påstanden er udokumentert og skal strykes; «ikke fra NBIM» står. Ingen tall endres. #2535 (tallvakt, frys-fasit, sluttsjekk) tar det med.

## Dom
Ordlyden er nå ærlig: «teamets parallelle hybridløsning, laget i teamet utenom landsbyen, ikke fra NBIM» i jurysvar 3, 13, 16, 17, 19, NESTE_VERSJON tiltak 4 og de fem kildefilene. Godkjent, gitt strykingen i #2542.

## Zip
`pakk_jury.sh` bygde zipen (utgang 0, 1,0 MB, 138 filer) i egen mappe. Pakket ut: 0 treff på NBIM-opphav utenom filnavnene, «ikke fra NBIM» i 7 filer, «offentlig repo» bare i svar 19 (strykes i #2542). Temp-mappene mine er slettet.
