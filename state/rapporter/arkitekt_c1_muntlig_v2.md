# Muntlig gjennomgang for juryen, 3 minutter (BYTT-utgaven, v2)

*Rettet etter juryrettelsene (#2641). Tallene står i `README.md` og `ERLIG_EVALUERING.md`.*

**1. Problemet og hovedtallet (30 s)**
NBIM følger nesten alltid styret. Arbeidet ligger i de få sakene der fondet stemmer *mot* styret: 58 av 1539 saker i test 2026. Derfor måler vi F1 på stemmene mot styret: hvor mange av dem agenten finner, og hvor ofte den har rett når den sier «mot». «Følg styret» får 96 % riktige, men finner null av de 58, altså F1 0. Det er gulvet, ikke en løsning.

**2. Metoden (55 s)**
Fasiten er NBIMs egne publiserte stemmer, 2019 til 2026. Vi splitter på tid: trener på årene før, velger på 2025 og tester på 2026 én gang. Etter modellfrysen, før vi målte nye kandidater, skrev vi ned en byttegrense: en ny modell erstatter den frosne bare hvis den i snitt over tre testår, 2024, 2025 og 2026, ligger minst 0,02 over, og ikke er mer enn 0,02 under i noe år. Hvert år er trent bare på årene før. En kontrollagent som ikke målte kandidatene, avgjør byttet. Tolv kandidater ble målt. Elleve falt, de fleste fordi de så bedre ut på 2026, men dårligere på 2024. Én besto: den frosne modellen pluss fire trekk om tidligere stemmer mot styret i samme selskap.

**3. Det ærlige tallet (30 s)**
<!-- VARIANT:HOVEDTALL -->
Kontrollagenten dømte bytte. Den nye modellen er levert og kjørte feilfritt fra kald start med samme tall. Hovedtallet er F1 **0,512** på stemmer mot styret, test 2026: agenten finner 32 av 58. Konfidensintervallet er 0,40 til 0,62. Den frosne modellen ga 0,476.
<!-- /VARIANT -->

**4. Forbeholdene (30 s)**
Den nye modellens tall for 2026 var kjent før byttegrensen ble skrevet. Årene som avgjør, 2024 og 2025, ble målt etterpå og gir +0,051 og +0,017, i snitt +0,034. Men intervallet for snittgevinsten er −0,005 til +0,078 og krysser null. Gevinsten er sannsynlig, ikke bevist. Det største forbeholdet: omtrent 0,06 av F1 kommer fra NBIMs egne tidligere stemmer i samme sesong. Uten den historikken er F1 0,415, målt på den frosne modellen. Det holder bare om NBIM har stemmene løpende.

**5. Mennesket beslutter (25 s)**
Agenten stemmer ikke. Den gir et forslag per sak med en kalibrert sannsynlighet for stemme mot styret og et ordrett sitat fra NBIMs retningslinjer. Saker med sannsynlighet mellom 0,15 og 0,85 går til et menneske, det samme gjør ukjente selskaper, datafeil og tekst som ligner en instruks til agenten.
<!-- VARIANT:RUTING -->
På testen gikk 164 av 1578 saker til et menneske, 10,4 %.
<!-- /VARIANT -->

**Avslutning (10 s)**
Hele løsningen kjører fra kald start med én kommando: `sh KJOR.sh`. Vi har vist dere et tall vi kan forsvare, ikke det høyeste vi fant.
