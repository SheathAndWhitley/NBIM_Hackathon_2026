# Case 1: juryavsnitt «Ærlig evaluering» skrevet (speider #2096)

Ny fil: `arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md`. Det er lenket fra toppen av `c1/leveranse/JURY.md` og fra pkt. 6 i `c1/JURY_METODE.md`.
- (1) Ablasjonstabellen: full, uten sakstype, h1, uten historikk og uten LGBM, med val og test og P/R. Kilde: c1_ablasjon_v2.md.
- (2) Forbeholdet: h2 forutsetter at NBIMs tidligere stemmer samme sesong er kjent. Uten det er test-F1 0,386. Kilder: c1_ablasjon_v2.md og dommer_ablasjon_v2.md.
- (3) Støy: forskjeller under ~0,02 er ±1 sak. KI-en til hovedtallet er [0,36; 0,59].
- Hovedtallet er 0,476 på MOT, det samme som i #2095-lista (c1_tall_likt.md).
- Hvert tall har en kildemarkør. Et skript sjekket at alle tall i fila finnes i de fem kilderapportene. Eneste unntak er årstallet 2024 («trent <2025» i kilden).

Forbehold jeg la inn selv: ablasjonen er målt på avvik (full 0,482), ikke på MOT. h1 er ikke målt på MOT alene, så fila oppgir ikke noe h1-tall på hovedmålet. Trengs det, må smed3 kjøre h1 med `maaler_offisiell_v3.py --score mot`.
Resten av JURY.md (N-PX-tall) er ikke rørt. Den hører til #1975.
