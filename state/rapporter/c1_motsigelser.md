# Case 1: motsigelser BYTT/STÅR i jurytekstene (#2619, 17:20)

Lest: c1/leveranse/{README,ERLIG_EVALUERING,JURY_SPORSMAL,kravrespons}.md og levering/{README,JURY_README,JURYSVAR,JURY_SPORSMAL}.md. Pakken er ikke redigert.

Referansetall (fra rapportene, test 2026, v3 `--score mot`):
- **frossen #2044 miks h2:** TP 30 FP 38 FN 28, P 0,441 R 0,517, **F1 0,476**, KI [0,36; 0,59], mot b2 +0,11 [0,01; 0,22], avvik (SCORE) 0,4817, h1 0,415 (−0,061).
- **repo4:** TP 32 FP 35 FN 26, P 0,478 R 0,552, **F1 0,512**, KI [0,40; 0,62], avvik 0,5294. h1 og b2-differanse er ikke målt for repo4 (så langt jeg fant).

Hovedproblem: tekstene er halvveis byttet. Tallene er stort sett repo4 (0,512), men mange setninger sier at det er **den frosne modellen** som leveres, og flere sidetall er fortsatt frossen-tall koblet til 0,512.

## A. Motsigelser uansett utfall (rettes både ved BYTT og STÅR)

| fil:linje | står nå | problem |
|---|---|---|
| c1/leveranse/README.md:11 vs :8, :12 | «Vi leverer den frosne agenten (V1)» + hovedtall 0,512 + «BYTT kl. 17:02» | sier både frossen og repo4 leveres |
| c1/leveranse/README.md:46–51 | utskrift `F1 0.5120` og `SCORE 0.481752` | 0,5120 er repo4, 0,481752 er frossen-avvik; repo4-avvik er 0,5294 (levering/README.md:6) |
| c1/leveranse/README.md:15 | «avvik 0,529 … (frossen 0,482)» | ok ved BYTT, men samme fil viser SCORE 0.481752 som om det var leverte |
| levering/JURY_README.md:27 | «SCORE … sidetall, 0.481752» | frossen-avvik; levering/README.md:6 sier 0,5294 |
| levering/README.md:69 vs :38/:83 | «164 av 1578 til menneske» vs «161 av 1539 (10,5 %)», :30 i JURYSVAR «10,4 %», c1/README:15 «101 usikre» | tre ulike rutingtall; si hvilken nevner/modell hvert gjelder |
| JURYSVAR.md:48 | «test 2026 0,476 [0,40; 0,62]» | frossen-tall med repo4-KI |
| levering/JURY_SPORSMAL.md:116 | «0,476 mot 0,520» | 0,476 er frossen; val 2025 står som 0,530 i JURYSVAR:48 og ERLIG:34 |

## B. Ved BYTT (repo4 leveres, 0,512): disse må endres

| fil:linje | står nå | foreslått rettelse |
|---|---|---|
| c1/leveranse/README.md:11 | «Vi leverer den frosne agenten (V1) med vilje. … V2 − V1 +0,040» | «Vi leverer repo4 (frossen + fire historikktrekk), byttet etter regelen i § 7. V2 (0,516) er ikke levert; V2 var +0,040 over den *frosne* (0,476), ikke over repo4.» |
| c1/leveranse/README.md:51 | `SCORE 0.481752` | `SCORE 0.529412` (kjør på nytt og lim inn ekte utskrift) |
| c1/leveranse/README.md:77 | «`kjor_agent.py` (… den frosne modellen «miks h2»)» | «… repo4 (`modell_repo4.py`, miks h2 + 4 repotrekk)» |
| c1/leveranse/ERLIG_EVALUERING.md:1, :3 | «hva den frosne modellen bygger på», «Modell: den frosne «miks h2»» | «repo4 (frossen miks h2 + fire historikktrekk, byttet 17:03)» |
| ERLIG_EVALUERING.md:29, :76 | «faller fra 0,512 til 0,415» | h1 er målt på frossen: «frossen faller fra 0,476 til 0,415 (−0,061); ikke målt for repo4» – eller mål repo4 med `--hist 1` |
| ERLIG_EVALUERING.md:32 | «V2 er +0,040 over den frosne agenten» | legg til «(V2 0,516 er +0,004 over levert repo4)» |
| ERLIG_EVALUERING.md:34 | «Ingen variant er valgt på test» | strid med byttet: regelen brukte test 2026 som ett av tre år, og ble skrevet etter at ett år var kjent. Skriv: «Repo4 er valgt på tre rullende testår der 2026 inngår; se forbeholdet i § 7.» |
| ERLIG_EVALUERING.md:38 | «Utgangspunktet reproduserer hovedtallet eksakt (TP 32 FP 35 FN 26)» | lt/ny/mt-forsøket ble kjørt på frossen (TP 30 FP 38 FN 28, 0,476). Rett til frossen-tallene og si «på den frosne» |
| ERLIG_EVALUERING.md:71 | «agenten, maskin alene (miks h2) … 0,512» | «(repo4)» |
| ERLIG_EVALUERING.md:76 vs JURYSVAR.md:23, c1/JURY_SPORSMAL.md:15, :73 | b2-margin «+0,15 [0,04; 0,25]» vs «+0,11 [0,01; 0,22]» | +0,11 er frossen. Bruk ett tall overalt: repo4-tallet hvis det er målt (parret bootstrap), ellers «+0,11 for frossen, repo4 ikke målt» |
| c1/leveranse/JURY_SPORSMAL.md:4 | «den frosne modellen (miks …)» | «repo4 (frossen + fire historikktrekk)» |
| c1/leveranse/JURY_SPORSMAL.md:15 | «95 % KI er [0,36; 0,59] … [0,37; 0,59]» | «[0,40; 0,62]» (repo4) |
| c1/leveranse/JURY_SPORSMAL.md:61 | «0,4762 for 2026 … Tallet for 2026 er likt hovedtallet», «snitt 0,482» | «Repo4 rullende: 0,5057 / 0,5309 / 0,5120, snitt 0,516; 2026 er likt hovedtallet. Frossen: 0,4545 / 0,5143 / 0,4762.» |
| c1/leveranse/JURY_SPORSMAL.md:77 | «Uten den er F1 på MOT 0,415, altså −0,061» | «for den frosne (0,476 → 0,415); ikke målt for repo4» |
| c1/leveranse/JURY_SPORSMAL.md:81 | «hovedtallet 0,476 er det eneste som er valgt uten å se test» | rett: hovedtallet er nå 0,512 (repo4), valgt etter tre-års-regelen med 2026 inkludert. Svaret om V2 må skrives om, ellers sier det rett ut at vi leverer 0,476 |
| c1/leveranse/JURY_SPORSMAL.md:83 | «I drift i dag setter vi den frosne agenten. Bare den har kaldstart …» | «I drift setter vi repo4; kaldstart, lekkasjesjekk og ruting er kjørt på nytt for repo4 (#2595/#2596)» – bare hvis dommeren har sagt grønn |
| c1/leveranse/kravrespons.md:7 | «95 %-intervall [0,36; 0,59]», «Modell og grense er valgt på 2025 og kjørt én gang på 2026» | «[0,40; 0,62]»; «valgt etter tre rullende testår (2024–26), se forbehold» |
| levering/README.md:105 | «kjørte den frosne agenten på nytt … Modellen er ikke endret», tabell 0,512 (:109–112) | robusthetstesten (#2144) er på frossen, hvor vanlig kjøring var 0,476. Enten rett 0,512 → 0,476 og si «frossen», eller kjør `robusthet_frossen.py` på repo4 |
| levering/JURY_README.md:68 | «`arbeid/oppgave_2044/train.py` | den frosne modellen (miks h2)» | legg til rad for `levering/modell_repo4.py` som levert modell |
| levering/JURY_README.md:27 | `0.481752` | `0.529412` |
| levering/JURY_SPORSMAL.md:37, :93–:111 | injeksjon/sitat «målt på den frosne modellen #2044» | legg til «(frossen; ikke målt på nytt for repo4)» eller mål |
| levering/JURY_SPORSMAL.md:65 | «0,500 [0,38; 0,61] mot 0,512» | 0,500 (A+B, TP 31) er sammenlignet med frossen (0,476) i rapporten; mot repo4 er det −0,012. Si hvilken |
| levering/JURY_SPORSMAL.md:70 | «avvik fra 0,482 til 0,386 … MOT fra 0,512 til 0,415» | frossen-tall: «0,476 til 0,415» |
| levering/JURY_SPORSMAL.md:116, JURYSVAR.md:48 | «0,476» som 2026-tall | «0,512» (repo4) eller merk «frossen» |

## C. Ved STÅR (frossen leveres, 0,476): disse må endres

Alt som sier 0,512 / [0,40; 0,62] / TP 32 FP 35 FN 26 / P 0,478 R 0,552 / avvik 0,5294 / repo4 levert.

| fil:linje | foreslått rettelse |
|---|---|
| c1/leveranse/README.md:8, :29, :46, :50, :62 | hovedtall **0,476**, KI [0,36; 0,59], TP 30 FP 38 FN 28, P 0,441 R 0,517; målerlinja `F1 0.4762` |
| c1/leveranse/README.md:12 | «… kontrollagenten dømte BYTT kl. 17:02 på vilkår om grønn pakke innen 18:45» → legg til «Vilkåret ble ikke oppfylt; dom 18:45 STÅR, frossen leveres.» |
| c1/leveranse/README.md:15 | «avvik 0,529 … (frossen 0,482)» → «avvik 0,482» |
| ERLIG_EVALUERING.md:6, :29, :34, :53, :71, :76 | 0,512 → 0,476; «under målet 0,5» stemmer da for test (:34 og :53 sier «0,512 … under målet 0,5», som er feil også i dag: 0,512 > 0,5) |
| ERLIG_EVALUERING.md:76 | b2-margin +0,15 → +0,11 [0,01; 0,22] |
| ERLIG_EVALUERING.md:86 | repo4-raden «ja, BYTT (dom #2570), levert» → «ja etter regelen, men ikke levert (pakken ble ikke grønn innen 18:45)»; :85 «levert til 17:03, eldre» → «levert» |
| c1/leveranse/JURY_SPORSMAL.md:6 | «Hvorfor leverer dere bare 0,512?» → 0,476 |
| c1/leveranse/kravrespons.md:10 | «0,512 ligger under målet» → «0,476 ligger under målet» |
| levering/README.md:3, :6, :42, :47, :49, :69, :77, :81–:83, :109–:112 | fjern «frosset modell repo4 … byttet 17:03», hovedtall 0,4762, avvik 0,4817 som sidetall, rutingtabellen fra frossen-kjøring (`kjor_agent_real_*` før bytte) |
| levering/JURYSVAR.md:5, :11, :19, :30, :32, :36–:38 | 0,512 → 0,476; «levert modell repo4» → «frossen #2044»; nøyaktighet regnes på nytt fra TP 30 FP 38 FN 28 (1539 − 66 feil = 95,7 %, ikke 96,0 %) |
| levering/JURY_README.md:7, :24 | `0.512000` → `0.476190` |
| levering/JURY_SPORSMAL.md:13, :47, :65, :70, :73, :80, :112, :115 | 0,512 → 0,476; P/R; «32 av 58» → «30 av 58»; F1 med menneske 0,792 må hentes fra frossen-kjøringen |
| alle | demo_utskrift.txt og FROSNE_SHA256 må komme fra STÅR-reserven (#2598), ikke håndrettes |

## D. Feil som gjelder i dag uansett
- ERLIG_EVALUERING.md:34 og :53 sier «0,512 … under målet 0,5». 0,512 er over 0,5. Ved BYTT: «så vidt over målet, innenfor KI». Ved STÅR stemmer «under» med 0,476.
- kravrespons.md:10 har samme feil («0,512 ligger under målet vårt på 0,5»).

## Anbefaling
Ved BYTT trengs ca. 25 setningsrettelser, de fleste er «frossen» → «repo4» og tre sidetall målt bare på frossen (h1 0,415, b2 +0,11, robusthet/injeksjon). Billigst og ærligst er å merke dem «målt på frossen, ikke på repo4» i stedet for å måle på nytt før 19:00. Ved STÅR bør smed3 bruke STÅR-reserven hel, og sjekke reserven mot listen i C. Til slutt `grep -n "0,512\|0,476\|frosne\|repo4"` over de åtte filene.
