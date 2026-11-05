# Case 1: svar på «er agenten 97 % treffsikker?» (#2210, ordre #241)

Nei, ikke samlet. Målt på test 2026 (1539 saker med fasit, måler v3, TP 30 FP 38 FN 28):
- Accuracy 95,7 % (1473/1539). Følg styret 96,2 % (1481/1539).
- Riktig på FOR-saker 97,4 % (1443/1481). Det er kilden til «97 %».
- Hovedtall: F1 0,476 på MOT. Finner 30 av 58 MOT-stemmer, 44 % presisjon.

Lagt inn:
- `arbeid/hack/levering/JURY_SPORSMAL.md`: nytt S0 øverst med svar og forklaring i vanlige ord.
- `arbeid/hack/c1/DEMO_MANUS.md`: én replikk i 0:00–0:40.

Kontroll: `c1_tallvakt.py` 0 avvik (14 filer, 144 påstander), og 0 avvik når de to filene sjekkes eksplisitt.
