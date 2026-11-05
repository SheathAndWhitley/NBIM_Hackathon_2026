# Case 1: hvor mye arbeid får mennesket, og hvor mange MOT fanger det? (#2377, smed2 05.11)

> **Eldre tall:** linjer merket «eldre frossen modell #2044» gjelder modellen som var frossen før byttet til repo4 (#2572). Målte tall er ikke endret. Dagens hovedtall står i `arbeid/hack/c1/tall_tabell.md`.

Test 2026, frossen #2044 (miks h2), kjørt fra kald kopi med `fremmed.sh`. Ingen frosne filer er endret. 1539 saker har fasit, og 58 av dem er ekte MOT mot styret.
Måler: `maaler_offisiell_v3.py ... test --data real --score mot`. Maskin alene gir **0,476190 (TP 30, FP 38, FN 28)** i alle rader.
`_pred_uten_ruting.csv` fra standardkjøringen er byte-identisk med `levering/kjor_agent_real_maskin_alene.csv`.
Hver sak havner i én bunke. «Til menneske» betyr `til_menneske=1` i agent.csv, det vil si båndet pluss ukjent selskap og injeksjon. Saker som ikke rutes er enten «auto MOT» (agenten flagger) eller «auto FOR» (resten).

| bånd P(MOT) | til menneske (per 100 saker) | ekte MOT: auto MOT (TP) / til menneske / auto FOR (FN) | falske flagg: auto / til menneske | F1 maskin alene (TP/FP/FN) | F1 hvis mennesket treffer på bunken | F1 hvis mennesket følger styret |
|---|---|---|---|---|---|---|
| tomt bånd (bare ukjent selskap/injeksjon) | 70 av 1539 (4,5) | 28 / 7 (2 flagget) / 23 av 58 | 37 / 1 | 0,476 (30/38/28) | 0,538 | 0,455 |
| smalt [0,25; 0,75) | 120 av 1539 (7,8) | 12 / 23 (18 flagget) / 23 av 58 | 5 / 33 | 0,476 (30/38/28) | 0,714 | 0,320 |
| **standard [0,15; 0,85)** (låst på val 2025, #2128) | **183 av 1539 (11,9)** | **9 / 32 (21 flagget) / 17 av 58** | **0 / 38** | **0,476 (30/38/28)** | 0,828 | 0,269 | <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->
| bredt [0,05; 0,95) | 220 av 1539 (14,3) | 9 / 33 (21 flagget) / 16 av 58 | 0 / 38 | 0,476 (30/38/28) | 0,840 | 0,269 |

## Slik leses det
- **Standard:** mennesket får 12 av 100 saker. I den bunken ligger 32 av de 58 ekte MOT (55 %) og alle de 38 falske flaggene. Det er omtrent 1 ekte MOT per 6 saker i bunken, mot 1 per 27 i hele året (3,8 %). Agenten tar 9 MOT selv, og alle 9 er riktige. 17 MOT (29 %) går til auto FOR, og dem ser ingen. <!-- delsett (bunken til mennesket), eldre frossen modell #2044; tallvakt: ignorer -->
- **Smalere bånd** gir mindre arbeid (8 per 100), men 5 falske flagg går ut automatisk og 23 MOT havner i auto FOR. **Bredere bånd** gir 2–3 saker mer per 100 for 1 MOT til.
- **De to siste kolonnene er grenser, ikke resultater.** Den ene antar at mennesket treffer riktig på hele bunken. Den andre er gulvet der mennesket alltid følger styret. Hvor F1 havner mellom dem, avhenger av mennesket, og det har vi ikke målt.
- Båndet [0,10; 0,90) gir nøyaktig samme tall som standard. Kalibreringen er isotonisk med trinnverdier, og det finnes ingen P(MOT) mellom 0,0896 og 0,1667.
- Dette er bare beskrivende. Tallene er fra test, og båndet er ikke valgt på nytt. Standarden er låst på val 2025.

## Kommando (fra landsbymappen)
```
sh arbeid/hack/levering/fremmed.sh /tmp/k2377_tomt --baand 0.5,0.5; for b in 0.25,0.75 0.15,0.85 0.05,0.95; do sh arbeid/hack/levering/fremmed.sh /tmp/k2377_${b/,/_} --baand $b; done
python3 -I arbeid/oppgave_2377/arbeidsmengde.py /tmp/k2377_tomt/ut /tmp/k2377_0.25_0.75/ut /tmp/k2377_0.15_0.85/ut /tmp/k2377_0.05_0.95/ut
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py /tmp/k2377_0.15_0.85/ut/_pred_uten_ruting.csv test --data real --score mot   # SCORE 0.476190, TP 30 FP 38 FN 28
```
Logger ligger i `arbeid/oppgave_2377/kjor_*.log` (tomt bånd: `kjor_tomt.log`). Tallvakta i fremmed.sh melder AVVIK for ikke-standard bånd. Det er ventet, fordi teksten i pakka beskriver standardbåndet.
