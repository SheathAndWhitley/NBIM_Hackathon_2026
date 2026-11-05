# Name that LLM: plan for første innsending fra kl. 20:05 (#2750)

Én side. Den samler `ntl_oppstart.md` (#2525), `ntl_forste_forsok.md` (#2510) og de åpne oppgavene #2560–#2562. Den endrer ingen av tallene der. Case 1-filer er ikke rørt.
KP: forventet 0,6212 nestet for snittet 3B+1,5B, fikk 0,6212 (ntl_3b_innsending.md:11). Forventet 0,586 offentlig for 1,5B-LoRA, fikk 0,586 (ntl_lora_resultat.md:44, ref 57968608).

## Utgangspunkt
- Beste offentlige: **0,586** (1,5B-LoRA, #1621). Beste lokale: **0,6212 nestet** (snitt 3B+1,5B, #1634), ikke sendt inn.
- Gapet fra nestet til offentlig er målt én gang: −0,025 (±0,03). Målet 0,65 offentlig tilsvarer da ca. **0,675 nestet**, altså +0,054 over det beste vi har.

## Hva vi leverer først: snittkjernen (oppgave A, #2561, smed4)
- Kjernen med likt snitt av 3B og 1,5B, bygget med `arbeid/oppgave_1618/bygg.py` (#1765). Ingen vektfisking.
- Den sendes **bare hvis** SJEKK ≥ 0,575 i kjerneloggen **og** nestet ≥ 0,618 hos dommeren. dommer2 må ha kjørt frys (`ntl_frys.py`) og kaldstart. Dommeren godkjenner innsendingen. Det blir 1 av 5 innsendinger i dag.
- Forventet offentlig: **0,59–0,60**. Hovedgevinsten er måling nr. 2 av gapet. Etter den bruker vi snittet av de to gapene i omregningen.

## Måleren (dommer, kl. 20:00–20:30, før noe forsøk teller)
- `tavle maaler --oppgave <id>` på **hver** NTL-oppgave: `arbeid/name_that_llm/maaler/maaler.py --uten-sann`. Tavlas måler-id er 8733327407; fila har sha1 64c6831405 i dag. Måleren skal ikke arve fra Case 1-målerne (#2139-feilen).
- Hovedtall: **nestet balansert treffsikkerhet** fra `arbeid/oppgave_1618/blend.py` på forsøkets OOF (`NTL_LORA_DIR`). Bare offentlig Kaggle-score teller som målt. Vi sender bare forsøk med nestet ≥ beste − 0,003.

## De to vinklene smedene starter på
| | Vinkel | Hvem | Første test og stoppregel | Kost |
|---|---|---|---|---|
| 1 | **Større modell:** 7B QLoRA 4-bit på et fast utvalg av 25 % av Open Pool (oppgave B, #2562) | smed2 | Under 250 tok/s etter 10 min: stopp. Trinn 1 SJEKK > 0,5665: fortsett. Under 0,55: 7B lukkes. | 30 min å bygge, ca. 7,5 t GPU (UKONTROLLERT anslag) |
| 2 | **Varians eller mangfold:** trinn 2 for 1,5B med nytt frø (10+f → 100+f), snittet med gammel OOF (oppgave C) | smed3 når diskrydden #2751 er ferdig | Nestet mot 0,6109. Løft ≥ +0,008: det er varians, flere frø gjør jobben og 7B nedprioriteres. Løft < +0,003: mangfoldet er ekte, og 7B prioriteres. | 60 min, ca. 30 min GPU, 0 innsendinger |
- Oppgave C finnes **ikke** på tavla ennå. Ordføreren må opprette den, med teksten fra `ntl_forste_forsok.md` avsnitt C.
- Trukket vinkel (topologi: «budsjettfordeling som bandit»): GPU-kvoten er 30 t per uke. A+B+C koster ca. 0,85 + 7,5 + 0,5 = **8,85 t (30 %)**. Kjør de billige armene først, for C avgjør verdien av B. Viser C at løftet er varians, erstatter 3 frø à 30 min (1,5 t) det meste av B. Det sparer ca. 6 t, altså 20 % av uka. B startes likevel straks, fordi den tar lang tid, men den dømmes først etter C.
- Speideren (#2560, 40 min) kan endre rekkefølgen. Bruker topp 20 noe som er bedre enn LoRA på 7B (data, ensembler, frø), vinner det over B.

## Lukkede spor (sporsjekk 'name that llm': 15 treff, 1 lukket, ingen nye)
- Overflatestil, funksjonsord, tokenizer-n-gram, NCD, trio-temperatur og parvis trio-logit: alle under støy (#1491).
- Sentrering/ungarsk innen klynge: 0,5705 lokalt, men **0,342 offentlig** (#1546, #1468). Bryter når testen har 1–3 svar per prompt.
- Gaggle-rader i kjeden: ingen løft (#1485). Gjelder bare kjeden. Som trinn 1-data for LoRA er det reserve fra fredag kl. 14 (#1484).
- Rå 3B alene: ikke sendt (#1634). 3B var ikke bedre enn 1,5B fordi den bare så 66 % av poolen. Det er ikke en lukking av større modeller.

## Stopp-punkter og ærlighet
- Fredag kl. 14: står ikke 7B SJEKK over grensa, går vi over til data (Gaggle-supersett i LoRA trinn 1).
- A gir ca. +0,010. Bare 7B ser ut til å kunne nå 0,65, og sjansen anslås til ca. 25 %. Står vi under 0,62 offentlig søndag, melder vi tallene til guden i stedet for å bruke flere dager.
