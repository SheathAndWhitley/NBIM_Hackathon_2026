# Byttplan Case 1 (#2572): frossen #2044 miks h2 -> repo4, bare hvis dommer2 sier BYTT (#2570)

Vinner hvis BYTT: **repo4** = oppgave_2490/abl.py (frossen #2044 + 4 historikktrekk fra NBIM-repoet:
prev_same_item, prev_same_person, prev_meeting_any_dev, hist_type_dev_rate). Benken #2567 (benk.txt):
F1 MOT 0,5057 / 0,5309 / 0,5120 for 2024/25/26 mot frossen 0,4545 / 0,5143 / 0,4762 (snitt +0,035, dårligste år +0,017).
Vinner en annen kandidat (#2568 snitt, person): samme steg, bytt modellfila og argv i steg 1.

## Staget og testet nå (16:50–17:15), ingen frosne filer rørt
`arbeid/hack/c1/bytte/`:
- `modell_repo4.py`: abl.py med relativ sti til `stemmeagent/` (var hardkodet til arbeid/hack/CASE/..., ville knekt kald kopi)
  og `import os`. Gir **byte-identiske** testprediksjoner med oppgave_2490/repo4_test.csv under låst miljø smed2_c1_mot.
- `stemmeagent/{__init__,config,ballot}.py`: bare det `ballot.py` trenger (numpy/pandas, ingen nye pakker).
- `c1_real.py`: frossen fil med 2 endringer (TRAIN -> modell_repo4.py, argv + `--repo`).
- Prøvekjørt hele agenten i /tmp/b2572tree under `env -i`: 7 s, måler v3 F1 MOT **0,5120** (TP 32 FP 35 FN 26,
  P 0,4776, R 0,5517); `--sak` med ny ukjent sak virker (rutes til menneske).
- `bytt.sh` (tørt som standard), `oppdater_lister.py`, `bytt_tall.py`.

## Stegene (mål: under 20 min)
0. BYTT-dom skriftlig fra dommer2. Kunngjør på tavla: «bytter frys, rør ikke levering/ til grønt».
1. `sh arbeid/hack/c1/bytte/bytt.sh` (tørt, se stegene), deretter `sh arbeid/hack/c1/bytte/bytt.sh --utfor`. Skriptet:
   - kopierer modell_repo4.py, c1_real.py, stemmeagent/ til arbeid/hack/levering/
   - legger nye filer i `c1_frys.py` FILER og `fremmed.sh` (pakk_jury.sh/frys_fasit.py leser FILER selv)
   - kjører agenten og skriver nye `kjor_agent_real_maskin_alene.csv`, `kjor_agent_real_pred_maaler.csv`,
     `kjor_agent_real_test2026.txt` (frossen `oppgave_2103/full_test.csv` står, gjelder gammel modell)
   - `bytt_tall.py --skriv`: ca. 180 erstatninger i 24 tekster (0,476->0,512, TP/FP/FN, P, R, 188->164 av 1578, 11,9->10,4 %),
     hopper over linjer om frossen/#2044/2024/2025
   - `c1_frys.py frys --tving` + ny fasit `frys_fasit_1600.sha256` + `frys_diff.sh --kilde`
   - tallvakt --vis og `c1_etterfrys.sh` (frysvakt, tallvakt, kald kopi)
2. For hånd (5 min, skriptet gjør det ikke):
   - KI for hovedtallet: `python3 -I arbeid/hack/levering/treffsikkerhet_ki.py` og bytt «[0,36; 0,59]» i README/TREFFSIKKERHET/JURY.
   - TN og accuracy i README:69 (fra måler v3-utskriften), modellnavn «miks h2» -> «miks h2 + 4 repotrekk (repo4)» i README,
     METODE, demo.sh-ekko, c1_real.py-docstring.
   - ERLIG_EVALUERING: tre-års-tabellen beholder frossen-radene; legg til at repo4 ble valgt etter regelen fastsatt før måling.
3. `grep -rn "0,476\|0\.476" arbeid/hack/levering/*.md arbeid/hack/c1/leveranse/*.md`: hver rest skal være om gammel modell.
4. `bash arbeid/hack/levering/sluttsjekk.sh` og `sh arbeid/hack/levering/pakk_jury.sh` -> ny jury-zip, `test_jury_zip.sh`.
5. Commit: `git add arbeid/hack/levering arbeid/verktoy/c1_frys.py arbeid/hack/c1 state/c1_frys.json && git commit`.

## Tilbake (hvis rødt og ikke rettet innen 10 min)
`git checkout $(cat /tmp/bytte2572_head.txt) -- arbeid/hack/levering arbeid/verktoy/c1_frys.py arbeid/hack/c1/leveranse`,
`rm -rf arbeid/hack/levering/stemmeagent arbeid/hack/levering/modell_repo4.py`, og gjenopprett `state/c1_frys.json`
fra kopien skriptet tok i steg 0: `cp /tmp/bytte2572_c1_frys.json state/c1_frys.json` (fila er ikke i git).

## Kjente risikoer
- KJORING-formatet fra dagens kjor_agent.py («avvik fra styret 73, av dem MOT 70») er ikke likt den frosne txt-fila
  («MOT styret 74»); tallvakta leser «til menneske X (p %)», sjekk at den er grønn.
- PR-AUC 0,5368 i agenten mot 0,5369 frittstående (annen inndatafil); F1/prediksjoner er like.
- Rutingsbåndet og kalibreringen låses på nytt på val 2025 av den nye modellen (rå grense 0,92321).
