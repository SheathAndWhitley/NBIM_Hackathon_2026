# Case 1: ferdige utfallssetninger for dommen 18:45, BYTT og STÅR (#2647)

Grunnlag: c1_juryles_bytt.md pkt. 4 (vilkåret uten utfall), dommen #2603. Eneste tall i nye setninger: F1 0,512, TP 32 / FP 35 / FN 26 (fra `c1_etterfrys.md`). Klokkeslettene 17:02 og 18:45 står alt i tekstene. **HH:MM er eneste felt som fylles** (tiden dommeren noterer for grønn kald start, eller dommens tid ved STÅR).

Filer: `arbeid/hack/c1/leveranse/` (R = README.md, K = kravrespons.md, J = JURY_SPORSMAL.md, E = ERLIG_EVALUERING.md). Linjenummer sjekket 17:30.

Slik limer du inn (under 2 min): bytt HH:MM, kjør én `sed`/Edit per rad med «Finn» → «BYTT»- eller «STÅR»-teksten. Kjør tallvakta etterpå (`bash arbeid/verktoy/c1_etterfrys.sh`). Merk: ved STÅR rulles pakken tilbake fra STÅR-reserven; finnes setningen «på vilkår …» der, gjelder STÅR-kolonnen for reservens linjer.

## R:12 (README.md)
- **Finn:** `innen 18:45. Det gjorde den (se `ERLIG_EVALUERING.md` § 7).`
- **BYTT:** `innen 18:45. Vilkåret ble oppfylt: pakken ble reprodusert fra kald start kl. HH:MM med F1 0,512 (TP 32, FP 35, FN 26), se `ERLIG_EVALUERING.md` § 7.`
- **STÅR:** `innen 18:45. Vilkåret ble ikke oppfylt innen fristen, så kontrollagenten dømte STÅR kl. HH:MM, og den frosne agenten er levert (se `ERLIG_EVALUERING.md` § 7).`

## K:7 (kravrespons.md)
- **Finn:** `dømte BYTT kl. 17:02 på vilkår om grønn pakke innen 18:45.`
- **BYTT:** `dømte BYTT kl. 17:02 på vilkår om grønn pakke innen 18:45; vilkåret ble oppfylt: pakken reprodusert fra kald start kl. HH:MM, F1 0,512.`
- **STÅR:** `dømte BYTT kl. 17:02 på vilkår om grønn pakke innen 18:45; vilkåret ble ikke oppfylt, så dommen kl. HH:MM ble STÅR, og den frosne agenten er levert.`
- (Egen sak, ikke denne oppgaven: K:7 «[0,36; 0,59]» og «valgt på 2025 og kjørt én gang» er rettet i c1_juryles_bytt.md pkt. B/1.)

## J sp. 19 (JURY_SPORSMAL.md, avsnittet som slutter «**Den frosne agenten står.**», linje 81)
- **Finn:** `**Den frosne agenten står.**`
- **BYTT:** `**Den frosne agenten sto mot V2 og hybriden.** Senere ble repo4 byttet inn etter regelen i § 7; vilkåret ble oppfylt: pakken reprodusert fra kald start kl. HH:MM, F1 0,512.`
- **STÅR:** `**Den frosne agenten står.** Også repo4 (§ 7) ble avvist: vilkåret om grønn kald start innen 18:45 ble ikke oppfylt, dom STÅR kl. HH:MM.`

## J sp. 23 (JURY_SPORSMAL.md, linje 100, setningen som slutter «står i pakken.»)
- **Finn:** `og begge tallene står i pakken.`
- **BYTT:** `og begge tallene står i pakken. Byttet var på vilkår, og vilkåret ble oppfylt: pakken reprodusert fra kald start kl. HH:MM, F1 0,512.`
- **STÅR:** I STÅR er svaret feil i sin helhet (premisset «dere byttet»). Lim inn i stedet for hele svaravsnittet: `Nei, vi byttet ikke. Repo4 besto regelen, men vilkåret om grønn kald start innen 18:45 ble ikke oppfylt, så kontrollagenten dømte STÅR kl. HH:MM. Den frosne modellen er levert og når ikke målet 0,5, og vi sier det rett ut. Derfor er agenten beslutningsstøtte som sender usikre saker til et menneske, ikke en erstatning for analytikeren.`

## E § 7 (ERLIG_EVALUERING.md:79)
- **Finn:** `**Status: kontrollagenten dømte BYTT til repo4 kl. 17:02 på vilkår om grønn pakke innen 18:45.**`
- **BYTT:** `**Status: kontrollagenten dømte BYTT til repo4 kl. 17:02 på vilkår om grønn pakke innen 18:45. Vilkåret ble oppfylt: pakken reprodusert fra kald start kl. HH:MM, F1 0,512 (TP 32, FP 35, FN 26).**`
- **STÅR:** `**Status: kontrollagenten dømte BYTT til repo4 kl. 17:02 på vilkår om grønn pakke innen 18:45. Vilkåret ble ikke oppfylt, så dommen kl. HH:MM ble STÅR: den frosne agenten er levert, og tallene under er bare dokumentasjon av forsøket.**`

## Sjekk
- Alle fem «Finn»-strenger finnes nøyaktig én gang i dagens filer (grep 17:30).
- Nye tall: bare 0,512 og 32/35/26, alle i `c1_etterfrys.md`. STÅR-setningene har ingen nye tall.
- Tallvakta: BYTT-setningene sier 0,512 = hovedtallet, skal gi 0 avvik. STÅR-setningene nevner ikke hovedtallet.
