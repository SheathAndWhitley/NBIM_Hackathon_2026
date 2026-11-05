# Case 1: tre demosaker fra den frosne agenten (#2260)

- Kjørt frossen #2044 miks h2 på test 2026 (standard, 5,7 s). `pred_maaler.csv` sha256 `b113b545…3653` = frossen fil. Ingen modellendring.
- Valg uten håndplukking (`arbeid/oppgave_2260/velg.py`): første sak i `agent.csv` av hver type; treff og bom blant saker maskinen avgjorde selv.
  - Treff, linje 276: Mobimo, «Transact Other Business», P(MOT) 1,0, sitat GVG 5.2 (NBIMs egen 2021-begrunnelse, ordrett lik fasit 2026).
  - Bom, linje 89: LOTTE Chemical, vedtektsendring, P(MOT) 0,09, agent FOR uten menneske, NBIM stemte MOT (falsk negativ).
  - Til menneske, linje 15: Kura Sushi, styrevalg, P(MOT) 0,58 i båndet, forslag MOT med sitat GVG 1.1; NBIM stemte MOT.
- Ærlig: første bom i fila (linje 39, Lundbeck, agent MOT, P 0,52) gikk til menneske, så første bom avgjort av maskinen er linje 89. Treffsakens retningslinjesitat (5.2.1, årsrapport) passer dårlig; begrunnelsessitatet bærer.
- Leveranse med ordrett utskrift: `arbeid/hack/CASE/demo_saker.md`.
- Kontroll: radene og hele agent.csv er identiske med kald kopi /tmp/fremmed (13:14).
- Funn: alle 38 FP gikk til menneske; av 28 FN gikk 11 til menneske og 17 ble FOR fra maskinen alene (som LOTTE). Stille feil går bare i retning «følg styret».
