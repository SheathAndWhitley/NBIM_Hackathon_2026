# Case 1: de tre rare-sak-funnene står nå i pakka (#2275)

Kilde: `state/rapporter/c1_rare_saker_dom.md` (dommer #2264). #2269 var ferdig før jeg skrev, så ingen skrivekollisjon.

- `arbeid/hack/c1/leveranse/BEGRENSNINGER.md` pkt. 3: nytt kulepunkt «Rare saker på den frosne agenten» med
  (a) ikke-latinsk eller uvanlig skrift rutes til menneske (også vietnamesisk), vakta kom før frys og endrer ingen stemme;
  (b) norsk/fransk tekst rutes riktig, men med villedende grunn «instruksjonslignende tekst»;
  (c) duplikat id: bare andre rad rutes, første får stemme uten ruting.
  «Gjør»-linja har fått to råd: sjekk språket når grunnen er instruksjonslignende tekst; fjern duplikate id-er før kjøring.
- `arbeid/hack/levering/README.md` linje 56: rutingsgrunnene lister nå «ikke-latinsk eller uvanlig skrift i forslaget»,
  pluss én setning om (b) og (c) med peker til BEGRENSNINGER pkt. 3.
- Ingen tall endret. `c1_tallvakt.py`: 15 filer, 160 påstander stemmer, 0 avviker, OK.
- Merk: `arbeid/` er i .gitignore, så endringen er ikke committet (som resten av pakka).
