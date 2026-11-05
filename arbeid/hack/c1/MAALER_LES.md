# Måleren for Case 1 – v2 (dommer, #1963)
- Hovedtall: F1 (SCORE) og PR-AUC (linja PRAUC) på **avvik fra utledet styre**. MOT-F1 er sekundært.
- Styret utledes av kilde (ISSUER→FOR, SECURITY HOLDER→AGAINST). `ledelsen`/`mgmt_felt_LEKKER` er fasiten og finnes ikke i test_input; måleren nekter hvis de dukker opp.
- Tren på data/train.csv, prediker data/test_input.csv. Fil: id,anbefaling(FOR/MOT/AVSTÅ),konfidens(0-1)[,p_avvik(0-1)]. Konfidens < 0,6 = rutet til menneske.
- Detaljer: state/rapporter/hack_c1_maaler_v2.md (v1: maaler_v1.py, state/rapporter/hack_c1_maaler.md)
