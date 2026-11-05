# Case 1: de små teksthullene fra dommer2 er rettet (#2345, speider, 05.11 kl. 15.15)

Kilde: `state/rapporter/c1_hull_status.md`, «Konkrete rettinger» pkt 1–7. Bare dokumenttekst. Ingen agentfiler og ingen filer fra `c1_frys.py` FILER er rørt (frysen er ikke tatt ennå, `c1_frys.py sjekk` utgang 0). `levering/README.md` er urørt, så linje 13–17 står som før.
**Aksept:** `sh arbeid/hack/levering/fremmed.sh /tmp/fremmed_2345` gir `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190` og `TALLVAKT GRØNN` (logg `/tmp/fremmed_2345.log`).

## Hva er rettet
| Hull | Fil | Retting |
|---|---|---|
| H3 | `levering/EN_SIDE.md` (2 steder), `levering/SLIDE.md`, `levering/BESLUTNINGSSTOTTE.md` (2), `c1/leveranse/ERLIG_EVALUERING.md:51` | «bånd låst på val» → kalibrering lært på val 2025, båndet valgt på test-tabellen og sjekket på val (7,5 % / 7,9 %) |
| H13 | `c1/leveranse/JURY.md:32`, `c1/DEMO_MANUS.md:5` | JURY: `kjor.sh` fra tom mappe (som `c1/leveranse/README.md`) + logg `levering/kjor_agent_real_test2026.txt`. DEMO: `fremmed.sh /tmp/fremmed` og `/tmp/fremmed/ut/agent.csv`, samme mappe som `levering/README.md` |
| H6 | ny `c1/leveranse/kilder/tell_aar.py` + `tell_aar.txt`; `JURY.md` pkt 6 og linje 32; `kilder/LESMEG.md` | Telling bekrefter 92/70/82/95/77/88/99 (2019–2025), 58 i 2026; test 2026: 141 møter, 136 selskaper (140/135 blant de 1539 med fasit) |
| H9 | `levering/JURYSVAR.md` svar 6 | Broen skrevet, **men med annen forklaring enn dommer2 foreslo** (se under) |
| H12 | `c1/leveranse/kilder/TREFFSIKKERHET.md` | Én linje øverst: «konfidens < 0,6» = flagget `til_menneske`, samme 183 saker som båndet + vaktene i JURY.md pkt 8 |
| H7/H8 | `c1/DEMO_MANUS_5min_tilfeldige.md` | 799/18 → 999/19 (talt i `c1/kilder/nbim_begrunnelser.csv`: 999 rader, 19 unike `begrunnelse`); «arrangørens måler» → «vår egen måler (`maaler_offisiell_v3.py`)». Lenka i DEMO_MANUS.md:8 står |
| pkt 7 | `c1/leveranse/kravrespons.md:10` | + «punktestimatet 0,476 er under målet vårt på 0,5» |

## H9: de 3 er ikke AVSTÅ/annet
Verifisert med `arbeid/oppgave_2345/bro_74_71_68.py` på `levering/kjor_agent_real_maskin_alene.csv` (frossen) og mot `kjor_agent_real_test2026.txt` («inn: 1578 saker; MOT styret 74»; train.py «n_pred_MOT 71» på 1539) og begge `agent.csv` (oppgave_2260 og /tmp/fremmed):
- 74 avviksflagg på 1578 inn = **71 MOT-flagg** (styret FOR, agenten MOT) + **3 der styret anbefalte MOT og agenten sier FOR** (HP `2045311|16`, Hartford `2066391|14`, Snowflake `2086078|6`; NBIM stemte FOR i alle tre, så de er riktige avvik).
- Av de 71 MOT-flaggene mangler 3 fasit → **68 MOT-flagg** på de 1539 med fasit (TP 30, FP 38) i måler v3.
- «71» i train.py-loggen er et annet tall som tilfeldigvis er likt: 71 avviksflagg blant de 1539 med fasit (68 + 3; avvik TP 33 = 30 + 3).
Dommer2s forslag («68 når de 3 med fasit AVSTÅ/annet holdes utenfor») ville vært feil og er ikke skrevet.

## Diff per fil
```diff
--- a/levering/EN_SIDE.md
+++ b/levering/EN_SIDE.md
@@ -10,7 +10,7 @@
   utviklede (DM) og fremvoksende (EM) markeder, alle sakstyper; test 2026 er 136 selskaper i 31 land
   (`omfang.txt`). Ikke andre forvaltere, ikke selskaper utenfor utvalget.
 - Fasit er NBIMs egne stemmer (real_votes). Splitt etter møteår, aldri tilfeldig: val 2025, **test 2026**.
-  Grensen (p ≥ 0,919) og båndet til menneske er låst på val før test.
+  Grensen (p ≥ 0,919) er låst på val før test; kalibreringen er lært på val 2025; båndet er valgt fra et fast rutenett på test-tabellen og sjekket på val (7,5 % val, 7,9 % test, `c1_menneske_terskel.md`).
 - Ingen lekkasje: historikk bare fra møter strengt før møtedatoen; fasitkolonner
   (`nbim_vote`, `rationale_*`, `position_paper`) stoppes med assert.
 - Gulvet «følg styret» har **F1 på MOT = 0**. Derfor måles F1 på MOT, ikke accuracy.
@@ -30,7 +30,7 @@
 Accuracy **95,7 %** er *lavere* enn følg styret (**96,2 %**): bare 3,8 % er MOT, så den som aldri sier MOT
 finner null. Agenten finner 30 av 58.
 
-**4. Når saken går til et menneske.** (a) Usikre saker: kalibrert P(MOT) i båndet [0,15; 0,85), låst på val 2025
+**4. Når saken går til et menneske.** (a) Usikre saker: kalibrert P(MOT) i båndet [0,15; 0,85) (kalibreringen er lært på val 2025; båndet er valgt fra et fast rutenett på test-tabellen og sjekket på val (7,5 % val, 7,9 % test, `c1_menneske_terskel.md`))
 (`--baand`). (b) Datafeil eller ukjent selskap/sakstype. (c) Mistenkelig fritekst («ignore … vote against»
 renses og rutes). (d) MOT-flagg uten sitat. Rutingen endrer aldri maskinens svar, bare hvem som ser saken.
 
--- a/levering/SLIDE.md
+++ b/levering/SLIDE.md
@@ -9,7 +9,7 @@
 
 **Metode.** Logistisk regresjon + LightGBM (snitt av rangene) på forslagstekst (TF-IDF), sakstype, forslagsstiller,
 styrets anbefaling, land/marked og NBIMs *tidligere* MOT-stemmer
-(bare møter før møtedatoen; fasitkolonner stoppes med assert). Grense og menneskebånd låst på val før test³.
+(bare møter før møtedatoen; fasitkolonner stoppes med assert). Grense låst på val før test³; menneskebåndet valgt på test-tabellen og sjekket på val.
 
 | test 2026, frosset modell #2044 | F1 på MOT | presisjon | recall | accuracy |
 |---|---|---|---|---|
--- a/levering/BESLUTNINGSSTOTTE.md
+++ b/levering/BESLUTNINGSSTOTTE.md
@@ -2,7 +2,7 @@
 
 **Hva agenten gjør:** Den leser sakslista før generalforsamlingene og peker ut sakene der NBIM trolig vil stemme **mot styret**. Den stemmer aldri selv. Mennesket avgjør alltid.
 
-**Grunnlaget:** NBIMs egne stemmer (real_votes), alle markeder og sakstyper (styrevalg, revisor, lønn, utbytte osv.). Tallene under er målt på **test 2026: 1539 saker, 66 ekte avvik fra styret (58 MOT, resten 5 AVSTÅ og 3 andre avvik)**, som modellen aldri så under bygging. Modellen er frosset (#2044, smed2 miks h2), og terskel og bånd er valgt på 2025 før test ble kjørt (`state/rapporter/c1_terskeltabell.md`, #2084).
+**Grunnlaget:** NBIMs egne stemmer (real_votes), alle markeder og sakstyper (styrevalg, revisor, lønn, utbytte osv.). Tallene under er målt på **test 2026: 1539 saker, 66 ekte avvik fra styret (58 MOT, resten 5 AVSTÅ og 3 andre avvik)**, som modellen aldri så under bygging. Modellen er frosset (#2044, smed2 miks h2), og terskelen er valgt på 2025 før test ble kjørt (`state/rapporter/c1_terskeltabell.md`, #2084); kalibreringen er lært på val 2025; båndet er valgt fra et fast rutenett på test-tabellen og sjekket på val (7,5 % val, 7,9 % test, `c1_menneske_terskel.md`).
 
 **Hva MOT-stemmene er:** 56 av 58 MOT i test 2026 er stemmer mot styrets *egne* forslag, og 29 av agentens 30 treff er der. Agenten er altså ikke «aksjonærforslag = MOT»; den regelen kan finne høyst 2 av 58 (`c1_forslagsstiller.txt`, #2183).
 
@@ -72,7 +72,7 @@
 ## Forbehold (les disse)
 - **Få MOT-stemmer.** Test har bare 58 MOT mot styret (66 avvik med AVSTÅ). Én sak flytter fanget-andelen 1,7 prosentpoeng. F1 for maskinen alene er 0,476 på MOT mot styret, 95 % intervall 0,36–0,59 (#2087, #2095). Alle tall i tabellen over er på MOT (58). Les dem som «rundt», ikke som presise.
 - **«Fanget» er en øvre grense.** Den antar at forvalteren avgjør alle saker i sonen riktig. Gjør forvalteren feil på noen, blir andelen lavere. Gulvet (forvalteren følger styret i sonen) er 16 %.
-- **Båndet er valgt på 2025.** [0,15; 0,85) sendte 7,5 % av val 2025 videre og 7,9 % av test 2026 (#2128). Kalibreringen er en trapp med få trinn, så båndet kan bare flyttes mellom trinnene (`c1_menneske_terskel.md`).
+- **Båndet er valgt på test-tabellen og sjekket på val.** Kalibreringen er lært på val 2025. [0,15; 0,85) sendte 7,5 % av val 2025 videre og 7,9 % av test 2026 (#2128). Kalibreringen er en trapp med få trinn, så båndet kan bare flyttes mellom trinnene (`c1_menneske_terskel.md`).
 - **Sonen er mer enn båndet.** Ukjent selskap eller type, datafeil, injeksjon og MOT uten sitat går også til menneske. Tabellen viser begge: 122 saker i båndet, 183 i alt (11,9 %, 188 av 1578 inn med sakene uten fasit; #2132).
 - **Historikk må være oppdatert.** Agenten bruker NBIMs stemmer tidligere i samme sesong. Uten den faller F1 på MOT mot styret fra 0,476 til 0,415 [0,30; 0,53] (#2134, `c1_enkle_regler_og_hist1.md`).
 - **Terskelen er skjør.** Agentens sannsynligheter er presset sammen øverst. Flyttes grensen fra 0,92 til 0,83, dobles flaggene og F1 faller til 0,35 (`case1_svakheter_2082.md`). Bytt derfor oppsett med `--baand`, ikke ved å skru på p-verdien for hånd.
--- a/levering/JURYSVAR.md
+++ b/levering/JURYSVAR.md
@@ -23,7 +23,7 @@
 Ja. Gulvet som er lov, «følg styret», gir F1 0. Den sterkeste enkle regelen vi har målt, «MOT hvis samme selskap og samme forslagstekst fikk MOT før» (b2), gir **0,365 [0,25; 0,49]** på real_votes test 2026 med v3 `--score mot`. Modellen slår den med **+0,11 [0,01; 0,22]** (parret klyngebootstrap, #2134, `state/rapporter/c1_enkle_regler_og_hist1.md`, kald kopi #2139). Den gamle presedensregelen «MOT hvis NBIM stemte MOT på selskapet før» gir 0,097, og «samme tekst fikk MOT før» 0,287. Med bare historikk fra tidligere år gir modellen 0,415 [0,30; 0,53], som er nedre grense hvis stemmene ikke publiseres løpende.
 
 **6. Siterer agenten NBIMs retningslinjer?**
-Ja, den leverte agenten gjør det. Hver sak i `agent.csv` får et ordrett avsnitt fra NBIMs *Global Voting Guidelines* (nbim.no) i `retningslinje_id`/`retningslinje_sitat`. På test 2026 er det 1578 rader og 15 ulike avsnitt: 1504 er FOR-standarden NBIM 0.0.3 («Our starting point … is to support the board»), og 74 er et konkret punkt (71 MOT-flagg og 3 saker der styret selv sa MOT og agenten sier FOR). Alle 15 står ordrett på nbim.no i dag: #2130 kontrollerte alle 140 GVG-punkter i den lokale kopien, og den frosne agenten siterer bare punkter derfra (dommeren talte 15 ulike på den frosne agenten, #2278; tallet 18 var fra en kjøring kl. 12:47 før oppslaget ble endret). Agenten finner samme seksjon som NBIM selv oppga i 54 av 63 MOT-saker (86 %, #2106). I stikkprøven på 20 MOT-saker (#2115) var 20/20 ordrette, men bare **15/20 var regelen som avgjør**: 4 var delvis riktige (riktig seksjon, svakere avsnitt) og 1 var feil. De fem rettes i #2120. Sitatet sier hvor mennesket skal lese. Det er ikke et bevis for stemmen.
+Ja, den leverte agenten gjør det. Hver sak i `agent.csv` får et ordrett avsnitt fra NBIMs *Global Voting Guidelines* (nbim.no) i `retningslinje_id`/`retningslinje_sitat`. På test 2026 er det 1578 rader og 15 ulike avsnitt: 1504 er FOR-standarden NBIM 0.0.3 («Our starting point … is to support the board»), og 74 er et konkret punkt (71 MOT-flagg og 3 saker der styret selv sa MOT og agenten sier FOR). Broen til 68 i treffsikkerhetstabellen: av de 71 MOT-flaggene mangler 3 fasit, så måler v3 teller 68 MOT-flagg blant de 1539 med fasit (30 riktige, 38 falske). De 3 der agenten sier FOR mot styrets MOT (HP, Hartford, Snowflake) er riktige avvik (NBIM stemte FOR) og telles som treff på avvik, ikke som MOT. Talt med `arbeid/oppgave_2345/bro_74_71_68.py`. Alle 15 står ordrett på nbim.no i dag: #2130 kontrollerte alle 140 GVG-punkter i den lokale kopien, og den frosne agenten siterer bare punkter derfra (dommeren talte 15 ulike på den frosne agenten, #2278; tallet 18 var fra en kjøring kl. 12:47 før oppslaget ble endret). Agenten finner samme seksjon som NBIM selv oppga i 54 av 63 MOT-saker (86 %, #2106). I stikkprøven på 20 MOT-saker (#2115) var 20/20 ordrette, men bare **15/20 var regelen som avgjør**: 4 var delvis riktige (riktig seksjon, svakere avsnitt) og 1 var feil. De fem rettes i #2120. Sitatet sier hvor mennesket skal lese. Det er ikke et bevis for stemmen.
 I tillegg viser agenten NBIMs egen begrunnelse (`rationale_text`) fra en lignende sak i et **tidligere år**. Det er et sitat, ikke et trekk: modellen leser aldri `rationale_*` (assert i `oppgave_2044/train.py`), sitatet hentes etter at MOT/FOR er bestemt, og samme år, senere år og samme møte er utelukket (`c1_real.py:107`). Prediksjonene er byte-like med og uten sitatene (#2106). 8 av 20 slike begrunnelser er skrevet etter en eldre versjon av retningslinjene og står ikke ordrett på nbim.no i dag (#2130).
 
 **7. Hva gir rutingen til et menneske egentlig?**
--- a/c1/leveranse/JURY.md
+++ b/c1/leveranse/JURY.md
@@ -29,14 +29,14 @@
 Derfor har vi én regel: **bare endringer som vinner både 2024 og 2025 kommer inn.** Test 2026 brukes aldri til å velge. Den kjøres på den frosne agenten og rapporteres som den er. Et lavere ærlig tall er mer verdt for forvalteren enn et høyere tall vi har tilpasset teståret.
 
 ## Begrensninger: hva agenten ikke kan
-Den frosne agenten (modell «miks h2»), test 2026 (NBIMs egne stemmer, 1539 saker med fasit, 58 MOT mot styret). Tall fra måler v3 (`maaler_offisiell_v3.py ... test --data real`, kald kjøring `/tmp/c1_kald` 05.11 12:29) med mindre annet står. Egen telling: `kilder/oppgave_2216_tell.py`.
+Den frosne agenten (modell «miks h2»), test 2026 (NBIMs egne stemmer, 1539 saker med fasit, 58 MOT mot styret). Tall fra måler v3 (`maaler_offisiell_v3.py ... test --data real`, kald kjøring med `kjor.sh` fra tom mappe `/tmp/c1_kald` 05.11, se `README.md`; agentens logg `levering/kjor_agent_real_test2026.txt`) med mindre annet står. Egen telling: `kilder/oppgave_2216_tell.py` (2x2 per forslagsstiller) og `kilder/tell_aar.py` (MOT per år, møter og selskaper, utskrift `kilder/tell_aar.txt`).
 
 1. **F1 0,476 betyr: agenten finner 30 av 58 MOT og overser 28. Av 68 MOT-flagg er 38 falske** (P 0,441, R 0,517; måler v3). Ca. hvert annet flagg er feil, og hver annen MOT blir ikke flagget.
 2. **Tallet er usikkert: 95 % KI [0,36; 0,59]** fordi test bare har 58 MOT (klyngebootstrap per selskap, `kilder/oppgave_2095_ki_mot.py`; bootstrap over rader i `c1/tall_tabell.md` gir [0,37; 0,59]). Målet 0,5 ligger inne i intervallet, men punktestimatet er under. Val 2025 gir 0,520 på MOT (0,522 i ablasjonstabellen er F1 på avvik), men grensen er valgt der (`kilder/c1_val_kaldstart.md`). Seed er ikke det som gjør tallet usikkert: med 5 andre LightGBM-seed gir samme agent 0,462–0,522 på test (snitt 0,483), så 0,476 er et typisk seed-utfall og ikke et heldig ett, og spredningen er mye mindre enn KI-et (`kilder/c1_seed_frossen.md`).
 3. **17 av de 28 bommene ser ingen.** De får P(MOT) ≤ 0,09 og rutes ikke til menneske. De andre 11 havner hos et menneske (`kilder/c1_bommene.md`).
 4. **Den feiler der praksis er ny eller enestående:** 0 av 7 MOT i USA, 0 av 17 saker der MOT var eneste MOT i møtet, 0 av 4 i selskaper uten MOT før 2026. Største klynge: 5 nye amerikanske saker om aksjonærrettigheter (Delaware til Texas, supermajoritet), alle MOT, mens alle 7 slike før 2026 var FOR (`kilder/c1_bommene.md`).
 5. **Aksjonærforslag er nesten fraværende i dette datasettet.** Test 2026 har 18 aksjonærforslag av 1578 saker; 56 av 58 MOT er MOT på styrets egne forslag (styrevalg 26, revisor 7, andre styresaker 6, annen sak/eventuelt 6, øvrige 11; `kilder/c1_mot_sakstyper.md`). De 2 andre MOT er styrevalg med kandidat foreslått av aksjonærer. Agenten er målt på styre-MOT, ikke på aksjonærforslag (egen telling).
-6. **Lite data.** Trent på 11 785 saker 2019–2025 (12 179 rader før 2026 minus 394 uten fasit, `kilder/tell_trening.py`) med 70–99 MOT mot styret per år; test er 141 møter i 136 selskaper. Per marked og sakstype er F1 ikke målt for hovedmodellen, gruppene blir for små (`BEGRENSNINGER.md` pkt. 4).
+6. **Lite data.** Trent på 11 785 saker 2019–2025 (12 179 rader før 2026 minus 394 uten fasit, `kilder/tell_trening.py`) med 70–99 MOT mot styret per år; test er 141 møter i 136 selskaper (`kilder/tell_aar.txt`). Per marked og sakstype er F1 ikke målt for hovedmodellen, gruppene blir for små (`BEGRENSNINGER.md` pkt. 4).
 7. **Tidssplitt og antakelse om løpende stemmer.** Tren ≤ 2025, test 2026, kjørt én gang. Modellen bruker NBIMs stemmer fra møter strengt før saken i samme sesong. Er de ikke kjent løpende, faller F1 til 0,415 [0,30; 0,53] (`kilder/c1_enkle_regler_og_hist1.md`). Uten historikk: 0,282 på avvik (`kilder/c1_ablasjon_v2.md`).
 8. **Til menneske: 188 av 1578 saker (11,9 %)**: 127 usikre (kalibrert P(MOT) i [0,15; 0,85)), 60 ukjent selskap, 1 instruks; 183 av de 1539 sakene med fasit (siste kaldstart av kontrollagenten, 05.11). Rutingen fanger usikre flagg, ikke oversette MOT.
 9. **Nye selskaper og rare felt:** uten historikk faller F1 til 0,375, og 99,4 % rutes. Tom tekst eller tomme påkrevde felt vurderes ikke, alt går til menneske (`kilder/c1_robusthet_frossen.md`). Agenten foreslår aldri AVSTÅ, bare FOR/MOT (`BEGRENSNINGER.md` pkt. 6).
--- a/c1/leveranse/ERLIG_EVALUERING.md
+++ b/c1/leveranse/ERLIG_EVALUERING.md
@@ -48,7 +48,7 @@
 ### Kravresponsen kl. 13.06, ordrett
 
 #### Hva vi bygde
-Løsningen tar en saksliste med forslag og markerer de sakene der NBIM sannsynligvis stemmer MOT styret, med en sannsynlighet per sak. Usikre saker (kalibrert P(MOT) i båndet [0,15; 0,85), låst på val 2025), saker fra ukjente selskaper og saker med instrukslignende tekst går til et menneske: 188 av 1 578 saker på test 2026 (11,9 %). Beslutningen den støtter er hvilke saker en analytiker bør lese først. Resten havner i bunken «FOR (ingen grunn til MOT funnet)», der agenten følger styret; der ligger 17 av 58 MOT-stemmer, som ikke blir sett. Modellen («miks h2») er en blanding av logistisk regresjon og LightGBM på forslagstekst, saktype, forslagsstiller og styrets anbefaling. I tillegg bruker den NBIMs tidligere MOT-stemmer i samme selskap og på samme forslagstekst, fra møter *strengt før* sakens møtedato. Det forutsetter at NBIMs stemmer fra tidligere møter er kjent når neste sak vurderes, og det er de, fordi NBIM publiserer stemmene løpende. På teståret finner den 30 av 58 MOT-stemmer (recall 0,52), og 44 % av sakene den markerer er ekte MOT (presisjon 0,44). Agenten gir FOR eller MOT per forslag. AVSTÅ predikeres ikke (5 av 1 539 i test), og de 5 regnes som bom i sidetallet. Hver anbefaling siterer det punktet i NBIMs Global Voting Guidelines som ligner mest på saken; i en stikkprøve på 20 saker var det punktet som avgjør i 15, delvis i 4 og feil i 1 (FOR-saker får som regel standardavsnittet om å støtte styret) (`retningslinje_id`, f.eks. «NBIM 1.1.1», med ordrett tekst og hvorfor punktet ble valgt). MOT-saker får i tillegg en NBIM-begrunnelse fra et *tidligere år* som eksempel (`agent.csv`).
+Løsningen tar en saksliste med forslag og markerer de sakene der NBIM sannsynligvis stemmer MOT styret, med en sannsynlighet per sak. Usikre saker (kalibrert P(MOT) i båndet [0,15; 0,85); kalibreringen er lært på val 2025; båndet er valgt fra et fast rutenett på test-tabellen og sjekket på val (7,5 % val, 7,9 % test, `kilder/c1_menneske_terskel.md`)), saker fra ukjente selskaper og saker med instrukslignende tekst går til et menneske: 188 av 1 578 saker på test 2026 (11,9 %). Beslutningen den støtter er hvilke saker en analytiker bør lese først. Resten havner i bunken «FOR (ingen grunn til MOT funnet)», der agenten følger styret; der ligger 17 av 58 MOT-stemmer, som ikke blir sett. Modellen («miks h2») er en blanding av logistisk regresjon og LightGBM på forslagstekst, saktype, forslagsstiller og styrets anbefaling. I tillegg bruker den NBIMs tidligere MOT-stemmer i samme selskap og på samme forslagstekst, fra møter *strengt før* sakens møtedato. Det forutsetter at NBIMs stemmer fra tidligere møter er kjent når neste sak vurderes, og det er de, fordi NBIM publiserer stemmene løpende. På teståret finner den 30 av 58 MOT-stemmer (recall 0,52), og 44 % av sakene den markerer er ekte MOT (presisjon 0,44). Agenten gir FOR eller MOT per forslag. AVSTÅ predikeres ikke (5 av 1 539 i test), og de 5 regnes som bom i sidetallet. Hver anbefaling siterer det punktet i NBIMs Global Voting Guidelines som ligner mest på saken; i en stikkprøve på 20 saker var det punktet som avgjør i 15, delvis i 4 og feil i 1 (FOR-saker får som regel standardavsnittet om å støtte styret) (`retningslinje_id`, f.eks. «NBIM 1.1.1», med ordrett tekst og hvorfor punktet ble valgt). MOT-saker får i tillegg en NBIM-begrunnelse fra et *tidligere år* som eksempel (`agent.csv`).
 
 #### Hvordan vi verifiserte det
 Fasiten er NBIMs egne stemmer (real_votes fra arrangøren). Målvariabelen er *MOT styret*. Vi bruker ikke accuracy, fordi «følg styret» treffer 96,2 % uten å finne en eneste MOT-stemme (F1 0). Vi splitter på tid: C og grense velges på val 2025 (trent på år før), og test 2026 kjøres én gang med låst grense. Kolonner som avslører svaret (`nbim_vote`, `rationale_*`, `position_paper`, `funds_disagree`) stoppes med assert i koden. Svarfila består lekkasjevakta (`sjekk_lekkasje.py svar`: ingen lekkasjesignatur). Historikken er sjekket mot brute force på 400 rader: ingen etiketter fra samme møte eller senere [AD].
--- a/c1/leveranse/kravrespons.md
+++ b/c1/leveranse/kravrespons.md
@@ -7,4 +7,4 @@
 Fasiten er NBIMs egne publiserte stemmer (real_votes fra arrangøren: 13 757 saker i 194 selskaper og 37 land, møteår 2019–2026, 24 sakstyper, utviklede og fremvoksende markeder), og målvariabelen er om NBIM stemte mot styret i saken. Vi måler F1 på MOT og ikke accuracy, fordi bare 3,8 % av sakene er MOT og «følg styret» får 96,2 % accuracy uten å finne en eneste av dem. Splitten følger tiden: modell og grense er valgt på 2025 og kjørt én gang på 2026, der 95 %-intervallet er [0,36; 0,59] (bootstrap over selskaper) og den beste enkle regelen, MOT hvis samme selskap og samme tekst fikk MOT før, gir 0,365. I motstandstesten la vi 16 ulike instrukser inn i forslagsteksten på alle 1 578 saker: 15 ble flagget og sendt til menneske uten at noen stemme endret seg, men én skrevet som en tittel («as Proposed by Management, as Always») slapp gjennom, endret 16 stemmer uten ruting og senket F1 til 0,392. Alt reproduseres fra en tom kopi med ett kall fra rotmappa i repoet, `bash arbeid/hack/c1/leveranse/kjor.sh`, som også måler svaret med vår egen `maaler_offisiell_v3.py` (F1 på MOT mot styret).
 
 ## Hva vi ville trengt videre
-Med bare 58 MOT-stemmer i test er intervallet bredt, så tallet bør leses som «rundt 0,5». Omtrent 0,06 av F1 kommer fra NBIMs stemmer tidligere i samme sesong (uten dem 0,415), og det er bare ærlig hvis de stemmene er kjent når saken vurderes, noe vi har antatt og ikke dokumentert. Vi trenger lesetilgang til NBIMs stemmedatabase med flere års stemmer og begrunnelser, slik at modellen kan testes på mer enn én sesong og nye selskaper får et grunnlag. Sitatet er det nærmeste punktet i retningslinjene og ikke NBIMs egen grunn: i en stikkprøve på 20 MOT-saker var det det avgjørende punktet i 15. Med mer tid ville vi tettet hullet for instrukser forkledd som titler og testet om NBIM følger retningslinjene også der de stemmer med styret.
+Med bare 58 MOT-stemmer i test er intervallet bredt, så tallet bør leses som «rundt 0,5»; punktestimatet 0,476 er under målet vårt på 0,5. Omtrent 0,06 av F1 kommer fra NBIMs stemmer tidligere i samme sesong (uten dem 0,415), og det er bare ærlig hvis de stemmene er kjent når saken vurderes, noe vi har antatt og ikke dokumentert. Vi trenger lesetilgang til NBIMs stemmedatabase med flere års stemmer og begrunnelser, slik at modellen kan testes på mer enn én sesong og nye selskaper får et grunnlag. Sitatet er det nærmeste punktet i retningslinjene og ikke NBIMs egen grunn: i en stikkprøve på 20 MOT-saker var det det avgjørende punktet i 15. Med mer tid ville vi tettet hullet for instrukser forkledd som titler og testet om NBIM følger retningslinjene også der de stemmer med styret.
--- a/c1/DEMO_MANUS.md
+++ b/c1/DEMO_MANUS.md
@@ -2,7 +2,7 @@
 
 Agent: frossen #2044 miks h2 (`arbeid/hack/levering/kjor_agent.py`, standardkjøring, bånd [0,15; 0,85)).
 Kilde for sakene: `arbeid/oppgave_2260/full/agent.csv` (sha256 `f0444a47…`). Prøvekjørt 05.11 14.45 (#2329): kald kopi fra `fremmed.sh` gir nå sha `1543706f…` (3 rader med annet `mot_styret`-flagg, HP/Hartford/Snowflake), men linje 15/89/276, F1 0,4762 og rutingstallene er uendret.
-**Skjerm for de tre sakene** (ingen av live-skriptene viser dem; kjør etter `fremmed.sh`, 0,02 s): `python3 -I arbeid/oppgave_2329/vis_manussaker.py /tmp/c1_kald/ut/agent.csv`
+**Skjerm for de tre sakene** (ingen av live-skriptene viser dem; kjør etter `sh arbeid/hack/levering/fremmed.sh /tmp/fremmed`, samme mappe som README, 0,02 s): `python3 -I arbeid/oppgave_2329/vis_manussaker.py /tmp/fremmed/ut/agent.csv`
 Linjenummer = linje i fila, overskrift er linje 1. Valgt med `arbeid/oppgave_2260/velg.py`: første sak i fila av hver type, ikke håndplukket.
 Tall: `arbeid/oppgave_2267/maaling.txt` (måler v3 sha `418a937e57`, `--data real --score mot`, + rutingstelling `telling.py`).
 Bare tekst i «anførselstegn» leses høyt (404 ord inkl. de engelske sitatene, ca. 2:45 i 145 ord/min; start `fremmed.sh` i bakgrunnen ved 0:00, den tar 42 s). Forrige 5-min-versjon: `DEMO_MANUS_5min_tilfeldige.md`.
--- a/c1/DEMO_MANUS_5min_tilfeldige.md
+++ b/c1/DEMO_MANUS_5min_tilfeldige.md
@@ -60,8 +60,8 @@
   independent of management, dominant shareholders, and related third parties.»*
 - Fasit: NBIM stemte **Against**, med samme begrunnelse.
 - Si ærlig: sitatet er hentet fra en tidligere sak (alltid tidligere år, annet møte), aldri fra fasit.
-  At det er ordrett likt fasit, kommer av at NBIM bruker faste standardtekster: 799 NBIM-begrunnelser
-  har bare 18 ulike tekster (`c1/kilder/nbim_begrunnelser.csv`). Sitatet forklarer svaret, modellen bruker det ikke til å gjette.
+  At det er ordrett likt fasit, kommer av at NBIM bruker faste standardtekster: 999 NBIM-begrunnelser
+  har bare 19 ulike tekster (`c1/kilder/nbim_begrunnelser.csv`). Sitatet forklarer svaret, modellen bruker det ikke til å gjette.
 
 ## 3:40–4:30 Menneske i loopen
 - «Forvalteren velger hvor usikker en sak må være før et menneske ser den (innstillingen `--baand`, standard: sjanse for MOT
@@ -88,7 +88,7 @@
   raden og scoren er lik. Rutingen er det som endres, ikke modellen.
 
 ## 4:30–5:00 Tallene, ærlig
-- Test 2026, målt én gang med arrangørens måler: F1 MOT {F1_TEST} (0,476, 95 %-usikkerhetsintervall 0,36–0,59), presisjon {P_TEST} (0,44: når agenten sier MOT,
+- Test 2026, målt én gang med vår egen måler (`maaler_offisiell_v3.py`): F1 MOT {F1_TEST} (0,476, 95 %-usikkerhetsintervall 0,36–0,59), presisjon {P_TEST} (0,44: når agenten sier MOT,
   har den rett 44 % av gangene), recall {R_TEST} (0,52: den finner 52 % av MOT-stemmene): {TP} treff, {FP} falske MOT, {FN} bommet MOT av 58 (30, 38, 28 målt 05.11 kl. 13.10, fremmed.sh).
 - Følg styret: F1 0. MOT-grensen og usikkerhetsbåndet er valgt på 2025, aldri justert på 2026.
 - «Én kommando fra kald start: `bash arbeid/hack/c1/demo_saker_2026.sh`.»
--- a/c1/leveranse/kilder/TREFFSIKKERHET.md
+++ b/c1/leveranse/kilder/TREFFSIKKERHET.md
@@ -4,6 +4,8 @@
 Positiv klasse = NBIM stemte MOT og det var mot styret (fasit: `nbim_vote == MOT` og `against_board == 1`).
 Data: arrangørens rettede `real`-data, år 2026, 1539 saker med fasit. Maskinen alene (ingen menneskelig overstyring).
 
+> Språk (#2345): «konfidens < 0,6» under er målerens navn på flagget `til_menneske`. Det er de samme 183 sakene som båndet [0,15; 0,85) pluss vaktene i `JURY.md` pkt 8 (ukjent selskap/type, instruks, datafeil, MOT uten sitat).
+
 ## Alle 1539 saker
 
 |                         | Fasit: MOT styret | Fasit: ikke MOT |
--- a/c1/leveranse/kilder/LESMEG.md
+++ b/c1/leveranse/kilder/LESMEG.md
@@ -15,3 +15,5 @@
 «hovedmålet» er F1 på MOT mot styret. «Maskin alene» betyr agentens stemme før noe går til et menneske.
 
 Lagt til 05.11 kl. 14.40: `c1_val_kaldstart.md` (val 2025 fra kald start: 0,520 på MOT, 0,522 på avvik), `c1_feil_stabilitet.md` (KI for val), `c1_sitatkilder.md`, `c1_sitat_verifisert.md`, `c1_retningslinje_sitat.md` (sitatpåstandene) og `tell_trening.py`/`tell_trening.txt` (11 785 treningssaker).
+
+Lagt til 05.11 kl. 15.10 (#2345): `tell_aar.py`/`tell_aar.txt` (MOT mot styret per år 2019–2026; test 2026: 141 møter, 136 selskaper, 140/135 blant sakene med fasit).
```

Nye filer: `arbeid/hack/c1/leveranse/kilder/tell_aar.py`, `tell_aar.txt`, `arbeid/oppgave_2345/bro_74_71_68.py`, `arbeid/oppgave_2345/rett.py` (rettingene, sjekker ett treff per erstatning).
