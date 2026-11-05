# MOT-vakt på forsøkstavla (#2049, ordre #231)

**Hva:** Når et forsøk måles (`tavle.py forsok --sti`, bakgrunn og automåling), leser tavla TP/FP/FN
på avvik fra styret fra målerens utskrift (både `maaler_offisiell.py` og `maaler.py` v2).
Predikerte MOT = TP+FP, fasit MOT = TP+FN. Notatet får `[MOT pred/fasit = x% av fasit]`.
Under 25 % av fasit, eller TP 0 (F1-MOT 0): `!! følger styret`, og statuslista viser `!!MOT-ANDEL`.
CLI skriver linja rett etter tallet. Målere uten TP/FP/FN gir ingen merke (ikke Case 1).

**Akseptsjekk** (kopi av tavla, oppgave #2034s måler, real val, `arbeid/oppgave_2049/test_mot_vakt.py`):

| forsøk | F1 avvik | MOT-merke | flagget |
|---|---|---|---|
| følg styret (`real_val_folg_styret.csv`) | 0,0000 | 0/103 = 0 %, F1-MOT 0 | ja (riktig) |
| typerate 0,15 (avviksrate per forslagstype+kilde fra train) | 0,0672 | 135/103 = 131 % | nei (riktig) |

KP: forventet følg styret 0/103 og F1 0 (dommer2s baseline, `maaler_offisiell.py baseline`), fikk 0/103 og 0,0000.

**Grenser:** Bare nye målinger får merket; eldre forsøk (f.eks. dommer2s følg-styret-baseline) må
måles på nytt for å flagges. Vakta sier ingenting om kvalitet: typerate har 131 % MOT-andel, men
F1 bare 0,067. Flagget er gulvet, ikke målet.
