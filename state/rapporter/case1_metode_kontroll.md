# Case 1: hvert tall i METODE.md kontrollert mot forsøkstavla (dommer #2005)

**Kort fortalt:** Pkt. 1–5 og 7 stemmer. Pkt. 6 (ruting) brukte tall fra den lekkende fullmodellen (#1955), og pkt. 8 hadde «45 %» fra en eldre modell. Begge er rettet direkte i `arbeid/hack/levering/METODE.md`, med en kursiv linje som sier hva som ble endret. Ingen av de ugyldige forsøkene #1017–1019 er sitert lenger.

Kilder: forsøk fra `state/tavle.db` (tabellen forsok), dommer-rapporter i `state/rapporter/`. «Regnet» betyr at jeg regnet det selv fra prediksjonsfilene.

| pkt | tall i METODE | kilde | dom |
|---|---|---|---|
| hode | følg styret 89,7 % riktige, F1 0 | #989 (0), accuracy 0,897 i hack_c1_maaler_v3_nbim.md | OK |
| 1 | train 1631 / 9,1 %, val 1506 / 9,0 %, test 1246 / 10,4 % | hack_c1_maaler_v3_nbim.md l.14–16 | OK |
| 2 | gulv 0,383 test, 0,361 val | #994 0,383275, #996 0,360784 | OK |
| 3 | float 8–9 mnd, ~11 rader, e1 < D−100 d | case1_lekkasjesjekk.md l.12–14 | OK |
| 3 | før sjekken 0,418 / 0,509 | #1007 0,417508, #1006 0,509225 | OK |
| 3 | lekkasjefri b 0,403 / 0,493 | #1015 0,402597, #1014 0,492647 | OK |
| 3 | kostnad −0,016 [−0,054; +0,021] | case1_lekkasjefri.md (#1988) | OK |
| 4 | 2000 trekk, 129–136 MOT, b test [0,42; 0,56], val [0,33; 0,47] | case1_lekkasjefri.md, maaler_v3 | OK |
| 5 | 0,474 [0,404; 0,538], rå 0,1833, val 0,429 | #1023 0,474286, #1022 0,428571, case1_hovedtall.md | OK |
| 5 | +0,090 [+0,034; +0,147], +0,069 [−0,023; +0,156] | case1_hovedtall.md | OK |
| 5 | P/R 0,38 / 0,64, følsomhet 0,46–0,49 | case1_hovedtall.md | OK |
| 5 | 1,25× 0,493, −0,020 [−0,065; +0,027], 0,47 ± 0,07 | #1014, case1_hovedtall.md | OK |
| 6 | ECE 0,013 | #1955 (full modell). Variant b: 0,025 (#1995) | **feil, rettet** |
| 6 | 125 saker ved 10 % | #1955. Variant b: 119 på test | **feil, rettet** |
| 6 | presisjon 0,38→0,50 test, 0,37→0,42 val | #1955 (lekker, #1018 ugyldig). Variant b: 0,38→0,43 test, 0,34→0,37 val (ruting_b.txt) | **feil, rettet** |
| 6 | «+0,05 til +0,12» | avledet fra feil tall. Variant b: +0,02 til +0,05 | **feil, rettet** |
| 6 | kilde «case1_ruting.md, #1017–1019» | ugyldige forsøk sitert | **fjernet**, nå case1_ruting_verifisert.md, #1026/#1027 |
| 7 | 1544 av 1544 ordrette, 1 av 30 støtter | case1_sitatsjekk.md (#1991) | OK (presisert: Vanguard-holdout, v6) |
| 8 | val 0,43 mot test 0,47 | #1022 / #1023 | OK |
| 8 | +0,071 [+0,009; +0,135] «det meste av gapet» | #1990, men målt på den eldre modellen (gap 0,09); for b er gapet 0,045 | **upresist, rettet ordlyd** |
| 8 | 45 % fanges verken av gulv eller modell | ingen kilde for b; stammer fra #1978 (eldre modell, recall 0,55) | **feil, rettet** til 36 % test (46/129), 31 % val (42/136), regnet |
| bunn | måler-sha | hovedtallet bruker ee16e5945c, ikke nevnt | **lagt til** |

## Nye tall jeg regnet selv
Union av gulv (`hack/c1/ut_v3/gulv_data_v3*.csv`) og variant b (`oppgave_1993/b_*_g.csv`) mot `data_v3*/fasit.csv`: test gulv 55, modell 83, union 83 av 129 (46 ufanget). Val gulv 46, modell 78, union 94 av 136 (42 ufanget). På test er gulvet en ren delmengde av modellens treff.

## Merk
Arkitekten (#2003) redigerte METODE.md mens jeg kontrollerte (pkt. 5, siste setning). Den versjonen er kontrollert. Endres tallene etter modellfrys kl. 16, må kontrollen kjøres på nytt (speider #1975).
