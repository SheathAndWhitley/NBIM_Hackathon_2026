# Case 1: nytt avsnitt i JURY.md, «Hvorfor vi ikke jaget testtallet» (#2298)

Lagt inn i `arbeid/hack/c1/leveranse/JURY.md` etter juryspørsmål 3. Hvert tall har kilde fil:linje i `kilder/`:
- Levert agent: 0,476 test 2026 (`c1_enkle_regler_og_hist1.md:1`), 0,520 val 2025 (`c1_val_kaldstart.md:23`).
- Tiltak 1: val 0,520231 → 0,550898 (+0,031, `c1_tiltak1_malt.md:18-19`), 2024 −0,015 KI [−0,043; 0,017] (`:25`).
- USA-ruting: test 0,476 → 0,504, val 0,520 → 0,488 (`c1_feil_stabilitet.md:23`).
- Regel: bare endringer som vinner både 2024 og 2025. Test 2026 brukes aldri til valg.

Ny kildefil: `kilder/c1_tiltak1_malt.md` er en kopi av `state/rapporter/arkitekt_tiltak1_malt.md`, med «#N» skrevet som «sak N», slik de andre kildene gjør. Linjene er de samme.
Tallvakta (`arbeid/verktoy/c1_tallvakt.py`) på JURY.md: 9 påstander om hovedtallet stemmer, 0 avviker, OK.
Sjekk etter frysen (#1975): tallene her er fra før kl. 16. Vinner India (#2294) eller person-trekkene (#2296) begge år, må avsnittet oppdateres.
