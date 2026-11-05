# Case 1: README-stier rettet etter speider #2687 (#2692)

Commit `09f6a18`. Speiderrapporten: `state/rapporter/c1_readme_stier.md`. Skript: `arbeid/oppgave_2692/rett_stier.py` (idempotent, stopper hvis gammel tekst ikke finnes nøyaktig én gang).

## Rettet (BYTT-tekstene i `c1/leveranse/`)
1. `README.md:28`: npx_votes-raden har nå «ikke i hovedtallet; bare i repoet, ikke i jury-zipen».
2. `README.md:30`: `arkiv/gammel_data/` merket «(bare i repoet, ikke i jury-zipen)».
3. `README.md:72`: `c1/hent_npx.py` og `c1/baseline.py` merket «(begge bare i repoet, ikke i jury-zipen)».
4. `JURY.md:9`: «kald kjøring fra tom mappe … med `kjor.sh` i repoet, i jury-zipen `sh KJOR.sh` med samme tall».
5. `JURY.md:28`: 96,0 % peker nå til `README.md` («Riktige tall fra kald start»); `TREFFSIKKERHET.md:16` er merket som den eldre frosne (95,7 %).

## Alt rettet av andre før jeg kom (sjekket i teksten)
6. `JURY.md:29`: står alt som repo4 0,529 med frossen 0,482 som eldre tall.
7. `kravrespons.md:10`: står alt «like over målet».
8. `kravrespons.md:7`: står alt [0,40; 0,62].

## Overlever ombygging
- README-rettelsene (1–3) ligger i BYTT-teksten, og `lag_staar.py` rører ikke de linjene, så STÅR-reserven arver dem: `reserve_staar/README.md` er bygd på nytt og `lag_staar.py --sjekk` sier LIK. `rett_staar.py --sjekk`: uendret.
- JURY.md er ikke i STÅR-kjeden (ingen reserve-utgave; `tilbake_fra_zip.sh` ruller den tilbake til zip 2587 ved STÅR). Da forsvinner 4 og 5, men 5 blir riktig igjen i STÅR (95,7 % er den frosne). Punkt 4 må i så fall kjøres på nytt: `python3 -I arbeid/oppgave_2692/rett_stier.py` (JURY-regel 5 vil da stoppe skriptet; kjør den ikke ved STÅR, eller ta regelen ut).

## Sjekker
| sjekk | resultat |
|---|---|
| tallvakt (`c1_tallvakt.py`) | 31 filer, 195 påstander, 0 avvik |
| ordsjekk BYTT (`oppgave_2646/ordsjekk.sh`) | 27 treff før og etter: 25 er `<!-- tallvakt`-kommentarer (telles for seg), resten KI-tall som er riktige for BYTT. Ingen treff på de nye linjene |
| ordsjekk STÅR (`oppgave_2648/ordsjekk_staar.sh`) | 34 treff, ingen på de nye linjene |
| frosne filer | ingen av de 21 frosne filene (c1_frys.py) er md; ikke rørt |

Ordsjekk-treffene er altså ikke 0, men de fantes før og gjelder ikke mine linjer. Vil noen ha dem til 0, er det 25 tallvakt-kommentarer og 6 KI-tall som er riktige for BYTT ([0,40; 0,62] m.fl.), dvs. mønsteret er skrevet for STÅR.

## Ikke gjort
- Jury-zipen (`SISTE_GRONNE.zip`) må pakkes på nytt med `pakk_jury.sh` for at rettelsene skal nå juryen; det hører til pakke-kjeden, ikke denne oppgaven.
- `https://vd.nbim.no/` (README:64) svarte ikke fra minien; lenken står urørt, må sjekkes i nettleser av guden.
