# Case 1: lederen målt uten kjennetegnene som lekker (dommer #1988)

Kode: frosset `arbeid/kandidater/smed2_c1_mot/train_v3.py` og `sec_feats.py`. Kopien `arbeid/oppgave_1988/train_v3_x.py` er identisk, bortsett fra at SEC-grensen leses fra `PVP_DAGER` (standard 20). Grensen er 1,25 × basisrate og 5 seeds, som i lederen. Kjørt fra kald start med fasit via `hack/c1/maaler.py`.
- **full** = lederen slik den er
- **a** = uten `s_float`. Jeg tok også ut de to kjennetegnene som er regnet ut fra float: `g_sbc_vs_float` og `s_lonn_vs_storr` (`--drop s_float,g_sbc_vs_float,s_lonn_vs_storr`). Ellers ville float ha lekket inn bakveien.
- **b** = som a, og i tillegg PvP/10-K e1 < D−100 d (`PVP_DAGER=100`)

| Variant | Val 2025 F1 | Val PR-AUC | Test 2026 F1 | Test PR-AUC | Forsøk (val / test) |
|---|---|---|---|---|---|
| full | 0,4175 | 0,357 | 0,5092 | 0,453 | #1007 / #1006 |
| a | 0,3987 | 0,338 | 0,5095 | 0,495 | #1013 / #1012 |
| b | 0,4026 | 0,334 | 0,4926 | 0,455 | #1015 / #1014 |
| gulv (NBIM stemte MOT før) | 0,361 | | 0,383 | | |

Full gir nøyaktig samme tall som #1006/#1007, så kald start er reprodusert.

Bootstrap med selskap (cusip) som klynge, 2000 trekk, 95 %-intervall på differansen i F1:
- Val: a − full −0,019 [−0,056, 0,018], b − full −0,015 [−0,052, 0,020]
- Test: a − full +0,001 [−0,035, 0,036], b − full −0,016 [−0,054, 0,021], b − a −0,017 [−0,035, 0,004]
- Intervallet for selve F1 er bredt: b på test ligger i [0,42, 0,56], b på val i [0,33, 0,47].

Når lekkasjen er borte, er ingen forskjell større enn støyen. Variant b slår fortsatt gulvet på begge år: +0,04 på val og +0,11 på test.

## Anbefaling: lever variant b kl. 13
**Test-F1 0,49 og val-F1 0,40.** Bare i b er hvert kjennetegn kjent før møtet uten forbehold. Variant a fjerner float, men lar de ~11 radene med svak PvP/10-K-lekkasje stå. Variant b koster ~0,017 på test, og det er innenfor støyen. Vi bør ikke kjøpe 0,017 med et forbehold juryen kan ta oss på.
Kommando: `PVP_DAGER=100 python train_v3_x.py --data <data> --drop s_float,g_sbc_vs_float,s_lonn_vs_storr --ut <fil>`. Det bør også bli ett flagg i smed2s frosne kode før modellfrysen kl. 16.

## Forbehold som står igjen
- Faktoren 1,25 × basisrate: det er fortsatt ikke vist at den ble valgt på val og ikke på test (se #1985). Til juryen bør vi si at grensen er valgt på val, og bare hvis det er sant. Ellers må den velges på nytt på val.
- Frames-API-et gir verdiene fra siste innsending, ikke første publisering. Den effekten er ikke målt.
