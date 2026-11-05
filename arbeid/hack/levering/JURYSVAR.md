# Jurysvar: de ti vanskeligste spørsmålene, med ærlige svar (Case 1)

> **Oppdatert grunnlinje (5.11 kveld):** Den sterkeste enkle regelen er «gjenta NBIMs forrige beslutning på samme sak eller person» (`arbeid/hack/c1/grunnlinje_gjenta_forrige.py`). Den gir F1 på MOT 0,42 / 0,51 / 0,51 for 2024–2026, snitt 0,48, mot agentens 0,51 / 0,53 / 0,51, snitt 0,52: agenten er bedre i snitt, men lik regelen i 2026. Der dette dokumentet sammenligner med regel b2 (0,365), er det en svakere regel. Lekkasjetesten: `arbeid/hack/c1/lekkasjetest.py`. <!-- tallvakt: ignorer: grunnlinje, ikke hovedtall -->

Alle tall har en kilde: forsøk-id (fra lagets interne oppgavetavle, som ikke er med i repoen) eller rapport i `state/rapporter/`; kopiene som ligger i zipen er listet i `arbeid/hack/c1/leveranse/kilder/LESMEG.md`. Tallene er hentet fra METODE.md, BESLUTNINGSSTOTTE.md og rapportene nevnt under. Ingen tall er målt for denne fila; tall som ikke står i METODE (svar 5: #2134, svar 6: #2130) har egen kilde i teksten.

> **Hovedtall (#231):** F1 **0,512 på MOT mot styret**, 95 % KI [0,40; 0,62], test 2026 på NBIMs egne stemmer
> (real_votes, frosset modell #2044 miks h2, 1539 saker, 58 MOT; P 0,478, R 0,552, TP 32 FP 35 FN 26), måler v3 `--score mot` (#2087, #2095).
> *Avvik:* 0,5294 er avvik fra styret (66 avvik: 58 MOT, 5 AVSTÅ, 3 andre; #2086), et sidetall.
> Alle svar gjelder hovedmodellen på real_votes.

**1. Agenten har lavere treffprosent enn «følg styret». Er den ikke dårligere?**
Ja, litt, målt i treffprosent: 96,0 % mot 96,2 % på test 2026 (regnet fra TP 32 FP 35 FN 26 av 1539, #2087). Men «følg styret» finner null MOT-stemmer og gir F1 0. Agenten bytter 35 riktige FOR-saker mot å finne 32 av 58 MOT-stemmer: presisjon 0,48 og recall 0,55, F1 0,512 [0,40; 0,62]. Omtrent halvparten av flaggene er ekte MOT, og litt over halvparten av MOT-sakene blir funnet. Derfor bruker vi F1 på MOT og ikke treffprosent.

**2. Dere fant en lekkasje. Hvor mye av resultatet var juks?**
Ingen del av 0,512. Forbudte kolonner (`nbim_vote`, `rationale_*`, `funds_disagree`, `position_paper`) stoppes med assert, og `position_paper` er tatt ut fordi den er NBIMs egen begrunnelse (97,5 % MOT når satt, `oppgave_2044/train.py`). Sakstypen lekker ikke: uten den gir modellen 0,500 [0,38; 0,61] mot 0,512 (#2103).

**3. Har dere tilpasset noe til testsettet?**
For hovedmodellen: nei. Grensen 0,9232 er valgt på val 2025 og låst før test 2026 kjøres én gang (`oppgave_2044/train.py`).

**4. Hvor sikkert er 0,512?**
Ikke veldig. 95 % KI er [0,40; 0,62] (#2095, `arbeid/hack/c1/leveranse/kilder/oppgave_2095_ki_mot.py`), regnet med klyngebootstrap der vi trekker selskaper (135) og ikke rader (2000 trekk). Det er bare 58 MOT-saker i test. Val 2025 gir 0,530 [0,42; 0,64]. Les tallet som «rundt 0,5, ± 0,12».

**5. Slår dere en enkel regel?**
Ja. Gulvet som er lov, «følg styret», gir F1 0. Den sterkeste enkle regelen vi har målt, «MOT hvis samme selskap og samme forslagstekst fikk MOT før» (b2), gir **0,365 [0,25; 0,49]** på real_votes test 2026 med v3 `--score mot`. Modellen slår den med **+0,11 [0,01; 0,22]** (parret klyngebootstrap, #2134, `arbeid/hack/c1/leveranse/kilder/c1_enkle_regler_og_hist1.md`, kald kopi #2139). Den gamle presedensregelen «MOT hvis NBIM stemte MOT på selskapet før» gir 0,097, og «samme tekst fikk MOT før» 0,287. Med bare historikk fra tidligere år gir modellen 0,415 [0,30; 0,53], som er nedre grense hvis stemmene ikke publiseres løpende. Men presedensregelen i teamets parallelle hybridløsning (laget av andre i teamet, parallelt med agenten, ikke fra NBIM), «avvik hvis siste stemme på samme direktør var et avvik; er direktøren ukjent fra før, brukes siste stemme på samme sakstekst» (avvik teller også AVSTÅ), gir 0,515 på vår måler og test 2026, +0,04 over vår frosne modell (0,476), med KI [−0,05; +0,13], altså innenfor støyen; hybriden (presedens først, så modell) gir 0,545 på vår splitt, +0,069 [+0,007; +0,133], som er et reelt forsprang på oss. Vår rangering er fortsatt best (PR-AUC 0,525 mot 0,318 for presedensregelen og 0,413 for hybriden), men hybridløsningens modell alene med dens terskel gir 0,538 på vår splitt, så vi kan bare si at vår rangering er best; modellen er ikke endret etter frysen (`arbeid/hack/c1/leveranse/kilder/c1_nbim_repo_sammenligning.md` (filnavnet er historisk, løsningen er ikke fra NBIM), dom `arbeid/hack/c1/leveranse/kilder/c1_nbim_repo_sammenligning_dom.md`). <!-- tallvakt: ignorer: hybridløsningens regel og hybrid, ikke hovedtall -->

**6. Siterer agenten NBIMs retningslinjer?**
Ja, den leverte agenten gjør det. Hver sak i `agent.csv` får et ordrett avsnitt fra NBIMs *Global Voting Guidelines* (nbim.no) i `retningslinje_id`/`retningslinje_sitat`. På test 2026 er det 1578 rader og 15 ulike avsnitt: 1504 er FOR-standarden NBIM 0.0.3 («Our starting point … is to support the board»), og 74 er et konkret punkt (71 MOT-flagg og 3 saker der styret selv sa MOT og agenten sier FOR). Broen til 68 i treffsikkerhetstabellen: av de 71 MOT-flaggene mangler 3 fasit, så måler v3 teller 68 MOT-flagg blant de 1539 med fasit (30 riktige, 38 falske). De 3 der agenten sier FOR mot styrets MOT (HP, Hartford, Snowflake) er riktige avvik (NBIM stemte FOR) og telles som treff på avvik, ikke som MOT. Talt med `arbeid/oppgave_2345/bro_74_71_68.py` (i repoet, ikke i zipen). Alle 15 står ordrett på nbim.no i dag: #2130 kontrollerte alle 140 GVG-punkter i den lokale kopien, og den frosne agenten siterer bare punkter derfra (dommeren talte 15 ulike på den frosne agenten, #2278; tallet 18 var fra en kjøring kl. 12:47 før oppslaget ble endret). Agenten finner samme seksjon som NBIM selv oppga i 54 av 63 MOT-saker (86 %, #2106). I stikkprøven på 20 MOT-saker (#2115) var 20/20 ordrette, men bare **15/20 var regelen som avgjør**: 4 var delvis riktige (riktig seksjon, svakere avsnitt) og 1 var feil. De fem rettes i #2120. Sitatet sier hvor mennesket skal lese. Det er ikke et bevis for stemmen.
I tillegg viser agenten NBIMs egen begrunnelse (`rationale_text`) fra en lignende sak i et **tidligere år**. Det er et sitat, ikke et trekk: modellen leser aldri `rationale_*` (assert i `oppgave_2044/train.py`), sitatet hentes etter at MOT/FOR er bestemt, og samme år, senere år og samme møte er utelukket (`c1_real.py:114`). Prediksjonene er byte-like med og uten sitatene (#2106). 8 av 20 slike begrunnelser er skrevet etter en eldre versjon av retningslinjene og står ikke ordrett på nbim.no i dag (#2130).

**7. Hva gir rutingen til et menneske egentlig?**
Den gjør ikke maskinen flinkere: maskinens egne svar er de samme (F1 0,512). Den flytter de usikre MOT-sakene til et menneske. Med standardoppsettet går 10,4 % av sakene til menneske, og der ligger 29 av 58 MOT og 32 av 35 falske flagg. Gjør mennesket dem riktig, blir F1 0,792; det er en øvre grense. Følger mennesket bare styret, blir det 0,306.

Test 2026 på NBIMs egne stemmer, levert modell repo4 (#2044 miks h2 + 4 repotrekk), faktisk standardkjøring (#2592, kalibrert P(MOT) i båndet [0,15; 0,85) pluss ukjent selskap/type, injeksjon, datafeil og MOT uten sitat). Positiv klasse: **MOT mot styret, 58 saker av 1539** (ikke de 66 avvikene). Inn 1578 saker, 164 (10,4 %) til menneske; av de 1539 med fasit 161 (10,5 %).

| oppsett | saker til menneske | MOT mot styret blant dem | maskin alene | maskin + menneske (øvre grense, antar riktig menneskelig avgjørelse) | gulv: menneske følger styret |
|---|---|---|---|---|---|
| ingen til menneske | 0 av 1539 (0,0 %) | 0 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,48 / R 0,55 / F1 0,512 |
| bare båndet: kalibrert P(MOT) i [0,15; 0,85) | 99 av 1539 (6,4 %) | 25 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,92 / R 0,62 / F1 0,742 (TP 36 FP 3 FN 22) | P 0,79 / R 0,19 / F1 0,306 |
| **standard** (bånd + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat) | 161 av 1539 (10,5 %) | 29 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,93 / R 0,69 / F1 0,792 (TP 40 FP 3 FN 18) | P 0,79 / R 0,19 / F1 0,306 |

«Maskin alene» er de samme svarene i alle rader: rutingen endrer aldri maskinens svar, bare hvem som ser saken. Kolonnen «maskin + menneske» er en **øvre grense, antar riktig menneskelig avgjørelse** på hver rutet sak. «Gulv» antar at mennesket bare følger styret. Den sanne verdien ligger mellom. 32 av 35 falske MOT-flagg havner hos mennesket (3 er MOT-flagg utenfor sonen, som forvalteren også leser); de 18 MOT ingen ser har lav P(MOT) (under 0,15) og fanges ikke av noe bånd.

Laget med: `python3 -I arbeid/hack/c1/menneske_tabell.py arbeid/oppgave_2592/agent.csv` (agent.csv i repoet, ikke i zipen; bare stdlib, leser fasit direkte, samme definisjon som måler v3 `--score mot`).

**8. Gjelder dette for alle NBIMs stemmer?**
Hovedtallet er målt på alle NBIMs stemmer i test 2026: **1539 saker med fasit, alle sakstyper** (styrevalg, revisor, lønn, utbytte osv.) **og alle markeder**, utviklede og fremvoksende (METODE pkt. 0, BESLUTNINGSSTOTTE). Sak 1 i demoen er et styrevalg. Det vi *ikke* har målt, er F1 per marked og sakstype for hovedmodellen. Med 58 MOT totalt blir gruppene små, så vi sier det rett ut i stedet for å vise tall vi ikke har (BEGRENSNINGER pkt. 4). Selskaper NBIM ikke har stemt i før, er svakere (0,375 i motstandstesten #2144), og 99,4 % av dem går til menneske.

**9. Hvorfor er 2026 svakere enn 2025? Har NBIM endret politikk?**
Det vet vi ikke. Val 2025 gir 0,530 [0,42; 0,64] og test 2026 0,512 [0,40; 0,62] (repo4, #2592). Intervallene overlapper nesten helt, så forskjellen kan være støy. Årsaken er ikke målt.

**10. Bruker modellen informasjon som ikke fantes før møtet?**
Ikke så langt vi vet. Hovedmodellen leser bare forslagstekst, kategorier og NBIMs stemmer fra møter strengt før møtedatoen (løpende historikk, METODE pkt. 0); forbudte felt stoppes med assert, og sakstypen lekker ikke (#2103).
