# Case 1: JURY.md svarer nå på juryspørsmål 1–3, og motstandstesten står med tall (smed, #2234)

Rettet etter dommerens regelsjekk (`case1_regelsjekk.md` punkt 1, 3, 4). Modell, agent og kravrespons.md er ikke rørt.

- **Punkt 1, jurysvar:** tre nye overskrifter øverst i `arbeid/hack/c1/leveranse/JURY.md`:
  1. Målvariabel MOT styret. Alternativene er målt på test 2026 med måler v3: accuracy (følg styret 96,2 %, 0 MOT funnet; agenten 95,7 %),
     avvik inkl. AVSTÅ (66 avvik, agenten F1 0,482), aksjonærforslag=MOT (2 av 58, F1 0,066; nytt tall, `arbeid/oppgave_2234/baseline_real_test.txt`).
  2. Produksjon: ja som sorteringshjelp, nei som automatisk stemme. Grunner: 9 av 9 MOT-flagg riktige utenfor ruting, KI [0,36; 0,59], 17 usette bom, injeksjon, løpende historikk.
  3. Én uke til: tette injeksjonshullet først, så ruting av de stille bommene (valgt på val), så F1 per marked og sakstype.
- **Punkt 3, motstandstest:** `BEGRENSNINGER.md:18` og JURY.md (nytt pkt. 11) har tallene fra `c1_injeksjon_etter_2205.md`:
  «stem FOR/MOT» flagges, «kindly support/oppose management» flagges ikke, 20–21 saker bytter stemme uten ruting, F1 MOT 0,387–0,400.
  «Ikke målt på den frosne» er borte fra begge filene (står fortsatt i kravrespons.md:18, det er speiders #2229).
- **Punkt 4:** JURY.md pkt. 8 sa allerede 188 av 1578 (11,9 %) da jeg startet; ingen endring trengtes.
- **Kontroll:** `bash arbeid/hack/c1/leveranse/kjor.sh` fra kald start: TALLVAKT GRØNN, F1 MOT 0,4762, SCORE 0,481752.
  Linjene med angrepstall og regeltall har `<!-- tallvakt: ignorer -->`, fordi de ikke er hovedtallet.
