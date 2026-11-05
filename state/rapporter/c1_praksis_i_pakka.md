# Case 1 (#2342): praksis-mot-policy-tallet er ført inn i jurypakka etter dom #2334

Bare tall dommeren godkjente (`state/rapporter/c1_praksis_dom.md`), med forbeholdet: tallet sier at NBIM stemte som den avledbare policy-stemmen, ikke at MOT-stemmene var riktige.

- `arbeid/hack/c1/leveranse/kravrespons.md:10` (1-sideren): 81 av 82 regelstyrte saker (n lite), 565 av 569 MOT fra 2020 med GVG-begrunnelse, pluss forbeholdet. 1-sideren er nå 514 ord (var 463).
- `arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md:68`: «bare målt indirekte» erstattet med alle tre tallene (98,8 %, 94,9 % av 13 327, 99,3 % av 569) og fire forbehold.
- `arbeid/hack/levering/KRAVRESPONS.md:86` (rad 35): «mangler» → dekket, med pekere.
- Skript, utskrift, rapport og dom er kopiert til `c1/leveranse/kilder/` så jury-zipen (#2346) har kilden. `oppgave_2331_praksis_mot_policy.py` (ROT rettet for ny plassering) gir byte-identisk utskrift med `arbeid/oppgave_2331/utskrift.txt`.
- `state/rapporter/c1_kravdekning.md`: krav 13 = dekket. Opptelling 28 dekket, 6 svake, 0 mangler.

Ikke i demoen. Frossen #2044 er ikke rørt (bare tekst og en kopi av et telleskript).
