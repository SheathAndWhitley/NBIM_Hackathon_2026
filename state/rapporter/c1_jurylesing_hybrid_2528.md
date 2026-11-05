# Case 1 (#2528): jurysvar og jury-spørsmål lest som juryen, med teamets hybridløsning ved siden av

Lest: `arbeid/hack/levering/JURYSVAR.md`, `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md` (JS), og det de peker på:
NESTE_VERSJON.md (NV), kilder/LESMEG.md og de to kildefilene `c1_nbim_repo_sammenligning*.md`. Ingen filer endret.

## Kort svar
Ingen setning i JURYSVAR eller JS sier at hybridløsningen kommer fra NBIM. Alle stedene sier «ikke fra NBIM».
Tre ting kan likevel gi juryen feil inntrykk eller gjøre sammenligningen urettferdig:
- en NBIM-overskrift i NV,
- filnavnet «nbim_repo» i hver kildepeker,
- ordet «landsbyen», som juryen ikke kjenner.

I tillegg sier JURYSVAR og JS to forskjellige ting om hvor gapet ligger.

## Funn, viktigst først
1. **NV:1** «… regnet fra feilene og NBIMs repo». Her står det fortsatt at noe kommer fra NBIM. Det er det eneste stedet igjen.
   Forslag: «… regnet fra feilene og teamets parallelle hybridløsning».
2. **JURYSVAR:23, JS:15, JS:57, JS:58, JS:74 og NV:56/61** peker alle på `kilder/c1_nbim_repo_sammenligning(_dom).md`.
   En jury som leser kildelista, ser «nbim_repo» fem ganger. Bare LESMEG:27 og en kursiv linje inne i fila forklarer
   at navnet er historisk. Forslag (billigst): skriv «(filnavnet er historisk, løsningen er ikke fra NBIM)» ved første
   peker i JURYSVAR:23 og JS:15. Alternativ: kopier fila til `c1_hybrid_sammenligning*.md`, la de gamle stå og bytt pekerne.
   Pekerne flytter seg da, så frys-fasit og tallvakt må kjøres på nytt.
3. **JURYSVAR:23 og JS:15, 57, 81, NV:53, LESMEG:27** sier «laget i teamet utenom landsbyen». Ordet «landsby» er ikke
   forklart i README, JURY eller kravrespons. For juryen er det sjargong og høres ut som en ekstern kilde.
   Forslag: «laget av andre i teamet, parallelt med agenten» (og stryk «landsbyen»).
4. **Motsigelse om hvor gapet ligger.** JURYSVAR:23 sier at gapet ligger i presedensregelen og terskelen, «ikke i modellen».
   JS:57 sier at hybridløsningens modell alene gir 0,538 (dom `kilder/c1_nbim_repo_sammenligning_dom.md:22`), og at vi
   derfor «ikke kan si at gapet ikke ligger i modellen». NV:62 sier også «ikke i rangeringen». En jury som leser begge,
   ser at vi stiller oss gunstigere i det ene svaret enn i det andre. Forslag: i JURYSVAR:23, bytt
   «så gapet ligger i presedensregelen og terskelen, ikke i modellen» med JS:57-ordlyden: «… men modellen deres alene med
   deres terskel gir 0,538, så vi kan bare si at vår rangering er best». JS:15 sier det samme som JURYSVAR i en litt
   mildere form («gapet ligger i presedensregelen og terskelen») og bør få samme retting. NV:62 kan få «i F1, ikke i PR-AUC».
5. **Rettferdighet i motsatt retning står bare i NV.** NV:71 sier at hybridløsningens egen test (2025–26) inneholder 2026,
   så utformingen kan være valgt med 2026 synlig. Det betyr at også hybridens tall på test 2026 er optimistiske.
   JURYSVAR:23 og JS:57 nevner det ikke, så det ser ut som om bare vi har sett test. Forslag: én bisetning i JS:57,
   for eksempel «hybridløsningens forfattere hadde 2026 i sin egen test, så tallene deres er like optimistiske som våre
   etter frysen». Ingen tall endres.
6. **JS:81** «ikke fra NBIM og ikke et offentlig repo». Det dekkes av #2542, som skal stryke «og ikke et offentlig repo».
   Ellers er alt i orden: setningen sier ikke at løsningen er fra NBIM.
7. Mindre ting: **JS:57** nevner «hybriden på dens egen splitt 0,523» uten å si at den splitten er trent til og med 2023 mot vår til og med 2024.
   Dommen sier at det er merket per rad i kildetabellen, så det er ikke galt. Men tallet sammenlignes direkte med 0,545.
   Forslag: «(trent til og med 2023)».

## Det som er i orden
- Tallene er de samme i JURYSVAR, JS og NV: 0,515, 0,545, +0,069 [+0,007; +0,133], PR-AUC 0,525/0,318/0,413 og 0,538.
- Alle sammenligninger bruker vår måler, vår test 2026 og samme fasit (dom :18).
- Kildefilene har overskrift og merknad om at løsningen ikke er fra NBIM (sammenligning :1 og :3, dom :1 og :27).

## Prioritet for smeden (alt er tekst, ingen tall endres)
1. NV:1 (ett ord).  2. JURYSVAR:23 og JS:15 om gapet (motsigelse).  3. «utenom landsbyen» blir «av andre i teamet» på 6 steder.
4. Merknad om filnavnet ved første peker.  5. Bisetning om at 2026 var synlig for hybridløsningen (JS:57).
Kjør tallvakt og frys-fasit etterpå (#2535).
