# Case 1: robusthetstest på den frosne agenten (#2044 miks h2, real_votes test 2026) (smed2 #2144)

Kommando (fra landsbymappen, ca. 1 min per test): `python3 -I arbeid/oppgave_2144/robusthet_frossen.py --ut state/rapporter/c1_robusthet_frossen.md`

Agent: `arbeid/kandidater/smed2_c1_mot/.venv/bin/python arbeid/hack/levering/kjor_agent.py --csv INN --historikk KOPI --ut DIR` (standard ruting: kalibrert P(MOT) i [0,15, 0,85) + datafeil/ukjent type/ukjent selskap). Modellen er ikke endret.  
Måler: `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py DIR/_pred_uten_ruting.csv test --data real --score mot` (F1 på MOT mot styret, maskin alene).  
Forstyrrelsen legges i inn-fila OG i 2026-radene i en kopi av real_votes, fordi agenten bruker den lagrede raden for kjente saker. Fasit er urørt (måleren leser originalfila).

| test | F1 MOT | endring | saker | MOT-flagg | sendt til menneske | viktigste rutingsgrunner | hva |
|---|---|---|---|---|---|---|---|
| basis | 0.476 | +0.000 | 1578 | 74 | 11.9% | usikker 127, ukjent selskap 70, instruksjonslignende tekst i forslaget 1 | uendret |
| nye_selskaper | 0.375 | -0.101 | 1578 | 94 | 99.4% | ukjent selskap 1568, usikker 241, instruksjonslignende tekst i forslaget 1 | company_id/navn byttet til ukjente: ingen selskapshistorikk før 2026 |
| tom_tekst | 0.000 | -0.476 | 1578 | 0 | 100.0% | kan ikke vurderes 1578 | proposal_text tom i alle 2026-saker |
| tomme_felt | 0.000 | -0.476 | 1578 | 0 | 100.0% | kan ikke vurderes 1578 | company, ticker, country, market, proposal_number, proponent tomme |
| ukjent_type | 0.496 | +0.020 | 1578 | 72 | 14.3% | usikker 173, ukjent selskap 70, instruksjonslignende tekst i forslaget 1 | proposal_type = NY_SAKSTYPE i inn OG historikk-kopi (typen havner da i historikken, så vakta ser den ikke) |
| ukjent_type_inn | 0.476 | +0.000 | 1578 | 74 | 100.0% | ukjent forslagstype 1578, felt avviker fra lagret sak (proposal_type) 1578, modellen brukte lagret rad 1578 | proposal_type = NY_SAKSTYPE bare i inn-fila (som en ny sak); modellen bruker lagret rad |
| tomme_valgfri | 0.455 | -0.021 | 1578 | 49 | 100.0% | land/marked mangler (country,market), modellen bruker disse feltene 1578, ukjent selskap 70, usikker 61 | company, ticker, country, market, proposal_number tomme (felt agenten ikke krever) |
| uten_styret | 0.467 | -0.010 | 1578 | 98 | 100.0% | styrets anbefaling mangler 1578, usikker 189, ukjent selskap 70 | mgmt_rec og mgmt_rec_raw tomme (manglende styreanbefaling) |

Målerlinje «MOT mot styret» per test:

- basis: `MOT mot styret: TP 30 FP 38 FN 28  P 0.4412  R 0.5172  F1 0.4762  (58 i fasit)`
- nye_selskaper: `MOT mot styret: TP 27 FP 59 FN 31  P 0.3140  R 0.4655  F1 0.3750  (58 i fasit)`
- tom_tekst: `MOT mot styret: TP 0 FP 0 FN 58  P 0.0000  R 0.0000  F1 0.0000  (58 i fasit)`
- tomme_felt: `MOT mot styret: TP 0 FP 0 FN 58  P 0.0000  R 0.0000  F1 0.0000  (58 i fasit)`
- ukjent_type: `MOT mot styret: TP 30 FP 33 FN 28  P 0.4762  R 0.5172  F1 0.4959  (58 i fasit)`
- ukjent_type_inn: `MOT mot styret: TP 30 FP 38 FN 28  P 0.4412  R 0.5172  F1 0.4762  (58 i fasit)`
- tomme_valgfri: `MOT mot styret: TP 23 FP 20 FN 35  P 0.5349  R 0.3966  F1 0.4554  (58 i fasit)`
- uten_styret: `MOT mot styret: TP 35 FP 57 FN 23  P 0.3804  R 0.6034  F1 0.4667  (58 i fasit)`
## Hva tabellen sier (smed2, 05.11)
- **Ingen krasj** i noen av de 8 testene. Hver test tar ca. 5 s. Basis gir det frosne hovedtallet **0,4762** (TP 30, FP 38, FN 28), så oppsettet er riktig.
- **Nye selskaper:** F1 MOT faller til 0,375 (−0,10). Uten selskapshistorikk mister modellen sitt sterkeste signal (løpende MOT-historikk h2). Vakta «ukjent selskap» sender likevel **99,4 %** til et menneske. Agenten vet altså at den ikke vet.
- **Tom tekst / tomme felt (med proponent):** agenten nekter å vurdere sakene (`proposal_text` og `proponent` er påkrevd). Den følger styret og sender **100 %** til et menneske. F1 MOT er 0 med vilje, ikke på grunn av en feil.
- **Ukjent forslagstype:** når typen bare er ny i inn-fila (`ukjent_type_inn`, som ved en ekte ny sak), slår vakta til på alle saker: **100 % til menneske**, og prediksjonen er uendret (0,476). Raden `ukjent_type` (der typen også ligger i historikk-kopien) viser at modellen tåler en ny kategori: 0,496, +0,02 er støy. Der ser vakta ikke typen, fordi den da finnes i historikken. Det er en svakhet i testoppsettet, ikke i agenten.
- **Manglende styreanbefaling:** 0,467 (−0,01). Det gir flere MOT-flagg (98 mot 74), og recall stiger (0,60) mens presisjonen faller (0,38). Før #2152 gikk bare 15,3 % til menneske (tom `mgmt_rec` ble stille antatt FOR). Nå går **100 %** til menneske med grunnen «styrets anbefaling mangler: antatt FOR, sjekk innkallingen».
- **Tomme valgfrie felt** (country/market m.fl.): 0,455 (−0,02). Før #2152 *sank* andelen til menneske til 8,2 %. Nå går **100 %** til menneske med grunnen «land/marked mangler (country,market)».
Forslaget er gjort i #2152 (se under). Modellen og MOT-flaggene er urørt.
Ikke testet her: «siste år» (kortere historikk), som er dekket av «bare år før» i c1_enkle_regler_og_hist1.md (0,415).

## Nye menneske-vakter (smed #2152, 05.11)
- `c1_real.py` har to nye rutingsgrunner: **«styrets anbefaling mangler»** (både `mgmt_rec` og `mgmt_rec_raw` er tomme) og **«land/marked mangler»** (`country` eller `market` er tom). De påvirker bare `til_menneske` og `rutingsgrunn`. P(MOT), MOT-flagg og anbefaling er uendret.
- **Basis er byte for byte uendret:** agent.csv, _pred_uten_ruting.csv og pred_maaler.csv er identiske med kjøringen før endringen (cmp). F1 MOT er 0,4762 (TP 30, FP 38, FN 28), og **188** av 1578 saker går til menneske (11,9 %). Det er 183 av de 1539 sakene med fasit, som i akseptkravet. fremmed.sh fra kald kopi er grønn etter endringen (29 s, 129 påstander stemmer, 0 avviker).
- **Funn:** ekte data HAR tomme `mgmt_rec`, i 39 saker i 2026. I 38 av dem er `mgmt_rec_raw` «None» («Close Meeting», «Receive Report» og lignende punkter uten stemmeanbefaling), og i 1 er den «One Year». Dette er ikke manglende data. En første versjon som bare så på `mgmt_rec`, sendte disse 39 sakene til menneske (222 i stedet for 188). Vakta krever derfor at også `mgmt_rec_raw` er tom.
- Enkeltsak (`--sak`) uten mgmt_rec og country gir til_menneske=1 med begge grunnene.
