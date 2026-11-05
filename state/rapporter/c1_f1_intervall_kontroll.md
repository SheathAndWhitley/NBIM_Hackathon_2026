# Case 1: kontroll av F1-intervallet i pakka (#2189)

Hovedtall F1 MOT 47,6 % (TP 30, FP 38, FN 28). Mitt intervall (#2186): 36,2–57,7 %. Krav: innen 2 pp.

| Fil | Før | Avstand til mitt | Status |
|---|---|---|---|
| EN_SIDE.md (tabell + svakhet 1) | [0,36; 0,59], klyngebootstrap per selskap | 0,2 / 1,3 pp | OK |
| JURYSVAR.md (hovedtall + spm. om sikkerhet) | [0,36; 0,59], klyngebootstrap per selskap | 0,2 / 1,3 pp | OK |
| TREFFSIKKERHET.md | **manglet** (#2185 ga bare P og R) | – | Rettet |

Rettet: la inn rad «F1 MOT (hovedtall) 47,6 %, 36,8–58,1 %» øverst i intervalltabellen og KI i punktlista.
Tallet er regnet med smed3s egen bootstrap (`saker()` fra treffsikkerhet_ki.py, frø 2185, 2000 trekk over saker):
`arbeid/oppgave_2189/f1_ki.py` → 1539 saker, F1 0,4762, 36,8–58,1 %. Avstand til mitt: 0,6 / 0,4 pp.
Klyngetallet (36–59 %) står i samme rad, så filene ikke ser ut til å motsi hverandre.

Ingen modell endret. c1_tallvakt: 14 filer, 139 påstander, 0 avviker, OK.
