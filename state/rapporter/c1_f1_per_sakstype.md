# Case 1: F1 på MOT per sakstype for den frosne agenten #2044 mot huskeregel A (smed2 #2375)

Test 2026, ekte data (sha 71ba5135…), samme regler som måler v3 `--score mot`. Agent = `arbeid/hack/levering/kjor_agent_real_maskin_alene.csv` (frossen #2044), huskeregel A = `arbeid/oppgave_2350/regel_A_test.csv`. Ingen modellendring.
Totalene stemmer eksakt med måleren (agent 0,476, regel A 0,243). Reproduser: `python3 -I arbeid/oppgave_2375/per_gruppe.py` (bare stdlib, utskrift i `arbeid/oppgave_2375/ut.txt`).

**Svakest:** agenten er svakest på **lønn** (F1 0,40, 3 av 4 MOT funnet, men 8 falske MOT, og huskeregel A er like god der: 0,43). Lønn har bare 4 MOT, så tallet er usikkert. Den store feilkilden i volum er **styrevalg** (F1 0,42, 26 av 38 falske MOT). Der slår agenten regelen klart (0,42 mot 0,15).

| gruppe | saker | MOT i fasit | agent TP/FP/FN | agent P | agent R | **agent F1** | regel A TP/FP/FN | regel A P | regel A R | **regel A F1** |
|---|---:|---:|---|---:|---:|---:|---|---:|---:|---:|
| styrevalg | 729 | 26 | 14/26/12 | 0,350 | 0,538 | **0,424** | 17/179/9 | 0,087 | 0,654 | **0,153** |
| lønn | 133 | 4 | 3/8/1 | 0,273 | 0,750 | **0,400** | 3/7/1 | 0,300 | 0,750 | **0,429** |
| aksjonærforslag | 16 | 2 | 1/0/1 | 1,000 | 0,500 | **0,667** | 2/0/0 | 1,000 | 1,000 | **1,000** |
| annet | 661 | 26 | 12/4/14 | 0,750 | 0,462 | **0,571** | 14/16/12 | 0,467 | 0,538 | **0,500** |
| **totalt** | 1539 | 58 | 30/38/28 | 0,441 | 0,517 | **0,476** | 36/202/22 | 0,151 | 0,621 | **0,243** |

Gruppering (bestemt før måling):
- **aksjonærforslag:** forslagsstiller = Shareholder, uansett sakstype. Det gjelder 16 saker. 10 av dem er styrevalg foreslått av aksjonærer, så styrevalg har 729 saker her og ikke 739 som i #2272.
- **styrevalg:** DIRECTOR_ELECTION fra ledelsen.
- **lønn:** SAY_ON_PAY, DIRECTOR_PAY og EQUITY_PLAN.
- **annet:** alt ellers, blant annet revisor, vedtekter, OTHER_MGMT og OTHER_BUSINESS (6/6 er en regel, se #2272).

Forbehold: lønn (4 MOT) og aksjonærforslag (2 MOT) har for få MOT til at F1 sier noe sikkert. Der kan én sak snu forskjellen mellom agent og regel. Konfidensintervall per sakstype finnes i `c1_feil_per_gruppe.md` (#2272).
