# Case 1: jurysvarene sier nå at A+B-forsøket er valgt bort (#2383)

Dommeren avgjorde i #2366 at A+B (nyeste historikk) ikke kommer inn, og frossen #2044 (0,476) står (`state/rapporter/c1_beslutning_nyeste_historikk.md` pkt. 8–10). Disse stedene er endret:

- `state/rapporter/c1_vanskelige_sporsmal.md` svar 2: «Om det kommer inn, avgjør dommeren» er byttet ut med dommen og kilden.
- Samme fil, merknaden om at svar 2 skal skrives om: den sier nå at det er gjort, og at ingen nye tall er lagt til.
- `arbeid/hack/c1/leveranse/JURY.md` punkt 12: «med mindre dommeren slipper det inn før kl. 16» er byttet ut med «prøvd og valgt bort av dommeren (#2366)» og kilden. Tallet 0,500 er bevisst holdt utenfor JURY.md.
- `arbeid/hack/levering/*.md` (JURY_SPORSMAL.md m.fl.) nevnte ikke A+B eller #2366, så de er ikke endret.

Sjekk: grep etter `#2366`, `avgjør dommeren` og `slipper det inn` treffer bare de nye formuleringene. `c1_tallsjekk.py --bare-ikke` er ren. `fremmed.sh` gir TALLVAKT GRØNN. Frysvakta sier at frysen ikke er satt ennå.
