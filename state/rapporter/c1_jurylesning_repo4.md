# Case 1: jurylesning av repo4-zipen (F1 0,512), oppgave #2601

Lest: `state/levering/c1_gronn/SISTE_GRONNE.zip` -> `jurypakke_c1_1724_5514792.zip` (150 filer), pakket ut i
`/tmp/jury2601.VkFM`. Lesevei som jurymedlem: rot-`README.md` -> `leveranse/kravrespons.md` -> `leveranse/README.md`
-> `leveranse/JURY.md` -> `DEMO_MANUS.md` + `demo_utskrift.txt`. Stier relative til `c1_stemmeagent/arbeid/hack/c1/`.
Bare lesing, ingen rettinger gjort.

## Krav -> hvor -> vurdering

| Krav | Fil / sted | Vurdering |
|---|---|---|
| Hovedtall likt overalt | rot-README 0.512000, leveranse/README 0,512 [0,40; 0,62] TP32 FP35 FN26, JURY.md, BEGRENSNINGER, MUNTLIG, demo_utskrift | OK i lesevegen. **Rødt i demo-manus og tre støttefiler** (se under) |
| Mål 0,5 nådd? | kravrespons:10, JURY.md:5, ERLIG_EVALUERING.md:53 | **Rødt: alle tre sier «0,512 under målet 0,5».** Feil, 0,512 > 0,5 |
| Byttet forklart (regel før måling) | leveranse/README:12, kravrespons:7, JURY_SPORSMAL sp. 20, MUNTLIG:17 | OK, sterkt i sp. 20 (2026 var kjent før regelen, 2024/25 avgjør, KI [−0,005; +0,078], 4 % under). kravrespons:7 sier «regel satt før måling på tre testår (2024–2026)», som overselger 2026 |
| KI krysser null sagt rett ut | README:12 viser [−0,005; +0,078]; sp. 20 «sannsynlig, ikke bevist» | OK i sp. 20; ordene «krysser null» står ikke i README/kravrespons |
| Test aldri brukt til å velge | JURY.md:3 «test kjørt én gang på den frosne agenten, aldri brukt til å velge» | **Svakt: stemmer ikke etter byttet** (repo4 ble funnet på 2026, sp. 20) |
| Modellnavn | JURY.md:9 «Den frosne agenten (modell miks h2)», JURY.md tabell «Hovedmodell, miks h2 … 0,512» | **Svakt: 0,512 er repo4, ikke miks h2** |
| Rester av 0,476 som hovedtall | se liste under | **Rødt** |
| SCORE 0.529412 vs 0,512 | rot-README forklarer at SCORE er avvik inkl. AVSTÅ | OK |
| Interne navn | `smed` i 52 filer, `dommer` 28, `landsby` 16, `~` 6, `#20xx` 35 (mest i `kilder/`); README:73 forklarer stiene | Svakt, kjent fra før |
| demo_utskrift frys-tid | linje 5 «frys 2026-11-05T17:10:34», frysvakta sier 17:18:18 | Lite, men en nøye jury ser det |

## 0,476 som hovedtall (rester, alle må rettes eller merkes «eldre frossen»)
1. `DEMO_MANUS.md:15` «Agenten: F1 0,476. Den finner 30 av 58» og `:56`, `:63`, `:67` (frysen står; 0,476 mot …). **Demoen leser opp feil hovedtall.**
2. `DEMO_MANUS_5min_tilfeldige.md:24,25,91` «Hovedtallet er F1 0,476».
3. `leveranse/JURY_SPORSMAL.md:81` (sp. 21?) «Fordi hovedtallet 0,476 er det eneste som er valgt uten å se test … frysen» – svarer som om vi IKKE byttet. Også `:57` «Fordi modellfrysen kl. 16 står».
4. `JURY_METODE.md:19` rad «Samme modell, F1 på MOT (hovedtall) **0,476**» og `:28` «vi ligger under det på test (0,476)».
5. `SVAKHETER.md:4` og `:75` (engelsk) 0,476 som hovedtall.
6. `tall_tabell.md:10,12` «beste MOT-modell 0.476».
7. `leveranse/kjor.sh:10` kommentar «MOT F1 0.4762».
OK-merket som eldre: JURY.md:58/60, BEGRENSNINGER:3, NESTE_VERSJON, ERLIG:85, kilder/*.

## Rettinger, rangert (det juryen trekker mest for)
1. **«0,512 under målet 0,5»** i kravrespons:10, JURY.md:5, ERLIG:53 -> «litt over målet 0,5, men KI [0,40; 0,62] dekker godt under». Treffer ærlig evaluering direkte og er en ren regnefeil.
2. **DEMO_MANUS.md 0,476/30 av 58** -> 0,512/32 av 58/P 0,48 (TP32 FP35 FN26). Demoen er det juryen hører.
3. **JURY_SPORSMAL:81 og :57** svarer som om frysen sto; skriv om til repo4 eller fjern spørsmålet.
4. **JURY.md:3 og :9 + tabellraden «miks h2»** -> «repo4 (miks h2 + 4 historikktrekk); 2026 ble brukt til å finne kandidaten, se sp. 20».
5. JURY_METODE:19/28, SVAKHETER:4/75, tall_tabell:10/12, DEMO_MANUS_5min_tilfeldige: oppdater eller merk «eldre frossen». kravrespons:7 «tre testår (2024–2026)» -> «avgjort på 2024 og 2025».
