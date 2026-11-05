# Case 1: hva koster sanntid? Årsvis kvote mot løpende terskel (smed2, #2883)

Regel skrevet før måling: `arbeid/oppgave_2883/REGEL.md`. Kode: `arbeid/oppgave_2883/sanntid.py`, logg: `kjor.log`. Forsøk #1251.
Samme repo4-filer, samme p_avvik, samme av-regel og samme måler (oppgave_2567/maaler_aar.py --score mot). Lederen gjenskapes nøyaktig: 0,5261.

| variant | sanntid? | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 |
|---|---|---|---|---|---|---|
| #2703 midt+av, **årsvis kvote** (k fra hele teståret) | nei | 0,3556* | 0,5083 | 0,5276 | 0,5424 | **0,5261** |
| S2: midt+av, **løpende terskel** (365 d vindu strengt før møtedato) | ja | 0,3636 | 0,5028 | 0,5276 | 0,5289 | **0,5198** |
| S1 = #2701 av alene (fast grense τ0 fra val T-1, så av) | ja | 0,3736 | 0,5269 | 0,5375 | 0,5246 | **0,5297** |

\* fra c1_natt_referanse.md (dommer2 laget 2022-andel). Min S2-vakt har ingen 2022-andel og bruker råandelen i vinduet, så den er en svak vakt.

## Funn
1. Sanntid koster midt+av 0,0063 i snitt (2024 −0,0055, 2025 0, 2026 −0,0134). Hele løftet i 2026 (+0,030 over frossen) krymper til +0,017. Det meste av 2026-gevinsten kom altså av at året ble sett under ett.
2. Den faktiske lederen i natt-referansen er #2701 «av alene» (0,5297), ikke #2703. Den er allerede sanntid: grensen τ0 er valgt på val-året T-1, og av-regelen bruker bare stemmer fra før teståret, som er strengere enn sanntid. Sanntid koster derfor lederen **0**.
3. Merknad 1 i c1_natt_lekkasje.md gjelder #2703 og alt som går gjennom topk der (#2875). Den gjelder ikke #2701.
4. S2 løfter ikke noe år over S1. Kvoten er ikke verdt å ta med i sanntidsagenten.

## Jurysetning
«Agentens beste regel (fast grense valgt på året før + NBIMs siste stemme på samme sak) bruker bare informasjon fra før møtedatoen og gir F1 0,530 på MOT over 2024-26. En variant som kalibrerte antall flagg på hele teståret, ga 0,526 og falt til 0,520 når den ble gjort sanntid, så vi bruker den ikke.»

Neste steg (forslag): ingen. Alle kandidater som går gjennom #2703-topk bør måles med S2-terskelen eller mot #2701, ikke mot årsvis 0,5261.
