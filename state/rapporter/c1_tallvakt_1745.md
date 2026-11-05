# Case 1: tallvakt og frysvakt på arbeidstreet kl. 17:45 (dommer #2676)

**Dom:** frysvakt grønn (21 filer uendret siden frys 2026-11-05T17:18:18). Tallvakt på standardsettet (levering/*.md, c1/leveranse/*.md, c1/*.md, 31 filer): 196 påstander stemmer, **0 avvik**. Måleren gir F1 0,512 (P 0,478, R 0,552, TP 32 FP 35 FN 26, 58 MOT i fasit).

**Utenfor standardsettet:** `c1/leveranse/kilder/*.md` (51 filer, går inn i jury-zipen og GitHub-kopien) gir **97 avvik**. Det er daterte kilderapporter, de fleste målt på den eldre frosne modellen (0,476, TP 30 FP 38 FN 28) eller om val 2025 / streng MOT / angrep. Tallene er riktige for det de rapporterer, men to steder sier rett ut at hovedtallet *skal være* 0,476 (c1_tall_likt.md:4, c1_streng_mot.md:30), og LESMEG.md sier ingenting om byttet til repo4 (0,512).

**Rettes av smed4 (#2671-stil, før tekststopp 19):**
1. LESMEG.md: én linje øverst: kildene er øyeblikksbilder fra i dag; rapporter uten «repo4» i navnet måler den eldre frosne modellen (F1 0,476); hovedtallet i pakka er repo4 0,512 (TP 32 FP 35 FN 26).
2. c1_tall_likt.md:4 og c1_streng_mot.md:30: «eldre:» like foran tallet (innen 45 tegn), ikke bare i HTML-kommentar bakerst.
3. Resten: merk linjene «eldre» der de er om 0,476-modellen, eller «tallvakt: ignorer» der de er om val/angrep/streng. Ikke endre tallene.

## Alle 97 avvik (fil:linje: påstand, måler)
```
TREFFSIKKERHET.md:20: F1 0,476, måleren sier 0.512
TREFFSIKKERHET.md:94: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_beslutning_nyeste_historikk.md:7: P 0,470, måleren sier 0.4776
c1_beslutning_nyeste_historikk.md:7: R 0,534, måleren sier 0.5517
c1_beslutning_nyeste_historikk.md:7: P 0,441, måleren sier 0.4776
c1_beslutning_nyeste_historikk.md:7: R 0,517, måleren sier 0.5517
c1_beslutning_nyeste_historikk.md:10: F1 0,476190, måleren sier 0.512
c1_feil_stabilitet.md:22: antall MOT 7, måleren sier 58
c1_feil_stabilitet.md:66: antall MOT 1, måleren sier 58
c1_huskeregel.md:3: F1 0,476, måleren sier 0.512
c1_injeksjon_etter_2205.md:22: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_injeksjon_hoflig.md:26: F1 0,476190, måleren sier 0.512
c1_kjoretid.md:14: F1 0,476190, måleren sier 0.512
c1_menneske_terskel.md:10: antall MOT 66, måleren sier 58
c1_mennesket_arbeid.md:12: til menneske 183 av 1539, måleren sier 161
c1_mennesket_arbeid.md:16: antall MOT 1, måleren sier 58
c1_motstand_etter_frys.md:18: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_neste_steg.md:4: F1 0,476, måleren sier 0.512
c1_offline_kaldstart.md:16: til menneske 188 av 1578, måleren sier 164
c1_offline_kaldstart.md:16: til menneske % 11,9, måleren sier 10.4
c1_offline_kaldstart.md:16: P 0,4412, måleren sier 0.4776
c1_offline_kaldstart.md:16: R 0,5172, måleren sier 0.5517
c1_offline_kaldstart.md:34: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_offline_kaldstart.md:34: P 0,4412, måleren sier 0.4776
c1_offline_kaldstart.md:34: R 0,5172, måleren sier 0.5517
c1_offline_kaldstart.md:35: til menneske 188 av 1578, måleren sier 164
c1_offline_kaldstart.md:35: til menneske % 11,9, måleren sier 10.4
c1_repo4_tall_2592.md:27: TP/FP/FN 36 3 22, måleren sier (32, 35, 26)
c1_repo4_tall_2592.md:27: F1 0,742, måleren sier 0.512
c1_repo4_tall_2592.md:27: P 0,92, måleren sier 0.4776
c1_repo4_tall_2592.md:27: R 0,62, måleren sier 0.5517
c1_repo4_tall_2592.md:27: F1 0,306, måleren sier 0.512
c1_repo4_tall_2592.md:27: P 0,79, måleren sier 0.4776
c1_repo4_tall_2592.md:27: R 0,19, måleren sier 0.5517
c1_repo4_tall_2592.md:28: TP/FP/FN 40 3 18, måleren sier (32, 35, 26)
c1_repo4_tall_2592.md:28: F1 0,792, måleren sier 0.512
c1_repo4_tall_2592.md:28: P 0,93, måleren sier 0.4776
c1_repo4_tall_2592.md:28: R 0,69, måleren sier 0.5517
c1_repo4_tall_2592.md:28: F1 0,306, måleren sier 0.512
c1_repo4_tall_2592.md:28: P 0,79, måleren sier 0.4776
c1_repo4_tall_2592.md:28: R 0,19, måleren sier 0.5517
c1_retningslinje_sitat.md:8: F1 0,4818, måleren sier 0.512
c1_robusthet_frossen.md:22: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_robusthet_frossen.md:22: F1 0.4762, måleren sier 0.512
c1_robusthet_frossen.md:22: P 0.4412, måleren sier 0.4776
c1_robusthet_frossen.md:22: R 0.5172, måleren sier 0.5517
c1_robusthet_frossen.md:23: TP/FP/FN 27 59 31, måleren sier (32, 35, 26)
c1_robusthet_frossen.md:23: F1 0.3750, måleren sier 0.512
c1_robusthet_frossen.md:23: P 0.3140, måleren sier 0.4776
c1_robusthet_frossen.md:23: R 0.4655, måleren sier 0.5517
c1_robusthet_frossen.md:24: TP/FP/FN 0 0 58, måleren sier (32, 35, 26)
c1_robusthet_frossen.md:24: F1 0.0000, måleren sier 0.512
c1_robusthet_frossen.md:24: P 0.0000, måleren sier 0.4776
c1_robusthet_frossen.md:24: R 0.0000, måleren sier 0.5517
c1_robusthet_frossen.md:25: TP/FP/FN 0 0 58, måleren sier (32, 35, 26)
c1_robusthet_frossen.md:25: F1 0.0000, måleren sier 0.512
c1_robusthet_frossen.md:25: P 0.0000, måleren sier 0.4776
c1_robusthet_frossen.md:25: R 0.0000, måleren sier 0.5517
c1_robusthet_frossen.md:26: TP/FP/FN 30 33 28, måleren sier (32, 35, 26)
c1_robusthet_frossen.md:26: F1 0.4959, måleren sier 0.512
c1_robusthet_frossen.md:26: P 0.4762, måleren sier 0.4776
c1_robusthet_frossen.md:26: R 0.5172, måleren sier 0.5517
c1_robusthet_frossen.md:27: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_robusthet_frossen.md:27: F1 0.4762, måleren sier 0.512
c1_robusthet_frossen.md:27: P 0.4412, måleren sier 0.4776
c1_robusthet_frossen.md:27: R 0.5172, måleren sier 0.5517
c1_robusthet_frossen.md:28: TP/FP/FN 23 20 35, måleren sier (32, 35, 26)
c1_robusthet_frossen.md:28: F1 0.4554, måleren sier 0.512
c1_robusthet_frossen.md:28: P 0.5349, måleren sier 0.4776
c1_robusthet_frossen.md:28: R 0.3966, måleren sier 0.5517
c1_robusthet_frossen.md:29: TP/FP/FN 35 57 23, måleren sier (32, 35, 26)
c1_robusthet_frossen.md:29: F1 0.4667, måleren sier 0.512
c1_robusthet_frossen.md:29: P 0.3804, måleren sier 0.4776
c1_robusthet_frossen.md:29: R 0.6034, måleren sier 0.5517
c1_robusthet_frossen.md:42: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_robusthet_frossen.md:42: til menneske 188 av 1578, måleren sier 164
c1_robusthet_frossen.md:42: til menneske 183 av 1539, måleren sier 161
c1_robusthet_kald_2380.md:3: F1 0,476190, måleren sier 0.512
c1_robusthet_reprod.md:10: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_robusthet_reprod.md:10: P 0,4412, måleren sier 0.4776
c1_robusthet_reprod.md:10: R 0,5172, måleren sier 0.5517
c1_robusthet_sjekk.md:6: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_robusthet_sjekk.md:6: F1 0,4762, måleren sier 0.512
c1_streng_mot.md:30: F1 0,476, måleren sier 0.512
c1_streng_mot.md:30: F1 0,482, måleren sier 0.512
c1_streng_mot.md:30: P 0,44, måleren sier 0.4776
c1_streng_mot.md:30: R 0,52, måleren sier 0.5517
c1_tall_likt.md:4: TP/FP/FN 30 38 28, måleren sier (32, 35, 26)
c1_tall_likt.md:4: F1 0,476, måleren sier 0.512
c1_tall_likt.md:4: P 0,441, måleren sier 0.4776
c1_tall_likt.md:4: R 0,517, måleren sier 0.5517
c1_titlecase_vakt.md:34: TP/FP/FN 29 40 29, måleren sier (32, 35, 26)
c1_val_kaldstart.md:24: TP/FP/FN 45 29 54, måleren sier (32, 35, 26)
c1_val_kaldstart.md:24: antall MOT 99, måleren sier 58
c1_val_kaldstart.md:24: P 0.608, måleren sier 0.4776
c1_val_kaldstart.md:24: R 0.455, måleren sier 0.5517
dommer_2090_streng_mot.md:26: antall MOT 99, måleren sier 58
```

Kommando: `python3 -I arbeid/verktoy/c1_tallvakt.py arbeid/hack/c1/leveranse/kilder/*.md` (standardsett: uten argumenter).
