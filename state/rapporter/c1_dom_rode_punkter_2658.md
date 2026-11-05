# Case 1: dom over de fem røde punktene fra jurylesningen (#2658, 17:45)

Grunnlag: `state/rapporter/c1_jurylesning_repo4.md` (#2601). Måler: `bash arbeid/oppgave_2658/sjekk_rod.sh [c1-rot]`,
ett punkt per linje, GRØNN/RØD, avslutter 1 ved rødt. Den tar både arbeidstreet og en utpakket zip.

## Status nå (17:45)
| Punkt | Zip 5514792 (den juryen leste) | Arbeidstre | Eier |
|---|---|---|---|
| 1 «0,512 under målet» kravrespons:10, ERLIG:53 (JURY.md:5 alt rettet) | RØD 3 | RØD 2 | smed2 #2653 |
| 2 DEMO_MANUS leser opp 0,476 / 30 av 58 (:4/:15/:56/:63/:67) | RØD 5 | RØD 5 | smed #2659 |
| 3 JURY_SPORSMAL svarer som om frysen sto (:57, :81, :82) | RØD 3 | RØD 3 | smed2 #2653 (:57/:81 lagt til i oppgaven) |
| 4 JURY.md «frossen miks h2» / «test aldri brukt til å velge» | RØD 2 | GRØNN | smed4 #2661 (gjort) |
| 5 0,476 som hovedtall i JURY_METODE, SVAKHETER, tall_tabell, DEMO_MANUS_5min | RØD 9 | RØD 9 | smed #2659 |

## Avgjørelser
- #2653 (smed2) utvidet: JURY_SPORSMAL:57 og :81 sto ikke i ordsjekk-lista, bare :82. Nå står alle tre.
- #2664 (min egen fra #2596) overlappet #2659 på fire filer. Omskrevet til bare restene (kjor.sh:10, JURY_README,
  leveranse/README:16, c1/*.md inn i tallvakta, ny zip), og venter på #2659.
- JURY.md:21 «Golv: frossen miks h2 ... 0,415» står: gulvet ER målt på den frosne, så merkelappen er sann. Skriptet unntar den.
- ERLIG:34 «Den frosne modellen (0,476) lå under målet» er sann og unntatt.
- Dom etter tekststopp: #2668 (dommer2, 19:00, venter på #2549): kjør skriptet på den nye zipen OG les de rettede
  linjene selv; ordene borte er ikke nok, setningene må være sanne. #1972 (endelig pakke 19:30) bør også kjøre skriptet.

## Akseptkrav for grønt
`sjekk_rod.sh` gir «ALT GRØNN» på utpakket tekststopp-zip, tallvakt GRØNN, og demo-utskriften sier samme tall som manuset (#2660).
