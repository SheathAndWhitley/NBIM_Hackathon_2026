# Case 1: rettinger etter jurylesingen (#2161), funn 4, 5, 8, 9, 10 (smed3 #2168)

Ingen nye tall. Alle tall er hentet fra `c1_enkle_regler_og_hist1.md` (#2134, kald kopi #2139), METODE § 7 (#2115) og BESLUTNINGSSTOTTE:33.
Agentkode, modell og kjor.sh er ikke rørt. Stier er fra `arbeid/hack/`.

- **Funn 4:** `c1/leveranse/kravrespons.md`: ny tabellrad b2 «samme selskap + samme tekst fikk MOT før», P 0,317 R 0,431 F1 0,365 (0,25–0,49). «Slår begge historikkreglene klart (0,476 mot 0,145)» er byttet til «slår den beste enkle regelen (b2, 0,365) med +0,11 [0,01; 0,22]». `levering/JURY_SPORSMAL.md:76-77` (H-F) har samme setning og er merket løst. EN_SIDE pkt. 3 har fått samme linje.
- **Funn 5:** «0,476 → 0,415 [0,30; 0,53] på MOT» står nå i BESLUTNINGSSTOTTE:44 (før: 0,48 → 0,39), METODE:22 (før: 0,386, «måles i #2134»; 0,386 står bare igjen som avvikstall fra #1038), EN_SIDE pkt. 5.3 (før: «faller klart») og i 1-sideren (h1-raden har fått KI).
- **Funn 8:** Bunken heter «FOR (ingen grunn til MOT funnet)» i BESLUTNINGSSTOTTE:10 og EN_SIDE pkt. 1. «Trenger ikke leses» er strøket. «17 av 58 MOT havner her» står i EN_SIDE pkt. 1 og 4 og i 1-sideren. «Mens resten kan følge styret» er strøket.
- **Funn 9:** 1-sideren sier «siterer det GVG-punktet som ligner mest; 15 av 20 avgjørende, 4 delvis, 1 feil i stikkprøven», og nevner at FOR-saker får standardavsnittet. GVG-sitatet er lagt til i EN_SIDE pkt. 1. `levering/KRAVRESPONS.md` rad 30 er oppdatert (A: GVG-oppslag #2106, B: tidligere begrunnelse).
- **Funn 10:** Øverst i `levering/KRAVRESPONS.md` og `levering/demo/README.md` står nå «INTERN, ikke del av leveransen», med en henvisning til juryens fil eller demo. EN_SIDE:26 #2127 er rettet til #2132.

Ikke gjort, fordi det ikke er mine filer: funn 4 i JURYSVAR:23 og BEGRENSNINGER pkt. 1 (+0,38) tilhører smed2. Funn 9 om «P(MOT) 100 % kalibrert» i `demo_utskrift.txt` er ikke rørt (frysvakt/demo). Merk at arbeid/ er i .gitignore, så rettingene er bare på disk og ikke committet.
