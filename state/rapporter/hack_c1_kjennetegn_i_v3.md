# Case 1 (#1984): kjennetegn fra #1958 i smed2s lgbm v3 gir et lite løft på val 2025 (+0,01 F1), og det kommer fra fallskjerm

**Én linje:** Kjennetegnene hjelper lite. Med #1982-regelen (gulv ELLER topp 4 %) gir de F1 0,439 mot 0,427 uten (#1010 mot #1009, måler 5707495ef8, VAL 2025, n 1506, 136 MOT). Nesten hele løftet kommer fra `undertype=fallskjerm` (0,438, #1011). Det er det eneste tillegget der intervallet ligger over null.

| variant (VAL 2025, regel #1982) | F1 | PR-AUC | diff mot uten, paret bootstrap 1000 | 5 frø |
|---|---|---|---|---|
| uten (frosset v3, 19c3e29) | 0,427 | 0,335 | – | 0,430 |
| med alle 5 kjennetegn | 0,439 | 0,303 | +0,012 [−0,011; +0,037] | 0,437 |
| med, uten k_fond_n | 0,433 | 0,334 | +0,007 [−0,011; +0,023] | – |
| bare fallskjerm | 0,438 | 0,334 | **+0,011 [+0,002; +0,021]** | 0,437 |

- "Uten" gjenskaper dommerens kalde val-kjøring byte for byte (modell alene 0,3758). Kopien er altså riktig. Arkitektens 0,435 for samme regel kommer fra en annen prediksjonsfil.
- Fondsprofilen er svak på data der NBIM er eneste forvalter og alle forslag er say-on-pay. `k_fond_n` blir da bare en klokke: på val er den konstant og høyere enn noen train-verdi. Den trekker PR-AUC ned (0,335 → 0,303) og gir en isotonisk terskel på 1,0 (likeverdier). **Den bør ikke brukes.** `sel_*`/`seltype_*` gjentar NBIM-historikken modellen alt har.
- Med modellen alene (smed2s interne terskel) blir alle kjennetegn verre: 0,376 → 0,307. Det er terskelflytt, ikke signal. Det støtter rangregelen fra #1982.
- **Anbefaling før frys:** legg til bare fallskjerm-flagget (lite, men stabilt over frø og bootstrap). Ikke ta inn fondsprofilen. Test 2026 er ikke kjørt her.
- Kode: `arbeid/kandidater/smed_v3_kjennetegn/` (`train_v3.py --kjennetegn [--kj-uten ...]`, `kjor.sh`). smed2s kode er ikke rørt.
