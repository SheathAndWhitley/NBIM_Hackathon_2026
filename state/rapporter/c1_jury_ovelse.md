# Case 1: tre juryspørsmål øvd, svar på under 60 sekunder (dommer, #2589, ordre #266 tiltak 6)

Skrevet 05.11 kl. 17.05. Hvert svar er til å si høyt på under 60 sekunder (120–150 ord, ca. 2,5 ord/sek). Hvert tall er sjekket mot pakka av dommer, kilde står under svaret. Ingen nye tall. Byttedommen kl. 18 (#2570) kan endre svar 1 bare hvis en kandidat vinner etter regelen i #265; da byttes «står» til «byttet etter regel skrevet før måling».

Valgt ut fra `leveranse/JURY_SPORSMAL.md`: spørsmål 19 (hvorfor ikke beste), 16 og 6 (båndet valgt på test) og 13 (to løsninger i laget). De tre er valgt fordi de angriper metodepoengene (60 %) direkte.

## 1. «Hvorfor leverer dere ikke den beste varianten?» (146 ord, ca. 55 sek)

Fordi 0,476 er det eneste tallet som er valgt uten å se test. Modell, C og grense ble valgt på val 2025 og låst kl. 16. Så ble test 2026 målt én gang.

Ja, vi har sett høyere tall på test etterpå: V2 gir 0,516, hybriden 0,545. Men begge er målt etter frysen, og vi har sett minst åtte testtall siden. Test har 58 MOT, og intervallet er omtrent pluss minus 0,1. Velger vi det beste av åtte blikk, måler vi flaks, ikke agenten.

V2 mot frossen er pluss 0,040, med intervall fra minus 0,007 til pluss 0,095. Det krysser null. Vi har gjort feilen før: t4e ga 0,529 på test og tapte på val.

Regelen vår står skrevet før målingen: en kandidat må vinne på val og ha intervall over null. Ingen gjorde det. Derfor står den frosne agenten, og V2 ligger i neste versjon.

Kilde: `leveranse/JURY_SPORSMAL.md` sp. 19; `NESTE_VERSJON.md:89-96`; `landsbyrapport:c1_byttedom_263.md` (tabell og «Antall testblikk»); V2 0,516 og KI [−0,007; +0,095] og hybrid 0,545 [+0,007; +0,133] reprodusert av dommer i #2529; t4e 0,529/0,468 i sp. 11.

## 2. «Har dere brukt test til å velge noe?» (136 ord, ca. 52 sek)

Ja, én ting, og det sier vi rett ut. Modell, C og grense er valgt på val. Men båndet for hvilke saker som går til et menneske, kalibrert P mellom 0,15 og 0,85, ble valgt fra en tabell på test 2026 og bare sjekket på val etterpå.

Det påvirker ikke hovedtallet. F1 0,476 måles på agentens stemmer uten ruting. Båndet avgjør bare hvor mange saker et menneske leser: 7,9 prosent på test, 7,5 prosent på val, så mønsteret holder begge år.

Det båndet gjør optimistisk, er påstanden om at flaggene agenten tar selv er presise. Den hviler på test og kan ikke brukes som bevis.

JURY.md sier «låst på val». Det er feil, og fila er frosset, så vi retter det i ærlig evaluering og i juryspørsmålene. Neste versjon velger båndet på val, som alt annet.

Kilde: `leveranse/ERLIG_EVALUERING.md:44` og § 6 punktet om båndet; `leveranse/kilder/c1_menneske_terskel.md` (tabellen: 122 saker, 7,9 %; val 7,5 %; «Bånd 1 og 2 ble valgt før måling», men valget mellom dem er gjort på testtabellen); `leveranse/JURY_SPORSMAL.md` sp. 6 og 16; `leveranse/JURY.md:40` (feilen).

## 3. «Dere har to løsninger i laget, og den andre slår dere. Hvorfor leverer dere ikke den?» (141 ord, ca. 54 sek)

Hybridløsningen er laget av andre i teamet, parallelt med agenten. På vår måler og test 2026 gir den 0,545 mot våre 0,476. Forskjellen er pluss 0,069, og intervallet ligger over null. Det er reelt på dette året.

Vi bytter likevel ikke, av tre grunner. For det første er terskel og trekk i hybriden valgt med 2025 i utvalget og 2026 synlig for forfatterne. Testtallet er derfor ikke en ren prediksjon. For det andre så vi tallet etter frysen kl. 16, og bytte da er å velge på test. For det tredje har bare vår agent kaldstart, lekkasjesjekk og ruting til menneske testet.

Det vi kan si, er at vår rangering er best: PR-AUC 0,525 mot 0,413 for hybriden. Det som hjelper i hybriden, er dens sikre nei, som fjerner falske MOT. Neste versjon kombinerer de to, med terskel valgt på val.

Kilde: `leveranse/kilder/c1_nbim_repo_sammenligning_dom.md` (tabellen: 0,545455; KI +0,069 [+0,007; +0,133]; PR-AUC 0,525 mot 0,413 i sp. 13); `landsbyrapport:c1_byttedom_263.md` (krav 1 og 3); `NESTE_VERSJON.md:89-96` (FP 38 → 34).

## Tallsjekk (dommer)

| tall i svarene | kilde | stemmer |
|---|---|---|
| 0,476 frossen test 2026, TP 30 FP 38 FN 28 | `c1/tall_tabell.md:10`, `ERLIG_EVALUERING.md` § 4 | ja |
| 0,520 frossen val 2025 | `c1_byttedom_263.md` (0,5202, offisiell måler) | ja |
| V2 0,516, +0,040 [−0,007; +0,095] | `c1_byttedom_263.md`, `NESTE_VERSJON.md:92` | ja |
| hybrid 0,545, +0,069 [+0,007; +0,133] | `c1_nbim_repo_sammenligning_dom.md` | ja |
| minst 8 testtall etter frys | `c1_byttedom_263.md` «Antall testblikk» | ja |
| t4e 0,529 test, 0,468 val | `JURY_SPORSMAL.md` sp. 11 (eldre måler v2, sies ikke høyt) | ja |
| bånd 7,9 % test, 7,5 % val | `c1_menneske_terskel.md` | ja |
| PR-AUC 0,525 / 0,413 | `JURY_SPORSMAL.md` sp. 13, dom #2465 | ja |
| FP 38 → 34 | `NESTE_VERSJON.md:94` | ja |
| 58 MOT i test, KI ca. ±0,1 | `tall_tabell.md:2`, `c1_bootstrap_f1.md` | ja |

## Råd til den som svarer
- Si «valgt på val, målt én gang på test» i første setning i alle tre. Det er metodepoenget.
- Ikke si tall med mer enn tre desimaler høyt. Intervallet er viktigere enn punktet.
- Bruk ikke «9 MOT-flagg er riktige» (JURY.md:40): det hviler på båndet som er valgt på test.
- Hvis juryen presser på svar 3: innrøm at hybridens modell alene gir 0,538 på vår splitt, så vi vet ikke at gapet ligger i regelen. Det står i sp. 13.
