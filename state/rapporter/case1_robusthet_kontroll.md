# Case 1: kontroll av robusthetsfiksen (#2000), dommer2 #2028

Testet kode: `arbeid/hack/levering/kjor_agent.py` sha256[:12] 8c86665a4f11 (11:45, inkluderer smeds `--til-menneske` fra #2029; standard 10 %). Kopi: `arbeid/oppgave_2028/kjor_agent_testet.py`.

| Punkt | Svar | Detaljer |
|---|---|---|
| (1) robust.py 12/12 | **ja** | `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2000/robust.py` fra tom /tmp/c1_robust: 12/12 ok, ingen krasj (55 s). |
| (2a) SCORE holdout 2026 uendret | **ja** | Ny tom utmappe /tmp/c1_kontroll_2028: SCORE 0,474286, PR-AUC 0,454970, tp 83 fp 138 fn 46, rutet 119 (9,6 %). |
| (2b) pred_maaler.csv uendret | **ja** | Diff mot `kjor_agent_pred_maaler.csv` (kopi `arbeid/oppgave_2028/ref_pred_maaler.csv`): 0 av 1246 rader endret, samme id-er, 119 med konfidens < 0,6 i begge. |
| (2c) ingen vanlig sak med nytt svar eller ny ruting | **ja** | agent.csv mot kjøring fra før fiksen (/tmp/c1_kald, 11:36): 0 saker endret i anbefaling, p_mot, til_menneske, rutingsgrunn, punkt, sitat. |

Antall saker som endret seg: **0** i svar/ruting/sitat. 109 saker har fått lagt til «| obs: ingen tidligere stemmer for selskapet» i `sitat_grunn` (bare et varsel som det står i #2000-rapporten; teksten før er uendret).

Merk: referansen før fiksen er en /tmp-kjøring, ikke en lagret fil; `arbeid/` er git-ignorert, så gammel kode finnes ikke i git.
