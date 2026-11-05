# Case 1 (#2754): siste lesning av ærlighetsdelen etter lekkasjetallene – 3 setninger til smed2

Lest: `arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md` og `KANDIDATER.md` (mappa, ikke zipen fra 17:44, som er eldre; #2740 bygger ny).
Ingen modellendring. Tallene under er hentet fra `kilder/c1_lekkasje_effekt.md` (2024 0,5057→0,4973, 2025 0,5309→0,5153, 2026 0,5120→0,5636).
KP: forventet repo4 0,5057/0,5309/0,5120, snitt 0,5162 i ERLIG § 7, og fikk 0,506/0,531/0,512 og 0,516. Det stemmer.

## 1. ERLIG_EVALUERING.md § 2, linje 28 (sterkere enn tallene, gjelder ikke levert modell)
Står nå: «h2 bruker NBIMs stemmer fra møter **strengt før** sakens dato i samme sesong. Kontrollagenten fant ingen lekkasje fra samme møte: 400 tilfeldige rader ble sjekket, og det ga 0 avvik [AD].»
Problem: Dette gjelder bare miks h2. Levert repo4 har 15 avvik på 400 rader (samme-dags-møter, KANDIDATER #2731). Juryen leser § 2 som forbeholdet for modellen som er levert.
Foreslått: «Miks h2 bruker NBIMs stemmer fra møter strengt før sakens dato i samme sesong (400 rader, 0 avvik [AD]). De fire repotrekkene i levert repo4 kan også bruke et annet møte samme dag (15 avvik på 400 rader, § 7). Med bare strengt tidligere dato blir F1 på MOT 0,497/0,515/0,564 (snitt 0,525). Endringen kommer av at valideringsåret velger en annen C og grense, ikke av samme-dags-treff (`kilder/c1_lekkasje_effekt.md`).»

## 2. ERLIG_EVALUERING.md § 7, linje 104 (marginen i avgjørende år er ikke robust)
Står nå: «De ble målt etter at regelen var skrevet (16:49–16:51) og gir +0,051 og +0,017 over frossen, i snitt +0,034. Det oppfyller kravet om +0,02 uten 2026.»
Problem: Lekkasjetallene står ikke noe sted i ERLIG. Med strengt tidligere dato er repo4 i 2025 0,515 mot frossen 0,514, altså +0,001 og ikke +0,017. Byttet holder fortsatt etter regelen (snitt +0,044, verste år +0,001 ≥ −0,02), men gevinsten i 2025 er borte.
Foreslått: legg til etter setningen: «Med historikk bare fra strengt tidligere dato (§ 2) blir gevinsten +0,042 og +0,001. 2025-gevinsten er altså innenfor valgstøyen (±0,05 per år fra nytt C/grense-valg), og bare 2024 bærer byttet.»

## 3. KANDIDATER.md linje 37 (utdatert, motsies av linje 41)
Står nå: «Det svekker repo4 litt: noe av tallet kan komme fra stemmer i samme-dags-møter … Treårstallene (snitt 0,5162) er ikke målt på nytt uten de berørte radene, …»
Problem: Linje 41 (dom #2744) har nå målt dette. 0/0/1 flagg endres, og F1-endringen kommer av modellvalget. Juryen ser to avsnitt etter hverandre som sier det motsatte.
Foreslått: bytt de to setningene med: «Effekten er nå målt (neste avsnitt): på de berørte radene endres 0/0/1 flagg, så tallet kommer ikke fra samme-dags-treff.»

## Sett, men ikke tatt med (kutt for å holde meg til 3)
- I `c1_lekkasje_effekt.md` betyr «frossen» repo4, mens den i ERLIG betyr #2044. KANDIDATER linje 41 er riktig. Bare kilden er tvetydig.
- ERLIG linje 59/62 («strengt før», «ingen etiketter fra samme møte») står i den ordrette 13:06-teksten. Rettes pkt. 1, bør en åttende kulepunkt i § 6 si at dette er utdatert for repo4. Det er valgfritt.
