# Case 1 jurylesing (#2544): JURY, BEGRENSNINGER, ERLIG_EVALUERING og demo_utskrift mot dommene #2529/#2527

Lest som en jury, ingen filer endret. Ingen setning i de fire filene sier at V2 eller hybriden er levert, og ingen kaller hybriden NBIMs (de nevner ikke V2 eller hybriden i det hele tatt). Funnene er derfor hull, motsigelser mellom filene og ord juryen ikke kjenner. Viktigst først.

## A. Motsigelser juryen kan se
1. **ERLIG_EVALUERING.md:32 og :38 – «støygrensen 0,02»** strider mot dommen #2529. Der står at forskjeller under ~0,02 ikke kan tolkes. En jury leser det som at +0,040 (V2 i README) er ekte, mens README og dommen sier at V2 er innenfor støyen (KI [−0,007; +0,095]).
   Forslag til :32: «Flyttes én sak, endres F1 med omtrent ±0,01, så forskjeller under ~0,02 er ren én-sak-støy. Også større forskjeller kan være støy: V2 er +0,040 over den frosne agenten, men KI-et er [−0,007; +0,095] (`JURY_SPORSMAL.md` sp. 19). Les forskjeller mot KI-et, ikke mot 0,02.» I :38 bytter du «under støygrensen på 0,02» med «under 0,02, altså én-sak-støy».
2. **JURY.md:40** sier at båndet er «låst på val 2025 og ikke valgt på nytt». **ERLIG_EVALUERING.md:49** sier at båndet ble valgt fra en tabell på test 2026 og bare sjekket på val, og at énsideren derfor ikke skal si «låst på val».
   Forslag til JURY.md:40: «Bare beskrivende: båndet [0,15; 0,85) er valgt fra et fast rutenett på test-tabellen og sjekket på val 2025 (7,5 % val, 7,9 % test, `kilder/c1_menneske_terskel.md`). Det er altså ikke uavhengig av test.»
3. **demo_utskrift.txt:4** sier «FRYSVAKT: ikke frosset ennå (<repo>/state/c1_frys.json finnes ikke)». Alle andre filer kaller agenten frossen. Demoen er kjørt 15:28, før frysen 16:00.
   Forslag: kjør demoen på nytt etter frysen (generalprøven #2493 kan levere den), eller rett linja til «# frys: demoen er kjørt 15:28, før modellfrysen 16:00; svarfila er byte-lik den frosne (`kilder/c1_motstand_etter_frys.md`)». Uansett skal den lokale stien ut.
4. **JURY.md:56–61 («Hvorfor vi ikke jaget testtallet»)** nevner ikke V2-avgjørelsen. Det er det sterkeste eksempelet på regelen, og juryen har nettopp sett det i README.
   Forslag til et nytt punkt etter :59: «**V2 (rullende valg, 0,516 på test):** målt på test etter frysen, +0,040 over den frosne agenten med KI [−0,007; +0,095], og ikke kjørt i pakka etter frysen. Kravene var skrevet ned før målingen, og V2 klarte ikke to av dem. Den frosne agenten står (`JURY_SPORSMAL.md` sp. 19).» Hybriden nevnes bare som «teamets egen hybridløsning, ikke fra NBIM», hvis den nevnes i det hele tatt.
5. **ERLIG_EVALUERING.md:4 og :9** viser til `kilder/c1_ablasjon_v2.md` og `dommer_ablasjon_v2.md`. Etter README kan juryen tro at «v2» i filnavnet er V2-varianten.
   Forslag: legg til «(v2 = andre kjøring av ablasjonen, ikke V2-varianten i README)» etter [A].
6. **Ulike tidspunkt for samme kaldstart:** README:11 sier «kald kopi 05.11 kl. 12.54», BEGRENSNINGER.md:3 sier «sist kontrollert av kontrollagenten kl. 13.37», og JURY.md:73 sier bare «siste kaldstart 05.11». Tallene er like (188/183), men tidspunktene spriker.
   Forslag: bruk ett tidspunkt overalt, helst den siste kaldstarten etter frysen.
7. **ERLIG_EVALUERING.md:46** sier «Merk fire ting», men lista har fem punkter (:47–51). **:47** sier «Én av de 15», mens resten av pakka bruker 16 instrukser.
   Forslag: «Merk fem ting», og «Én av de 16».
8. **ERLIG_EVALUERING.md:70** sier «`bash arbeid/hack/c1/kaldstart.sh` (31–52 s)», mens README:30–42 sier `kjor.sh` og 29–52 s. Det ser ut som to ulike veier til hovedtallet.
   Forslag: legg til «(gammel kommando; i dag: `kjor.sh`, se README)» eller sett inn en kort merknad i §6-lista om at kommandoen er byttet.
9. **ERLIG_EVALUERING.md:73** sier «les tallet som «rundt 0,5»». Det pynter tallet: 0,476 ligger under målet, og JURY.md:5 sier det rett ut. Teksten står ordrett fra kl. 13.06, men juryen leser den likevel.
   Forslag: legg til et sjette punkt i §6-lista: «"rundt 0,5" i teksten under er for rundt: les 0,476 (0,36–0,59), under målet 0,5.»
10. **ERLIG_EVALUERING.md:56** sier «og det er de, fordi NBIM publiserer stemmene løpende». Det står ordrett, og :51 tar forbehold, men forbeholdet står fem linjer over. Juryen som leser :56 alene, får en påstand uten kilde.
    Forslag: sett «[se forbehold § 6, siste punkt]» rett etter setningen.

## B. Ord juryen ikke kjenner
11. **demo_utskrift.txt:1** sier «smed2 #2044-modell». «smed2» er et internt rollenavn. Forslag: «modell miks h2».
12. **demo_utskrift.txt:2 og :29** sier «(sak 2132)». Forslag: stryk, eller skriv «(kalibreringen, `kilder/...`)».
13. **demo_utskrift.txt:4** inneholder `<repo>/...`, både en lokal sti og ordet landsby (se punkt 3).
14. **JURY.md:77** sier «(forsøk 2363)» og «valgt bort av dommeren (sak 2366)». Forslag: «Å vekte nyeste historikk tyngst er prøvd og valgt bort av kontrollagenten, fordi …» uten numrene.
15. **ERLIG_EVALUERING.md:41** sier «uten landsbystier». Forslag: «uten stier til utviklingsmappa».
16. **«Dommeren»** står i ERLIG_EVALUERING.md:19, :28 og :70 og i JURY.md:77. README forklarer «dommer» som kontrollagent, men ERLIG og JURY bruker «kontrollagenten» andre steder. Forslag: bruk «kontrollagenten» overalt.
17. **ERLIG_EVALUERING.md:43** viser `/tmp/c1_kald_2395` og `arbeid/oppgave_2395/`, interne oppgavenumre. Det er greit som sti, men teksten bør si én gang at stiene bare finnes i repoet. Det gjør den allerede delvis med «(i repoet, ikke i zipen)». Lav prioritet.

## C. Tall mot README: stemmer
Sjekket mot README: 0,476 [0,36; 0,59], TP 30 FP 38 FN 28, P 0,441, R 0,517, 188/1578 og 183/1539 (11,9 %), 127+60+1 = 188, 0,482 [0,375; 0,580], b2 0,365, golvet 0,415, val 0,520 (MOT) og 0,522 (avvik, bekreftet 0,5217 i `kilder/c1_val_kaldstart.md:24`, så det er ikke 0,522-feilen fra dommen), accuracy 95,7/96,2. Bånd-tabellen i JURY.md:44–47 summerer riktig (58 MOT og 38 falske per rad). Demoen viser 0.4762 og 183/1539. **Ingen tallavvik.**

Liten merknad: i demo_utskrift.txt:9–10 viser treffet to ulike sitater (GVG 5.2 og NBIM 5.2.1 om årsrapporten) på «Transact Other Business». En jury kan lure på hvilket som gjelder. Det er dekket av svakheten med sitatet (BEGRENSNINGER pkt. 5), så ingen endring trengs.

## Prioritet for smed4 (#2546)
Punkt 1–4 bør inn før sluttsjekken kl. 18. Punkt 11–14 er raske søk-og-erstatt. Punkt 3 og 11–13 krever at demo_utskrift kjøres på nytt eller redigeres, men demo_utskrift.txt står ikke i `state/c1_frys.json`, så den kan endres uten å bryte frysen.
