# Muntlig gjennomgang for juryen, 3 minutter (BYTT-utgaven)

*Omtrent 400 ord, rolig tempo. Tallene er hentet fra `README.md` og `ERLIG_EVALUERING.md` § 7.*

**1. Problemet (30 s)**
NBIM stemmer på tusenvis av generalforsamlinger. Nesten alltid stemmer fondet med styret. Det er de få sakene der det stemmer *mot* styret, som krever arbeid. Derfor er «følg styret» bare gulvet. Den regelen får 96 % riktige, men finner null av stemmene mot styret, altså F1 0. Vårt hovedtall er F1 på stemmene mot styret, ikke accuracy.

**2. Metoden (60 s)**
Fasiten er NBIMs egne publiserte stemmer, 2019 til 2026. Vi splitter på tid: vi trener på årene før, velger på 2025 og kjører testen på 2026 én gang. Etter modellfrysen fikk vi ordre om å prøve å løfte treffet. Før vi målte noe, skrev vi ned en byttegrense: en kandidat erstatter den frosne modellen bare hvis den i snitt over tre rullende testår, 2024, 2025 og 2026, ligger minst 0,02 over, og ikke er under −0,02 i noe år. Hvert år er trent bare på årene før. En kontrollagent som ikke målte kandidatene, avgjør byttet. Hovedtallet har den målt på nytt fra kald start. Sju kandidater ble målt i første runde. Seks falt, de fleste fordi de så bedre ut på 2026, men dårligere på 2024. Én besto: repo4, den frosne modellen pluss fire historikktrekk, som om samme sak og samme person har fått stemmer mot styret før. Etter byttet fikk vi én runde til med samme regel, nå med repo4 som den frosne. Atten varianter ble målt til kl. 18:15, den beste lå +0,014 over i snitt og var bedre alle tre år, men kravet var +0,02, så repo4 står. <!-- tallvakt: ignorer: kandidatrunde 18:15, ikke hovedtall -->

**3. Det ærlige tallet (30 s)**
<!-- VARIANT:HOVEDTALL -->
Kontrollagenten dømte BYTT. Hovedtallet er F1 **0,512** på stemmer mot styret, test 2026, 58 slike stemmer blant 1539 saker. Det betyr at agenten finner 32 av 58. KI er 0,40 til 0,62. Den eldre frosne modellen ga 0,476.
<!-- /VARIANT -->

**4. Forbeholdet (30 s)**
Vi sier det selv før dere spør: repo4s tall for 2026 var kjent før regelen ble skrevet. 2026 er derfor ikke et friskt testår for repo4. Årene som avgjør, 2024 og 2025, ble målt etter regelen og gir +0,051 og +0,017, i snitt +0,034. Det holder uten 2026. Men KI for snittgevinsten er −0,005 til +0,078 og krysser null. Gevinsten er sannsynlig, ikke bevist.

**5. Mennesket beslutter (30 s)**
Agenten stemmer ikke. Den gir et forslag per sak med en kalibrert sannsynlighet for stemme mot styret og et ordrett sitat fra NBIMs retningslinjer for stemmegivning. Saker med sannsynlighet mellom 0,15 og 0,85 går til et menneske. Det samme gjør ukjent selskap eller sakstype, datafeil og tekst som ser ut som en instruks til agenten.
<!-- VARIANT:RUTING -->
På testen gikk 164 av 1578 innkomne saker til et menneske, 10,4 %. Av de 1539 sakene med fasit var det 161.
<!-- /VARIANT -->
Mennesket bruker tiden på de usikre sakene, ikke på alle.

**Avslutning (10 s)**
Hele løsningen kjører fra kald start med én kommando: `sh KJOR.sh`. Vi har vist dere et tall vi kan forsvare, ikke det høyeste vi fant.
