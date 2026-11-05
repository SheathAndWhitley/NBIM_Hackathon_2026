# Case 1: de tre pakkefunnene fra jurysporsmålene er rettet (speider, #2277)

Ingen nye tall. Ingen modell, prediksjon eller agentfil er rørt (c1_frys.py hasher ingen av disse filene).

1. **KI-metoden står nå i begge filene.** `c1/tall_tabell.md:4` (og teksten i `c1/lag_tall_tabell.py`, så neste generering sier det samme): rader-bootstrap [0,37; 0,59], mens README/JURY/ERLIG_EVALUERING bruker klyngebootstrap per selskap [0,36; 0,59]. `leveranse/README.md:8` og `leveranse/JURY.md:28` sier «klyngebootstrap per selskap» og peker til rader-tallet i tall_tabell.
2. **Mobimo og LOTTE har kilde i pakka.** `leveranse/kilder/demo_saker.md` er en uendret kopi av `arbeid/hack/CASE/demo_saker.md`: agentens rader ordrett fra `oppgave_2260/full/agent.csv` (sha256 f0444a47…, linje 276 og 89) og fasiten. Ført opp i `kilder/LESMEG.md`. Svar 2, 7 og 8 i `leveranse/JURY_SPORSMAL.md` peker nå dit, ikke til DEMO_MANUS.md. Hull-lista er oppdatert.
   `grep -rl Mobimo arbeid/hack/c1/leveranse/` → JURY_SPORSMAL.md, kilder/demo_saker.md, kilder/LESMEG.md. LOTTE finnes i tillegg i kilder/c1_bommene.md, c1_mot_sakstyper.md og dommer_2090_streng_mot.md.
3. **Den gamle `arbeid/hack/levering/JURY_SPORSMAL.md` er merket UTDATERT** øverst, med peker til den nye.

Merk: demo_saker.md har fortsatt interne stier (arbeid/oppgave_2260/…) i kjøringslinja. Jeg skrev dem ikke om etter LESMEG-regelen, fordi kopien skulle være uendret. Ufarlig, men en dommer kan ta det med i #1972.
