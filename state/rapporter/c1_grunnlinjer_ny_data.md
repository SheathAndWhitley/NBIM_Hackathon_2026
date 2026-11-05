# Case 1: grunnlinjene målt på nytt på den nye dataen (#2222, smed2)

Data: `state/opplastet/20261105_114241_real_votes.csv` (sha256 71ba5135…e525e6, 13 757 rader, datavakta i v3 godkjente den).
Vindu: test = år 2026, 1539 vurderte rader, 66 avvik fra styret, 58 MOT mot styret.
Måler: `arbeid/hack/c1/maaler_offisiell_v3.py <fil> test --data real --score mot`.
Accuracy regnet som dashbordet (#2214): (n − FP − FN) / n fra avvik-linja.

| Modell | Accuracy | P (MOT) | R (MOT) | F1 MOT (v3 --score mot) | Avvik-F1 (tavla, v2) | Tavla-forsøk |
|---|---|---|---|---|---|---|
| Følg styret | 0,9571 | 0 | 0 (0/58) | **0,0000** | 0,0000 | #1135 |
| Alltid MOT for aksjonærforslag (gulv) | 0,9578 | 0,667 | 0,034 (2/58) | **0,0656** | 0,0580 | #1136 |
| Frossen #2044 miks h2 | 0,9539 | 0,441 | 0,517 (30/58) | **0,4762** | 0,4818 | #1137 |

TP/FP/FN, MOT mot styret: følg styret 0/0/58, gulv 2/1/56, miks h2 30/38/28.
Accuracy-forskjellen er bare 0,4 prosentpoeng mellom alle tre. Det er derfor accuracy ikke kan være hovedtallet.

## Sammenlignet med dashbordet
- **Følg-styret-accuracy 0,9571** er lik dashbordets `acc_styret` (0,95712).
- **Tavla-tallene er avvik-F1, ikke F1 på MOT.** Rundens måler (#2034, sha 9d81a418dd) er `maaler_offisiell_v2.py ... test --data real` uten `--score mot`.
  Den teller AVSTÅ og andre avvik også: 66 positive mot 58. Derfor viser tavla 0,0580 og 0,4818 der v3 MOT viser 0,0656 og 0,4762.
  Avvik-linja i v3 gir nøyaktig de samme tallene som v2, så måleren og dataene stemmer. Forskjellen er bare definisjonen.
- Frossen miks h2: v3 MOT 0,476190 er lik det frosne hovedtallet (0,47619, #2103 og #2225). Ny data endret altså ikke tallet.
- **Dashbordets «beste» er #1033 (t4e, 0,5294 avvik-F1, acc 0,9584).** Det er ikke den frosne modellen. Hovedtallet i jurypapirene skal fortsatt være 0,476 (miks h2, F1 MOT).
  Dommeren/ordføreren bør avgjøre om dashbordet skal vise frossen modell eller måle med `--score mot`.

## Funn: rad,p-fila til den frosne modellen virker ikke på ny data
`arbeid/oppgave_2044/pred_miks_h2.csv` (formatet rad,p) er UGYLDIG på den nye fila: 39 id mangler, fordi radnumrene peker inn i den gamle datafila.
Bruk id-fila `arbeid/oppgave_2103/full_test.csv` (kopi i `arbeid/oppgave_2222/miks_h2_test.csv`). Den gir 0,476190.
c1_frys.py tar sha av begge. Ingen bør måle pred_miks_h2.csv mot ny data.

## Kjør på nytt
```
cd arbeid/oppgave_2222 && python3 -I lag_grunnlinjer.py
for f in folg_styret aksj_mot miks_h2; do python3 -I ../hack/c1/maaler_offisiell_v3.py ${f}_test.csv test --data real --score mot; done
python3 -I ../hack/c1/maaler_offisiell_v3.py baseline test --data real --score mot   # samme tall for grunnlinjene
```
Tavla avviste forsøk under `--oppgave 2222`: måler 8733327407 er endret på disk. De ligger derfor under rundens måler (#2034).
