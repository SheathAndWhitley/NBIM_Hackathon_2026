# Case 1: ett sett hovedtall i juryfilene (speider #2095, 05.11 ca. kl. 12.50)

**Settet som nå står i de rettede filene** (kilde #2087, sjekket med måler v3 kl. 12.45, gir SCORE 0,476190):
- **Hovedtall (#231):** F1 **0,476 på MOT mot styret**, test 2026, real_votes. P 0,441, R 0,517, TP 30 FP 38 FN 28, 58 MOT mot styret av 1539.
  **95 % KI [0,36; 0,59]**, klyngebootstrap per selskap (135), 2000 trekk, seed 0. Nytt skript: `arbeid/oppgave_2095/ki_mot.py`.
  Val 2025: 0,520 [0,41; 0,63].
- **Sidetall:** avvik fra styret inkl. 5 AVSTÅ 0,482 [0,375; 0,580] (#2086). Følg styret 0.
- **Ruting:** 176 av 1578 saker inn (11,2 %) hos agenten, og 171 av de 1539 med fasit (11,1 %) hos måleren. Begge stemmer, nevneren er ulik.

#2090 (dommeren verifiserer MOT-tallet) var ikke ferdig da dette ble skrevet. Endrer dommeren tallet, må filene under rettes igjen.

## Rettet (bare tekst, ingen kode)
| fil | hva |
|---|---|
| `c1/leveranse/README.md` | Boks med hovedtallet øverst. «Resultat» heter nå grunnlinje på N-PX. KI 0,31–0,45 er merket som N-PX. «kjor.sh er deterministisk» er byttet med «kjor_agent.py ga samme tall to ganger (#2077, #2080)» |
| `c1/leveranse/BEGRENSNINGER.md` | Hovedtall-linja og pkt. 1 har 0,476 [0,36; 0,59] og begge nevnerne. Pkt. 2–6 og 8 er merket som målt på N-PX-modellen |
| `c1/JURY_METODE.md` | Tabellen har en egen hovedtall-rad 0,476, og 0,482 heter avvik. KI og recall er rettet, og MOT er definert uten AVSTÅ |
| `levering/KRAVRESPONS.md` | «Hovedtallet nå» er 0,476, KI og begge nevnerne. Krav 9 er løst i tekst. Mindre-punktet og H6 er merket |
| `levering/BESLUTNINGSSTOTTE.md` | 66 heter avvik (58 er MOT). Intervall-linja har begge tallene |
| `levering/kjor_agent_real_test2026_LES.md` (ny) | Forklarer «streng MOT 0,0000», «konfidens < 0,6» og 171/176. Selve loggen er ikke endret |

## Gjenstår (ikke rørt, stort eller eid av andre)
1. `levering/README.md`, `levering/METODE.md`, `levering/JURYSVAR.md`: alt gjelder den gamle N-PX-modellen (0,474 [0,40; 0,54], 1246 saker, 119 rutet). De må skrives om eller tas ut av pakken. Dette hører til #1975 (speider 16.05) og H2 (arkitekt).
2. `c1/leveranse/kravrespons.md` (1-sideren) og `JURY.md` gjelder N-PX-regelen 0,383. Det er H1 og #1975.
3. Tabellen i `BESLUTNINGSSTOTTE.md` (c1_terskeltabell) teller avvik (66). Skal den telle MOT (58), må #2084 kjøres på nytt med v3 `--score mot`.
4. `levering/kjor_agent_real_test2026.txt`, `KJORING_til_menneske_*.txt` og `kjor_agent_holdout2026.txt` er rå logger. De to siste er N-PX (0,474286) og bør ut av pakken. Den første bør lages på nytt med v3 når H3 er rettet, så «streng MOT 0» forsvinner.
5. `levering/demo/README.md` sier at ruting er «konfidens < 0,6» og at sitatene er Vanguard. Begge deler gjelder stubben (H5, smed #2093).
6. Etter frys kl. 16: kjør `python3 -I arbeid/oppgave_2095/ki_mot.py <ny svar_test.csv> test` og bytt tallet overalt. Finn stedene med `grep -rn "0,476\|0,36; 0,59" arbeid/hack/levering arbeid/hack/c1`.
