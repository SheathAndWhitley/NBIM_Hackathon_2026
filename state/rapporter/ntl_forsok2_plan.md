# Name that LLM: forsøk 2, Gaggle-rader i 1,5B LoRA trinn 1 mot kontroll med like mange pool-rader (#2804)

Én side. Bygger på forsøk 1 (`ntl_forste_eksperiment.md`, #2801: 7B mot 1,5B, `N_FULL=32000`, ca. 1000 steg). Ingen innsending. Case 1 er ikke rørt.
**KP:** forventet 17 370 rene Gaggle-rader og hookpunkt `op.sample(N_FULL, random_state=0)`. Fikk 17 370 (`ntl_gaggle_pool_1485.md:3`) og `ntl_3b.py:154`. Fila `arbeid/oppgave_1485/gaggle_ny_ren.parquet` (7,9 MB) finnes. Kolonnene er ikke lest lokalt, fordi pyarrow mangler i landsbymiljøet.

## Hvorfor dette er forsøk 2
- Uansett utfall i forsøk 1 er data neste spørsmål. Taper 7B (B − A < +0,005), er data reservesporet (#1484). Vinner 7B, skal den uansett ha mest mulig ren data.
- Gaggle er bare lukket for **kjeden** (#1485: −0,003). I LoRA er det **ikke testet**.
- Lærdom #1490: ekstra rader må måles mot en kontroll med **like mange ekstra pool-rader**. Ellers måler vi bare «mer data».
- Kjøring A fra forsøk 1 (1,5B, 32 000 pool-rader) brukes om igjen som referanse. Da trengs bare to nye kjøringer.

## Forsøket (1,5B, fp16, bare trinn 1, `FOLDS` tom, samme GPU-antall som A)
| Kjøring | Trinn 1-data | Rader | Steg (ca.) |
|---|---|---|---|
| A (fra forsøk 1) | 32 000 pool, `random_state=0` | 32 000 | 1000 |
| **K** (kontroll) | de samme 32 000 + 17 370 andre pool-rader (`random_state=1`, ikke i de 32 000) | 49 370 | 1540 |
| **G** (Gaggle) | de samme 32 000 + 17 370 Gaggle-rader | 49 370 | 1540 |
- K og G stokkes med samme frø (0) etter sammenslåing. Begge får lineært fallende læringsrate over sine 1540 steg.
- GPU: ca. 2 × 60 min (2,33 s/steg målt), totalt ca. 2 t, eller 7 % av ukekvoten. Det kan kjøres parallelt med 7B-kjøringen hvis Kaggle tillater to økter.

## Måler og hovedtall
- **Hovedtall:** `SJEKK` = `TRINN1 train.csv (ren OOF) bal.acc` (2699 rader, aldri i pool eller Gaggle), som **parvis G − K**. Dommeren setter måler 8733327407 på oppgaven før kjøringen.
- Støtte: G − A og K − A (verdien av mer data i det hele tatt), og treff per klasse for de 18 klassene.
- Støy: parvis SE ca. 0,008 (anslaget fra forsøk 1, UKONTROLLERT). Grensen +0,015 tilsvarer ca. 2 SE.

## Akseptregel (fastsatt FØR måling, endres ikke etter at tallet er sett)
1. **Bytt** (Gaggle inn i trinn 1 for neste fullkjøring, både 1,5B og 7B om den overlever): **G − K ≥ +0,015**, **og** ingen klasse faller mer enn 0,10 i treff fra K til G. Faren er gemini-3.8-flash: fra 0,93 til 0,77 i #1485, mulig feilmerking 3.7/3.8.
2. **Mellomsone** +0,005 ≤ G − K < +0,015, eller vakten i punkt 1 slår ut: ett forsøk til, G′, med Gaggle-rader **bare** for klassene som løftet seg rent i #1485 (glm-5.3-flash, gemini-3.1-pro, qwen3.8-max). Det måles mot K med samme regel. Deretter er saken avgjort.
3. **Lukk** (Gaggle lukket også for LoRA, i sporsjekk): G − K < +0,005.
4. K − A måles uansett. Er K − A < +0,005, mettes 1,5B allerede ved ca. 32 000 rader. Da er modellstørrelse (7B) viktigere enn data. Det tallet skal inn i dommen over forsøk 1.

## Forventet tall
- A er målt i forsøk 1 (ca. 0,49, UKONTROLLERT). K − A: ca. +0,02, fordi mer data hjalp 3B fra steg 1000 (#2801-kurvene).
- G − K: ca. +0,005, med 30 % sjanse for ≥ +0,015 (UKONTROLLERT). Argmax ble bedre med Gaggle i #1485 (+0,01), og LoRA bruker argmax, ikke ungarsk.

## Trukket vinkel (trekk 1793901467)
- **1. Logistikk, «bytt rekkefølgen på stegene» (valgt, med tall):** Gaggle-radene kjøres **sist** i trinn 1 (en læreplan) i stedet for stokket inn. Kost: én kjøring til (60 min GPU). Gevinsten er ukjent. **Forkastet i kveld:** stokket G må gi et tall først. En læreplan med lavere læringsrate på slutten gir Gaggle-radene mindre vekt, så den er dårligere hvis radene er gode. Den blir aktuell bare hvis G viser klassefall (vakten i punkt 1). Da skal den kjøres før G′.
- 2. Finans, «gjør støyen til signal»: radene vektes etter hvor sikker en pool-modell er på merket. Krever en ekstra modell. Forkastet.
- 3. Lingvistikk, bjelkesøk: ikke relevant for klassifisering. Forkastet.

## Smed-klar oppgavetekst (for smed3 eller smed4, fra 20:05, etter at A i forsøk 1 er ferdig)
**Tittel:** Name that LLM: forsøk 2, Gaggle-rader i 1,5B LoRA trinn 1 mot kontroll med like mange pool-rader (ingen innsending)
**Gjør:**
1. Kopier `arbeid/oppgave_1622/kernel_3b/ntl_3b.py` til egen mappe. Legg inn to miljøvariabler etter linje 154:
   - `EKSTRA=pool`: legg til 17 370 pool-rader som ikke er blant de 32 000 (`op_full.drop(op.index).sample(17370, random_state=1)`).
   - `EKSTRA=gaggle`: legg til `gaggle_ny_ren.parquet` (last den opp som Kaggle-datasett; kolonnene tilpasses `text` og `model`; rader med `model` utenfor de 18 klassene kastes, og antallet logges).
   - Slå sammen og stokk med `random_state=0`. Logg antall rader per klasse.
2. Kjør K (`MODELL=Qwen2.5-1.5B N_FULL=32000 EKSTRA=pool`) og G (`... EKSTRA=gaggle`). Bruk `FOLDS` tom, `MAXTID1_MIN=300`, og samme GPU-antall som A i forsøk 1.
3. Hent fra loggene SJEKK og treff per klasse på train.csv. Ta også med tapet per 100 steg.
**Akseptkrav:** `state/rapporter/ntl_forsok2_resultat.md` med SJEKK for A, K og G, G − K, K − A og en tabell over treff per klasse. Dommen følger regel 1–4 i `ntl_forsok2_plan.md` ordrett. Det blir ingen ny terskel. Stopp hvis G krasjer på kolonner eller etiketter: rapporter det, og ikke gjett merkene.
**Tidsboks:** 2,5 t (ca. 30 min bygging, ca. 2 t GPU). **Krever:** at dommeren har satt måleren på oppgaven før kjøringen.
