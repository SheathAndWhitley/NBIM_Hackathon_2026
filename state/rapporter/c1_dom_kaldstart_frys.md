# Case 1: dom over kaldstarten av den frosne pakka (#2473, dommer2, 05.11 kl. 16:08)

**GODKJENT.** Smed3s kaldstart (#2285) er reprodusert av meg fra en ny tom tmp-mappe: F1 MOT 0.476190, prediksjonene bit-like de frosne, og frys_diff er LIK mot fasiten for kildefilene.

## 1. Kaldstart, kjørt selv
```
BEHOLD=1 bash arbeid/hack/c1/kaldstart.sh        # logg: arbeid/oppgave_2473/kaldstart_dommer2.log
EXIT 0
FRYSVAKT GRØNN: 17 filer like som ved frys 2026-11-05T16:00:01
  -- _pred_uten_ruting.csv   MOT mot styret: TP 30 FP 38 FN 28  P 0.4412  R 0.5172  F1 0.4762  (58 i fasit)   SCORE 0.476190
  -- pred_maaler.csv         MOT mot styret: TP 30 FP 38 FN 28  P 0.4412  R 0.5172  F1 0.4762  (58 i fasit)   SCORE 0.476190
  måler sha256[:10] 418a937e57
GRØNN F1_MOT 0.476190 REF 0.476190 AVVIK +0.000000 (grense 0.005) tid 64s
```
Samme tall som smed3 (TP 30 FP 38 FN 28, 0.476190, 91 s hos smed3, 64 s hos meg).

Kald utdata mot de frosne prediksjonsfilene (sha256[:12]):
```
22ac6717e128  /tmp/c1_kald.dS5deg/ut/_pred_uten_ruting.csv
22ac6717e128  arbeid/hack/levering/kjor_agent_real_maskin_alene.csv   bit-lik
b113b545dd86  /tmp/c1_kald.dS5deg/ut/pred_maaler.csv
b113b545dd86  arbeid/hack/levering/kjor_agent_real_pred_maaler.csv    bit-lik
```

## 2. frys_diff mot fasiten
```
sh arbeid/hack/levering/frys_diff.sh --kilde
fasit: arbeid/hack/levering/frys_fasit_1600.sha256 (114 filer)   sammenlignet: --kilde (114 filer)
FRYS LIK: 0 avvik
```
Frysvakta (`python3 -I arbeid/verktoy/c1_frys.py sjekk`): GRØNN, 17 av 17 filer like som ved frys 16:00:01.

## 3. Merknader (ikke avvik i denne dommen)
- Mot den siste bygde jury-zipen (/tmp/d2462_jury.zip, kl. 16:00) gir frys_diff 3 avvik: BORTE speider_2399_recall_budsjett.md (legges inn nå, #2469), ENDRET DEMO_MANUS.md og NESTE_VERSJON.md (tekst, #1975/#2457). Ingen av dem rører modell, prediksjoner, måler eller agent. Zipen må bygges på nytt før #2476 dømmer den; da skal frys_diff mot zipen gi LIK.
- #2474 (AVVIK i #2247) sammenligner med en eldre referanse fra #2243 der 7 av 9 «ulike» filer mangler i referansen. Frysen kl. 16:00:01 er autoriteten, og den er uendret. Det dømmes i #2474, ikke her.
- TALLSJEKK-varsel fra kaldstart.sh: ett tall «16,23» i NESTE_VERSJON.md:58 ikke funnet i noen måling. Gjelder jurytekst, hører til #2255/#2470.

Tmp-kopien min er slettet. Smed3s kopi står i /tmp/c1_kald.UdVwk6.
