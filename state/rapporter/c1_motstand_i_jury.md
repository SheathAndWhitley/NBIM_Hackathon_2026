# Case 1: motstandstesten etter frys er lagt inn i jurytekstene (smed2, #2479)

**Kort:** Tallene fra kjøringen etter frysen (#2266) er like de som allerede sto i pakka. Derfor er bare kilden og henvisningene lagt til. Ingen tall er endret, og ingen frosne filer er rørt (frysvakta er GRØNN, 17 filer). Commit 8b8289e.

## Endret
- `c1/leveranse/kilder/c1_motstand_etter_frys.md` (ny): kopi av `c1_motstand_etter_frys.md` (#2266) med stier skrevet om slik LESMEG beskriver. Tabellraden med TP 29 FP 40 FN 29 (tall under angrep) har fått merket `tallvakt: ignorer`, slik JURY pkt. 11 allerede har.
- `JURY.md` pkt. 11: parentesen sier nå at testen er kjørt på nytt etter modellfrysen kl. 16 på den frosne agenten fra kald kopi, med de samme tallene, og peker på kilden.
- `ERLIG_EVALUERING.md` (avsnittet om motstandstesten): én setning om det samme.
- `kilder/LESMEG.md`: en linje om den nye kilden.
- `pakk_jury.sh` er ikke endret. Linje 31 kopierer allerede hele `c1/leveranse/`, også `kilder/`. Fila er dessuten midt i smed4s arbeid (#2475).

## Tall (fra kilden, uendret)
16/16 kjente instrukser fanges, 0 stille endringer, verste F1 MOT 0,457 (as Proposed by Management, as Always). Rent: 0,476. Av 16 nye tittel-instrukser slipper 6, med 18–27 stemmer endret uten ruting og F1 0,39–0,42.

## Tallvakt
- `c1_tallvakt.py` standard: 18 filer, 168 påstander, **0 avvik**.
- På de fire endrede filene: 25 påstander, **0 avvik**.

## Gjenstår for andre
- `frys_fasit_1600.sha256` er **ikke** laget på nytt. En ny fasit gir NY for `kilder/c1_motstand_etter_frys.md` og ENDRET for JURY, ERLIG_EVALUERING og LESMEG, men tar også med smed4s pyproject/uv.lock og en endring i NESTE_VERSJON som ikke er committet. Den som lager fasiten på nytt etter #2475/#2476, eller i #1972, får med mine filer automatisk: `python3 -I arbeid/hack/levering/frys_fasit.py > arbeid/hack/levering/frys_fasit_1600.sha256`.
