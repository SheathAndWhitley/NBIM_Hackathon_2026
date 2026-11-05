# Slik bruker forvalteren stemmeagenten i hverdagen

**Hva agenten gjør:** Den leser sakslista før generalforsamlingene og peker ut sakene der NBIM trolig vil stemme **mot styret**. Den stemmer aldri selv. Mennesket avgjør alltid.

**Grunnlaget:** NBIMs egne stemmer (real_votes), alle markeder og sakstyper (styrevalg, revisor, lønn, utbytte osv.). Tallene under er målt på **test 2026: 1539 saker, 66 ekte avvik fra styret (58 MOT, resten 5 AVSTÅ og 3 andre avvik)**, som modellen aldri så under bygging. Modellen er frosset (#2044, smed2 miks h2), og terskelen er valgt på 2025 før test ble kjørt (`state/rapporter/c1_terskeltabell.md`, #2084); kalibreringen er lært på val 2025; båndet er valgt fra et fast rutenett på test-tabellen og sjekket på val (7,5 % val, 7,9 % test, `c1_menneske_terskel.md`).

**Hva MOT-stemmene er:** 56 av 58 MOT i test 2026 er stemmer mot styrets *egne* forslag, og 29 av agentens 30 treff er der. Agenten er altså ikke «aksjonærforslag = MOT»; den regelen kan finne høyst 2 av 58 (`c1_forslagsstiller.txt`, #2183).

## Arbeidsflyten
1. **Sakslista inn.** Selskap, land, møtedato, sakstype, forslagstekst og styrets anbefaling. NBIMs tidligere stemmer brukes som historikk.
2. **Agenten sorterer hver sak i én av tre bunker:**
   - **FOR (ingen grunn til MOT funnet):** agenten følger styret. Ikke lest av noen i standardoppsettet, og her ligger 17 av 58 MOT-stemmer (se under).
   - **Mulig MOT:** flagget med grunn og NBIMs egen begrunnelse fra en tidligere MOT-stemme (`c1_real_2053`, #2053). Forvalteren bekrefter eller avviser.
   - **Til menneske:** saker nær grensen, saker med datafeil, saker med mistenkelig tekst (injeksjon) og MOT uten sitat. Her avgjør forvalteren uten agentens svar.
3. **Forvalteren stemmer.** Avviste flagg og avgjorte saker lagres og brukes når agenten trenes på nytt.

## Send til menneske: hva forvalteren får i dag
Av 100 saker er **3,8 MOT mot styret** (58 av 1539). MOT er altså sjeldent, og det er dette agenten skal finne.

Test 2026 på NBIMs egne stemmer, levert modell repo4 (#2044 miks h2 + 4 repotrekk), faktisk standardkjøring (#2592, kalibrert P(MOT) i båndet [0,15; 0,85) pluss ukjent selskap/type, injeksjon, datafeil og MOT uten sitat). Positiv klasse: **MOT mot styret, 58 saker av 1539** (ikke de 66 avvikene). Inn 1578 saker, 164 (10,4 %) til menneske; av de 1539 med fasit 161 (10,5 %).

| oppsett | saker til menneske | MOT mot styret blant dem | maskin alene | maskin + menneske (øvre grense, antar riktig menneskelig avgjørelse) | gulv: menneske følger styret |
|---|---|---|---|---|---|
| ingen til menneske | 0 av 1539 (0,0 %) | 0 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,48 / R 0,55 / F1 0,512 |
| bare båndet: kalibrert P(MOT) i [0,15; 0,85) | 99 av 1539 (6,4 %) | 25 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,92 / R 0,62 / F1 0,742 (TP 36 FP 3 FN 22) | P 0,79 / R 0,19 / F1 0,306 |
| **standard** (bånd + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat) | 161 av 1539 (10,5 %) | 29 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,93 / R 0,69 / F1 0,792 (TP 40 FP 3 FN 18) | P 0,79 / R 0,19 / F1 0,306 |

«Maskin alene» er de samme svarene i alle rader: rutingen endrer aldri maskinens svar, bare hvem som ser saken. Kolonnen «maskin + menneske» er en **øvre grense, antar riktig menneskelig avgjørelse** på hver rutet sak. «Gulv» antar at mennesket bare følger styret. Den sanne verdien ligger mellom. 32 av 35 falske MOT-flagg havner hos mennesket (3 er MOT-flagg utenfor sonen, som forvalteren også leser); de 18 MOT ingen ser har lav P(MOT) (under 0,15) og fanges ikke av noe bånd.

Laget med: `python3 -I arbeid/hack/c1/menneske_tabell.py arbeid/oppgave_2592/agent.csv` (bare stdlib, leser fasit direkte, samme definisjon som måler v3 `--score mot`).

**Hva det betyr i hverdagen (standardoppsettet):**
- Forvalteren leser **11,4 av 100 saker**: 10,5 i sonen (161 saker) og 0,9 MOT-flagg utenfor sonen (14 saker, 11 ekte og 3 falske MOT).
- Gjør forvalteren sonesakene riktig, blir **inntil 69 % av MOT-stemmene funnet** (40 av 58), mot 55 % for maskinen alene. Det er en øvre grense. Følger forvalteren bare styret i sonen, blir det 19 %.
- **18 av 58 MOT (1,2 per 100) ser ingen.** Agenten ga dem lav P(MOT), så de havner verken i sonen eller blant flaggene.
- **Timer:** rundt 56 per 1539 saker (161 × 20 min + 14 × 10 min). Antagelse, ikke målt: 20 min per sak i sonen og 10 min per MOT-flagg (samme som #2032).

**Andre oppsett:** båndet stilles med `kjor_agent.py --baand LO,HI` (standard `0.15,0.85`). Smalere bånd gir mindre lesing og færre MOT funnet (raden «bare båndet» viser bidraget fra båndet alene). Terskelen for MOT-flagget (p ≥ 0,923) er låst. Eldre «vid» og «høy presisjon»-oppsett i `c1_terskeltabell.md` (#2084) er målt på avvik (66) med den gamle sonen, ikke med denne definisjonen, og er derfor ikke tatt med her.

## Hva slags saker MOT-stemmene er (#2181)
NBIM stemmer nesten bare mot styret på **styrets egne forslag**: 56 av de 58 MOT-sakene i test 2026 er styrets forslag. De 2 andre er styrekandidater foreslått av aksjonærer, og de 14 andre aksjonærforslagene med fasit (8 styrekandidater og 6 andre saker) fikk ingen MOT. «Aksjonærforslag = MOT» er derfor ingen løsning her. Nesten halvparten er styrevalg (28 av 58), så kommer revisor (7) og «annen sak»/eventuelt (6 av 6 fikk MOT). Agenten finner 32 av 58: alle 6 «annen sak» og 15 av 28 styrevalg, men bare 3 av 7 revisorsaker og 1 av 6 «andre styresaker».

| sakstype (forslag fra) | MOT | saker | MOT-andel | agenten fant |
|---|---|---|---|---|
| styrevalg (styret) | 26 | 729 | 3,6 % | 14 |
| øvrige (styret): vedtekter 3, say-on-pay 3, emisjon 2, nærstående 1, aksjeprogram 1, regnskap 1 | 11 | 571 | 1,9 % | 5 |
| revisor (styret) | 7 | 130 | 5,4 % | 3 |
| andre styresaker (styret) | 6 | 87 | 6,9 % | 1 |
| annen sak / eventuelt (styret) | 6 | 6 | 100 % | 6 |
| styrevalg (aksjonærforslag) | 2 | 10 | 20,0 % | 1 |
| andre aksjonærforslag | 0 | 6 | 0 % | 0 |

Gjenskapes med (fra landsbymappen, bare stdlib, skriver tabellen): `python3 -I arbeid/oppgave_2181/mot_sakstyper.py`

## Robusthet: hva agenten gjør når inndata er rare

Vi forstyrret inndataene og kjørte den frosne agenten på nytt (test 2026, 1578 saker, etter de nye vaktene fra #2152). Modellen er ikke endret. Ingen test krasjet.

| situasjon | F1 på MOT (maskin alene) | til menneske | hva agenten gjør |
|---|---|---|---|
| vanlig kjøring | 0,512 | 10,4 % | standard |
| nye selskaper (ingen historikk) | 0,375 | 99,4 % | mister selskapshistorikken, som er det sterkeste signalet. Vakta «ukjent selskap» sender nesten alt til menneske |
| tom forslagstekst | 0 (med vilje) | 100 % | vurderer ikke saken («kan ikke vurderes»), følger styret, sender alt til menneske |
| ukjent sakstype i ny sak | 0,512 | 100 % | vakta «ukjent forslagstype» slår til på alle saker. Svarene er uendret |
| styrets anbefaling mangler | 0,467 | 100 % | antar FOR, flagger flere MOT (98 mot 74). Alt går til menneske med «styrets anbefaling mangler: sjekk innkallingen» |
| land/marked mangler | 0,455 | 100 % | grunn «land/marked mangler». Færre MOT-flagg (49) |

Kort sagt: der agenten mangler grunnlag, sier den fra og sender saken til et menneske, i stedet for å gjette stille. Tallene i kolonne 2 bygger på bare 58 MOT og flytter seg mye med få saker. Les dem som retning. Hele tabellen med målerlinjer: `state/rapporter/c1_robusthet_frossen.md`.

Gjenskapes med (fra landsbymappen, under 1 min i alt): `python3 -I arbeid/oppgave_2144/robusthet_frossen.py --ut state/rapporter/c1_robusthet_frossen.md`

## Forbehold (les disse)
- **Få MOT-stemmer.** Test har bare 58 MOT mot styret (66 avvik med AVSTÅ). Én sak flytter fanget-andelen 1,7 prosentpoeng. F1 for maskinen alene er 0,512 på MOT mot styret, 95 % intervall 0,40–0,62 (#2087, #2095). Alle tall i tabellen over er på MOT (58). Les dem som «rundt», ikke som presise.
- **«Fanget» er en øvre grense.** Den antar at forvalteren avgjør alle saker i sonen riktig. Gjør forvalteren feil på noen, blir andelen lavere. Gulvet (forvalteren følger styret i sonen) er 16 %.
- **Båndet er valgt på test-tabellen og sjekket på val.** Kalibreringen er lært på val 2025. [0,15; 0,85) sendte 7,5 % av val 2025 videre og 7,9 % av test 2026 (#2128). Kalibreringen er en trapp med få trinn, så båndet kan bare flyttes mellom trinnene (`c1_menneske_terskel.md`).
- **Sonen er mer enn båndet.** Ukjent selskap eller type, datafeil, injeksjon og MOT uten sitat går også til menneske. Tabellen viser begge: 99 saker i båndet, 161 i alt (10,5 %, 164 av 1578 inn med sakene uten fasit; #2132).
- **Historikk må være oppdatert.** Agenten bruker NBIMs stemmer tidligere i samme sesong. Uten den faller F1 på MOT mot styret fra 0,512 til 0,415 [0,30; 0,53] (#2134, `c1_enkle_regler_og_hist1.md`).
- **Terskelen er skjør.** Agentens sannsynligheter er presset sammen øverst. Flyttes grensen fra 0,92 til 0,83, dobles flaggene og F1 faller til 0,35 (`case1_svakheter_2082.md`). Bytt derfor oppsett med `--baand`, ikke ved å skru på p-verdien for hånd.

## Slik leser du p_mot
Merk: tallet 0,923 under er den rå modellskåren (kolonnen `raa_score` i agent.csv). Kolonnen `p_mot` i agent.csv er kalibrert (#2132): der går MOT-flagget ved 0,232, og 0,15–0,85 er båndet som rutes til menneske. Rangeringen er den samme i begge.

p_mot er agentens skår for MOT. Bruk den som **rekkefølge**, ikke som prosent: modellen flagger først fra p ≥ 0,923 (repo4), og skalaen driver fra år til år (`case1_svakheter_2082.md`). Sorter MOT-flaggene etter p_mot og les de høyeste først.

## Når agenten tar feil
- **Falskt MOT-flagg:** på test 2026 havnet 32 av 35 falske flagg i sonen, der forvalteren avgjør selv. Utenfor sonen var 11 av 14 flagg ekte og 3 falske (den frosne modellen hadde 0 falske der). Et falskt flagg koster lesetid, ikke en feil stemme.
- **Oversett MOT** (1,2 per 100, 18 av 58 MOT på test): ingen ser saken, og NBIM følger styret der NBIM ellers ville stemt mot. Dette er den alvorlige feilen. Agenten ga disse sakene P(MOT) under 0,15, så dagens bånd fanger dem ikke. Hvor mye lesing et bredere bånd koster, er ikke målt på denne definisjonen.
- **Se ekstra på disse:** de oversette MOT er mest saker der NBIM har endret praksis og historikken ikke hjelper: på test 2026 (analysen er gjort på den frosne modellen; repo4 har 18 usette, 7 av dem i USA som før) var 5 av de 17 usette amerikanske saker om aksjonærrettigheter (flytting fra Delaware til Texas, høyere terskel for aksjonærforslag, supermajoritet, utsettelse av møtet), alle MOT og ingen flagget. Et menneske bør lese slike saker selv, sammen med styrevalg i selskaper som aldri har fått MOT før (0 av 4 funnet). Rådet er funnet på test og ikke validert, n = 5 (`c1_bommene.md`, #2192).
- **Sitatet er fra en annen sak.** Begrunnelsen er NBIMs egen tekst, men hentet fra nærmeste tidligere MOT-stemme (annet møte, tidligere år). Den sier hvorfor NBIM stemte mot der, ikke nødvendigvis her. Les den som et hint (#2053). I en stikkprøve var punktet fra retningslinjene regelen som avgjør i 15 av 20 saker (#2115).
- **Tilbakefall:** følg andelen avviste MOT-flagg utenfor sonen hver måned. På test var den 0 av 9 (lite tall). Avviser forvalteren mer enn rundt halvparten, har noe endret seg, og agenten skal trenes på nytt.

## Hva agenten ikke skal brukes til
- **Ikke til å stemme automatisk.** Alene finner den halvparten av MOT-stemmene (på MOT mot styret R 0,55, P 0,48, #2087; på avvik R 0,50, P 0,47, `c1_bootstrap_f1.md`).
- **Ikke som NBIMs begrunnelse utad.** Sitatet er fra en annen sak.
- **Ikke uten oppdatert stemmehistorikk** (se forbehold).
- **Ikke på fritekst uten vern.** Mistenkelig tekst («ignore … vote against») renses og sendes til menneske (#2047, `c1_real_2053`).
