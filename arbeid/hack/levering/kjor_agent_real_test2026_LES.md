# Slik leses kjor_agent_real_test2026.txt (#2095, oppdatert #2179)

Loggen er rå utskrift fra agenten og måler v2 og er ikke endret. Den er fra den kalde kjøringen 05.11 kl. 13.07
(frossen #2044-modell, kalibrert bånd). Tre linjer kan misforstås:

- **«streng MOT: TP 0 FP 0 FN 0 ... F1 0,0000»** (linje 15 og 22) er ikke et null-tall. Måler v2 teller ikke streng MOT
  når svaret er 0/1. Måler v3 (`c1/maaler_offisiell_v3.py`) retter det. Hovedtallet, **F1 0,512 på MOT mot styret**
  (TP 32 FP 35 FN 26, KI [0,40; 0,62]), kommer fra v3 med `--score mot` (#2087).
- **«SCORE 0.481752»** er avvik fra styret inkl. AVSTÅ (66 avvik, mot 58 MOT). Det er et sidetall, ikke F1 på MOT.
- **«ruting (konfidens < 0.6)»** er målerens etikett. Agenten ruter når kalibrert P(MOT) er i [0,15; 0,85)
  (linje 3; loggen skriver «låst på val» om C og grensen, båndet er valgt på test-tabellen og sjekket på val, se `c1/leveranse/kilder/c1_menneske_terskel.md`). Agenten: 164 av 1578 saker inn (10,4 %, linje 2). Måleren: 161 av de 1539 sakene
  med fasit (10,4 %, linje 23). Linje 16 («0 til menneske») er måleren med ruting slått av.
  Begge tall er riktige, nevneren er ulik.

Sjekk: `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/hack/levering/kjor_agent_real_maskin_alene.csv test --data real --score mot`

Eldre logg: `arkiv/kjor_agent_holdout2026.txt` er fra 11.40 med en tidligere modell på gammel data.
Den er ikke grunnlag for noe tall i pakka.
