# Case 1 (#2193): terskelen er valgt på val, ikke på test

- Ny tabell i `arbeid/hack/levering/TREFFSIKKERHET.md` (seksjonen «Terskelen er valgt på val 2025»). Den viser P, R og F1 på MOT mot styret for 7 terskler, på val 2025 og test 2026.
- Skriptet er `arbeid/hack/c1/terskel_val_test.py`. Det kjører modellen uendret via `c1_real.kjor_modell`.
- Valgt terskel 0,9188 har høyest val-F1 (0,520). På test gir den 0,476 (TP 30 FP 38), det samme som måleren.
- Best på test er 0,95 med 0,532. Den er ikke valgt. Forskjellen er 3–4 TP og ligger innenfor støyen.
- Terskelen velges i `oppgave_2044/train.py:100-108`, på avvik med AVSTÅ. Tabellen viser hovedmålet MOT mot styret.
- c1_tallvakt: OK, 139 påstander stemmer og 0 avviker. Modell og terskel er ikke endret.
