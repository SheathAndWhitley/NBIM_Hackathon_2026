# Case 1: demoen viser nå hovedtallet 0,476 og «rå / sjanse for MOT» på skjermen (smed2 #2235)

Modell, agent og prediksjoner er ikke endret. Kald start ga GRØNN, F1_MOT 0,476190, avvik 0. Endret: `demo_saker_2026.sh`, `demo_mangler_styret.sh`, `kaldstart.sh`, `leveranse/kjor.sh` (kommentar), `leveranse/README.md`.
c1_frys.py sier «ikke frosset ennå» (exit 0). Ingen frosne filer er rørt.

## Rettet
1. `demo_saker_2026.sh`: siste linje er måler v3: `HOVEDTALL maaler_offisiell_v3.py full/_pred_uten_ruting.csv test --data real --score mot: F1 MOT 0.476190`. 0,4818 står over den, merket «avvik inkl. avstå (sidetall, ikke hovedtallet)».
2. Begge demoene skriver `rå <raa_score>  sjanse for MOT <p_mot>`, ikke `score <p_mot>`.
3. `kaldstart.sh` kopierer også `hack/c1/demo_*.sh` til kopien.
4. `leveranse/kjor.sh:2-4`: kommentaren sier nå real_votes -> fremmed.sh -> agent -> måler v3. N-PX gjelder bare SPOR=npx.
5. `README.md`: kallet er `bash arbeid/hack/c1/leveranse/kjor.sh` (fra landsbymappen). Datakilden står som NBIMs offentlig publiserte stemmer (vd.nbim.no), utlevert som fil av arrangøren. Ny krediteringslinje: hent_npx.py (endret) og baseline.py bygger på startpakken og brukes bare i SPOR=npx.

## Bevis (05.11 kl. 13.37, kald kopi /tmp/c1_kald.NvZLXS, kjørt fra kopiens rot)
`BEHOLD=1 bash arbeid/hack/c1/kaldstart.sh` -> `GRØNN F1_MOT 0.476190 REF 0.476190 AVVIK +0.000000`, 62 s, måler sha 418a937e57.

`bash arbeid/hack/c1/demo_saker_2026.sh /tmp/c1_demo2235` (15,4 s, exit 0), siste linjer:
```
   agent: MOT (mot styret 1)  rå 0.96994  sjanse for MOT 0.5217  til menneske 1 usikker: kalibrert P(MOT) 0.52 i båndet [0.15, 0.85)
agentens egen sjekk, avvik inkl. avstå (sidetall, ikke hovedtallet): SCORE 0.4818
  MOT mot styret: TP 30 FP 38 FN 28  P 0.4412  R 0.5172  F1 0.4762  (58 i fasit)
HOVEDTALL maaler_offisiell_v3.py full/_pred_uten_ruting.csv test --data real --score mot: F1 MOT 0.476190
```
`bash arbeid/hack/c1/demo_mangler_styret.sh /tmp/c1_mangler2235` (9,7 s, exit 0), siste linjer:
```
   agent: FOR (styret lest som FOR, mot styret 0)  rå 0.2623  sjanse for MOT 0.0075
   til menneske: 1  grunn: styrets anbefaling mangler: antatt FOR, sjekk innkallingen; felt avviker fra lagret sak (mgmt_rec); modellen brukte lagret rad
```

## Til speider (#1975)
DEMO_MANUS.md bør si at siste linje nå er HOVEDTALL 0,476, og at skjermen viser «rå 0,912 / sjanse for MOT 0,19». Jeg har ikke rørt manuset, JURY.md, BEGRENSNINGER.md eller kravrespons.md.
