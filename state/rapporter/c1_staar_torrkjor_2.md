# Case 1 (#2681): STÅR-kjeden tørrkjørt i fersk kald kopi etter ordsjekk-rettelsene: GRØNN, men byggeskriptet måtte rettes

Dato 05.11 kl. 17:45–18:10, smed3. Kald kopi `/tmp/staar_torr_2681` (1,0 GB: hack uten arkiv, oppgave-mappene kjeden bruker, verktoy/*.py, kandidatens pyproject/uv.lock, c1_frys.json, real_votes). Leveranse/ og levering/ i landsbyen er ikke rørt. Kopien er slettet etter kjøringen; logg per steg står i `/tmp/staar_2681_logg/`, zip i `/tmp/jurypakke_staar_2681.zip`.

## Akseptkrav
| krav | resultat |
|---|---|
| tallvakt 0 avvik | **GRØNN**: 22 filer, 177 påstander, 0 avvik (`c1_tallvakt.py --rot KOPI`, etter cp av 5 STÅR-filer + staar_rest.py) |
| ordsjekk 0 treff | **0 treff på BYTT-ord** (grønn/tallvakt/benk/«0,512 til 0,415»/repo4 uforklart) i de fem reserve_staar-filene og i kopiens leveranse/ og GITHUB_README_UTKAST. Skriptet som helhet gir 37 treff, alle av de slagene #2654 merket som riktige i STÅR («[0,36; 0,59]», «under målet», «valgt på test», «Den frosne agenten står») pluss `<!-- tallvakt`-kommentarer; «0 treff» kan ikke oppnås med skriptet slik det er skrevet. Eneste BYTT-ord-treff: `levering/README.md:45` («TALLVAKT GRØNN», BYTT-fila, smed2 sin liste #2639) |
| zip-test 0.476190 | **GRØNN**: pakk_jury 146 filer (50 s), test_jury_zip FRYSVAKT/TALLVAKT/ZIPTEST GRØNN, HOVEDTALL 0.476190, TP 30 FP 38 FN 28 TN 1443 STEMMER, ny prediksjonsfil = frossen (56 s) |

Zipen inneholder #2654-rettelsene: «repo4 (frossen + fire historikktrekk)» i kravrespons (1), «benk» 0 i ERLIG, «0,512 på MOT» 0 i README. tilbake_fra_zip: 17 frosne filer like frys 16:00, FRYS AVVIK 11 (filer laget etter zip 2587, ventet som i #2631/#2640).

## Funn 1: `lag_staar.py` var brutt av #2653 (BYTT-tekstendring kl. 17:3x)
`--sjekk` stoppet med «fant 0 treff» (README «Vi leverer repo4, ikke V2»), og etter rettelse tre til i kravrespons. #2653 endret BYTT-README/kravrespons etter at reglene ble skrevet. Rettet i `arbeid/oppgave_2598/lag_staar.py` (5 regler, BYTT-siden oppdatert, to nye): README «Vi leverer repo4 (frossen modell + fire historikktrekk)», README-linje 9 der byttesetningen «repo4 … ble deretter byttet inn …» strykes i STÅR, kravrespons-vilkåret («på vilkår om at pakken kjørte feilfritt fra kald start, og det gjorde den»), kravrespons «repo4 (frossen modell + …)», «0,512 ligger like over målet», og ny regel KI «[0,40; 0,62]» → «[0,36; 0,59]» (uten den ville en nybygd STÅR-kravrespons fått BYTT-intervallet). Nå: `--sjekk` LIK for begge.
Reserven er bygget på nytt: eneste tekstendring i `reserve_staar/README.md` er «valgt på test» → «valgt ut fra test» (#2653-ordlyden), ingen tall. Tallvakt i kopien med den nye README: 0 avvik. Zip-testen ble kjørt med README før denne ene fraseendringen.
Regel for alle: hver gang BYTT-tekstene endres, kjør `python3 -I arbeid/oppgave_2598/lag_staar.py --sjekk`; sier den «fant 0 treff», er STÅR-kjeden rød før den starter.

## Funn 2: disken er nesten full
Første pakk_jury-kjøring feilet med «No space left on device» (Data-volum 97 %, 6,3–6,7 GB ledig). `/tmp/ren_head_2514` (27 GB) og `/tmp/staar_ovelse_2631` (15 GB) er gamle kopier fra tidligere oppgaver; jeg har ikke slettet dem (ikke mine). En pakk+test-runde trenger ca. 0,8 GB. Bør ryddes før 19:30-verifiseringen.

## Tid
Kopi 65 s, kjede 0a–6: 5 s, pakk 50 s, test 56 s, pakk-runde 1 (feilet på disk) 66 s. Tidsboksen (15 min) ble overskredet med ca. 10 min pga. byggeskript-rettelsen.
