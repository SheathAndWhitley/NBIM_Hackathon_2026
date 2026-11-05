# Case 1: jurylesingens funn rettet i README, BEGRENSNINGER, ERLIG_EVALUERING og JURYSVAR (smed2 #2167, 05.11)

Kilde: `state/rapporter/c1_juryles.md` (speider #2161). Ingen nye tall: alt er hentet fra c1_robusthet_frossen.md (#2144), c1_enkle_regler_og_hist1.md (#2134), METODE.md og BESLUTNINGSSTOTTE.md. Stier fra `arbeid/hack/`. Kode, kjor.sh og agent er ikke rørt (frysvakt).

| Funn | Fil | Retting |
|---|---|---|
| 1 | `c1/leveranse/README.md` | Linje 3–5 skrevet om for real_votes (alle sakstyper/markeder, kalibrert P(MOT), bånd [0,15; 0,85) + vakter, NBIM GVG-sitat). Linje 44: bånd og GVG-sitat i stedet for 10 %-bånd/Vanguard. Linje 86: «logreg + LightGBM (#2044 miks h2)». N-PX-stegtabell, N-PX-tabell, målvariabel og de gamle begrensningene flyttet til «Vedlegg: grunnlinje, ikke levert (N-PX)». Ny kort «Begrensninger» peker til BEGRENSNINGER.md og ERLIG_EVALUERING.md. N-PX-kildene merket «grunnlinje, ikke levert». |
| 2 | `c1/leveranse/BEGRENSNINGER.md` | Nye pkt. 1–6 gjelder bare den leverte agenten. Vanguard-pkt. 7 erstattet av pkt. 5 (NBIM GVG ordrett, 15/20 avgjørende, #2115/#2130). Fritekst-pkt. 8 erstattet av pkt. 3 med #2144-tabellen (nye selskaper 0,375 / 99,4 % til menneske, tom tekst/felt 100 %, ukjent type 100 %, uten styreanbefaling 0,467, tomme land/marked 0,455; injeksjon 82/174 bare målt på #2046). «Bare amerikansk say-on-pay» erstattet av pkt. 4: F1 per marked/sakstype ikke målt for hovedmodellen. Gamle N-PX-pkt. 2–6 + Vanguard-motstand flyttet til vedlegg A–F «grunnlinje, ikke levert». |
| 3 | `levering/JURYSVAR.md` svar 8 | Testsettet er 1539 saker, alle sakstyper og markeder; F1 per gruppe er ikke målt (sagt rett ut); nye selskaper 0,375 (#2144). N-PX-avsnittet merket grunnlinje. |
| 4 | `JURYSVAR.md` svar 5, BEGRENSNINGER pkt. 1 | b2-regelen 0,365 [0,25; 0,49], differanse +0,11 [0,01; 0,22] (#2134, kald kopi #2139). +0,38 fjernet fra BEGRENSNINGER. Regel a (0,097) og b (0,287) nevnt i svar 5. |
| 5 | `c1/leveranse/ERLIG_EVALUERING.md` pkt. 2 | «0,476 → 0,415 [0,30; 0,53] på MOT»; 0,386 står bare som avvik-sidetall. Også lagt inn i BEGRENSNINGER pkt. 2 og JURYSVAR svar 5. |
| 6 | `c1/leveranse/README.md`, `levering/README.md` | Fet linje «HOVEDTALL F1 MOT mot styret 0,4762» står før SCORE-utskriften, og det står at `SCORE 0.481752` er avvik/sidetall. kjor.sh er ikke endret. |
| 7 | `ERLIG_EVALUERING.md:3` | «Val-modellen er trent på 2019–2024, test-modellen på 2019–2025 (11 785 saker).» |
| 10 | `JURYSVAR.md:3,7-8`, begge README, BEGRENSNINGER, ERLIG_EVALUERING | «Ingen tall er nye» byttet til at tall utenfor METODE har egen kilde (svar 5: #2134, svar 6: #2130). Avvikstypene står likt: 66 avvik = 58 MOT, 5 AVSTÅ, 3 andre. Innledningen i JURYSVAR nevner nå alle svar med N-PX-avsnitt. |

**Akseptkrav:** `grep -n "Vanguard\|say-on-pay\|N-PX"` i de fem filene gir bare treff i vedlegg/avsnitt merket «grunnlinje, ikke levert» (README-kildelista: under punktet merket grunnlinje; ERLIG_EVALUERING og levering/README: 0 umerkede).

**Til andre:** BEGRENSNINGER er nummerert om (AVSTÅ var pkt. 9, nå pkt. 6). `levering/KRAVRESPONS.md:38,83` (intern, ikke min) viser fortsatt til «pkt. 9». `c1/leveranse/kravrespons.md:17` lover #2144 i BEGRENSNINGER; det står nå i pkt. 3.
