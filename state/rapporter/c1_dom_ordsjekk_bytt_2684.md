# Case 1 (#2684): dom over BYTT-ordsjekken etter #2653, kl. 17:50

**Dom: BYTT er GODKJENT.** Ordsjekken viser 0 synlige treff utover de godtatte, tallvakta har 0 avvik, frysvakta er grønn.

Kjørt selv kl. 17:47 etter at #2653 var lukket (commit 4c40dc6):
- `bash arbeid/oppgave_2646/ordsjekk.sh` → 27 treff totalt: 25 er `<!-- tallvakt`-kommentarer (skal stå til 19:00),
  2 er `levering/README.md:45` («TALLVAKT GRØNN» forklart, godtatt i #2679). Utskrift: `/tmp/dom2684_bytt.txt`.
- `python3 -I arbeid/verktoy/c1_tallvakt.py` → F1 0,5120 (TP 32 FP 35 FN 26), 31 filer, 195 påstander, 0 avvik, OK.
- `python3 -I arbeid/verktoy/c1_frys.py sjekk` → FRYSVAKT GRØNN, 21 filer like som ved frys 17:18:18.

## De 8 punktene fra #2679, lest linje for linje
| Pkt | Fil:linje | Nå |
|---|---|---|
| 1 | kravrespons.md:10 | «0,512 ligger like over målet vårt på 0,5» |
| 2 | ERLIG:53 | «les 0,512 (0,40–0,62), like over målet 0,5» |
| 3 | kravrespons.md:7 | «[0,40; 0,62]» |
| 4 | ERLIG:29, J:23 | «for den eldre frosne modellen fra 0,476 til 0,415», merket ikke målt på nytt for repo4 |
| 5 | J:81–83 | «I drift i dag setter vi repo4», V2 er neste versjon; «Den frosne agenten står» er borte |
| 6 | README.md:9 | setningen om byttet etter regelen på tre testår (2024–2026) er lagt til |
| 7 | internspråk | «grønn pakke», «benk A/B», «grønne» borte i synlig tekst |
| 8 | repo4 første gang | forklart «frossen modell + fire historikktrekk» i levering/README:3, README:11, J:12 |

De tidligere godtatte treffene ERLIG:34/104 og J:69 («valgt på test») er omskrevet til «valgt ut fra test» med samme mening; innholdet er fortsatt sant.

## Ikke dømt her
Innholdet i `<!-- tallvakt`-kommentarene (fjernes ved tekststopp 19:00, #2549) og STÅR-kjeden (#2681, dømmes av dommer2 ved 18:45 i #2603).
