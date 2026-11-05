# Case 1: pakka sjekket mot regelverket, punkt for punkt (dommer, #2230, ordre #243)

Sjekket 05.11 kl. 13.31–13.45. Pakka er `arbeid/hack/c1/leveranse/`. Regelverket er lest ordrett fra
`startpakke/Regler_og_bedommingskriterier.pdf.pakk_ut.txt` (R), `case1_stemmegivning/README.md` (C1) og
`FinTech Hackathon H2026.pdf.pakk_ut.txt` (FH). README-kallet er kjørt på nytt: `bash arbeid/hack/c1/leveranse/kjor.sh`
gir rc 0 på 31 s, `MOT mot styret: TP 30 FP 38 FN 28 P 0.4412 R 0.5172 F1 0.4762` og TALLVAKT GRØNN.

## MANGLER: ordføreren lager oppgaver av disse

1. **Juryspørsmål 1–3 er ikke besvart i JURY.md** (R pkt. 6). JURY.md har bare «Begrensninger» og «Slår dere noe enkelt?».
   Det trengs tre overskrifter med svar: (1) hvorfor målvariabelen *MOT styret* og hvilke alternativer vi vurderte
   (avvik inkl. AVSTÅ, aksjonærforslag=MOT, accuracy), (2) om vi ville turt å sette det i produksjon (ærlig svar: som
   sorteringshjelp for en analytiker, ikke som automatisk stemme, med grunner), (3) hva vi ville gjort først med én uke til.
   Ingen av de tre ordene «målvariabel», «produksjon» eller «uke» finnes i JURY.md, ERLIG_EVALUERING.md eller README.md.
2. **Kravresponsen er for lang** (R pkt. 2–3, FH l. 124: maks én side, 3–5 setninger per overskrift). Nå er den 846 ord
   pluss en tabell, med ca. 13 / 18 / 8 setninger under de tre overskriftene (`kravrespons.md:4`, `:7`+`:18`, `:21`).
   Dette er allerede oppgave #2229 (speider).
3. **Motstandstesten på den frosne modellen er ikke ført inn i pakka** (C1 «Motstandstesten … rapporter svaret uansett»).
   Testen er gjort (#2188, #2212: `state/rapporter/c1_injeksjon_etter_2205.md`). Resultat: «stem FOR/MOT» flagges og alle
   saker går til menneske. Frasen «kindly support/oppose management» flagges ikke, og 20–21 saker endrer stemme uten å gå
   til menneske, så F1 MOT faller til 0,387–0,400. Pakka sier fortsatt at testen «ikke er målt på den frosne»:
   `BEGRENSNINGER.md:18`, `JURY.md:17`, `kravrespons.md:18`. Svakheten skal stå der med tallene.
4. **Motstridende tall for «til menneske»**: `JURY.md:15` sier 228 av 1578 (14,4 %) og kaller 188 «eldre». Kald kjøring nå
   (`/tmp/c1_kald/ut/KJORING.txt`, 13:31, og opptelling i agent.csv) gir **188 av 1578 (11,9 %)**, det samme som
   README:11, kravrespons:4 og BEGRENSNINGER:3. Rett JURY.md pkt. 8, ellers ser det ut som pyntede tall.

## Bør rettes (små, trekker ikke direkte ned)

5. `kjor.sh:2-4` sier fortsatt «hent NBIMs N-PX fra SEC -> tidssplitt per N-PX-år». Standardveien (l. 11–19) bruker real_votes.
   Kommentaren bør si det, så leseren ikke blir forvirret.
6. Gamle N-PX-filer ligger i leveransemappa og brukes ikke av hovedveien: `run.sh`, `rapport.py`, `resultat.py`, `sporlogg.py`,
   `motstand_inj.py`, `utkast_1100/`. De bør flyttes eller merkes «brukes bare av SPOR=npx». Ellers kan juryen tro at
   `sporlogg.py` er sporbarheten til agenten. Den ekte sporbarheten er `agent.csv` og `KJORING.txt`.
7. `README.md:12` og `:29` skriver `bash leveranse/kjor.sh`, og det virker bare fra `arbeid/hack/c1`. Skriv kallet fra
   landsbymappen (`bash arbeid/hack/c1/leveranse/kjor.sh`) eller som «fra hvor som helst: bash <sti>/kjor.sh».
8. Kreditering: `README.md:62` sier «Ingen kopiert prosjektkode utover startpakken». Skriv i stedet en egen linje om at
   `c1/hent_npx.py` (endret) og `c1/baseline.py` bygger på arrangørens startpakke og brukes bare i SPOR=npx.
9. `KJORING.txt` (som kald kjøring skriver) har linja «TEST 2026 (samme andel flagget som val …) F1 0.5». Den er merket
   «bruker test-fordeling», men en jurymedlem kan lese den som hovedtall. Den bør fjernes eller få tydeligere merking.
10. Datakilde: `README.md:62` sier «Ingen data fra oppdragsgiver», mens fila kom fra arrangøren, og juryen er fra NBIM (FH l. 161).
    Skriv at real_votes er NBIMs *offentlig publiserte* stemmer (vd.nbim.no), utlevert som fil av arrangøren.
11. R pkt. 3 sier «Fem overskrifter», men malen lister bare tre, og FH l. 124 sier «tre deler». Tre overskrifter er riktig.
    Ingen endring.

## Tabell: krav → fil:linje → status

| # | Krav (kilde) | Hvor i pakka | Status |
|---|---|---|---|
| 1 | Kravrespons maks 1 side (R 2, FH 124) | `kravrespons.md` (846 ord + tabell) | **MANGLER** (#2229) |
| 2 | 3–5 setninger per overskrift, ingen markedsføring (R 3) | `kravrespons.md:4,7,21` (13/18/8) | **MANGLER** (#2229) |
| 3 | Overskriftene i malen (R 3) | `kravrespons.md:3,6,20` | OK |
| 4 | README med ett kall som gir hovedtallet (R 2) | `README.md:28-44`, `kjor.sh:11-19` (kjørt nå: F1 0,4762) | OK (sti, punkt 7) |
| 5 | Kilder med URL (R 5) | `README.md:54-62` (vd.nbim.no, GVG, posisjonsnotater) | OK (ordlyd, punkt 10) |
| 6 | AI-verktøy og hva de ble brukt til (R 5) | `README.md:64-69` | OK |
| 7 | Kopiert kode kreditert (R 5) | `README.md:62` | DELVIS (punkt 8) |
| 8 | Baseline oppgitt og slått (R 4, C1) | `kravrespons.md:9-16`, `JURY.md:19-31` (følg styret 0, b2 0,365, modell 0,476, +0,11 [0,01; 0,22]) | OK |
| 9 | Presisjon/recall på MOT, ikke accuracy (C1) | `README.md:8-9`, `kravrespons.md:7,16` | OK |
| 10 | Tidssplitt, ingen tilfeldig splitt (R 4, C1) | `kravrespons.md:7`, `JURY.md:14` (tren ≤2025, val 2025, test 2026 én gang) | OK |
| 11 | Ingen lekkasje / kategori-lekkasje (R 4, C1) | `kravrespons.md:7`, KJORING.txt «FORBUDT og ikke brukt … snitt med brukt: set()» | OK |
| 12 | Hver anbefaling siterer kilden (C1) | `agent.csv`: retningslinje_id, retningslinje_sitat, retningslinje_grunnlag; `BEGRENSNINGER.md:24` | OK |
| 13 | Konfidens og overlevering til menneske (C1) | `README.md:4-5`, agent.csv `p_mot`, `til_menneske`, `rutingsgrunn` | OK (tall i JURY:15 feil, punkt 4) |
| 14 | Motstandstesten rapportert uansett resultat (R 4, C1) | `BEGRENSNINGER.md:18`, `JURY.md:17`, `kravrespons.md:18`: «ikke målt på den frosne» | **MANGLER** (punkt 3) |
| 15 | Sporbarhet i hva løsningen gjorde (R 4) | agent.csv per sak + `KJORING.txt` (features, forbudte kolonner, grense) | OK (rot, punkt 6) |
| 16 | Ingen irreversible handlinger uten logg (R 4) | `README.md:52` «Løsningen stemmer ikke … et menneske beslutter» | OK |
| 17 | Erklærte begrensninger (R 1, 4) | `BEGRENSNINGER.md` 1–8, `JURY.md:5-17`, `ERLIG_EVALUERING.md` | OK (punkt 3–4 er utdatert) |
| 18 | Demo ikke bare håndplukket, holdout vist (R 4) | `demo.sh` (seed 0), `demo_utskrift.txt:3-7` viser F1 0,4762 på test 2026 før eksemplene | OK |
| 19 | Juryspørsmål 1–3 besvart (R 6) | `JURY.md`: finnes ikke | **MANGLER** (punkt 1) |
| 20 | Påstander reproduserbare fra koden (R 4) | kjor.sh: tallvakt 153 påstander, 0 avvik | OK |
| 21 | Bare åpne kilder, ikke interne data (R 5) | `README.md:14-23,55-57` | OK (ordlyd, punkt 10) |
| 22 | Fallgruve klasseubalanse (C1) | `kravrespons.md:7` (følg styret 96,2 % acc, F1 0) | OK |

**Dom:** Kjernen holder: tallet reproduseres, baseline er slått, tidssplitt og lekkasjevakt er på plass. Fire ting mangler
før 19.30: jurysvar 1–3, én side, motstandstesten på den frosne modellen og tallet 228/188 i JURY.md.
