# Case 1: kritisk jurylesning av evalueringen i BYTT-zipen (#2655)

Lest: `jurypakke_c1_1724_5514792.zip` (state/levering/c1_gronn), filene under `c1_stemmeagent/arbeid/hack/c1/leveranse/`. Linjetall gjelder filene i zipen. Ingen nye tall: alle tall i forslagene står allerede i pakka (kilde i parentes).

**Svar på de tre spørsmålene:**
- *Utvalgsskjevhet (repo4 valgt på samme testår):* ærlig sagt i ERLIG § 7 (linje 104), men README:9, ERLIG:34 og JURY_SPORSMAL:7 sier det motsatte. Juryen vil se at teksten motsier seg selv. Det er funn 1 og 4.
- *0,512 hviler på 58 MOT, KI:* ærlig sagt. README:8–9, ERLIG:6 og 33 og BEGRENSNINGER:7 har 58 og [0,40; 0,62]. Her trengs ingen endring.
- *Ca. 0,06 fra samme-sesong-historikk:* ikke ærlig for repo4. 0,061 er målt på den eldre frosne modellen (0,476 → 0,415, `kilder/c1_enkle_regler_og_hist1.md:14`). Pakka regner det mot 0,512, og der er differansen 0,097. Repo4 legger til fire trekk av samme slag, og trekket uten samme-sesong-historikk er ikke målt på repo4. Det er funn 2.

## Funn 1 (MÅ): «Valgt på val, kjørt én gang på test» stemmer ikke for repo4
- `README.md:9` (leveranse): «Valgt på val 2025 (0,530), kjørt én gang på test (rutingsbåndet er valgt på test og sjekket på val).»
- `ERLIG_EVALUERING.md:34`: «Ingen modellvariant, C eller grense er valgt på test [A]»
- Hvorfor: ERLIG:104 sier selv at repo4 ble funnet mens 2026-tallet var kjent, og at 2026 ikke er et friskt testår. En jury som leser README først, får det motsatte inntrykket.
- Ny setning, README:9 (erstatter fra «Valgt på val»): «Grensen er valgt på val 2025 (0,530). Selve modellen repo4 ble valgt etter en regel over tre testår der 2026 var med, og repo4 ble funnet mens 2026-tallet var kjent. Derfor er 0,512 ikke et friskt testtall og er trolig noe optimistisk. De to årene som ble målt etter at regelen var skrevet, gir 0,506 (2024) og 0,531 (2025) (`ERLIG_EVALUERING.md` § 7). Rutingsbåndet er valgt på test og sjekket på val.»
- Ny setning, ERLIG:34 (erstatter første ledd): «Ingen C eller grense er valgt på test [A]. To ting er valgt med test synlig: rutingsbåndet [0,15; 0,85) (§ 6, `JURY_SPORSMAL.md` sp. 16) og selve modellen repo4, som ble funnet med 2026-tallet kjent og valgt etter en regel der 2026 var med (§ 7).»

## Funn 2 (MÅ): «omtrent 0,06» og golvet 0,415 gjelder den gamle modellen, men står mot 0,512
- `README.md:14`, `ERLIG_EVALUERING.md:29`, `ERLIG_EVALUERING.md:76`, `kravrespons.md:10`.
- Hvorfor: 0,512 − 0,415 = 0,097, ikke 0,06. 0,06 er differansen for den frosne modellen (0,476 → 0,415, −0,061 [−0,143; +0,022], `kilder/c1_enkle_regler_og_hist1.md:14`). README:14 sier i parentes «målt på den frosne modellen», men ikke at tallet for repo4 mangler. ERLIG:29 skriver «fra 0,512 til 0,415», og det er feil sammenstilling.
- Ny setning, README:14: «**Største forbehold:** for den eldre frosne modellen kom 0,061 av F1 fra NBIMs egne tidligere stemmer i samme sesong (0,476 → 0,415 [0,30; 0,53]). For repo4, som legger til fire historikktrekk av samme slag, er dette ikke målt, og andelen kan være større. Det er ærlig bare om NBIM har sine tidligere stemmer løpende (`ERLIG_EVALUERING.md` § 2, `JURY_SPORSMAL.md` sp. 18).»
- Ny setning, ERLIG:29: «Uten den antakelsen faller F1 på MOT mot styret for den eldre frosne modellen fra 0,476 til 0,415 [0,30; 0,53] (bare historikk fra tidligere år, `--hist 1`, `kilder/c1_enkle_regler_og_hist1.md`). For repo4 (0,512) er golvet uten løpende historikk ikke målt.»
- ERLIG:76 og kravrespons:10: bytt «omtrent 0,06 av F1 kommer fra … (uten den: 0,512 → 0,415 …)» med «for den eldre frosne modellen kom 0,061 av F1 fra stemmer tidligere i samme sesong (0,476 → 0,415); for repo4 er det ikke målt». Merk at ERLIG § 6 kaller teksten «ordrett kl. 13.06», men den er redigert til repo4-tall etterpå. Legg til en linje i lista på ERLIG:45–53: «Tallene for repo4 (0,512, 32 av 58, 18 av 58) er satt inn etter kl. 13.06; resten er ordrett.»

## Funn 3 (MÅ): «0,512 ligger under målet 0,5» er feil fortegn
- `kravrespons.md:10`: «0,512 ligger under målet vårt på 0,5»
- `ERLIG_EVALUERING.md:53`: «les 0,512 (0,40–0,62), under målet 0,5»
- `JURY_SPORSMAL.md:7`: «Val ligger over målet (0,530) og test under. Vi har ikke valgt noe på test for å komme over 0,5.»
- Hvorfor: rester fra 0,476. Den siste setningen i JURY_SPORSMAL:7 er usann etter BYTT (funn 1).
- Ny setning, kravrespons:10: «Med 58 MOT i test er intervallet bredt: 0,512 ligger like over målet 0,5, men KI [0,40; 0,62] går godt under målet.»
- Ny setning, ERLIG:53: «**«rundt 0,5»** i teksten under betyr 0,512 (0,40–0,62): like over målet 0,5, men innenfor støyen.»
- Ny setning, JURY_SPORSMAL:7: «Grensa er valgt på val 2025. Modellen repo4 ble valgt med test 2026 i regelen (ERLIG § 7), så 0,512 er ikke et rent engangstall. Val (0,530) og test (0,512) ligger begge like over målet. Med 58 MOT i test er ±0,05 innenfor støyen, så 0,5 ligger godt inne i intervallet.»

## Funn 4 (BØR): sp. 19 forklarer utvalgsskjevhet, men frikjenner 0,512 for den
- `JURY_SPORSMAL.md:81`: «Fordi hovedtallet 0,476 er det eneste som er valgt uten å se test. … Velger vi det beste av flere testblikk, blir tallet for høyt.»
- Hvorfor: hovedtallet er nå 0,512, og repo4 er det beste av 12 kandidater (6 i benk A og 6 i benk B, ERLIG:86–102) målt på de samme tre testårene. Argumentet treffer da vårt eget tall. Juryen vekter ærlig evaluering høyest, og det er bedre at vi sier det selv.
- Ny setning, JURY_SPORSMAL:81 (erstatter første setning): «Fordi den eldre frosne 0,476 var det eneste tallet valgt uten å se test. Repo4 (0,512) ble valgt etterpå blant 12 kandidater målt på de samme tre testårene, så også 0,512 har noe av den skjevheten vi beskriver under. Derfor krevde regelen både snitt og verste år, og de avgjørende årene er 2024 og 2025, der repo4 er +0,051 og +0,017 over frossen (ERLIG § 7).»

## Funn 5 (BØR): ERLIG beskriver fortsatt den frosne modellen som den leverte
- `ERLIG_EVALUERING.md:3`: «Modell: den frosne «miks h2» …»
- `ERLIG_EVALUERING.md:7`: «Der får full modell 0,482» (det er den frosne; README:17 gir 0,529 for repo4)
- `ERLIG_EVALUERING.md:59`: tabellraden «agenten, maskin alene (miks h2) … 0,512»
- Hvorfor: ablasjonen i § 1–2 er kjørt på den eldre modellen, men står under hovedtallet til repo4. Juryen kan tro at ablasjonen forklarer 0,512.
- Ny setning, ERLIG:3: «Levert modell: repo4, altså den frosne «miks h2» (snitt av logreg og LightGBM, løpende historikk) pluss fire historikktrekk (§ 7). Ablasjonen i § 1–2 er kjørt på den eldre frosne miks h2 (0,476 på MOT), ikke på repo4.»
- Ny setning, ERLIG:7: «Ablasjonen under er målt på den eldre frosne modellen og på **avvik fra styret** (66 avvik: 58 MOT, 5 AVSTÅ, 3 andre). Der får den 0,482, og repo4 får 0,529 [A, S].»
- ERLIG:59: bytt «(miks h2)» med «(repo4 = miks h2 + 4 historikktrekk)».

## Sjekket og i orden
- KI og 58 MOT står ved hovedtallet i README, ERLIG og BEGRENSNINGER.
- ERLIG:104 sier ærlig at regelen ble skrevet 16:49, at 2026-tallet var kjent 16:13, at KI for snittet krysser null og at gevinsten er «sannsynlig, ikke bevist». Det er den sterkeste teksten i pakka. Funn 1 og 4 handler om at resten av pakka skal si det samme.
