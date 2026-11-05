# Case 1: råvarer til lærdomsboka, tidslinje over dagens feil og rettinger (#2794)

Grunnlag for #2563 (20:05). Bare lesing. Klokkeslett er tidspunktet rettingen ble committet eller logget, ikke når feilen oppstod. Kilde står bak hvert punkt (commit-hash, rapport eller tavle-logg).

| Kl. | Id | Hva måtte rettes | Årsak (én setning) | Kilde |
|---|---|---|---|---|
| 16:45–16:54 | #2550 #2558 #2574 | «rundt 0,5» i README/kravrespons byttet til 0,36–0,59, kjøretid 31–52 s vs 29–52 s | Tekst ble skrevet før KI og kjøretid var målt, og ble ikke oppdatert overalt. | 83f152c, 5442ccd, ff399dd |
| 16:50–16:55 | #2566 #2582 | «dommeren» → «kontrollagenten» i JURY.md:77, kravrespons:10, JURY_SPORSMAL:52 | Internt landsbyspråk lekket inn i jurytekst; første runde (#2550) fant ikke alle forekomstene. | 492382b, fa6fae9 |
| 17:01 | #2577 | BYTT til repo4 ga 54 tallvakt-rester (ned til 23 med bytt_tall.py, resten for hånd) | Samme tall stod i mange filer med ulike avrundinger, så byttet kunne ikke gjøres mekanisk. | 7bcbbcd, 4fe23fe |
| 17:09 | #2593 | Byttplanens git-tilbakerulling virket ikke | 46 pakkefiler var usporet fordi arbeid/ og state/ ligger i .gitignore. | 32a8612 |
| 17:21 | #2592 | sjekk_treffsikkerhet.sh forventet gamle tall, siste 0,476-rester, modellnavn i demo.sh | Sjekkskriptet hadde frossen-modellens tall hardkodet. | ecb7e1b |
| 17:25 | #2631 | STÅR-kjeden i LES.md var rød | MUNTLIG og 3 tekster utenfor zipen hadde allerede BYTT-tall, så reserven var ikke lenger en ren reserve. | 9358e57 |
| 17:34 | #2658 | 4 av 5 røde jurypunkter i arbeidstreet, 5 av 5 i zip 5514792 | Rettingene fra jurylesningen var ikke kommet inn i zipen som skulle leveres. | 8f80292 |
| 17:39 | #2660 | demo_utskrift.txt viste frys 17:10:34 og «AVVIK FRA MANUS» | Utskriften var laget før ny frys 17:18 og ny demosak etter byttet. | c3ab2a3 |
| 17:50–17:51 | #2671 #2685 | Tallavvik fra #2624 (grenser, avvik-F1, ruting) og 97 tallvakt-avvik i leveranse/kilder | Kildefiler fra den frosne modellen (#2044) var ikke merket «eldre», så tallvakta så dem som feil. | e9cf0f8, ab44e95 |
| 17:56 | #2681 | lag_staar.py fant 0 treff | Reglene pekte på BYTT-tekst som var endret i #2653, så STÅR-byggingen var stille brutt. | 52b8b99 |
| 18:17 | #2723 | 8 punkter fra speider #2717, bl.a. to bytteregler i omløp («vinner 2024 og 2025» mot snitt 3 testår), «kjørt én gang» strøket | Bytteregelen ble formulert flere steder før den var skrevet ned ett sted. | 7dce245 |
| 18:19 | #2724 | Ikke-UTF-8 inn-fil krasjet c1_real.py (UnicodeDecodeError), latin-1-fallback lagt inn | Robusthetstesten hadde ikke vært kjørt med feil tegnkoding før frysen. | e0730dc, c1_robusthet_rettet.md |
| 18:27 → 18:45 | #2738 #2788 | Frysvakta slo ut på c1_real.py; dom GODTA, frystid satt tilbake til 17:18:18 | Krasjfiksen ga ny frys 18:19:39 uten at frysdommen var gitt først. | tavle-logg 18:27:44, e1438a9 |
| 18:20 | #2735 | MUNTLIG pkt. 2 «tolv» → sju | Tall i muntlig manus uten kilde. | 072aaaa |
| 18:20–18:24 | #2731 #2741 #2744 | Samme-dags-lekkasje i repo4: 15 avvik/400 (11 rader), 14 av 1539 testrader; strengt tidligere dato gir snitt 0,516 → 0,525 | Lekkasjesjekken ble kjørt på repo4 først etter at byttet var gjort. | 10f71c7, 445a4ee, 372a0f3 |
| 18:24 | #2749 | GitHub-repoens historikk skrevet om til én commit | Tidlige commits hadde objekter (pred_miks_h2) som ikke skulle ut. | e005e81 |
| 18:34–18:39 | #2770 #2779 | «29 av 30 treff» merket eldre modell, «±0,12» → 95 % KI [0,400; 0,621] | Tekst fra den frosne modellen og et grovt usikkerhetsmål sto igjen etter byttet. | 303f5e8, 5d3540e |
| 18:45 | #2762 | GitHub-synken tok med bare 161 filer, nå 957 | Hvitlista i synken var smalere enn ordre #277 («alt Case 1-arbeid»). | 9beee0b |
| 18:47 | #2789 | Frys-etiketten i c1_frys.json sa «#2044 miks h2» selv om filene var repo4 | Ved byttet 17:18 ble hashene oppdatert, men etiketten ikke. | c1_byttedom_endelig_2603.md:17 og :24, 0b7e0e9 |
| 18:47 | #2785 #2791 | Fem README-punkter fra den eksterne lesningen (ett hovedtall 0,512, regelen før byttet, 2044 merket, arbeidsmapper, 39 saker uten styreanbefaling) | README hadde flere tall som konkurrerte om å være hovedtallet. | 9d5c855 |
| 18:50 | #2788 | Disken var full (118 MB ledig); 37 gamle sluttsjekk-logger i /tmp slettet, nå 22 GB | Hver sluttsjekk la igjen logger i /tmp, og ingen ryddet. | tavle-logg 18:50:24 (smed, fremgang #2788) |

## Mønstre (råstoff til «tre ting vi gjorde feil»)
1. **Samme tall i mange filer.** Punktene kl. 17:01, 17:21, 17:25, 17:50, 17:56, 18:34 og 18:47 (README) skyldes alle at ett tall stod i flere tekster og måtte rettes for hånd ved hvert bytte. Det kostet minst 10 commits mellom 16:45 og 18:47.
2. **Frys og metadata kom ut av takt.** Kl. 17:39 (gammel frys i demo), 18:19→18:45 (frystid) og 18:47 (etikett): hashene var riktige, men tekst og tid rundt dem ble ikke oppdatert sammen med dem.
3. **Sjekker kjørt etter beslutningen, ikke før.** Lekkasjen i repo4 (18:20) og ikke-UTF-8-krasjet (18:19) ble funnet etter byttet og frysen 17:18. Bytteregelen (#265) var riktig satt før måling, men lekkasje- og robusthetssjekkene var ikke med i den.

Ekstra: drift (disk 18:50) og git-oppsett (17:09, 18:24) var små, men begge kunne stoppet leveransen.
