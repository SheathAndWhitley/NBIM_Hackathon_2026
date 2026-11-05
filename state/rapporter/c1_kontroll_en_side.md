# Case 1: kontroll av speiderens endringer i EN_SIDE og BESLUTNINGSSTOTTE (#2201)

Dommer, 05.11 kl. 13.30. Sjekket mot filene på disk kl. 13.18 (EN_SIDE.md) og 13.16 (BESLUTNINGSSTOTTE.md). `arbeid/` er gitignorert, så det finnes ingen diff. Jeg sjekket påstandene i speiderens rapport `c1_en_side_jurylest.md` (#2190) og det som står i filene nå. **#2197 (kutte til én side) er fortsatt tatt av speider.** Kuttene derfra er ikke med her og må sjekkes igjen når #2197 er lukket.

Gjenskapt selv:
- `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/hack/levering/kjor_agent_real_pred_maaler.csv test --data real --score mot` gir TP 30, FP 38, FN 28, F1 0,4762.
- `python3 -I arbeid/hack/c1/menneske_tabell.py arbeid/oppgave_2132/agent.csv` gir hele menneske-tabellen, likt med BESLUTNINGSSTOTTE tegn for tegn.
- `c1_tallvakt.py` gir OK (14 filer, 139 påstander, 0 avvik).

| # | Påstand (fil) | Kilde | Dom |
|---|---|---|---|
| 1 | 56 av 58 MOT er mot styrets egne forslag, og 29 av 30 treff er der (EN_SIDE, BESL.) | `c1_forslagsstiller.txt`: Management 56/29, Shareholder 2/1, sum 58/30 | OK |
| 2 | «Aksjonærforslag = MOT» kan finne høyst 2 av 58 | samme (Shareholder 2) | OK |
| 3 | 183 av 1539 (11,9 %) til menneske, 188 av 1578 inn | `kjor_agent_real_test2026.txt` l.2 og målerlinje «183 til menneske» | OK |
| 4 | 32 av 58 MOT blant de rutede, alle 38 falske flagg i sonen | menneske_tabell.py (står ikke i kjor_agent-loggen) | OK (se merknad a) |
| 5 | 41 av 58, F1 0,828 som øvre grense, 0,269 som gulv | menneske_tabell.py, standardraden | OK |
| 6 | 17 av 58 ser ingen (P(MOT) < 0,15) | FN 17 i standardraden | OK, står nå én gang i EN_SIDE |
| 7 | Lesetid ca. 62 t, merket som antatt | 183×20 + 9×10 = 3750 min = 62,5 t; 9 flagg utenfor sonen: 30 TP − 21 TP i sonen (32 MOT i sonen − 11 lagt til av menneske) | OK |
| 8 | 12,5 av 100 lest (11,9 + 0,6) (BESL.) | (183+9)/1539 = 12,48 % | OK |
| 9 | Grensen p ≥ 0,919 og båndet [0,15; 0,85) er låst på val 2025 | loggen l.3: rå grense 0,91885, bånd [0,15, 0,85) | OK |
| 10 | Accuracy 95,7 % mot 96,2 % for følg styret | (30+1443)/1539 = 95,7 %; 1481/1539 = 96,2 % | OK |
| 11 | Avvik-sidetall 0,4818 (66 saker) | loggen: avvik TP 33 FP 38 FN 33, F1 0,4818 | OK |
| 12 | Beste enkle regel 0,365 [0,25; 0,49], agenten +0,11 [0,01; 0,22] (#2134) | `c1_enkle_regler_og_hist1.md` l.13/36 | OK |
| 13 | Uten historikk fra samme sesong: 0,415 [0,30; 0,53] (#2134) | samme, l.14 | OK |
| 14 | Sitat: 15 av 20 var regelen som avgjør (#2115) (erstatter løftet om #2012) | `c1_sitat_verifisert.md`: 20/20 ordrett, 15/20 passer, 4 delvis, 1 feil | OK |
| 15 | Setningen om N-PX er fjernet fra BESL. | grep «N-PX» i EN_SIDE og BESL.: 0 treff; «#2012»: 0 treff | OK |
| 16 | KI [0,36; 0,59] | tallvakt OK, #2087/#2095 | OK |
| 17 | Flyttingen av `KJORING_til_menneske_10/15.txt` (og `kjor_agent_holdout2026.txt`) til `levering/arkiv/` brekker ingen henvisning | grep i `levering/` (md, py, sh, demo/), `c1/*.py|*.sh`, `verktoy/*.py`, kaldstart/fremmed/sluttkontroll: ingen viser til dem. Eneste lenke, `kjor_agent_real_test2026_LES.md:17`, peker riktig til `arkiv/`. `fremmed.sh` og `sluttkontroll.sh` bruker `ut/KJORING.txt` fra egen kjøring, ikke de flyttede filene. Bare interne rapporter i state/ og `c1/arkiv/` nevner de gamle navnene. | OK |

**Avvik: 0.**

Merknader (ikke feil):
- a) Speiderens rapport sier at kilden til menneske-tabellen i EN_SIDE er `kjor_agent_real_test2026.txt`. Bare 183/188 står der. Tallene 32, 41, 0,828, 0,269 og 17 kommer fra `menneske_tabell.py`. EN_SIDE viser til begge kildene, så det trengs ingen retting.
- b) De 71 avvik-flaggene i loggen mot 68 MOT-flagg (TP 30 + FP 38) stemmer med hverandre. Måler v3 teller en MOT-prediksjon bare der styret ikke selv sier MOT (`maaler_offisiell_v3.py:83`).
- c) Gammelt, ikke fra #2190: `kjor_agent_real_test2026.txt` har fortsatt v2-linjen «streng MOT: TP 0» og etiketten «konfidens < 0.6». Det kan forvirre en jury som åpner loggen (sagt før i `c1_tall_likt.md`). Bør lages på nytt med v3 ved frysen.
- d) EN_SIDE har 659 ord og er fortsatt over én side. Det gjøres i #2197 og må sjekkes igjen etterpå.
