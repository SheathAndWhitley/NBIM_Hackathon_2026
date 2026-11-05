# Dom #2520: BEGRENSNINGER pkt 9 (rare inndata, #2512) – GODKJENT, alle fem svakheter er dømt i #2507, ordlyden pynter ikke

**Dom:** BEGRENSNINGER.md pkt 9 (linje 41–47, commit 2f24f0c) står. Hver av de fem svakhetene finnes som nummerert punkt i dommen #2507 (`dom_2499_rare_inndata.md`, svakhet 1–5), tallene stemmer med dommen, og tallsjekken er grønn. Ingen rettelse kreves før frysen.

## Svakhet for svakhet (BEGRENSNINGER mot dom #2507)
| pkt i BEGRENSNINGER | dom #2507 | likt |
|---|---|---|
| Tom fil (0 byte): utgang 0, tom agent.csv, «bare overskrift» | svakhet 1 (dømt på smedens logg) | ja |
| Manglende kolonne / semikolon stopper ikke, «mangler felt» per rad | svakhet 2, bekreftet på fil d | ja |
| Falsk injeksjonsgrunn på AI-saker, `injeksjon_hoflig.py:21` | svakhet 3, bekreftet i koden (regexen har `ai` alene, sjekket av meg nå) | ja |
| P(MOT) avhenger av batchen, opptil 0,007, grense 0,91885 mot 0,91896 | svakhet 4 (smedens maks 0,0072, grenser bekreftet) | ja, 0,0072 avrundet til 0,007 er innenfor |
| Uleste rader får `anbefaling` = FOR, `c1_real.py:210` | svakhet 5 (dommerens egen), `r.get("mgmt_rec") or "FOR"` står på linje 210 | ja |

Påstanden «Ingen tekst i real_votes eller test 2026 har «AI»»: sjekket real_votes.csv nå, 0 treff på ordet «AI» som helt ord. Test 2026 ligger i samme fil. Holder.

## Pynter ordlyden?
Nei. Teksten sier «fem svakheter står, ingen er rettet», og hvert punkt oppgir det trygge utfallet og det som er galt (f.eks. «Rutingen er trygg, grunnen er feil»). «Gjør:»-rådet til juryen er dekket av dommen (anbefaling bare ved til_menneske=0, P(MOT) med to desimaler). Én detalj: overskriften i dom #2507 sier «fire svakheter», mens brødteksten lister fem. BEGRENSNINGER valgte fem, som er det ærligste. NESTE_VERSJON.md linje 114–118 har svakhet 3 og 5 slik dommen krevde.

## Tallvakt og frys
- `python3 -I arbeid/verktoy/c1_tallsjekk.py --bare-ikke --feil`: 2652 tall i 18 filer, utgang 0 (grønn).
- `frys_diff.sh --kilde`: 1 avvik, JURY_SPORSMAL.md. Det kommer fra commit a180521 (#2522, «sak 2511» → «sak #2511») etter at fasit sist ble regenerert i fd77f82. Ikke fra #2512. #2519 (fasit etter siste tekstendringer) tar det.
- Kildekopiene i `kilder/` er like landsbyrapportene bortsett fra `<arbeidsmappe>`-maskering av stier, som er avtalt (#2513).
- BEGRENSNINGER.md er uendret mot HEAD.

## Ikke dekket
Jeg kjørte ikke de rare filene om igjen (det er gjort i #2507). Dommen her er på tekst mot dom.
