# Case 1: juryens fem vanskeligste spørsmål, med svar i pakken eller MANGLER (#2721, speider, 05.11 ca. 18:30)

Stier er relative til `arbeid/hack/c1/leveranse/`. Pakken svarer godt på det meste. Det som mangler, er at tre ting motsier hverandre, og at runden kl. 18:15 ikke står i pakken.

## 1. «Dere fant repo4 ved å se på 2026. Er ikke 0,512 tilpasset teståret?»
**SVAR FINNES.** `JURY.md:4`, `JURY_SPORSMAL.md:91-93` (sp. 21), `JURY_SPORSMAL.md:87` (sp. 20), `ERLIG_EVALUERING.md:104`. Pakken sier rett ut at 2026 ikke er et friskt år, og at det er 2024 og 2025 (målt etter regelen) som avgjør byttet. Det er ærlig og godt.

## 2. «Hvor mange kandidater prøvde dere, og hva med den siste runden?» (flere sammenligninger)
**MANGLER / MOTSIGELSE.**
- `JURY_SPORSMAL.md:87` sier «Sju kandidater ble prøvd, og én besto». `MUNTLIG.md:9` sier «Tolv kandidater ble målt på to benker. Elleve falt». Juryen ser at tallene ikke stemmer.
- Runden fra ordre #265 (siste forsøk til 18:15, beste kandidat +0,014, kravet var +0,02, den frosne modellen står) finnes ikke i pakken. `grep 0,014` gir 0 treff i leveranse/ og DEMO_MANUS.md. Uten den ser det ut som om vi har skjult en ny runde med testblikk.
- **Til smed2 (#2723):** Bruk ett totaltall for kandidatene i sp. 20 og MUNTLIG, regnet fra kandidatloggen. Legg til én linje i `ERLIG_EVALUERING.md` § 7 og sp. 20: «18:15-runden: N kandidater, beste +0,014 i snitt, under kravet +0,02, ingen bytte».

## 3. «Er gevinsten over den frosne modellen og over målet 0,5 mer enn støy?»
**SVAR FINNES.** `JURY.md:72` (+0,036 [−0,008; +0,085], «innenfor støy»), `JURY_SPORSMAL.md:95-97` (sp. 22: TP 30→32, FP 38→35, «sannsynlig, ikke bevist»), `JURY_SPORSMAL.md:99-101` (sp. 23: målet ble bare nådd etter byttet).
**Motsigelse i tallene mot b2:** `JURY.md:23` sier at modellen slår b2 med **+0,15 [0,04; 0,25]** (repo4). Men `JURY_SPORSMAL.md:48` (sp. 11) og `JURY_SPORSMAL.md:73` (sp. 17) sier at «agenten» slår b2 med **+0,11 [0,01; 0,22]** og kaller det «så vidt over null». +0,11 gjelder den eldre frosne modellen (0,476; `kilder/c1_enkle_regler_og_hist1.md:18,36`).
- **Til smed2:** Merk +0,11 i sp. 11 og sp. 17 som «eldre frossen», eller bytt til repo4-tallet +0,15 [0,04; 0,25]. Tallet for huskeregelen, +0,23, gjelder trolig også den frosne modellen og må sjekkes.

## 4. «Lekker historikken fra samme sesong, også i de fire nye trekkene i repo4?»
**SVAR FINNES, MED ET ÆRLIG HULL.** `JURY_SPORSMAL.md:76-78` (sp. 18: strengt tidligere møter, sjekket mot 400 rader med 0 avvik, golvet 0,415 for en ekstern bruker), `JURY_SPORSMAL.md:89` (sp. 20: protokollsjekk #2575 består, men **400-rad-sjekken er ikke kjørt på nytt for repo4**), `JURY.md:23,77`.
- Hullet er oppgitt, men det er det første en kritisk jury tar tak i. **Valgfritt for smed2/dommer, bare hvis det rekker:** kjør 400-rad-sjekken på repo4 og skriv resultatet i sp. 20. Hvis ikke, står teksten som den gjør.

## 5. «Får mennesket bedre beslutninger, og er rutingsbåndet valgt på test?»
**SVAR FINNES.** `JURY.md:40` (båndet er valgt fra et rutenett på test og sjekket på val, «ikke uavhengig av test»), `JURY.md:50` («Hvor godt mennesket treffer i bunken, har vi ikke målt»), `JURY_SPORSMAL.md:68-70` (sp. 16: båndet er det eneste som er valgt fra test), `ERLIG_EVALUERING.md:59` (kalibreringen er lært på val 2025).
**Utdatert linje:** `JURY_SPORSMAL.md:70` (sp. 16) siterer «alle 9 MOT-flagg agenten tar selv er riktige». Det gjelder den frosne modellen. For repo4 er det 11 av 14 (`JURY.md:34`). **Til smed2:** merk tallet «eldre frossen», eller bytt til 11 av 14.

## Småting (lav prioritet)
- `JURY_SPORSMAL.md:104` («Hull vi kjenner») sier «To KI-er står i pakka: [0,40; 0,62] … og [0,40; 0,62]». Begge tallene er like, så setningen ser ut som en feil. Bruk tre desimaler ([0,397; 0,616] mot [0,400; 0,621]) eller stryk punktet.

## MANGLER til smed2 før 19:00, i prioritert rekkefølge
1. Ett totaltall for kandidatene (sp. 20 sier 7, MUNTLIG sier 12), og 18:15-runden (+0,014, ingen bytte) inn i `ERLIG_EVALUERING.md` § 7 og sp. 20.
2. b2-forspranget: sp. 11 og sp. 17 sier +0,11 (eldre frossen), mens `JURY.md:23` sier +0,15 (repo4).
3. Sp. 16: «9 av 9» → repo4 11 av 14.
4. (Valgfritt) Lekkasjesjekk med 400 rader på repo4.
