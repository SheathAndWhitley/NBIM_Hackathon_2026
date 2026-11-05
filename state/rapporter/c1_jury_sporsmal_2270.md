# Case 1: ti vanskelige jurysporsmål med svar og kilde (speider, oppgave 2270)

Levert: `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md`. Den har ti spørsmål med svar på 2–3 setninger, og hvert svar har en fil:linje-kilde i `c1/tall_tabell.md` eller pakka. Ingen nye tall og ingen #nummer-pekere (sjekket med grep).

Spørsmålene: 0,476 under målet, følg styret 96 %, KI og enkel regel, hvorfor ikke ablasjonen som scorer høyere på test, lekkasje og løpende historikk, test brukt til å velge (båndet!), LOTTE, Mobimo-sitatet, USA 0 av 7, injeksjon i Title Case.

Funn til dommeren og ordføreren:
1. Det finnes to KI-er i pakka: [0,37; 0,59] i tall_tabell.md (bootstrap over rader, linje 4 og 10) og [0,36; 0,59] i JURY/README (klyngebootstrap). Svaret nevner begge. Bør tall_tabell si hvilken metode?
2. Mobimo og LOTTE står bare i `c1/DEMO_MANUS.md`, ikke i `leveranse/`. Følger ikke demo-manuset med i pakka, må kildene for svar 7–8 flyttes.
3. Usikkerhetsbåndet [0,15; 0,85) ble valgt fra en tabell på test (ERLIG_EVALUERING.md:44). Det er det svakeste metodepunktet en jury kan finne, og svar 6 sier det rett ut.
4. Den eldre `arbeid/hack/levering/JURY_SPORSMAL.md` (kl. 12.55) har gamle #-pekere og er ikke rørt.
