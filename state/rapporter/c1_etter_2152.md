# Case 1: agenten kjørt på nytt etter menneske-vaktene (#2162, etter #2152)

**Kjøring** 05.11 kl. 13:07:47, 5 s: `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/c1_2162`
- Ny `levering/kjor_agent_real_test2026.txt` (kopi av KJORING.txt). Innholdet er likt kjøringen kl. 13:04 utenom tidsstempelet.
- `levering/kjor_agent_real_pred_maaler.csv` var fra 12:07 (gammelt bånd, 171 til menneske). Byttet med ny fil (183 til menneske).
  Stemmekolonnen er lik. Bare konfidensen har endret seg. `kjor_agent_real_maskin_alene.csv` (frysvaktens fil) er byte-lik og ikke rørt.

**Tall**
- F1 på MOT (v3 `--score mot`): **0,4762 uendret** (P 0,4412, R 0,5172, TP 30 FP 38 FN 28, 58 MOT). Gjelder med ruting, uten ruting og for den gamle fila.
- Til menneske: **188 av 1578 inn (11,9 %)**, **183 av 1539 med fasit (11,9 %)**, 1 med injeksjon, 0 som ikke kunne vurderes.
- v2-sidetallet (avvik) er fortsatt 0,4818.

**c1_tallvakt.py**
```
Måler v3 --score mot på arbeid/hack/levering/kjor_agent_real_maskin_alene.csv: F1 0.4762  P 0.4412  R 0.5172  TP 30 FP 38 FN 28  (58 MOT i fasit, 66 avvik)
Kjøring: til menneske 188 av 1578 inn (11.9%), 183 av 1539 med fasit (11.9%)
13 filer, 132 påstander om hovedtallet stemmer, 0 avviker
OK
```

**Tall som spriker (tallvakta fanger dem ikke, til smed2 #2158)**
1. `levering/kjor_agent_real_test2026_LES.md` linje 9–11: står «10 %-båndet», «228 av 1578 (14,4 %)», «223 av 1539 (14,5 %)» og «kald kjøring kl. 12.29 (#2094)».
   Riktig er kalibrert bånd [0,15; 0,85), 188 av 1578 (11,9 %), 183 av 1539 (11,9 %) og kjøring kl. 13:07 (#2162). Linjenumrene 2, 16 og 23 stemmer.
2. `levering/KRAVRESPONS.md` linje 46: står «176 til menneske (av 1578 inn), måleren 171». Er det ment som historikk, bør det merkes. Ellers skal det stå 188 / 183.
- Ikke et avvik: `JURY_SPORSMAL.md:46` «176 flagg» gjelder grense 0,83, ikke ruting. Tallene «122 av 1539 (7,9 %)» i README, BESLUTNINGSSTOTTE og JURYSVAR gjelder raden «bare båndet» og er riktige.
