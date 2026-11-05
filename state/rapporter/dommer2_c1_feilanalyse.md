# Case 1: feilanalyse av MOT-stemmene smed2 v3 og gulvregelen bommer på (dommer2, #1983)

Måler 823c9610fe, `data_v3` test 2026 (NBIM N-PX): 1246 forslag, 129 MOT.
- smed2 v3 (`pred_v3.csv`, #990): tp 51, **fp 39, fn 78**, F1 0,466.
- gulvet (`gulv_data_v3.csv`, #984): tp 55, **fp 103, fn 74**, F1 0,383.
Begge tall er reprodusert med `maaler.py`. Kode og råutskrift: `arbeid/oppgave_1983/feil.py` og `feil.txt` (kjøres i smed2s venv, fordi den gjenbruker `train_v3.feats`).

**Forslagstype:** alle 1246 testforslag er say-on-pay med kilde ISSUER. Typen deler derfor ikke feilene. Jeg deler i stedet på teksten (årlig say-on-pay mot golden parachute/fusjon) og på selskapets kjennetegn. **Selskap:** ingen selskap har mer enn 2 feil (Core Scientific 2 fn, Norfolk Southern 2 fp, Viatris 2 fp for gulvet; smed2 har høyst 1 per selskap). Feilene samler seg altså ikke på enkeltselskaper. De samler seg på hva vi vet om selskapet.

## Topp 5 feilgrupper
| # | gruppe | n | MOT | smed2 tp/fp/fn, F1 | gulv tp/fp/fn, F1 |
|---|---|---|---|---|---|
| 1 | **Ny MOT der NBIM bare stemte FOR før** (fn) | 979 | 55 | 8/5/**47**, 0,24 | 0/0/**55**, 0,00 |
| 2 | **Gjentatt MOT-historikk, men NBIM snur til FOR** (fp) | 158 | 55 | 35/**28**/20, 0,59 | 55/**103**/0, 0,52 |
| 3 | **Mangler SEC-lønnsdata** (Pay-vs-Performance) | 857 | 83 | 18/26/**65**, 0,28 | 30/83/53, 0,31 |
| 4 | **Selskap NBIM ikke har stemt på før** | 109 | 19 | 8/6/11, 0,48 | 0/0/**19**, 0,00 |
| 5 | **Golden parachute / fusjonslønn** | 46 | 15 | 4/5/**11**, 0,33 | 3/2/12, 0,30 |

Til sammenligning: der SEC-lønn finnes (n 389, 46 MOT) får smed2 F1 **0,72** (gulvet 0,55). Der CEO-lønna steg mer enn 20 % (n 91, 18 MOT) får smed2 **0,76**. Der Vanguard har stemt mot lønna før (n 31, 11 MOT) får smed2 0,70.

## Hva det betyr
1. **Gruppe 1 er hovedtapet: 47 av 78 fn hos smed2 (60 %).** Det er nye MOT-stemmer på selskaper der NBIM bare har stemt FOR, og der Vanguard heller ikke har stemt mot. Ingen historikk varsler. Gulvet kan ikke se dem i det hele tatt. Bare lønnsfakta kan fange dem.
2. **Gruppe 2 er gulvets svakhet: 103 fp.** NBIM stemmer MOT bare i 35 % av tilfellene der de har stemt MOT før (55 av 158). Modellen kutter fp fra 103 til 28 og mister 20 tp. Det er hele forskjellen mellom 0,38 og 0,47.
3. **Gruppe 3 er et datahull, ikke en modellgrense.** Navnematchingen virker: 1183 av 1246 får CIK. Men 794 rader har CIK uten Pay-vs-Performance-lønn før møtet. Modellen er dobbelt så god der dataene finnes (0,72 mot 0,28). Å tette dekningen (ECD-XBRL for regnskapsår 2025, eller DEF 14A direkte) er det billigste løftet før modellfrysen kl. 16. Forbehold: dekningen henger trolig sammen med selskapsstørrelse, så noe av forskjellen kan komme av utvalget og ikke av lønnsdataene.
4. **Gruppe 4 (nye selskaper):** gulvet sier FOR på alle. Modellen finner 8 av 19 via Vanguard og SEC. Dette er et argument for modellen framfor regelen.
5. **Gruppe 5 (golden parachute):** 15 MOT av 46 er en MOT-rate på 33 %, mot 9 % for årlig say-on-pay. Begge bommer på 11–12 av dem. En egen regel eller et eget flagg for fusjonslønn er et kandidattiltak, men det må testes på val og ikke på disse tallene.

## Forbehold (til evalueringskapitlet)
- Grupperingen er laget på **test**, så den beskriver feilene. Tiltak velges og måles på `data_v3_val`. Å velge terskler eller regler ut fra tabellen over ville være test-tuning.
- Små grupper (n 31–46) har brede usikkerhetsintervall. Én sak flytter F1 i en gruppe med 15 MOT med ca. 0,03–0,05.
- Konsekvens for ruting til menneske: gruppe 1 og 3 er der modellen er mest usikker og bommer mest. Saker uten lønnsdata og uten historikk er de naturlige kandidatene for manuell vurdering.
