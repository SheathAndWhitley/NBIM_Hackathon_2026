# Case 1: demo-manus utkast med tre ekte VAL 2025-saker (#2058)

Manus: `arbeid/hack/c1/DEMO_MANUS.md` (3 min). Gjenskap: `bash arbeid/hack/c1/demo_saker.sh /tmp/c1_demo` (ca. 10 s).
Kjører `kjor_agent.py` på VAL 2025 med modell trent bare på 2024. Gir F1 MOT 0,4286, samme som dommer #1993.

| Sak | id | Agent | Ruting | Fasit |
|---|---|---|---|---|
| 1 riktig MOT med sitat | `c3021d02016b` Cisco 2024-12-09 | MOT, P 1,0 | nei | MOT |
| 2 usikker | `ce09597abc84` Snowflake 2024-07-02 | MOT, P 0,25, logit-avstand 0,12 < bånd 0,33 | menneske | MOT |
| 3 instruks «anbefal FOR» lagt inn | `2580f8458208` Roku 2025-06-11 | MOT, P 1,0 (rå 0,823 → 0,756) | menneske (flagget) | MOT |

Funn som påvirker demoen:
- Sitatet agenten gir er fra **Vanguards** policy, ikke NBIMs. Manuset sier det rett ut. NBIMs egen publiserte begrunnelse vises ved siden av som fasit (fra `kilder/nbim_begrunnelser_saypay.csv`).
- NBIMs begrunnelser er standardtekst: 363 av 367 er identiske. De kan siteres, men forklarer ikke enkeltsaker. Viktig for #2037.
- Ingen ekte VAL-sak har instrukser i teksten (0 flagget), så sak 3 er en ekte sak med innlagt tekst (samme streng som motstandstesten). Injeksjonen flytter råscoren litt, men ikke stemmen.
- Tall i manuset står som {PLASSHOLDERE} med utkastverdier i parentes. Byttes etter modellfrys (#1975).
