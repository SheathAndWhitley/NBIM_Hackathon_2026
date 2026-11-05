# Case 1: ferdige rettelser for de 5 jurypunktene (#2637, BYTT og STÅR)

Kilde for funnene: `c1_juryles_staar.md` (#2634). Tall bare fra `c1_etterfrys.md` 17:18 (F1 0,512, TP 32 FP 35 FN 26, SCORE 0.529412 i kald kopi) og tallene som alt står i pakken. Ingen nye tall. Jeg har ikke rørt noen fil. smed2 limer inn.
Stier er relative til `arbeid/hack/`. B = BYTT (`c1/leveranse/` + `levering/`), S = STÅR (`c1/reserve_staar/`).

**To feil i BYTT fant jeg mens jeg lette (bør limes inn først):** B-README sier fortsatt «Vi leverer den frosne agenten (V1)» (1a), og B-ERLIG § 3 sier at 0,512 «ligger under» målet 0,5 (2b). Begge er usanne i BYTT.

## 1. V1 er ikke det samme som den frosne
**1a. Fil: `c1/leveranse/README.md:11` (B). Gjelder også `levering/README.md` hvis setningen står der (grep «(V1)»).**
Gammel: `> Vi leverer den frosne agenten (V1) med vilje. Varianten V2 gir 0,516 på test, men ble målt på test etter frysen og er innenfor støyen (V2 − V1 +0,040, KI [−0,007; +0,095]); se `JURY_SPORSMAL.md` sp. 19.`
Ny: `> Vi leverer repo4, ikke V2. V2 er en tidligere variant (0,516 på test), men den ble målt på test etter frysen uten en regel satt før måling, og avstanden til V1 (en eldre variant, ikke den frosne) er innenfor støyen (+0,040, KI [−0,007; +0,095]); se `JURY_SPORSMAL.md` sp. 19.`
(behold `<!-- tallvakt: ignorer: V2, ikke hovedtall -->` bak)

**1b. Fil: `c1/reserve_staar/README.md:11` (S).**
Gammel: `> Vi leverer den frosne agenten (V1) med vilje. Varianten V2 gir 0,516 på test, men ble målt på test etter frysen og er innenfor støyen (V2 − V1 +0,040, KI [−0,007; +0,095]); se `JURY_SPORSMAL.md` sp. 19.`
Ny: `> Vi leverer den frosne agenten med vilje. V1 og V2 er eldre varianter, ikke den frosne (V1-raden i `ERLIG_EVALUERING.md` § 7 er derfor et annet tall enn «frossen»). V2 gir 0,516 på test, men ble målt på test etter frysen og er innenfor støyen (V2 − V1 +0,040, KI [−0,007; +0,095]); se `JURY_SPORSMAL.md` sp. 19.`
(behold tallvakt-kommentaren bak)

## 2. «Valgt på test» motsier § 3
**2a. Fil: `c1/reserve_staar/ERLIG_EVALUERING.md:34` (S).**
Gammel: `- Ingen variant er valgt på test [A]. Målet var F1 0,5. Hovedtallet på test ligger under det (0,476), mens val ligger over (0,520) [S].`
Ny: `- Ingen modellvariant, C eller grense er valgt på test [A]; det eneste som er valgt på test, er rutingsbåndet [0,15; 0,85) for hva som går til menneske (§ 6 og `JURY_SPORSMAL.md` sp. 16). Målet var F1 0,5. Hovedtallet på test ligger under det (0,476), mens val ligger over (0,520) [S].`

**2b. Fil: `c1/leveranse/ERLIG_EVALUERING.md:34` (B).**
Gammel: `- Ingen variant er valgt på test [A]. Målet var F1 0,5. Hovedtallet på test ligger under det (0,512), mens val ligger over (0,530) [S].`
Ny: `- Ingen modellvariant, C eller grense er valgt på test [A]; det eneste som er valgt på test, er rutingsbåndet [0,15; 0,85) for hva som går til menneske (§ 6 og `JURY_SPORSMAL.md` sp. 16). Målet var F1 0,5. Hovedtallet på test (0,512) ligger like over det, og val ligger på 0,530 [S]. Den frosne modellen (0,476) lå under målet.`
(Båndet står i § 6, linje 59; sjekket.)

## 3. For mange høyere tall uten forklaring
**3a. Fil: `c1/reserve_staar/README.md`, ny linje rett etter linje 12 (S), inne i hovedboksen.**
Gammel: (ingen)
Ny: `> **Hvorfor vi leverer et lavere tall enn flere andre i pakken:** alle høyere tall (V2 0,516, NBIM-hybrid 0,545, 0,529, repo4 0,512) er enten målt på test etter frysen uten en regel satt på forhånd, eller faller under den frosne på 2024. Repo4 er det eneste som besto regelen, og den ble ikke levert fordi den ikke var reprodusert fra kald start før fristen.`
(tallvakt-kommentar: `<!-- tallvakt: ignorer: sidetall, ikke hovedtall -->`)

**3b. Fil: `c1/reserve_staar/MUNTLIG.md:13` (S).**
Gammel: `KI er 0,36 til 0,59. Repo4 ga 0,512.`
Ny: `KI er 0,36 til 0,59. Repo4 ga 0,512, men det tallet er fra 2026, året repo4 ble funnet på, så det er ikke et friskt testår for den; se neste punkt.`

**3c. Fil: `c1/leveranse/README.md`, ny linje rett etter linje 12 (B).**
Gammel: (ingen)
Ny: `> **Om de andre tallene i pakken:** V2 0,516, NBIM-hybrid 0,545 og 0,529 er målt på test etter frysen uten en regel satt på forhånd, og står bare som sidetall. Repo4 er levert fordi den besto en regel satt før måling på 2024 og 2025, ikke fordi 0,512 er høyest.`
(tallvakt-kommentar som 3a)

## 4. Uforklart internspråk
**4a. Fil: `c1/reserve_staar/README.md:12` (S).**
Gammel: `og kontrollagenten dømte BYTT kl. 17:02 på vilkår om grønn pakke innen 18:45. Kandidaten besto regelen, men pakken med repo4 ble ikke grønn i tide, så den frosne agenten står med 0,476`
Ny: `og kontrollagenten (en egen agent som ikke målte kandidatene) dømte BYTT kl. 17:02 på vilkår om at hele pakken med repo4 kjørte feilfritt fra kald start, med samme tall, innen 18:45. Kandidaten besto regelen, men pakken med repo4 var ikke reprodusert fra kald start før fristen, så den frosne agenten står med 0,476`

**4b. Fil: `c1/leveranse/README.md:12` (B).**
Gammel: `og kontrollagenten dømte BYTT kl. 17:02 på vilkår om grønn pakke innen 18:45 (se`
Ny: `og kontrollagenten (en egen agent som ikke målte kandidatene) dømte BYTT kl. 17:02 på vilkår om at hele pakken med repo4 kjørte feilfritt fra kald start, med samme tall, innen 18:45. Det gjorde den (se`

**4c. Fil: `c1/reserve_staar/ERLIG_EVALUERING.md:106` og `c1/reserve_staar/JURY_SPORSMAL.md:87` (S), samme setning i begge (i ERLIG står «Den ble likevel», i JURY_SPORSMAL «Den er likevel»).**
Gammel: `… ikke levert, fordi pakken med repo4 ikke var grønn før tekststoppen.`
Ny: `… ikke levert, fordi pakken med repo4 ikke var reprodusert fra kald start (samme tall, uten feil) før vi måtte låse tekstene kl. 19.`

**4d. Fil: `c1/reserve_staar/ERLIG_EVALUERING.md:86` (S), siste celle i repo4-raden.**
Gammel: `besto regelen, ikke levert (pakken ikke grønn i tide)`
Ny: `besto regelen, ikke levert (ikke reprodusert fra kald start før fristen)`

**4e. Fil: `c1/reserve_staar/MUNTLIG.md:13` (S).**
Gammel: `Repo4 besto regelen, men pakken med repo4 ble ikke grønn i tide, så den frosne agenten står.`
Ny: `Repo4 besto regelen, men vi rakk ikke å kjøre hele pakken med repo4 feilfritt fra kald start før fristen, så den frosne agenten står.`

**4f. Fil: `c1/reserve_staar/MUNTLIG.md:9` og `c1/leveranse/MUNTLIG.md:9` (begge).**
Gammel: `En kontrollagent som ikke målte selv, avgjør byttet.`
Ny: `En kontrollagent som ikke målte kandidatene, avgjør byttet. Hovedtallet har den målt på nytt fra kald start.`

**4g. Fil: `ERLIG_EVALUERING.md:81` i både `c1/leveranse/` og `c1/reserve_staar/` (begge).**
Gammel: `Benk A (samme måler på alle, ferdige svarfiler per år):`
Ny: `Sammenligning (samme måler på alle kandidater, én ferdig svarfil per kandidat og testår):`

**4h. Fil: `README.md:77` i begge (begge).**
Gammel: `den frosne modellen «miks h2»`
Ny B: `modellen (internt kalt repo4: den frosne «miks h2» pluss fire historikktrekk)` — sjekk først at setningen i B faktisk gjelder repo4-kjøringen; gjelder den den frosne, behold som S.
Ny S: `den frosne modellen (internt kalt «miks h2»)`

Navnet «repo4» står i mange setninger. Ikke bytt det overalt, det tar for lang tid. Det holder at README forklarer det første gang (står alt: «repo4 (frossen + fire historikktrekk)»).

## 5. MOT-F1 og gulvet øverst, SCORE-linja, sesong-historikken
**5a. Fil: `c1/reserve_staar/README.md:9` (S).**
Gammel: `Følg styret gir 0.`
Ny: `Følg styret har 96,2 % accuracy, men predikerer aldri MOT (TP 0), så F1 på MOT er 0; det er gulvet. MOT er positiv klasse fordi de 58 av 1539 sakene der NBIM stemmer mot styret, er de som krever arbeid.`

**5b. Fil: `c1/leveranse/README.md:9` og `levering/README.md` hvis setningen står der (B).** Samme gamle og nye setning som 5a.

**5c. Fil: `c1/reserve_staar/README.md`, ny linje i hovedboksen etter linje 10 (S).**
Gammel: (ingen)
Ny: `> **Største forbehold:** omtrent 0,06 av F1 kommer fra NBIMs egne tidligere stemmer i samme sesong. Uten den historikken er F1 0,415 [0,30; 0,53], bare +0,05 over den beste enkle regelen (0,365). Det er ærlig bare om NBIM har sine tidligere stemmer løpende (`ERLIG_EVALUERING.md` § 2, `JURY_SPORSMAL.md` sp. 18).`

**5d. Fil: `c1/leveranse/README.md`, samme plass (B).**
Gammel: (ingen)
Ny: `> **Største forbehold:** omtrent 0,06 av F1 kommer fra NBIMs egne tidligere stemmer i samme sesong. Uten den historikken er F1 0,415 [0,30; 0,53] (målt på den frosne modellen), bare +0,05 over den beste enkle regelen (0,365). Det er ærlig bare om NBIM har sine tidligere stemmer løpende (`ERLIG_EVALUERING.md` § 2, `JURY_SPORSMAL.md` sp. 18).`
(I B-ERLIG linje 76 står «uten den: 0,512 → 0,415». 0,415 er målt på den frosne, så gapet for repo4 er ikke målt. Skriv ikke «≈0,10» uten måling. Forbeholdet står i § 2; sjekket.)

**5e. SCORE-linja. Fil: `c1/reserve_staar/README.md:46` (S).**
Gammel: `**Hovedtall i utskriften: linja `MOT mot styret … F1 0.4762`.** Siste linje, `SCORE 0.481752`, er avvik fra styret (sidetall), ikke hovedtallet.`
Ny: `**Les bare linja `MOT mot styret … F1 0.4762`; det er hovedtallet.** Linja `SCORE 0.481752` rett under er IKKE hovedtallet: den er F1 på alle avvik fra styret, AVSTÅ medregnet (66 saker), og står der bare fordi rundens måler krever den.`

**5f. SCORE-linja. Fil: `c1/leveranse/README.md:46` (B).**
Gammel: `**Hovedtall i utskriften: linja `MOT mot styret … F1 0.5120`.** Siste linje, `SCORE 0.481752`, er avvik fra styret (sidetall), ikke hovedtallet.`
Ny: `**Les bare linja `MOT mot styret … F1 0.5120`; det er hovedtallet.** Linja `SCORE 0.529412` er IKKE hovedtallet: den er F1 på alle avvik fra styret, AVSTÅ medregnet (66 saker), og står der bare fordi rundens måler krever den.`
**Feil i BYTT:** utdraget i `c1/leveranse/README.md:48–52` viser `SCORE 0.481752` og en avvik-linje med TP 33 FP 38 FN 33. Dette er den frosne kjøringen. Den kalde repo4-kjøringen (`c1_etterfrys.md`) skriver `SCORE 0.529412`. Gammel: `SCORE 0.481752`. Ny: `SCORE 0.529412`. Avvik-linja (`  avvik: TP 33 FP 38 …`) slettes fra utdraget. Repo4-tallene for den linja finnes ikke i etterfrys, så vi skriver ikke inn nye. Samme feil i `levering/README.md:43` og `:47` og `levering/JURY_README.md:27` (`0.481752`), som bør bli `0.529412`. **Før du limer inn:** se etter i den kalde utskriften (`/tmp/c1_etterfrys_logg.*/3_*`) at «SCORE 0.529412» er siste SCORE-linje. Står begge tallene der, er 0.481752 et annet sidetall. Da skal den nye setningen nevne begge.

## Rekkefølge for smed2
1a og 2b (usanne i BYTT), så 5f-SCORE og 5a/5b, så 4a/4b/4f, så resten. Kjør tallvakt etter innliming: `bash arbeid/verktoy/c1_etterfrys.sh`. Alle nye tall finnes alt i pakken eller i etterfrys.

**SCORE-sjekk gjort:** den kalde repo4-kjøringen 17:18 (`/tmp/c1_etterfrys_logg.Dzr9/3_fremmed.txt:18-21`) skriver bare `SCORE 0.529412`. `0.481752` står bare i eldre logger av den frosne (7Qol, zzC8). 5f gjelder. Avvik-linja i utdraget i B-README skal byttes, ikke slettes. Linja er ordrett fra samme kjøring, så den gir ingen nye tall:
Gammel: `  avvik: TP 33 FP 38 FN 33  P 0.4648  R 0.5000  F1 0.4818  PR-AUC 0.5245`
Ny: `  avvik: TP 36 FP 34 FN 30  P 0.5143  R 0.5455  F1 0.5294  PR-AUC 0.5368`
(Dette erstatter «avvik-linja slettes» i 5f.) Merk at den kalde utskriften ikke har noen egen linje som begynner med `MOT mot styret:`. Hovedtallet kommer som `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000`. smed2 må se i `KJOR.sh`-utskriften i jury-zipen om `MOT mot styret: TP 32 …`-linja finnes der. Finnes den ikke, skal 5f si «linja `HOVEDTALL F1 MOT mot styret … 0.512000`».
