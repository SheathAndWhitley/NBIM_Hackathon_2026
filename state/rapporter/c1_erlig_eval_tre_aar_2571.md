# Case 1 (#2571): tre-års-tallene ført inn i ERLIG_EVALUERING § 7

Ny seksjon `arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md` § 7 «Forsøkt etter ordre om bedre treff», lagt nederst
så linjehenvisningene fra JURY_SPORSMAL (ERLIG:28-29, 32, 34, 37-38, 44, 46, 54, 67) står. § 4 (linje 37) har fått
én peker-setning på samme linje.

Kilder: #2567 `arbeid/oppgave_2567/benk.txt` (benk A, 7 kandidater) og #2568 `arbeid/oppgave_2568/snitt.log`
(benk B, 7 varianter), begge F1 på MOT mot styret per testår 2024/2025/2026 med måler v3. Tallene er sjekket mot
smed4s `c1_tre_aar_kandidater.md` (like). Alle er merket **foreløpige og ikke dommergodkjente** (dom #2570 venter).

Regelen (ordre #265, satt før måling): snitt ≥ +0,02 over frossen og intet år < −0,02.

| kandidat | 2024 | 2025 | 2026 | snitt | verste år | mot frossen snitt / verste | regel |
|---|---|---|---|---|---|---|---|
| frossen | 0,455 | 0,514 | 0,476 | 0,482 | 0,455 | 0 / 0 | ref |
| repo4 | 0,506 | 0,531 | 0,512 | 0,516 | 0,506 | +0,035 / +0,017 | oppfyller på papiret, KI [−0,005; +0,078] |
| person | 0,418 | 0,516 | 0,525 | 0,486 | 0,418 | +0,005 / −0,037 | nei |
| V2 | 0,407 | 0,547 | 0,516 | 0,490 | 0,407 | +0,009 / −0,047 | nei |
| NBIMhybrid | 0,407 | 0,509 | 0,545 | 0,487 | 0,407 | +0,006 / −0,047 | nei |
| V1 / V1p | 0,405 / 0,402 | 0,519 / 0,519 | 0,481 / 0,492 | 0,468 / 0,471 | 0,405 / 0,402 | −0,013 / −0,050 | nei |
| snitt frossen+person (B) | 0,508 | 0,506 | 0,470 | 0,495 | 0,470 | +0,013 / −0,009 | nei (snitt under 0,02) |
| øvrige benk B (frossen_t, snitt_fh, snitt3, hybrid, person) | | | | 0,480–0,486 | 0,407–0,446 | ≤ +0,005 / ≤ −0,008 | nei |

Også inn: 2023 som fjerde kontrollår (#2573): alle på 0,32–0,38, repo4 +0,005 over frossen. Merket som kontroll,
ikke del av regelen.

Vakter etterpå: tallvakt 169 påstander, 0 avvik (hovedtallet 0,476190 uendret). frys_fasit regenerert (138 filer,
samme filsett), `frys_diff.sh --kilde` FRYS LIK 0 avvik. Merk: første frys_diff før regenerering viste 5 avvik, der tre
(demo_utskrift.txt, JURYSVAR.md, METODE.md) var andres endringer som ble committet i cc0de67/5ed458a mens jeg jobbet.

Ikke gjort: ingen nye målinger. Faller byttedommen (#2570) på BYTT, må § 7 sin statuslinje («ingen kandidat er
godkjent, og den frosne modellen står») og 2026-kolonnen for «frossen (levert)» oppdateres av den som bytter.
