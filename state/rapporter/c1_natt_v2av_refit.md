# Case 1 natt #2891: månedlig re-trening oppå v2+av gir BYTT mot frossen, men ingen gevinst over v2+av (smed)

Arkitektens vinkel A (rr.py `--refit 1`) er stablet på lederen v2+av (#2887). Modellen trenes på nytt hver måned på alle møter før månedens start. C og grensen t0 velges på vanlig val, ikke på re-trent val. k er låst til 32/64/48, og av-regelen er uendret.
Regelen står i `arbeid/c1_natt/v2refit/svar/REGEL.md`, skrevet 19:49:05, før svarfilene. Val-tallene er identiske med v2 (2023: C=3, grense 0,9224, F1 0,3853), og av vant val alle tre år som før.
Kandidaten er målt med natt-måleren (`mal_kandidat.sh`) og står som forsøk #1264 på tavla.

| år | frossen | v2+av (#2887) | v2+av+refit | diff mot frossen | diff mot v2+av |
|---|---|---|---|---|---|
| 2023 (vakt) | 0,3535 | 0,3723 | 0,3579 | +0,004 | −0,014 |
| 2024 | 0,5057 | 0,5731 | 0,5795 | +0,074 | +0,006 |
| 2025 | 0,5309 | 0,5667 | 0,5525 | +0,022 | −0,014 |
| 2026 | 0,5120 | 0,5391 | 0,5536 | +0,042 | +0,015 |
| snitt 24-26 | 0,5162 | 0,5596 | **0,5619** | **+0,0457** → BYTT | **+0,0023** |

**Konklusjon: ærlig nei.** Bytteregelen gir BYTT mot frossen, men nesten hele gevinsten kommer fra v2+av, som allerede står. Re-treningen legger til +0,002 i snitt, og vaktåret 2023 faller 0,014 mot v2+av. Det er støy, ikke signal. Jeg anbefaler å beholde v2+av som leder, med enklere kode og én trening per år.

Robusthet (`k_spredning.py`, ikke brukt til valg) viser refit mot v2+av for alle ni kombinasjoner av k og år:
2024: k32 +0,006, k48 +0,008, k64 −0,023 · 2025: k32 −0,009, k48 0,000, k64 −0,014 · 2026: k32 +0,005, k48 +0,014, k64 −0,010.
Fire celler går opp, fire går ned og én står likt. Snittet er −0,0025. Effekten av re-treningen er altså null, med en spredning på ±0,015. Det stemmer med arkitektens tall for vinkel A på frossen (+0,007, innenfor støyen).

Forbehold: med samme k-lås som #2887 ligger refit-varianten 0,002 over. Uten låsen ville den tapt like ofte. Står 02-dommen mellom v2+av og denne, bør v2+av velges.

Filer: `arbeid/c1_natt/v2refit/` (v2refit_rull.py = v2_rull.py + refit_pred, v2refit.py, k_spredning.py, svar/ med REGEL.md, DOM.md og 4 csv-er, spredning/).
