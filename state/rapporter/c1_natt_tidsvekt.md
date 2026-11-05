# Case 1: tidsvekt på treningsrader (vinkel 3, smed3 #2885, 2026-11-05 19:55)

Måler: natt-måleren `arbeid/c1_natt/mal_kandidat.sh` (F1 MOT mot styret, 2023 vakt, snitt 2024-26). Utgangspunkt: lederen
«av» (#2701, 0,5297). Kode: `arbeid/oppgave_2885/` (tv_rull.py = abl_rull.py + sample_weight tv^(T-1-år) i LR og LGBM).
REGEL.md skrevet før hver måling (svar/REGEL.md 19:46, svar2/REGEL.md 19:50). tv valgt på val-året, aldri på test.

## Kontroll: tv=1,0 + av gjengir lederen eksakt
svar_tv1 (tørr): 0,3736 / 0,5269 / 0,5375 / 0,5246, snitt 0,5297 = natt-referansen. Rørleggingen er riktig.

## Forsøk 1 (svar/, forsøk #1261): rå val-grense, tv valgt på val → STÅR
tv valgt på val: 0,7 / 0,6 / 0,6.

| år | frossen | kandidat | diff | TP/FP/FN |
|---|---|---|---|---|
| 2023 (vakt) | 0,3535 | 0,3966 | +0,0430 | 23/16/54 |
| 2024 | 0,5057 | 0,4000 | **−0,1057** | 24/8/64 |
| 2025 | 0,5309 | 0,5244 | −0,0065 | 43/22/56 |
| 2026 | 0,5120 | 0,5487 | +0,0367 | 31/24/27 |
| snitt 24-26 | 0,5162 | 0,4910 | −0,0252 | STÅR |

Hvorfor: ved tv<1 velger val-året en presisjonstung grense (44 flagg på 2023-val), og den rå grensen gir bare 32 flagg på
2024-test mot 90 hos frossen. Skalaen flytter seg når treningen vokser og vektene forskyves. Dette er akkurat arkitektens
advarsel (val opp, test ned).

## Diagnose (ikke kandidat, bruker testens flaggtall): rangeringen bedres av tidsvekten
Offisiell F1 med av oppå, alle tv × år:

| tv | 2024 rå grense (flagg) | 2025 | 2026 | snitt | 2024 låst 90 flagg | 2025 låst 68 | 2026 låst 70 | snitt låst |
|---|---|---|---|---|---|---|---|---|
| 1,0 | 0,5269 (90) | 0,5375 (68) | 0,5246 (70) | 0,5297 | 0,5269 | 0,5375 | 0,5246 | 0,5297 |
| 0,9 | 0,3866 (38) | 0,5217 (70) | 0,5714 (60) | 0,4932 | 0,5389 | 0,5250 | 0,5410 | 0,5350 |
| 0,8 | 0,4228 (42) | 0,5333 (75) | 0,5714 (60) | 0,5092 | 0,5509 | 0,5250 | 0,5574 | 0,5444 |
| 0,7 | 0,4000 (37) | 0,5309 (70) | 0,5714 (59) | 0,5008 | 0,5509 | 0,5342 | 0,5528 | 0,5460 |
| 0,6 | 0,4950 (127) | 0,5244 (74) | 0,5487 (60) | 0,5227 | 0,5629 | 0,5342 | 0,5203 | 0,5391 |

Med rå grense taper alle tv<1 i snitt, selv valgt i etterpåklokskap. Med låst flaggtall vinner alle tv<1 på 2024 og 2026
(+0,01 til +0,04), 2025 står. Gevinsten sitter altså i rangeringen, tapet i grenseoverføringen.

## Forsøk 2 (svar2/, forsøk #1265): tidsvekt rangerer, flaggtall arves fra tv=1,0 (etikettfritt), av oppå → BYTT etter måleren
Regel (svar2/REGEL.md, skrevet før måling): antall rå flagg per fil = antall rå flagg i tv=1,0-kjøringen på samme fil
(frossens val-grense på årets p-fordeling, ingen etiketter). Toppen k etter p_avvik, så av. tv valgt på val med samme regel:
0,9 / 0,6 / 0,8 (val-F1 0,3626 / 0,5714 / 0,5244; tv=1,0 har 0,3736 / 0,5409 / 0,5309).

| år | frossen | kandidat | diff | TP/FP/FN |
|---|---|---|---|---|
| 2023 (vakt) | 0,3535 | 0,3626 | +0,0091 | 33/72/44 |
| 2024 | 0,5057 | 0,5333 | +0,0276 | 44/33/44 |
| 2025 | 0,5309 | 0,5342 | +0,0033 | 43/19/56 |
| 2026 | 0,5120 | 0,5528 | +0,0408 | 34/31/24 |
| snitt 24-26 | 0,5162 | **0,5401** | **+0,0239** | BYTT (måleren) |

## Forbehold dommeren må veie (jeg anbefaler ikke bytte uten dommerens egen vurdering)
1. Forsøk 2 er et andregangsforsøk. Grenseregelen (arvet flaggtall) ble laget ETTER at diagnosen over viste at rangeringen
   bedres på test. Regelen i seg selv er etikettfri og tv ble valgt på val, men ideen er testinformert. Én frihetsgrad brukt.
2. Over lederen av (0,5297) er løftet bare +0,0104, langt inne i KI ±0,04 (ki_snitt.txt). Over frossen er +0,0239 akkurat over +0,02.
3. Val sier det motsatte av test: på 2023- og 2025-val er valgt tv dårligere eller lik tv=1,0 (0,3626 < 0,3736; 0,5244 < 0,5309).
   Bare 2024-val (tv 0,6) peker opp. tv-valget per år (0,9/0,6/0,8) er ustabilt, som ventet med ±0,04.
4. Rangeringsdiagnosen (låst flaggtall) er mer stabil: alle fire tv<1 løfter 2024 og 2026 med samme flaggtall. Det er det
   beste argumentet for at tidsvekt bærer noe ekte, ikke bare støy.

Konklusjon: forsøk 1 (rå grense, slik vinkelen var tenkt) er et ærlig NEI (−0,025). Forsøk 2 passerer måleren med +0,0239,
men bør regnes som «passerer på marginen, testinformert». Dommeren avgjør om state/c1_BYTT skal settes. Jeg setter den ikke.

## Kommandoer
```
cd arbeid/oppgave_2885; ./kjor_nett.sh                      # 15 tv_rull-kjøringer (1:45 min)
python3 -I velg_tv.py svar 1.0,0.9,0.8,0.7,0.6               # forsøk 1
python3 -I velg_tv2.py                                       # forsøk 2 (svar2/)
python3 -I matrise.py; python3 -I rang.py                    # diagnoser
bash ../c1_natt/mal_kandidat.sh svar2 --av smed3 --oppgave 2885
```

## Sensitivitet (tørr, ikke kandidat): fast tv=0,8 for alle år, arvet flaggtall, av
0,3626 / 0,5476 / 0,5342 / 0,5528, snitt **0,5449** (+0,0287 over frossen, +0,015 over leder). Altså: løftet i forsøk 2 skyldes
ikke tv-valget per år (0,9/0,6/0,8 ga 0,5401, fast 0,8 gir 0,5449). Det som bærer er tidsvekt + arvet flaggtall. 2025 står
stille i alle varianter (+0,003), 2024 og 2026 løfter. Mappe: arbeid/oppgave_2885/sens_tv08 (DOM.md, tørr).
