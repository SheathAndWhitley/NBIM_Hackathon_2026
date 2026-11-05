# Case 1: NESTE_VERSJON.md committet, ren HEAD for jury-zipen (#2504, smed2, 05.11 ca. 16.35)

**Commit 8ed8ac3**: `arbeid/hack/c1/leveranse/NESTE_VERSJON.md` (+52/−4) og bare NESTE_VERSJON-linja i `frys_fasit_1600.sha256`.

## Hva diffen var
- Staget (fra #2480/#2487-sporet): tittel «fire tiltak» og nytt **Tiltak 4: presedens først** (repoets regel 0,515, hybrid 0,545 +0,069 [+0,007; +0,133], PR-AUC 0,525/0,318/0,413, 68 flagg P 0,441 mot 52 P 0,577), og en setning i «Rekkefølge».
- Ikke staget (#2498 m.fl.): tre punkter: personnøkkel som trekk (0,525, +0,049 [+0,016; +0,090], 14 endrede saker), personnøkkel rullende 2024/2025/2026 (0,418/0,455, 0,516/0,514, +0,049), og hybrid+rangering V2 (0,516, P 0,485, R 0,552, 32/34/26, FP 38 → 34). Alt merket «ikke hovedtall».

## Sjekk
- Tallvakt (`c1_tallvakt.py --rot .`): F1 0,4762 TP 30 FP 38 FN 28, 18 filer, 169 påstander, **0 avvik**.
- Hvert nytt tall slått opp for hånd i kildene: `state/rapporter/c1_repotrekk_neste_versjon.md:12-21`, `kilder/c1_personnokkel_rullende.md:15-20`, `state/rapporter/c1_hybrid_pluss_rangering.md:16-29`. Alle stemmer (P/R for V2 regnet fra 32/34/26).
- Modellfrysvakt (tavla): 17 filer uendret siden frys 16:00. Ingen frosne filer eller levering/-tekster rørt.
- `frys_diff.sh --kilde` etter commit: NESTE_VERSJON ikke lenger avvik. Igjen: 2 avvik som hører til andres åpne arbeid, se under.

## Ikke mitt, står ukommittert (rørt ikke)
- `kilder/LESMEG.md` (+2) og ny `kilder/c1_personnokkel_rullende.png`: dommer, #2508 (figuren).
- `JURY_SPORSMAL.md` (1 linje): smed4, #2505 (personnøkkel i jurytekstene).
Den som lukker dem må committe og oppdatere fasit-linjene sine, ellers kommer de ukommittert med i zipen igjen.
- Merk: NESTE_VERSJON peker på figuren som `arbeid/oppgave_2497/c1_personnokkel_rullende.png`, en sti som ikke er i zipen. Når png-en er i `kilder/`, bør pekeren bli `kilder/c1_personnokkel_rullende.png` (for #2508/#2509).
