# Case 1: jurylesning av dagens grønne zip (frossen, 0,476), oppgave #2600

Lest: `state/levering/c1_gronn/SISTE_GRONNE.zip` -> `jurypakke_c1_1647_83f152c.zip`, pakket ut i `/tmp/jury2600.QopB`
(138 filer). Lesevei som en jurymedlem: `README.md` i roten -> `leveranse/kravrespons.md` -> `leveranse/JURY.md` ->
`DEMO_MANUS.md` + `leveranse/demo_utskrift.txt`. Ingen nye tall og ingen rettinger. Målestokken er arrangørens
`Regler_og_bedommingskriterier.md` og `case1_stemmegivning/README.md`. Stier under er relative til `c1_stemmeagent/arbeid/hack/`.

## Krav -> hvor i zipen -> vurdering

| Krav (kilde) | Fil / avsnitt | Vurdering |
|---|---|---|
| **Metode 30 %:** målvariabel og hvorfor | kravrespons «Hvordan vi verifiserte det»; JURY.md «Juryspørsmål 1» (accuracy, avvik inkl. AVSTÅ, aksjonærforslag-regel, N-PX-fasit feillest) | OK, sterkt |
| Avgrensning, hvilken beslutning den støtter | kravrespons «Hva vi bygde» (rekkefølge for analytiker, stemmer ikke selv); leveranse/README «Begrensninger» | OK |
| **Evaluering 30 %:** baseline oppgitt og slått | JURY.md «Slår dere noe enkelt?» (følg styret 0, regel b2 0,365, golv 0,415, KI) | OK, sterkt |
| Riktig metrikk (P/R på MOT, ikke accuracy) | kravrespons, JURY.md spm. 1, demo 0:00 | OK |
| Tidssplitt, ingen lekkasje | JURY.md «Slik målte vi»; JURY_SPORSMAL spm. 5 og 18; ERLIG_EVALUERING pkt. 2 | Svakt: løpende historikk fra samme sesong er «antatt og ikke dokumentert» (kravrespons). Ærlig, men golvet 0,415 står bare i JURY.md, ikke i ett-sidaren |
| Test brukt én gang / ikke til å velge | JURY.md:4 «aldri brukt til å velge» mot JURY.md:40 «båndet er valgt fra et fast rutenett på test-tabellen»; ERLIG:34 «Ingen variant er valgt på test» | **Svakt: motsier seg selv i samme fil** |
| Reproduserbart, ett kall | rot-README «Kjør (ord for ord)», `KJOR.sh` med frysvakt + tallvakt | OK, sterkt |
| Kilder med URL i README | bare i `c1/leveranse/README.md` «Datakilder», ikke i rot-README | Svakt (står i README nr. 2 av 3) |
| AI-verktøy oppgitt i README | bare i `c1/leveranse/README.md` «AI-verktøy» | Svakt (samme) |
| Ekstern kode kreditert | `c1/leveranse/README.md` «Kreditering» | OK |
| **Beslutningsstøtte 20 %:** forstå og overprøve et enkeltresultat | rot-README kolonnetabell for `ut/agent.csv`; demo viser treff, bom og til-menneske | OK, men to sitater per sak (`punkt/sitat` og `retningslinje_id`) spriker: Mobimo får GVG 5.2 som treffer og NBIM 5.2.1 om årsrapport som ikke gjør det |
| Siterer kilden per anbefaling | `retningslinje_sitat`, `sitat_kilde`; kravrespons «15 av 20» | OK, ærlig om at sitatet ikke er NBIMs grunn |
| Konfidens og overlevering | `til_menneske`, `rutingsgrunn`; JURY.md «Les dette først» | OK. Tallet spriker: 188 av 1 578 (kravrespons) mot 183 av 1539 (JURY.md, demo). Begge kan stemme, men forklares ikke |
| **Robusthet 20 %:** motstandstesten | kravrespons (16 kjente + 16 nye, 6 slipper forbi, F1 0,39–0,42); JURY.md pkt. 11 | OK, sterkt og ærlig |
| Sporbarhet | `agent.csv`, `FROSNE_SHA256.txt`, `KJORING.txt`, frysvakt | OK |
| Erklærte begrensninger | `BEGRENSNINGER.md`, JURY.md «Begrensninger», bommene (0 av 7 USA) | OK |
| **Leveranse:** kravrespons maks 1 side, 3–5 setninger per overskrift | `c1/leveranse/kravrespons.md`: 584 ord, 3 overskrifter, ca. 5 / 9 / 11 setninger | Svakt: for tett, særlig «Verifisert» og «Videre» |
| Demo 5 min, ikke håndplukket, holdout | `DEMO_MANUS.md` (første av hver type, test 2026) | OK. Men `demo_utskrift.txt` linje 4 sier «FRYSVAKT: ikke frosset ennå (~/…)» |
| Juryens spørsmål 1–3 | JURY.md spm. 1–3 | OK |

## Det juryen ville trekke mest for (maks 5 rettinger, rangert)

1. **Selvmotsigelse om test.** JURY.md:4 sier test er «aldri brukt til å velge», men JURY.md:40 og ERLIG:49 sier at
   båndet [0,15; 0,85) ble valgt på test. ERLIG:34 sier «Ingen variant er valgt på test». JURY_SPORSMAL spm. 16
   viser til en formulering i JURY.md («låst på val 2025») som ikke står der lenger. Dette treffer «ærlig evaluering»
   direkte. Retting: én setning i JURY.md:4 og ERLIG:34 («unntak: rutingsbåndet, valgt på test, påvirker ikke F1»),
   og fjern den gamle kryssreferansen i spm. 16.
2. **Interne filer og sjargong i zipen.** `levering/KRAVRESPONS.md` begynner med «INTERN, ikke del av leveransen …
   landsbyens egen sjekkliste; flere HULL-punkter er utdaterte», men ligger i zipen. I .md-filene står «smed» 106
   ganger, «dommer» 77, «landsby» 47, «guden» 3 og `~` 7. 15 henvisninger av typen `landsbyrapport:…` i
   5 filer (mest NESTE_VERSJON.md, JURY_SPORSMAL.md) peker på filer juryen ikke har. Retting: ta `levering/KRAVRESPONS.md`
   ut av zipen, og merk `landsbyrapport:`-kildene som «ikke med i zipen».
3. **Tre README-er, to kravresponser, to JURY_SPORSMAL.** Rot-README, `levering/JURY_README.md` (kopi) og
   `c1/leveranse/README.md`. JURY_SPORSMAL finnes med 10 og med 19 spørsmål (overskriften sier «atten»). Kilde-URL-ene
   og AI-erklæringen, som reglene krever «i README», står bare i README nr. 3. Retting: flytt «Datakilder» og
   «AI-verktøy» (eller en lenke til dem) inn i rot-README, og si øverst i rot-README hvilke fire filer juryen skal lese.
4. **Kravresponsen er for tett.** Malen sier 3–5 setninger per overskrift. «Hvordan vi verifiserte det» har ca. 9
   og «Hva vi ville trengt videre» ca. 11, med V2-tallet 0,516, sitatstikkprøven og praksis/policy-tall blandet sammen.
   Golvet 0,415 (antakelsen om løpende historikk) bør stå som én klar setning. Retting: kutt til 5 setninger per overskrift
   og flytt resten til JURY.md.
5. **Små avvik som får en dataperson til å stusse.** 188 av 1 578 (kravrespons) mot 183 av 1539 (JURY.md, demo) går
   til menneske, uten forklaring. `demo_utskrift.txt` er fra 15:28 og sier «ikke frosset ennå» med utviklingssti.
   To sitatfelt per sak gir et sprikende sitat i demoens treff-sak (Mobimo: 5.2 passer, 5.2.1 årsrapport gjør det ikke).
   Retting: en halv setning om 1 578 med vs. 1539 med fasit, ny demo_utskrift fra kald kopi, og si i README hvilket
   sitatfelt som er «avgjørende punkt».

## Det som står sterkt (bør ikke røres)
Baseline-tabellen med KI og enkle regler, motstandstesten med de 6 som slipper forbi, `KJOR.sh` med frys- og tallvakt,
bommene (0 av 7 USA) og at demoen viser én bom. Dette er akkurat det reglene sier rangeres over «beste modell».

## Til repo4-lesingen (#2601)
De samme fem punktene gjelder trolig i repo4-zipen, siden de handler om tekst og pakking og ikke om modellen. Sjekk i
tillegg at hovedtallet er byttet overalt (rot-README, kravrespons, JURY.md, demo) og at «aldri brukt til å velge» ikke
blir enda mer feil når byttet er gjort etter måling på tre testår.
