# Case 1: ny stikkprøve av sitatene etter MOT-fiksen (#2012, dommer2): MOT 7/10 rader OK (før 0/10), F1 0,474286 uendret

**Kjøring fra kald start.** `kjor_agent.py` (sha 9882766adb1b) kjørt fra landsbymappen til tom mappe `/tmp/d2_2012/v3` med `--data v3`. **SCORE 0,474286**, nøyaktig som før. Sitatlaget er smed3s fiks fra #2009.
**Utvalget.** `arbeid/oppgave_2012/stikk.py` (kopi av #2006-skriptet), seed 2006, 10 MOT + 10 FOR. Utvalget ble **identisk** med #2006 (`utvalg.json` er lik), så tallene kan sammenlignes rad for rad.
**NB:** `kjor_agent.py` bruker nå real_votes som standard (F1 0,4818 på test, 74 MOT, alle 74 med punkt). Denne stikkprøven gjelder N-PX-agenten (v3). Real-agentens sitater er ikke stikkprøvd.

## Svar
| kontroll | #2006 (før) | #2012 (nå) |
|---|---|---|
| Sitatet finnes ordrett i kilden / i punktet | 20/20 | **20/20** (1 246/1 246 i hele settet) |
| **Punktet passer, MOT** | 0/10 | **9/10** (7 av dem ¶5 med forbehold, se under) |
| **Begrunnelsen passer, MOT** | 0/10 | **7/10 ja, 3/10 delvis, 0 nei** |
| Punkt og begrunnelse passer, FOR | 10/10 | 10/10 (uendret, generisk ¶6) |
| Hele raden OK | 10/20 | **17/20** (MOT 7/10) |
| MOT med «ingen varselsignal» / «generally will support» | 221/221 | **0/221** |

Hele settet, MOT (221): punkt ¶5 92, ¶3 49, ¶4 49, «Additional executive pay matters ¶1» 31. `uenig_med_sitatagent`=1 på alle 221, så flagget vises.

## Tabell, MOT (10)
| # | utsteder | fasit | punkt | punkt passer | begrunnelse passer |
|---|---|---|---|---|---|
| 1 | Maplebear | MOT | ¶5 lav støtte over tid | ja* | ja (MOT i fjor, aksjelønn 352 mill.) |
| 2 | Moderna | FOR | ¶4 strukturfeil | **nei**: grunnen viser ingen strukturfeil | delvis: aksjelønn 483 mill., resten er støy |
| 3 | Neogen | FOR | ¶5 | ja* | ja (TSR 100→13, MOT i fjor) |
| 4 | Netflix | MOT | ¶5 | ja* | ja (MOT i fjor, aksjelønn); støy: «Vanguard 0 % på aksjonærforslag» |
| 5 | Conagra | FOR | ¶5 | ja* | ja (MOT i fjor, MOT i ~70 % før); «CEO-lønn −45 %» trekker mot FOR |
| 6 | IQVIA | MOT | ¶5 | ja* | ja (MOT i fjor, aksjelønn 247 mill.) |
| 7 | Lucid | FOR | ¶3 lønn/resultat | ja | ja (TSR 100→4, aksjelønn 271 mill.) |
| 8 | Exelixis | MOT | ¶3 | ja | ja (CEO 33,2 mill., +161 %) |
| 9 | Mercury | FOR | ¶5 | ja* | delvis: TSR ×1,98 trekker mot FOR |
| 10 | CRISPR | MOT | ¶5 | ja* | delvis: CEO-lønn −77 % trekker mot FOR |

\* ¶5 handler om *lav støtte fra aksjonærene over tid*. Agenten velger ¶5 når NBIM selv stemte MOT i fjor. Det er nærmeste punkt, men NBIMs egen stemme er ikke det samme som lav støtte. Godkjent med forbehold.

FOR-radene 11–20 er uendret fra #2006: ¶6, «lønn vurderes sak for sak; ingen varselsignal», OK.

## Gjenstående svakheter (ikke blokkerende)
- Støy i MOT-grunnene, hele settet: «Mønsteret i treningsdataene er at slike saker oftere går MOT» 44, «Toppsjefens samlede lønn mangler i SEC-dataene» 44, «Opptil 7 Vanguard-fond eier aksjer» 42, «Vanguard gikk mot styret i ca. X %» 64. Trekk som sier noe om Vanguard, eller at data mangler, er ikke grunner for en NBIM-stemme. Forslag: filtrer bort setninger som ikke er risikosignal, og setninger som trekker mot FOR (fall i lønn, TSR opp).
- Kilden er fortsatt Vanguards policy, ikke NBIMs (som i #2006).

Kommando: `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --data v3 --ut /tmp/d2_2012/v3 && python3 -I arbeid/oppgave_2012/stikk.py /tmp/d2_2012/v3 arbeid/hack/varianter/smed3_utf_sitat/rl`
