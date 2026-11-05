# Case 1: demo-manuset lest som jury uten ML-bakgrunn, uklare ord rettet (#2199)

Fil: `arbeid/hack/c1/DEMO_MANUS.md` (det levering/ peker til: KRAVRESPONS.md:75, JURY_SPORSMAL.md:76). Før-kopi: `/tmp/DEMO_MANUS_for_2199.md`.

**Lesetid:** hele fila lest med stoppeklokke 13:19:46–13:20:59 (rask lesing, 1178 ord). Replikkene i «» i 5-minuttersdelen er
389 ord før og 459 ord etter rettingen: **2:36 før, 3:04 etter** ved 150 ord/min tale. Det gir ca. 2 min til å vise skjermen. Det holder, men det er stramt.
Hele 5-min-delen (med tabell, kodeblokk og regi) er 1039 ord, så taleren må ikke lese regi og kodeblokker høyt.

## Endringer (13)
| # | Linje (før) | Uklart for jury | Rettet til |
|---|---|---|---|
| 1 | 24 | «F1 på MOT» ble aldri forklart | én setning: tall 0–1 som teller både hvor mange MOT den finner og hvor ofte den har rett |
| 2 | 28 | tabellkolonne «rå score (P(MOT) kalibrert)» | «rå score (sjanse for MOT)» |
| 3 | 30 | «P(MOT) 0,19 i båndet [0,15, 0,85)» (intervallnotasjon) | «sjanse for MOT 19 %, mellom 15 og 85 %» |
| 4 | 37–38 | «MOT-grensen (rå, 0,919; kalibrert 0,191)», «usikkerbåndet» | rå 0,912 rett under grensen 0,919; 19 % sjanse; 15–85 % regnes usikkert |
| 5 | 41 | «recall» | «recall, andelen av MOT-stemmene den finner» |
| 6 | 46 | «sakstype modellen ennå ikke fanger godt»: **uten tall** | bare 2 MOT på emisjoner i 2026 (TREFFSIKKERHET/BESLUTNINGSSTOTTE:46), for få til å si noe |
| 7 | 48–49 | «snitt av rangen», «kalibrert isotonisk» | «plasseringen», «oversetter scoren til en sjanse, lært på fasiten fra 2025 (kalibrering)» |
| 8 | 55 | «P(MOT) 52 % kalibrert», «P i båndet [0,15, 0,85)» | «sjanse for MOT 52 %», «mellom 15 og 85 %» |
| 9 | 62 | «NBIM bruker faste standardtekster»: **uten tall** | talt nå: 799 NBIM-begrunnelser, bare 18 ulike tekster (`c1/kilder/nbim_begrunnelser.csv`) |
| 10 | 63 | «forklaring, ikke feature» | «Sitatet forklarer svaret, modellen bruker det ikke til å gjette» |
| 11 | 66–67 | «`--baand`», «[0,15, 0,85)», «Kalibreringen låses» | «innstillingen `--baand`», «mellom 15 og 85 %», «Oversettelsen til sjanse lærer vi på 2025» |
| 12 | 69 | «injeksjon» | «en skjult instruks i sakteksten (injeksjon, f.eks. «ignorer retningslinjene»)» |
| 13 | 90–92 | «KI», presisjon/recall uten mening, «Grense og bånd» | «95 %-usikkerhetsintervall», presisjon = rett 44 % når den sier MOT, recall = finner 52 %; «MOT-grensen og usikkerhetsbåndet» |

Ikke endret: topptekst og trekkbeskrivelse (seed, sha, miks h2). Det er regi og etterprøvbarhet, ikke tale. {KLAMMER} står til #1975 etter frysen.

## Tallvakt
`python3 -I arbeid/verktoy/c1_tallvakt.py`: 14 filer, 139 påstander stemmer, **0 avvik**, OK.
Med DEMO_MANUS.md som argument: 0 avvik, men **0 påstander sjekket**. Tallvakta kjenner ikke igjen `{F1_TEST} (0,476)`-formatet.
Derfor sjekket jeg for hånd mot måleren: F1 0,4762, P 0,4412, R 0,5172, TP/FP/FN 30/38/28, 58 MOT, 183 av 1539 til menneske (11,9 %).
KI 0,36–0,59 stemmer med EN_SIDE.md:19. Alt stemmer.

## Forslag
- #1975 (16:05): når {KLAMMER} byttes ut, bør tallvakta få et mønster for `{X} (tall)`, eller så må manuset kjøres for hånd som over.
