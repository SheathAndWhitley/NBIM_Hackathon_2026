# Fjernet fra levering/METODE.md (ordre #242, gammel data: SEC-N-PX/Vanguard)

## Vedlegg: eldre N-PX-modell
*Alt under gjelder den eldre N-PX-modellen (SEC N-PX, bare amerikanske say-on-pay, 1246 test-saker, 129 avvik). Metoden (tidssplitt, lekkasjesjekk, klyngebootstrap, grense bare på val) er den samme som i pkt. 0, men tallene (0,474, 0,383 osv.) er N-PX-tall og **ikke hovedtallet**.*

**Spørsmålet (N-PX):** Når stemmer NBIM MOT styrets anbefaling på amerikanske say-on-pay-forslag?
**Hovedmål:** F1 på MOT mot styret (#231). For N-PX-modellen under ble det målt som avvik fra styret. Sekundært PR-AUC. Accuracy brukes aldri alene: å følge styret gir 89,7 % riktige og finner null avvik (forsøk #989).

## 1. Data og tidssplitt
- **Fasit:** NBIMs egne stemmer fra SEC Form N-PX (Norges Bank, CIK 1374170). Feltet `managementRecommendation` betyr «med/mot ledelsen», altså selve fasiten. Det leses aldri. Styrets anbefaling utledes fra hvem som har fremmet forslaget.
- **Kjennetegn:** NBIMs tidligere stemmer på samme selskap, **Vanguards** publiserte N-PX-stemmer (bare innsendinger før møtedatoen), SEC-tall (lønn, TSR, aksjelønn) og forslagsteksten.
- **Splitt etter møteår, aldri tilfeldig:** train N-PX 2024 (1631 forslag, 9,1 % MOT), **val** 2025 (1506, 9,0 %), **test** 2026 (1246, 10,4 %). Val-modellen er trent på 2024, test-modellen på 2024+2025. Test ble kjørt etter at valgene var låst.

## 2. Gulvet vi måtte slå (N-PX-modellen)
«Følg styret» gir F1 0 (#989). Det ærlige gulvet er en ettlinjes regel: **MOT hvis NBIM stemte MOT på selskapet før**. Den gir F1 0,383 på test (#994) og 0,361 på val (#996). Alle N-PX-modeller ble målt mot den. Den er ikke hovedtallet.

## 3. Lekkasjesjekk, og hva den kostet
Hvert kjennetegn er sjekket for om det var kjent før møtet (dommer #1985/#1988). To ting ble funnet:
- `s_float` lekker, fordi floaten publiseres 8–9 måneder etter float-datoen. Den er fjernet, sammen med to kjennetegn som er avledet av den.
- PvP- og 10-K-tall lå for nær møtedatoen i ~11 rader. Grensen ble strammet til regnskapsår-slutt < møte − 100 dager.

| variant | val 2025 F1 | test 2026 F1 | forsøk |
|---|---|---|---|
| før sjekken | 0,418 | 0,509 | #1007 / #1006 |
| **lekkasjefri (b), grense 1,25×** | **0,403** | **0,493** | #1015 / #1014 |

Kostnaden er −0,016 på test, KI [−0,054; +0,021]. Den er innenfor støyen, men vi betaler den, slik at «alt er kjent før møtet» holder uten forbehold.

## 4. Usikkerhet: bootstrap med selskap som klynge
Samme selskap går igjen i mange rader, så vi trekker selskaper og ikke rader (2000 trekk). Med bare 129–136 MOT-saker per år er intervallet bredt: med grensen 1,25× (#1014/#1015) ligger test-F1 for b i [0,42; 0,56] og val-F1 i [0,33; 0,47]. Hovedtallets intervall står i pkt. 5 (#1993).

## 5. Grensen, og N-PX-modellens tall (erstattet av 0,476 på MOT)
**N-PX-modellens tall (ikke lenger hovedtall): F1 0,474 på test 2026, 95 % KI [0,404; 0,538]** (forsøk #1023, dommer #1993). Grensen er valgt **bare på val 2025** (best F1 der, rå 0,1833) og låst før test ble kjørt én gang. Val-F1 er 0,429 (#1022), men optimistisk fordi grensen er tilpasset der. Modellen slår gulvregelen med **+0,090 [+0,034; +0,147]** på test (#1023 mot #994) og +0,069 [−0,023; +0,156] på val (#1022 mot #996). Presisjon/recall på test: 0,38 / 0,64 (#1023). Å flytte grensen innenfor området der val-F1 er ≥ 95 % av toppen gir 0,46–0,49 på test, mindre enn KI (#1993).
*Sidetall:* den tidligere grensen 1,25 × basisrate gir 0,493 (#1014). Den brukes ikke som hovedtall, fordi faktoren ble sammenlignet med test-F1 ved siden av, og val alene ville ikke ha pekt på den (#1985, #1993). Forskjellen (−0,020 [−0,065; +0,027]) er innenfor støyen. Forvent ca. 0,47 ± 0,07 neste sesong (halve KI-bredden, #1993).

### Treffprosent mot F1 på N-PX test 2026 (gammel modell, dommer #2010, kald start)
| Variant | tp | fp | fn | tn | Treff % | Presisjon | Recall | F1 |
|---|---|---|---|---|---|---|---|---|
| 1) Følg styret | 0 | 0 | 129 | 1117 | 89,6 | – | 0,000 | 0,000 |
| 2) Gulvregelen (N-PX) | 55 | 103 | 74 | 1014 | 85,8 | 0,348 | 0,426 | 0,383 |
| 3) N-PX-agenten uten ruting | 83 | 138 | 46 | 979 | 85,2 | 0,376 | 0,643 | 0,474 |
| 4) Agenten med 10 % ruting (øvre grense) | 91 | 98 | 38 | 1019 | 89,1 | 0,481 | 0,705 | 0,572 |

1246 N-PX-saker, N-PX 129 av dem MOT (positiv klasse = forvalteren stemmer mot styret). Rad 4: de 119 rutede sakene (18 MOT) antas avgjort riktig av mennesket, så den er en øvre grense. F1 0,47 betyr altså ikke 94,5 % treff; treffprosenten er 85,2. Treffprosent er feil mål fordi 89,6 % av sakene er FOR: «følg styret» får høyest treff uten å finne en eneste MOT-stemme, og agenten taper treff fordi hvert ekte funn koster rundt 1,7 falske alarmer. F1 måler bare det oppgaven handler om, hvor mange av de 129 MOT-stemmene vi finner (recall) og hvor mange av flaggene våre som holder (presisjon), og der går vi fra 0 til 0,47.

## 6. Ruting til menneske
Kalibrering med isotonisk regresjon er låst på val, og ECE på test er 0,025. Sakene nærmest grensen går til et menneske, med båndet låst på val. Ved 10 % ruting (N-PX: 119 saker på test, ca. 120 per år, 18 av N-PX 129 MOT) stiger MOT-presisjonen på maskinens egne saker fra 0,38 til 0,43 [0,35; 0,50] på test, og fra 0,34 til 0,37 på val. Recall på maskinens saker er 0,66 på test. Riktig forventning er altså +0,02 til +0,05 i presisjon. Det beste er å la mennesket **bekrefte maskinens usikre MOT-flagg**: med skjevt bånd (c = +0,50, låst på val) blir system-F1 0,65 [0,58; 0,71] på test (#1027), mot 0,57 [0,50; 0,63] med symmetrisk bånd (#1026). Systemtallene forutsetter at mennesket svarer riktig, så de er en øvre grense. (Kilde: `case1_ruting_verifisert.md`, dommer2 #1995, variant b fra kald start.)
*Dommer #2005: pkt. 6 hadde tall fra den lekkende fullmodellen (#1955: ECE 0,013, 125 saker, presisjon 0,50/0,42, +0,05–0,12). Byttet med variant b-tallene fra #1995 (#1026/#1027).*

## 7. Sitater i den eldre N-PX-agenten (ikke den leverte)
Den eldre N-PX-agenten siterte ordrett fra **Vanguards** *Proxy voting policy for U.S. portfolio companies* (feb 2025), ikke NBIM: 1544 av 1544 sitater var ordrette, men bare 1 av 30 sjekkede sitater støttet stemmen klart (#1991). Den leverte agenten siterer NBIM, se pkt. 7 over.

## 8. Svakheter vi vet om (N-PX-modellen; for hovedmodellen se pkt. 0 og `case1_begrensninger.md`)
- **2025 mot 2026:** val er svakere (0,43 mot 0,47 med val-valgt grense, #1022/#1023). Gapet forklares av at test har to års NBIM-historikk og val bare ett: på den eldre modellen (før lekkasjesjekken, gap 0,09) ga to års historikk mot ett +0,071, KI [+0,009; +0,135], på test (#1990). Det er ikke målt på nytt for variant b. Det er ikke et regimeskifte i NBIMs retningslinjer, så langt vi kan måle.
- **Frames-API:** SEC-tallene kommer fra siste innsending, ikke første publisering. Omarbeidede tall kan lekke litt. Effekten er ikke målt.
- 36 % av MOT-sakene på test (46 av 129) fanges verken av gulvet eller modellen; på val 31 % (42 av 136). På test fanger modellen alle MOT-sakene gulvet fanger. Det er taket for historikk og andre fonds stemmer (dommer #2005, regnet fra #1023/#1022 og gulvfilene til #994/#996).
*Dommer #2005: «45 %» kom fra den eldre modellen (#1978, eller-kombinasjon recall 0,55) og er byttet med tallet for variant b. Linja om #1990 sier nå at +0,071 gjelder den eldre modellen.*
- Bare amerikanske say-on-pay-forslag. Styrevalg og aksjonærforslag er ikke dekket.

Alle forsøkstall: `uv run python tavle.py forsok-list --alle`. Måler for N-PX-tallene: `arbeid/hack/c1/maaler.py` (sha cb9243ddee test, 5707495ef8 val; N-PX-tallet #1022/#1023 er målt med ee16e5945c). Hovedtallet 0,476 er målt med `arbeid/hack/c1/maaler_offisiell_v3.py --score mot` (#2087), KI med `arbeid/oppgave_2095/ki_mot.py`.
