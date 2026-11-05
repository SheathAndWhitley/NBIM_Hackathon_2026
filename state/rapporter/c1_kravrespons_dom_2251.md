# Case 1: dom over kravresponsen på én side (dommer #2251, 05.11 kl. 14.06)

**Dom: GODKJENT.** Fila er `arbeid/hack/c1/leveranse/kravrespons.md` (speider #2229, 14.00). Jeg la inn én bisetning som navngir måleren (se nederst); ellers er fila speiders.

## Sjekklista fra #2245
| krav | funn | ok |
|---|---|---|
| Én fil, begge README peker på den | `c1/leveranse/README.md:6` og `levering/README.md:13` peker på `c1/leveranse/kravrespons.md`; `EN_SIDE.md` kalles eldre utdyping; `levering/KRAVRESPONS.md` er merket INTERN linje 1 | ja |
| Maks 1 side | 436 ord, 2 571 tegn (grense 450 / 3 500); cupsfilter 12 cpi gir 1 side (1 Page-objekt i PDF) | ja |
| Tre overskrifter fra malen, 3–5 setninger | Hva vi bygde 4, Hvordan vi verifiserte det 5, Hva vi ville trengt videre 5 | ja |
| Tall lik `c1/tall_tabell.md`/pakka | F1 0,476, P 0,44, R 0,52, 30 av 58 (tall_tabell, README:24). 188 av 1 578 (README:8, BEGRENSNINGER:3). 3,8 % = 58/1539 (regnet). 96,2 % (JURY:7, README:24). 0,365 (JURY:45). 0,415 og 0,06 = 0,476−0,415 (JURY:49). 16/15/1 instrukser, 16 stemmer, F1 0,392 (ERLIG_EVALUERING:42). 20 saker, 15 avgjørende (BEGRENSNINGER:24, JURY:36) | ja |
| KI med metode | [0,36; 0,59] «bootstrap over selskaper» = klyngebootstrap per selskap i ERLIG:33, BEGRENSNINGER:7, JURY:28. Avviker med 0,01 fra tall_tabellens radbootstrap [0,37; 0,59], metoden er oppgitt, godtatt | ja |
| Måler oppgitt | Manglet. Lagt inn av meg: kjor.sh «måler svaret med vår egen `maaler_offisiell_v3.py` (F1 på MOT mot styret)». kjor.sh:17 kjører den. Ingen sha i énsideren; fil-sha er fortsatt 418a937e57 | ja (etter rettelse) |
| Ingen påstand med bare #nummer | 0 treff på `#[0-9]` | ja |
| Ingen markedsføring, begrensningene står | 58 MOT og bredt KI, løpende historikk som udokumentert antakelse, sitat er peker ikke grunn, åpent hull for Title Case-instruks | ja |

## Forbehold
1. Motstandstest-setningen (15 av 16 fanget) gjelder bare hvis injeksjonsvakta fra #2237 er med i frysen kl. 16. Smed #2257 melder vakta lagt inn med byte-lik test 2026. Tas den ut, må setningen skrives om (speider #1975).
2. JURY.md pkt. 11 og BEGRENSNINGER.md beskriver fortsatt det gamle «kindly support»-hullet. Ikke énsiderens feil, men #1975/#2255 bør rette det så pakka er konsistent.
3. ERLIG_EVALUERING.md:42 og BEGRENSNINGER.md:7 peker på `state/rapporter/...` og `arbeid/oppgave_...`, altså utenfor leveransemappa. Énsideren gjør det ikke. Står igjen til #2255.

## Min endring
Siste setning i «Hvordan vi verifiserte det»: fra «...ett kall fra prosjektmappen: `bash .../kjor.sh`.» til «...ett kall fra prosjektmappen, `bash .../kjor.sh`, som også måler svaret med vår egen `maaler_offisiell_v3.py` (F1 på MOT mot styret).» Kopi før endring: `arbeid/oppgave_2251/kravrespons_for_dommer_1400.md`. Ord 423 → 436, setninger uendret.
