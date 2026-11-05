# Case 1: står dommen fra #2366 i den frosne pakka? JA (#2374, dommer, 2026-11-05 15:14)

Dommen (#2366): nyeste-historikk A+B (#2363) bygges IKKE inn. Frossen #2044 miks h2 står med F1 MOT 0,476190.
Pakka som fryses kl. 16 er nøyaktig det. Bevis under, alt kjørt 15:10–15:14, før frysen.

## 1. Hva fryses, og peker det på #2044?
- Frysjobben: LaunchAgent `no.landsby.c1frys` er lastet (launchctl list), kjører `c1_frys.py frys` kl. 16:00 og skriver `state/c1_frys.json`. Fila finnes ikke ennå, som ventet.
- Fryslista (`arbeid/verktoy/c1_frys.py`) inneholder `arbeid/oppgave_2044/train.py` og `pred_miks_h2.csv`, ikke noe fra `oppgave_2363`.
- `c1_real.py` linje 35 laster `oppgave_2044/train.py` med runpy. Levert agent på tavla (`tavle levert`) peker på `kjor_agent_real_maskin_alene.csv`, forsøk 1046, måler v3 MOT.
- grep etter `nyest|snurate|train_nh|oppgave_2363` i de fem frosne kodefilene (train.py, kjor_agent.py, c1_real.py, vern.py, case1_mot.py): 0 treff.
  `train_nh.py` (#2363) skiller seg fra frossen train.py med 52 linjer; ingen av dem er i pakka. `fremmed.sh` kopierer ikke `hent_npx.py`/`usikkerhet.py` (eneste filer i c1/ som nevner ordet «nyeste», og de er ikke i agentens kjørevei).

## 2. Hasher (sha256, første 16 tegn, endringstid)
| fil | sha256 | endret |
|---|---|---|
| arbeid/oppgave_2044/train.py | 772fb71500e397cc | 11-05 11:53 |
| arbeid/oppgave_2044/pred_miks_h2.csv | 40afcc3e2fec85b2 | 11-05 11:53 |
| arbeid/oppgave_2103/full_test.csv | 69702192d3a4309e | 11-05 12:32 |
| arbeid/hack/levering/kjor_agent.py | dedc94062cf414e9 | 11-05 13:28 |
| arbeid/hack/levering/c1_real.py | 439b49f7483674e5 | 11-05 14:32 |
| arbeid/hack/levering/kjor_agent_real_maskin_alene.csv | 22ac6717e1287c5a | 11-05 12:07 |
| arbeid/oppgave_2047/vern.py | 19c3629fa670ffd8 | |
| arbeid/oppgave_2046/case1_mot.py | d403dd3c8f3b5876 | |
| arbeid/hack/levering/injeksjon_hoflig.py | 51cd0698342cfd7b | |
| arbeid/hack/levering/retningslinje_oppslag.py | 0a45c013471bd0b1 | |

Modell- og prediksjonsfilene fra #2044 er ikke rørt siden 11:53, altså lenge før #2363 (14:xx) og dommen (15:06).
A+B-filene fra #2363/#2366 (`pred_test_AB.csv` md5 8343bfc1…, `svar_test_AB.csv` md5 576b532e…) har andre hasher enn alt i fryslista.

## 3. Ett kjørt tall (måler v3 `--score mot`, test 2026, kjørt nå)
| fil | SCORE | TP / FP / FN |
|---|---|---|
| levert: kjor_agent_real_maskin_alene.csv | **0,476190** | 30 / 38 / 28 |
| frossen full_test.csv (#2103) | 0,476190 | |
| A+B-svaret fra #2363 (til sammenligning, IKKE i pakka) | 0,500000 | |

Levert fil gir 0,476190, som dommen sa, ikke A+B sitt 0,500000.

## Svar: JA
Pakka som fryses kl. 16 er frossen #2044 uten nyeste-historikk, nøyaktig som dommen i #2366. Ingenting å rette.
Etter kl. 16 bør `python3 -I arbeid/verktoy/c1_frys.py status` vise OK med sha-ene over (første 12 tegn er like).
