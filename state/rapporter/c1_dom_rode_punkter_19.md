# Case 1 (#2668): dom over de fem røde punktene i tekststopp-zipen (19:02) — dommer2, 05.11 19:16

**Zip:** `state/levering/c1_gronn/SISTE_GRONNE.zip` = `jurypakke_c1_1902_cbae393.zip`, sha256 e6dae498…7818 (stemmer med .sha256-fila). Pakket ut i tom `/tmp`-mappe.

## sjekk_rod.sh: ALT GRØNN (etter én skriptrettelse)
Første kjøring: 4 av 5 grønne. Punkt 5 slo på `SVAKHETER.md:77` (engelsk del): «measured on the older frozen #2044 … older 0.476». Innholdet er riktig merket, men skriptet godtok bare norsk «eldre». Rettet skriptet til å godta «older» også (`arbeid/oppgave_2658/sjekk_rod.sh`, mitt eget verktøy, ikke pakken). Ny kjøring: **ALT GRØNN**. Ingen tekst i zipen er rørt.

## De rettede linjene, lest for sannhet (ikke bare ordfjerning)
| linje | påstand | dom | kilde |
|---|---|---|---|
| kravrespons:10 | 0,512 like over målet 0,5; eldre frossen mistet ca. 0,06 uten samme-sesong-stemmer (0,415) | sann | 0,476−0,415=0,061 |
| kravrespons:10 | **«for repo4 er golvet ikke målt»** | **usann** | arkitekt #2645 (`c1_repo4_uten_historikk.md`, 17:35): repo4 uten samme sesong = **0,396** [−0,196; −0,027 mot 0,512], ikke reprodusert av dommer |
| ERLIG:53 | «rundt 0,5» leses som 0,512 (0,40–0,62), like over målet | sann | c1_repo4_tall_2592: KI [0,400; 0,621] |
| JURY_SPORSMAL:57 | repo4 byttet inn etter regelen; frossen 0,476, hybrid 0,545, PR-AUC 0,525 | sann | byttedom 17:02, sammenligning.md:11 |
| JURY_SPORSMAL:81 | hovedtall 0,512, byttet 17:02, avgjort av 2024/2025 | sann | c1_byttregel_forhand (+0,051/+0,017, regel 16:49 før måling 16:49–16:51) |
| JURY_SPORSMAL:82 | dommen 16:37 lot frossen stå mot V2/hybrid; 17:02 repo4 etter regelen | sann | c1_byttedom_265 |
| DEMO_MANUS:15 | 0,512, 32 av 58, 48 %, «atten måter, beste +0,014» | sann | TP32/58=0,552, P 0,478; KANDIDATER.md: 18 målinger, beste +0,0135 |
| DEMO_MANUS:56/63 | tallkildetabell, 96 av 100 | sann | c1_repo4_tall_2592 (TP 32 FP 35 FN 26, 161 av 1539), følg-styret 96,2 % |
| DEMO_MANUS:67 | kald kjøring sak 2596 gir samme tall, saker byttet etter «første av hver type» | sann | c1_demo_manus_repo4.md |

## Rødt: ett punkt, to linjer
`leveranse/kravrespons.md:10` og `leveranse/README.md:14` sier at golvet for repo4 ikke er målt. Det er målt (arkitekt #2645, rapport 17:35, før rettelsene #2653 17:45 og #2723 18:17). Tallet er verre enn teksten antyder: repo4 faller 0,512 → 0,396 (−0,116) uten samme-sesong-stemmer, mot −0,061 for eldre frossen; hele forspranget over frossen kommer fra samme-sesong-historikk. Dagens tekst underdriver pakkens største forbehold. Oppgave lagt til smed2 med linjenummer. Forbehold: 0,396 er arkitektens tall, ikke reprodusert av dommer; teksten bør si det.
Dette er en tekstendring etter tekststopp 19:02. Om den tas inn i endelig pakke 19:30 avgjør lederen; jeg anbefaler ja, fordi juryen vekter ærlig evaluering 60 %.
