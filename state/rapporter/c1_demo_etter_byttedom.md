# Case 1 demo fra kald kopi, før byttedommen (#2577): STÅR er grønt, BYTT tørrkjørt med to hindre

Begge sporene ble kjørt 16:54–17:02 (smed), før dommen. **Dom 17:01 (#2570, c1_byttedom_265.md): BYTT til repo4.** Den ekte demoen med ny frys kan først kjøres når #2592 har laget frysen. Den er en del av akseptkravet i #2592 (kald kopi F1 MOT 0,5120), og tørrkjøringen under viser at den virker når tekstrestene er rettet.

## STÅR (frossen #2044 miks h2): GRØNN
`sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald_2577 --ny` fra landsbymappen, ny kald kopi:
- HOVEDTALL F1 MOT (måler v3 --score mot): **0.476190** (avvik-sidetall 0.481752)
- FRYSVAKT GRØNN (17 filer like frysen 16:00:01), TALLVAKT GRØNN, ORDVAKT GRØNN, exit 0
- kjøretid: hele demo.sh **33 s**, agenten i kopien 21 s
- hash: ut/agent.csv `1543706f9d94…f3a1a`, ut/pred_maaler.csv `b113b545dd86…3653`, byte-like kopien fra 16:01 (/tmp/c1_kald_1975)
- demo_utskrift.txt er skrevet på nytt. Bare linje 2 er endret («ny kald kopi … 16:54» i stedet for «gjenbrukt … 16:01»). Ny sha256 `264fa5be…3f1a`.
- `frys_diff.sh --kilde` viser ENDRET i ERLIG_EVALUERING.md (#2571 pågår) og demo_utskrift.txt (linje 2). Det er bare tekst, og det tas med i tekststoppen kl. 19 (#2549).

**Står dommen: ingenting mer å gjøre for demoen.**

## BYTT (repo4): tørrkjørt i egen git-worktree i /tmp, ekte filer ikke rørt
Jeg kjørte en kopi av bytt.sh --utfor (egne /tmp-navn, uten steg 6) og så demo.sh fra ny kald kopi:
- agenten: F1 MOT **0.5120** (TP 32 FP 35 FN 26, P 0,4776, R 0,5517), til menneske 164/1578 (10,4 %), 161/1539 på test. Dette stemmer med #2572.
- demo med ny modell virker: HOVEDTALL 0.512000, frysvakt grønn (21 filer), ordvakt grønn, ca. 34 s. Utskrift: `state/rapporter/c1_demo_bytt_torr_2577.txt`
- hash: pred_maaler.csv `d02cf884…4a0c`, agent.csv `24ee6b18…a0c`

**To hindre før en BYTT-demo blir grønn:**
1. **TALLVAKT RØD, 54 avvik i 13 filer** etter bytt_tall.py (180 erstatninger). fremmed.sh går da ut med feil, og `demo.sh --ny` stopper. Restene er avrundede former og andre tellinger som bytt_tall.py ikke dekker: «P 0,44», «R 0,52», «til menneske 183 av 1539» (skal bli 161), «0,476» i noen setninger, og i tillegg BESLUTNINGSSTOTTE 8, JURYSVAR 13, levering/README 11. **Rettet 17:02 (smed):** `bytt_tall.py` dekker nå 183 av (de) 1539 -> 161, 11,9 % rett etter 1539 -> 10,5 %, P 0,44 -> 0,48, R 0,52 -> 0,55 og 30/38/28 -> 32/35/26. Testet på dagens tekster i kald kopi /tmp/c1_kald_2577b med tallvakta mot repo4-kjøringen: 227 erstatninger, **avvik 54 -> 23**. De 23 som står igjen ligger alle på linjer som også nevner frossen/2025/V1, og dem rører skriptet med vilje ikke. De må skrives om eller merkes «eldre» for hånd, med 1–5 per fil i 11 filer (JURYSVAR 5, BEGRENSNINGER 5). Liste: `state/rapporter/c1_bytt_tallvakt_rester_2577.txt`. Med `--rester` skriver skriptet også linjene «FOR HÅND». Tallet 54 gjaldt HEAD-tekstene, mens 23 er målt på arbeidstreets tekster kl. 17:02; endrer andre tekstene før byttet, kan tallet flytte seg litt. Anslag nå: ca. 10 min for hånd (23 linjer) i tillegg til KI/TN/modellnavn i steg 2.
2. **DEMO_MANUS.md må skrives om**: vis_manussaker melder AVVIK FRA MANUS. treff_maskin blir 2033470|1 (Kura Sushi, linje 15) og til_menneske blir 2038357|7 (H. Lundbeck, linje 39). Bom-saken (LOTTE) står.
3. Mindre ting: demo.sh og demo-utskriften sier fortsatt «modell miks h2» (allerede i BYTTEPLAN steg 2). `k()` i bytt.sh har `|| true`, så et steg som feiler, stopper ikke skriptet, og det skriver «Ferdig» likevel. Les utskriften linje for linje.

Pakkefasiten (frys_fasit.py) ble ikke testet i worktree-en, fordi den trenger rapportfiler jeg ikke kopierte. Det er ikke en feil i planen.

## Kommando etter dommen
- STÅR: ingenting. Valgfritt: `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald_x --ny`, vent grønt på tre vakter og 0.476190.
- BYTT: bytt.sh --utfor, rett de 23 restene (lista) og DEMO_MANUS, så `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald_bytt --ny`. Forventet 0.512000 og tre grønne vakter.
