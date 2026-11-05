# Case 1: demo-manus (under 3 min), tre ekte saker fra repo4-agenten (oppdatert sak 2659, 05.11 kl. 17.50)

Agent: repo4 (miks h2 + fire historikktrekk, `modell_repo4.py`, frys 17:18; standardkjøring, bånd [0,15; 0,85)). Erstatter den eldre frosne miks h2 (F1 0,476, se nederst).
Kilde for sakene: `ut/agent.csv` fra dommerens kalde kjøring av jury-zipen (sak 2596, `/tmp/c1_dom_2596/zt`, agent.csv sha `24ee6b182f55…`, pred_maaler.csv sha `d02cf88475bf…` = frossen).
**Før demoen (ikke i de 3 minuttene):** i roten av repoet, kjør `sh KJOR.sh` (lager `.venv_kjor` og `ut/agent.csv`, ett til to minutter fra tom cache). **Live under demoen:** `sh arbeid/hack/c1/leveranse/demo.sh` (gjenbruker kjøringen, under 1 s), og for de tre sakene på skjermen `python3 -I arbeid/hack/c1/vis_manussaker.py ut/agent.csv` (0,03 s).
Linjenummer = linje i fila, overskrift er linje 1. Valgt med et eget skript i repoet (sak 2260, ikke i zipen): første sak i fila av hver type, ikke håndplukket.
Tall: `arbeid/oppgave_2659/maaling.txt` (måler v3 `--data real --score mot` på den kalde `pred_maaler.csv`) + rutingstelling på den kalde `agent.csv` (`arbeid/oppgave_2659/telling.txt`; arbeidsfilene er i git-historikken).
Bare tekst i «anførselstegn» leses høyt (ca. 340 ord i «»; ca. 2:20 i 145 ord/min, ca. 2:40 med pauser). Den kalde kjøringen er ferdig før start, så ingenting venter under opplesingen.
**Hvis MUNTLIG og denne demoen deler én 5-min-luke:** hopp over MUNTLIG pkt. 1, pkt. 3 og avslutningen (demoåpningen sier det samme). Da er det ca. 300 + 360 ord, ca. 4:40 ren taletid, under 5 min med pauser. Hver for seg er begge under 3:30.

---

## 0:00–0:35 Måltallet
«NBIM stemmer med styret i 96 av 100 saker. Å alltid følge styret gir høy treffprosent, men finner null
stemmer mot. Vi måler derfor én ting: F1 på stemmene MOT styret, på 2026, et år modellen aldri har trent på.
Følg styret: F1 0. Agenten: F1 0,512, med usikkerhet fra 0,40 til 0,62. Den finner 32 av 58 stemmer mot
styret, og 48 % av flaggene er ekte. Vi prøvde atten måter å slå den på etter frysen; den beste ga +0,014,
under kravet vi skrev på forhånd, så den står.
Vi viser tre saker: ett treff, én bom og én sak agenten sendte til et menneske. Vi valgte den første av
hver type i agentens utfil, ikke de peneste.»

## 0:35–1:10 Treff: Kura Sushi (agent.csv linje 15, `2033470|1`)
Skjerm: Kura Sushi, Inc., 28.01.2026, «Elect Director Tanaka, Kunihiko». Agent MOT, `p_mot 1.0`, `til_menneske 0`, punkt GVG 1.1.

«Kura Sushi foreslår å gjenvelge et styremedlem. Agenten sier MOT, sannsynlighet 1,0, og avgjør selv.
Den siterer NBIMs egen begrunnelse fra 2021 for samme forslag i samme selskap: *"A majority of
shareholder-elected board members in a non-controlled company should be independent of management,
dominant shareholders, and related third parties."*
NBIM stemte mot. Sitatet kommer fra en tidligere sak, aldri fra fasiten.»

## 1:10–1:55 Bom: LOTTE Chemical (agent.csv linje 89, `2048411|10`)
Skjerm: LOTTE Chemical Corp., 20.03.2026, «Amend Articles of Incorporation (Office Term)». Agent FOR, `p_mot 0.0887`, `til_menneske 0`.

«Her tar agenten feil. Sannsynlighet for MOT 0,09, under usikkerhetsbåndet, så maskinen sa FOR uten å spørre
noen. Begrunnelsen er bare NBIMs utgangspunkt: *"Our starting point when deciding how to vote is to support the board."*
NBIM stemte MOT, fordi aksjonærene skal få stemme over endringer i vedtektene.
Dette er feiltypen vi er mest redd for. Av 26 MOT-stemmer agenten overså, gikk 8 til et menneske,
men 18 ble FOR helt uten kontroll, som denne. Stille feil går nesten bare én vei: mot å følge styret.
Av 35 falske MOT gikk 32 til et menneske; bare 3 gikk ut uten kontroll.»

## 1:55–2:35 Til menneske: Lundbeck (agent.csv linje 39, `2038357|7`)
Skjerm: H. Lundbeck A/S, 18.03.2026, «Reelect Lars Erik Holmqvist as Director». Agent MOT, `p_mot 0.2321`, `til_menneske 1`, rutingsgrunn «usikker: kalibrert P(MOT) 0.23 i båndet [0.15, 0.85)», punkt GVG 2.1.

«Sannsynlighet for MOT 0,23. Alt mellom 15 og 85 prosent er usikkert, så saken går til et menneske, med
forslag MOT og NBIMs ord fra en tidligere sak om samme person: *"Board members should devote sufficient time
to fulfil their responsibilities effectively."*
NBIM stemte FOR i 2026. Her hadde maskinen alene tatt feil; mennesket får forslaget, sitatet og grunnen
til tvilen, og kan rette det. I 2026 går 161 av 1539 saker, 10,5 %, til et menneske.»

## 2:35–2:50 Avslutning
«Én kommando fra kald start gir de samme radene. Grensene er valgt på 2025 og aldri justert på 2026.»
Skjerm: tidsstempelet i linje 2 av `leveranse/demo_utskrift.txt` (frysen i linje 5) viser at den kalde kjøringen ble gjort rett før demoen.

---

### Tallkilder (leses ikke høyt)
| Tall i manus | Utskrift |
|---|---|
| F1 0,512; 32 av 58; 48 % (P 0,4776); 35 falske MOT; 26 oversett | `maaling.txt`: «MOT mot styret: TP 32 FP 35 FN 26 P 0.4776 R 0.5517 F1 0.5120 (58 i fasit)» |
| KI 0,40–0,62 | klynge-bootstrap, `leveranse/kilder/c1_repo4_tall_2592.md` (KI [0,40; 0,62]) |
| 161 av 1539, 10,5 % | `maaling.txt`: «161 til menneske (10.5%)», «1539 vurderte rader» |
| FN 8 menneske / 18 maskin; FP 32 menneske / 3 maskin | `telling.txt`: «FN maskin 18 menneske 8», «FP maskin 3 menneske 32» |
| 1,0 / 0,09 / 0,23 og sitatene | `agent.csv` linje 15 / 89 / 39, ordrett (`vis_manussaker.py ut/agent.csv`) |
| «96 av 100 følger styret» | følg-styret-treffprosent 96,2 % (`leveranse/kilder/TREFFSIKKERHET.md:16`) |

### Sjekk etter bytte til repo4 (sak 2659, 05.11 kl. 17.50)
Kald kjøring av jury-zipen (dommer sak 2596): F1 MOT 0,5120 (0.512000), TP 32 FP 35 FN 26, 161 av 1539 til menneske, FN maskin 18 / menneske 8, FP maskin 3 / menneske 32. `vis_manussaker.py` på den: treff = linje 15 (Kura Sushi, før menneskesak), bom = linje 89 (LOTTE, uendret, p_mot 0.0887), menneske = linje 39 (Lundbeck). Sakene i manuset er byttet etter samme regel (første av hver type), ikke valgt for å se penere ut. Eldre Mobimo-sak (linje 276) er fortsatt et maskintreff i repo4, men ikke det første. `vis_manussaker.py` er oppdatert til de nye id-ene og sier MANUS OK på den kalde kjøringen.
Ved ny sjekk: `sh KJOR.sh`, så `sh arbeid/hack/c1/leveranse/demo.sh` (varsler hvis sakene ikke lenger stemmer med manuset). Endres sakene: bytt saker og tall, ikke behold de gamle.

### Eldre frossen modell (før bytte, bare historikk)
Eldre frossen miks h2 (sak 2044, frys 16:00): F1 MOT 0,476 [0,36; 0,59], TP 30 FP 38 FN 28, 183 av 1539 til menneske. Erstattet av repo4 17:18 (sak 2592). <!-- tallvakt: ignorer: eldre frossen modell -->

### Hvis juryen spør «NBIM-repoet slår dere, hvorfor ikke bytte?» (sak 2487, leses ikke i de 2:50)
Vi byttet: repo4 er vår modell med NBIM-repoets historikktrekk lagt til (sak 2592), avgjort med regel satt før måling. Se `leveranse/JURY_SPORSMAL.md` sp. 20. Eldre svar (pkt. 13, eldre frossen 0,476 mot 0,515 / 0,523 / 0,545) gjelder den eldre frosne modellen. <!-- tallvakt: ignorer: eldre frossen modell og NBIM-repoets regel -->
