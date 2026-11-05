# Case 1: MOT-flagg som bare bygger på gammel historikk, sendt til menneske? (#2365, ordre #251, smed2 05.11)

Analyse, ingen modellendring. Frossen #2044 miks `--hist 2` er kjørt på nytt i en kopi. Test 2026 er byte-identisk med `oppgave_2044/pred_miks_h2.csv`. Val 2024 er tilbakeblikk med samme oppskrift (trent <2024, samme C=3 og rå grense 0,9188 fra val 2025).
MOT = v3 `--score mot` (NBIM MOT og against_board 1; agentens MOT = flagg der styret ikke sier MOT). Test- og valtallene er sjekket med `maaler_offisiell_v3.py` direkte (0,476190/0,513274 test, 0,520231/0,481013 val).

## Kategorier for MOT-flagg (selskapets egne etiketter fra møter før radens dato)
| År | ingen MOT i selskapet før (ekte/falske) | siste MOT året før | **siste MOT 2+ år tilbake** | presisjon «gammel» | presisjon resten |
|---|---|---|---|---|---|
| val 2024 | 5/4 | 34/24 | **8/15 (23 flagg)** | 0,35 | 0,58 |
| val 2025 | 2/4 | 36/17 | **7/8 (15)** | 0,47 | 0,64 |
| test 2026 | 2/1 | 27/25 | **1/12 (13)** | 0,08 | 0,53 |

**«MOT året før som er snudd i sesongen» finnes ikke i noen av årene: 0 flagg.** Selskapene har ett møte i året, så det er ikke noe møte i sesongen før saken som kan snu MOT-en. Den brede lesningen (alle møter etter siste MOT fulgte styret) gir også 0. I praksis gjelder regelen derfor bare «siste MOT 2+ år tilbake».

## Hva skjer om disse går til menneske
«Agent» = F1 på det agenten selv sier (flyttede saker teller som ikke MOT). «Perfekt menneske» = øvre grense der mennesket treffer på alt det får.
| År | flyttet (ekte/falske) | andel til menneske | F1 frossen | F1 agent | diff [95 % KI, klyngebootstrap] | F1 perfekt menneske |
|---|---|---|---|---|---|---|
| val 2024 | 23 (8/15) | 1,2 % | 0,528 | 0,503 | −0,025 | 0,577 |
| **val 2025** | 15 (7/8) | 0,8 % | 0,520 | **0,481** | **−0,039 [−0,105; +0,010]** | 0,545 |
| test 2026 (etterkontroll) | 13 (1/12) | 0,8 % | 0,476 | 0,513 | +0,037 [−0,005; +0,076] | 0,526 |

Streng variant («eneste grunn»: samme modell uten historikk flagger heller ikke saken): 8/5/6 flyttet (2/1/0 ekte), 0,2–0,4 % til menneske, F1 agent 0,529 / 0,524 / 0,500 (diff +0,001 / +0,004 / +0,024).

## Slik leses det
- **Gamle flagg er svakere hvert år** (presisjon 0,08–0,47 mot 0,53–0,64 for resten). Det er et ekte og stabilt mønster, og det støtter å la et menneske se på dem.
- **Men å fjerne dem fra agentens MOT ville vi valgt bort på val:** begge valår taper F1 (−0,025 og −0,039). Bare test 2026 vinner, og det er der vi ikke får velge. Med en gammel MOT som eneste grunn var 35–47 % av flaggene ekte før 2026. Det er godt over bruddpunktet (omtrent F1/2 ≈ 0,26) der fjerning lønner seg. 2026 skiller seg ut (1 av 13), og det passer med de falske MOT og praksisskiftet (#2363/#2364).
- **Som ruting (flagget beholdes, mennesket bestemmer) er det trygt:** 0,8–1,2 % av sakene til menneske, 13–23 saker i året. F1 stiger i alle tre år hvis mennesket treffer. Det dårligste tilfellet er at mennesket alltid sier FOR, og da får vi radene «F1 agent» over.
- **Anbefaling: ingen endring i frossen agent.** Hvis vi vil, kan gammel historikk som eneste grunn nevnes i jurysvaret som kjent svakhet og kandidat for menneskekontroll, med val-tallene over. Tallet 0,513 på test skal ikke brukes som resultat, fordi det er valgt etter å ha sett test.

## Filer og kommandoer (fra landsbymappen)
```
cd arbeid/oppgave_2044 && for h in 2 0; do uv run --project ../oppgave_2023 python ../oppgave_2365/frossen_kopi.py ../hack/CASE/20261105_114241_real_votes.csv --variant miks --hist $h --ut /tmp/k2365_h$h.csv; done; cd ../..
cmp /tmp/k2365_h2.csv arbeid/oppgave_2044/pred_miks_h2.csv          # identisk med frossen
uv run --project arbeid/oppgave_2023 python arbeid/oppgave_2365/ruting.py arbeid/hack/CASE/20261105_114241_real_votes.csv   # tabellene + svarfiler
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2365/test_rutet.csv test --data real --score mot   # 0,513274 (val_rutet.csv val: 0,481013)
python3 -I arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2365/val_frossen.csv arbeid/oppgave_2365/val_rutet.csv val
```
`frossen_kopi.py` er train.py fra #2044 med to tillegg. Det første lagrer 2024/2025/2026. Det andre retter krasj ved `--hist 0` (DATO og LGBM leste historikk uansett). Hist 2-utdata er uendret, sjekket med cmp. Frossen `oppgave_2044/train.py` er ikke rørt.
Forsøket på tavla ble avvist fordi #2365 ikke har egen måler (bare dommeren kan sette den). Tallene er målt direkte med v3. sha256 av fila var 418a937e57 da jeg kjørte; andre rapporter oppgir 8b09c36e01, og dommeren bør sjekke om det er samme utregning.
