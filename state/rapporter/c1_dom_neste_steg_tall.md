# Dom #2420: hvert tall i neste-steg-rapporten har en kilde

Dommer, 05.11 kl. 15.45. Lest: `state/rapporter/c1_neste_steg.md` (#2409) og `arbeid/hack/c1/leveranse/NESTE_VERSJON.md`.
Ingen nye målinger. Hvert tall er slått opp i kilderapporten eller tavladatabasen (forsøk/oppgaver). Takene er regnet etter for hånd.

**Resultat: 0 tallfeil. Alle tall står i kilden.** To forbehold og én upresis henvisning under tabellen.

| tall | kilde | ok/avvik |
|---|---|---|
| F1 0,476 test 2026 (TP 30, FP 38, FN 28, 58 MOT) | `c1_feil_per_gruppe.md:4` | ok, 60/126 = 0,476 |
| F1 0,520 val 2025 (TP 45, FP 29, FN 54) | `arbeid/oppgave_2274/feil_val2025.md:1` | ok, 90/173 = 0,520 |
| 26 av 38 falske MOT på styrevalg (test) | `c1_feil_per_gruppe.md:25` (FP 26), `c1_falske_mot.md` «Tall» | ok |
| 22 av 29 falske MOT på styrevalg (val) | `feil_val2025.md:7` (FP 22) | ok |
| alle 9 falske MOT i USA snudd MOT→FOR | `c1_falske_mot.md` «Til juryen» og «Tall» | ok |
| samme person MOT året etter, USA: 4 av 4 (24→25), 0 av 5 (25→26) | `c1_falske_mot.md` «Tall» | ok |
| tak tiltak 1: 0,600 test / 0,596 val | `arkitekt_c1_neste_versjon.md` tabell | ok, regnet etter: 60/(60+12+28)=0,600; 90/(90+7+54)=0,596 |
| nyeste historikk A+B: val 2025 +0,021, val 2024 +0,028, KI dekker null | `c1_beslutning_nyeste_historikk.md` pkt. 9 | ok |
| PR-AUC 0,509 mot 0,525; USA fortsatt 9 falske MOT | `c1_beslutning_nyeste_historikk.md` pkt. 6 | ok |
| dom #2366 ikke inn; forsøk #2363 | tavle.db oppgaver 2363, 2366 (done) | ok |
| forfall med år (#2283): val 0,520→0,551, 2024 0,567→0,552 | `arkitekt_tiltak1_malt.md` tabell (0,520231→0,550898; 0,5672→0,5524) | ok |
| `rationale_section` finnes i dataene | `opplastet_20261105_114241_real_votes.md:7` (kolonneliste) | ok |
| kandidater på 0,01–0,04 F1 | India +0,008/+0,042, A+B +0,021/+0,028, tiltak 1 +0,031 | ok (avrundet spenn) |
| India +0,042 val 2025, p ≈ 0,06; 2024 +0,008, én sak, p = 1,0 | `c1_india_paret.md` tabell og «Slik leses det» | ok |
| seed-støy spenn 0,030 på 2024 | `c1_india_seeds.md` l. 24 | ok |
| bootstrap på test ca. ±0,1 | `c1_bootstrap_f1.md` l. 13 og 24 (v2: [0,375; 0,580]); v3-KI 0,35–0,59 i `c1_feil_per_gruppe.md:4` | ok |
| 9 FN test (revisor 4 + OTHER_MGMT 5), 10 FN val (4 + 6) | `c1_feil_per_gruppe.md:26-27`, `feil_val2025.md:9-10` | ok |
| tak tiltak 3: 0,578 test / 0,601 val | `arkitekt_c1_neste_versjon.md` | ok, regnet etter: 78/135=0,578; 110/183=0,601 |
| av 58 MOT på test havner 32 hos menneske (smed3 #2323, forsøk #1171) | tavle.db forsok 1171, notat | ok |
| revisorens år og honorar ikke i dataene | `opplastet_..._real_votes.md:7` (ingen slik kolonne) | ok |
| DEF 14A-fakta i sitatagenten «#1949–#1959» | tavle.db: sitatagent er #1950 og #1959; #1951–#1958 er andre oppgaver | upresis henvisning, ikke tallfeil |
| t4e 0,529 på test, forsøk #1033, måler v2; val 0,468 mot 0,522 | tavle.db forsok 1033 (0,529412, sha 9d81a418dd, vinkel «val 0,468»); `c1_valgt_bort.md` rad 1; 0,522 = frossen v2 val i `c1_bootstrap_f1.md:16` | ok |
| k=50: F1 0,517, 30 av 66 MOT, presisjon 0,60, tilfeldig 0,03 | `speider_2399_recall_budsjett.md` tabell og l. 23; forsøk #1179 | ok, se forbehold 1 |
| styrevalg USA → menneske: test 0,476→0,504, val 0,520→0,488 | `c1_feil_stabilitet.md:23` | ok |
| (#2409), (#2280), «sak 2283» | tavle.db oppgaver, alle done | ok |

## Forbehold (ingen av dem er tallfeil)
1. **k=50-tallene er på 66 MOT (v2-avvik), ikke 58 (v3).** Grunnlaget er `arbeid/oppgave_2044/pred_miks_h2.csv`, ikke utdata fra den leverte `kjor_agent`. Samme modell, men speideren skriver selv at det «bør måles på nytt på den frosne kjor_agent-utgangen etter kl. 16 før det siteres». Teksten i begge rapporter sier riktig at det ikke er hovedtall. Står det i JURY.md, bør det stå «66 MOT (avviksmåler v2)» ved siden av.
2. **t4e 0,529 er v2, hovedtallet 0,476 er v3.** Rapportene sier «måler v2» ved tallet, så det er ærlig merket. Les dem ikke som samme skala.
3. **Nummerering:** `arkitekt_c1_neste_versjon.md` kaller revisor/OTHER_MGMT «tiltak 2» og India «tiltak 3»; neste-steg-rapporten og NESTE_VERSJON.md kaller revisor «tiltak 3» og har «flere val-år» som tiltak 2. Tallene er like, bare nummeret er byttet. Kan forvirre en jury som leser begge.

## Avvik meldt til arkitekten
Bare henvisningen «#1949–#1959» (bør være «#1950 og #1959»). Lite nok til å rette med én linje i NESTE_VERSJON.md før frysen, eller la stå.
