# Case 1 (#2679): dom over ordsjekk-rettelsene i BYTT og STÅR, kl. 17:50

**Dom:** STÅR er GODKJENT (0 gjenstående ordsjekk-treff i reserve_staar, 0 ekte tall-avvik). BYTT er IKKE ferdig:
alle 8 punkter fra #2646/#2648 står fortsatt (24 synlige treff). #2653 ble tatt av smed2 først kl. 17:49, så det er
ikke en feil hos smeden, bare ikke gjort ennå. Frysvakt GRØNN (21 filer, frys 17:18:18). Ny dom på BYTT må tas når #2653 lukkes.

Kjørt selv: `bash arbeid/oppgave_2646/ordsjekk.sh` (BYTT), `bash arbeid/oppgave_2648/ordsjekk_staar.sh` (STÅR),
`python3 -I arbeid/verktoy/c1_tallvakt.py` (treet) og samme med `--svar arbeid/hack/levering/c1_v1/ut/pred_maaler.csv`
på `c1/reserve_staar/*.md`, `c1_frys.py sjekk`. Utskrift: `/tmp/dom2679_bytt.txt`, `/tmp/dom2679_staar.txt`.

## Tall
| Sett | Ordsjekk totalt | `<!-- tallvakt` (skal stå til 19:00) | Synlige treff | Gjenstående ekte | Tallvakt |
|---|---|---|---|---|---|
| BYTT (`c1/leveranse/` + `levering/README.md`) | 50 | 28 | 22 | **8 punkter, 19 linjer** | 196 påstander, 0 avvik |
| STÅR (`c1/reserve_staar/` + `levering/README.md`) | 36 | 22 | 14 | **0** (13 riktige i STÅR + 1 BYTT-fil) | 35 påstander, 3 måler-avvik (se under) |

## BYTT: gjenstående, fil:linje (stier under `arbeid/hack/`)
1. `c1/leveranse/kravrespons.md:10` «0,512 ligger under målet vårt på 0,5» → «like over». Regnefeil.
2. `c1/leveranse/ERLIG_EVALUERING.md:53` «les 0,512 (0,40–0,62), under målet 0,5» → «like over målet 0,5».
3. `c1/leveranse/kravrespons.md:7` «[0,36; 0,59]» → «[0,40; 0,62]» (KI-et til den frosne står i BYTT-teksten).
4. `c1/leveranse/ERLIG_EVALUERING.md:29` og `c1/leveranse/JURY_SPORSMAL.md:23` «fra 0,512 til 0,415» → «fra 0,476 til 0,415 (målt på den frosne)».
5. `c1/leveranse/JURY_SPORSMAL.md:82` «Den frosne agenten står.» er usant i BYTT (se også :81, :83).
6. `c1/leveranse/README.md:9` «Valgt på val 2025 (0,530), kjørt én gang på test» mangler setningen om byttet etter regelen på tre testår.
7. Internspråk: `kravrespons.md:7`, `ERLIG_EVALUERING.md:79` «grønn pakke innen 18:45»; `ERLIG_EVALUERING.md:79/93/102/104` «benk A/B»;
   `ERLIG_EVALUERING.md:106`, `JURY_SPORSMAL.md:88` «grønne». (`JURY_SPORSMAL.md:52` «tallvakt» er borte: ok.)
8. repo4 uforklart første gang: `levering/README.md:3`, `c1/leveranse/README.md:11`, `c1/leveranse/JURY_SPORSMAL.md:12`.

Godtatt i BYTT (riktige): `ERLIG_EVALUERING.md:34` og `:104` «valgt på test», `JURY_SPORSMAL.md:69`, `levering/README.md:45` («TALLVAKT GRØNN» forklart).

## STÅR: alt som vises er riktig i STÅR
«[0,36; 0,59]» (README:8, kravrespons:7, J:15/92, ERLIG:6/33), «under målet» med 0,476 (kravrespons:10, ERLIG:53),
«Den frosne agenten står» (J:82), «valgt på test» (README:9, J:69, ERLIG:34). «grønn», «benk», «tallvakt» (J:52) og repo4-uforklart er borte.
Eneste rest er `levering/README.md:3`, som er BYTT-fila (pkt. 8 over); ved STÅR rulles den tilbake av `tilbake_fra_zip.sh` (JURY_README fra zip 2587).

**Tallvakt STÅR, 3 avvik er målerens, ikke tekstens:** `reserve_staar/README.md:10` (×2) og `MUNTLIG.md:22` sier «188 av 1578 (11,9 %)» til menneske.
Tallvakta leser KJORING.txt fra repo4-kjøringen (164). Den frosne kjøringens tall er 1578 inn og 11,9 % (`kilder/c1_robusthet_frossen.md:11`, rad basis),
og 0,119 × 1578 = 188. Tekstene er riktige for STÅR. Hvis STÅR velges, må tallvakta kjøres med den frosne KJORING.txt (`--kjoring`), ellers blir den rød på disse tre.

## Neste
- Smed2 (#2653): de 19 linjene over. Ikke rør `<!-- tallvakt`-kommentarene før 19:00.
- Dommer: ny ordsjekk + tallvakt på BYTT når #2653 er lukket (oppfølgingsoppgave lagt, venter på #2653).
