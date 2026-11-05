# Case 1: demo-eksempel der saken mangler styrets anbefaling (#2157)

- Kommando: `bash arbeid/hack/c1/demo_mangler_styret.sh` (ca. 10 s, kald start, modellen urørt).
- Samme ekte 2026-sak som sak 2 i demoen (Arbonia AG, `2041102|2`), kjørt med og uten `mgmt_rec`/`mgmt_rec_raw`.
- Med anbefaling: FOR, score 0,0075, ikke til menneske.
- Uten: FOR (antatt), samme score, **til menneske** med grunn «styrets anbefaling mangler: antatt FOR,
  sjekk innkallingen; felt avviker fra lagret sak (mgmt_rec); modellen brukte lagret rad».
- Lagt inn som «Sak 7» under «Menneske i loopen» i `arbeid/hack/c1/DEMO_MANUS.md`, med utskrift og ærlig merknad.
- Obs til manusansvarlig: manusets {S2} (0,262) er fra 12.20 og en annen skala; agenten gir nå 0,0075 for
  samme sak (kalibrert P(MOT) etter #2128). Fylles uansett etter frysen.
