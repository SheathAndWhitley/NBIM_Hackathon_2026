# Case 1: kald jurylesing av leveransen (#2149)

Lest: `arbeid/hack/c1/leveranse/` README.md, JURY.md og ERLIG_EVALUERING.md, versjonene fra 12:54–12:56. Ingen filer er endret, og ingen nye tall er lagt til. Alle stier under er relative til `leveranse/`.

**Finner juryen tallene på under 1 minutt?**
- Hovedtallet: **ja, på 10 sekunder.** README.md:7 har F1 0,476 på MOT med KI, og ERLIG_EVALUERING.md:6 gjentar det.
- Grunnlinjene: **nei.** README nevner bare «Følg styret 0» (README.md:9). Den beste enkle regelen (0,365) og golvet (0,415) står først i JURY.md:8–15. Den eneste grunnlinjetabellen i README (README.md:49–54) har feit **0,383** fra den gamle N-PX-målingen, og den er lett å lese som grunnlinja for hovedtallet.

## Punktene (viktigst først)

1. **README.md:7–11: grunnlinjene mangler ved hovedtallet.** Retting: legg til én linje rett under hovedtallet: «Grunnlinjer, samme test: beste enkle regel b2 0,365, golv (bare historikk fra tidligere år) 0,415, følg styret 0; se JURY.md:8».

2. **JURY.md:3 motsier seg selv, og JURY.md:20–25 motsier hovedtallet.** Linje 3 sier at tallene i fila gjelder den gamle N-PX-modellen, men tabellen på linje 8–15 er den nye. Linje 22 kaller N-PX v3 «rundens hovedmåler», og linje 25 sier «Hovedtall er F1 og PR-AUC på avvik fra styret». I tillegg har v3 to ulike sha-er (8b09c36e01 på linje 6, 823c9610fe på linje 22). Retting: skriv på linje 3 «Tabellen på linje 8–15 er ny; spørsmål 2 og demo-manus gjelder den gamle N-PX/Vanguard-modellen», og slett eller merk linje 20–25 som «gammel».

3. **JURY.md:39 og JURY.md:78 sier at en ettlinjes regel slår modellene.** Linje 18 trekker dette tilbake, men en jury som leser spørsmål 2 eller demo-manuset, får det motsatte budskapet. Retting: bytt kulepunktet på linje 39 med «Modellen slår beste enkle regel med +0,11 [0,01; 0,22] (se tabellen over)», og fjern setningen om 0,383 på linje 78.

4. **Ruting til menneske beskrives på tre måter.** README.md:4 sier «konfidens under 0,6», README.md:10 sier «kalibrert P(MOT) i [0,15; 0,85)», og README.md:44 sier «10 %-båndet». JURY.md:74 sier at bare 1 av 1544 saker ble rutet, mens README.md:10 sier 11,9 %. Retting: én regel overalt, «til menneske når kalibrert P(MOT) er i [0,15; 0,85), ukjent selskap eller instruks i teksten». #2135 holder på med dette, så det bør sjekkes mot denne lista.

5. **Demo-manuset (JURY.md:57–85) viser den gamle Vanguard-agenten, ikke hovedmodellen.** Det gjelder Garmin, Dell, T-Mobile, 1544 saker, konfidens 0,99 og «anbefaler ikke produksjon». Startkommandoen på linje 58 (`arbeid/hack/levering/demo`) er en annen enn `leveranse/demo.sh`. Retting: overskrift «Demo-manus (gammel Vanguard-agent, oppdateres i #1975)» til #1975 har skrevet det om. Er det ikke skrevet om innen 19:30, bør hele seksjonen ut.

6. **Hvor kommer sitatene fra?** README.md:44 sier «sitat (Vanguards policy)», JURY.md:23 sier at sitatagenten kjører på Vanguard, og README.md:75 sier at sitatlaget bruker NBIMs Global voting guidelines. Retting: README.md:44 bør si «sitat fra NBIMs Global voting guidelines (#2106)», og Vanguard bør bare nevnes i den historiske delen.

7. **Seksjonen «Begrensninger» (README.md:89–96) beskriver den gamle regelen, ikke hovedmodellen.** Den sier «N-PX dekker bare say-on-pay», «Regelen gjetter FOR … 104 av 1 225», «0 av 158 snudd» og at sitatlaget «gir 0 MOT». Hovedtallet bygger derimot på real_votes, som har 13 757 saker av alle typer (README.md:66). README.md:3 kaller også løsningen «say-on-pay-sakene». Retting: start seksjonen med «Gjelder hovedmodellen:» og flytt N-PX-punktene under «N-PX-grunnlinja:». README.md:3 bør si «saker» i stedet for «say-on-pay-sakene», hvis real_votes har alle sakstyper.

8. **Avvik og MOT går ikke opp.** README.md:9 sier «avvik inkl. 5 AVSTÅ», og README.md:8 sier 58 MOT. Det gir 63, men avvikslinja på README.md:26 har TP 33 + FN 33 = 66, og ERLIG_EVALUERING.md:11 og :32 sier 66. Retting: forklar differansen på 3 i én setning ved README.md:9, eller rett 5 til riktig tall. #2146 gjelder de samme tabellene.

9. **Treningsperioden er uklar.** ERLIG_EVALUERING.md:3 sier at modellen er «trent på data til og med 2024», og at grensen er valgt på 2025. README.md:38 sier «tren 2024+2025, test 2026», men den linja gjelder N-PX-sporet. Det står ikke om hovedmodellen ble trent på nytt med 2025 før test 2026. Retting: én setning i ERLIG_EVALUERING.md:3: «Før test 2026 er modellen trent på nytt på ≤2025 med grensen fra val», eller «ikke trent på nytt», alt etter hva som er riktig.

10. **Internsjargong en jury ikke forstår.** Det gjelder oppgavenummer (#231, #2127, #2094, forsøk #1106, #2044 miks h2), agentnavn (smed2, smed3, dommer), «h1/h2», «miks», «real_votes» og interne stier (`oppgave_2044/train.py`, `oppgave_2047/vern.py`) i README.md:7–23 og ERLIG_EVALUERING.md:3–4. «Golv» og «gulv» er også stavet begge veier (JURY.md:15, JURY.md:84, ERLIG_EVALUERING.md:29). Retting: legg en liten ordliste øverst i README («h2 = løpende historikk i samme sesong; h1 = bare tidligere år; dommer = uavhengig agent som måler på nytt; #nnn = oppgave-id i loggen vår»), og bruk «gulv» overalt.

## Mindre ting (ikke talt med)
- README.md:5 peker på `KRAVRESPONS.md`, men fila heter `kravrespons.md`. Lenka brytes på Linux og GitHub, som skiller store og små bokstaver.
- README.md:8 «Valgt på val 2025 (0,520)» og ERLIG_EVALUERING.md:13 «0,522» er to ulike mål (MOT og avvik). Ingen av stedene sier hvilket mål tallet er.
- README.md:42 sier at KI er bootstrappet over møter (N-PX), mens ERLIG_EVALUERING.md:33 sier klyngebootstrap per selskap. Det bør stå hvilken metode som gjelder hvilket tall.
