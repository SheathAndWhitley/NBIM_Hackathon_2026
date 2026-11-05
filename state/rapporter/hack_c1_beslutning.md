# Case 1: ordførerens beslutninger kl. 11:05 (gjelder alle)

1. **Hovedtall = avvik fra styret** (`mot_ledelsen`): F1 og PR-AUC på stemmer der fondet går mot styrets anbefaling.
   Her har «følg styret» recall 0, og det er beslutningen agenten avlaster. MOT-F1 rapporteres som sekundærtall.
   Grunn: med utledet styre (ISSUER=FOR, aksjonærforslag=MOT) gir «følg styret» allerede MOT-F1 ca. 0,79-0,84,
   så MOT alene måler nesten bare forslagstype.
2. **Forvalter låst: Vanguard (CIK 36405)** for data og test. Retningslinjene som siteres er Vanguards
   proxy voting policy. NBIM (1374170) er bare en valgfri ekstra test hvis tida tillater det.
3. **`mgmt_felt_LEKKER` / `ledelsen` er fasiten** og brukes aldri som feature, baseline eller i test_input.
   Forsøk målt med feltet er ugyldige.
