# Jurypakke-verktøy (#2352): zip + kald test i ett steg

`arbeid/verktoy/jurypakke.py` bygger zip fra pakkeliste, pakker ut i tom /tmp-mappe, kjører
`<python> -I <args>` der med tomt miljø, og sjekker utgangskode + at ingen fil/utskrift
inneholder <repo>. Håndbok: `arbeid/handbok/jurypakke.md`.

## Test (lekepakke arbeid/oppgave_2352/leke/)
| tilfelle | forventet | fikk |
|---|---|---|
| grønn pakke, kjor.py | 0 | 0, GRØNT |
| pakke med hardkodet sti (lekk.py) | 1 | 1, `lekk.py:1` flagget |
| kjor.py avslutter med 3 | 1 | 1, "utgangskode 3, forventet 0" |
| samme med `--utgang 3` | 0 | 0 |
| sti mangler i lista | 1 | 1, sti listet |
| `data => inndata` omdøping | inndata/saker.csv i zip | ja |
| __pycache__/*.pyc | ikke i zip | ikke i zip |

## Funn på ekte pakkeliste (tørt, ingen kjøring, arbeid/hack urørt)
`arbeid/oppgave_2333/pakkeliste.txt` med `--rot .`: 154 filer, 1,3 MB, **16 filer inneholder
landsbystien** (målerne v2/v3/nbim, sitatvakt, menneske_tabell, maaler.sh, fremmed.sh,
c1_tallvakt, demo-reserve, to .md). Full liste: `arbeid/oppgave_2352/lekk_pakkeliste_2333.txt`.
Noen er bare tekst i rapporter (ufarlig, men ser rart ut for juryen); .py/.sh-filene vil feile
eller lese fra landsbyen hvis de kjøres hos juryen. Til smed (#2346) og dommer2 (#2348).
Pakkelista blander også arbeid/hack, arbeid/kandidater, arbeid/verktoy, oppgave_20xx og
state/opplastet, så `--rot arbeid/hack` krever `kilde => mål`-linjer for resten.
