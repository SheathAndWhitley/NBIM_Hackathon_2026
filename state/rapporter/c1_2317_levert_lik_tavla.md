# Case 1 (#2317): levert agent gir tallene tavla viser, avvik 0

Dommer, 2026-11-05 14:45. Etter dommen i #2297 (India valgt bort) og #2312 (bytte droppet)
er levert agent fortsatt frossen #2044 miks h2 (`tavle.py levert` peker på
`arbeid/hack/levering/kjor_agent_real_maskin_alene.csv`, måler v3 MOT 418a937e57).

## Hva jeg gjorde
1. Kald kopi med `sh arbeid/hack/levering/fremmed.sh /tmp/d_2317` (eget uv-prosjekt, `env -i`,
   bare arrangørens data). Logg: `arbeid/oppgave_2317/fremmed.log`. Tallvakt grønn, 36 s.
2. Målte tre tall på tre filer med `maaler_offisiell_v3.py ... test --data real --score mot`,
   regnet accuracy og følg-styret nøyaktig som server.py (#2214, samme regex på målerens
   «vurderte rader/avvik»- og «avvik: TP FP FN»-linjer). Skript: `arbeid/oppgave_2317/sammenlign.py`.

## Resultat

| fil                                   | F1 MOT   | accuracy  | følg styret | n    | TP/FP/FN (avvik) |
|---------------------------------------|----------|-----------|-------------|------|------------------|
| tavla: levert fil i landsbymappen     | 0.476190 | 95.3866 % | 95.7115 %   | 1539 | 33/38/33         |
| kald kopi: `_pred_uten_ruting.csv`    | 0.476190 | 95.3866 % | 95.7115 %   | 1539 | 33/38/33         |
| kald kopi: `pred_maaler.csv` (ruting) | 0.476190 | 95.3866 % | 95.7115 %   | 1539 | 33/38/33         |

AVVIK = 0 på alle tre tall. Kald kopis `_pred_uten_ruting.csv` er byte-identisk med den leverte
fila (sha256 22ac6717e128…). Tavlas tall (F1 0,476, acc 95,39 %, følg styret 95,71 %) er dermed
reprodusert fra kald start.

Merk: accuracy er regnet på «avvik fra styret» (inkl. AVSTÅ), slik dashbordet gjør; F1-hovedtallet
er på streng MOT (TP 30 FP 38 FN 28). Det er samme definisjon som i commit b808382.

Frysvakta var ikke aktiv (frys kl. 16). Sjekken må gjentas av #2285 etter frys.
