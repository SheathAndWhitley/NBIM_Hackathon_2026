# Case 1: tre ekte saker fra test 2026, ett treff, én falsk alarm, én bom (#2343, smed2)

Agent: frossen #2044 (kjor_agent.py, maskin alene), kjørt på nytt 05.11 kl. 14.50 inn i `arbeid/oppgave_2343/ut/`.
Prediksjonene er identiske med `levering/kjor_agent_real_maskin_alene.csv`, og v3 `--score mot` gir 0,476190
(TP 30, FP 38, FN 28). Fasit er NBIMs faktiske stemme i real_votes 2026, lest *etter* kjøringen. Ingen agentfiler er endret.

| | (1) Treff | (2) Falsk alarm | (3) Oversett MOT |
|---|---|---|---|
| Selskap | Grupo Pochteca SAB de CV (Mexico), 30.04.2026 | Dell Technologies (USA), 25.06.2026 | Dell Technologies (USA), 25.06.2026, samme møte |
| Sak | Elect and/or Ratify Directors … and Audit Committee (sak 4) | Elect Director Michael S. Dell (sak 1) | Change State of Incorporation from Delaware to Texas (sak 11) |
| Styret / agenten / NBIM | FOR / **MOT** / MOT | FOR / **MOT** / FOR | FOR / FOR / **MOT** |
| P(MOT), kalibrert | 1,00 (rå 0,993) | 0,52 (rå 0,956) | 0,014 (rå 0,406) |
| Retningslinje sitert | NBIM 3.1.1 (GVG 3.1): «The company should have a robust nomination and election process …» | NBIM 1.2.1 (GVG 1.2): «Board decisions that are particularly vulnerable to conflicts of interest should have additional safeguards.» | NBIM 0.0.3: «Our starting point … is to support the board.» (følger styret) |
| Til menneske? | Nei, sikker nok til å gå rett ut | **Ja**, P(MOT) i båndet [0,15; 0,85) | Nei, under båndet |

**Hvorfor:**
1. *Treff.* NBIM har stemt MOT styrevalget i Pochteca hvert år i data (2019–2023, 2025), og agenten fant både mønsteret og NBIMs egen begrunnelse fra 2022 (GVG 3.1), som er samme seksjon NBIM brukte i 2026.
2. *Falsk alarm.* NBIM stemte MOT Michael Dell 2019–2022, men FOR 2023–2026. Agenten veide den gamle historikken og 2020-begrunnelsen tungt. Usikkerheten ble likevel fanget: saken gikk til et menneske, som ser de tre siste FOR-stemmene i oppslaget.
3. *Bom.* Eneste tidligere Delaware→Texas-sak i data er Tesla 2024, og der stemte NBIM **FOR**. Agenten hadde ingenting å lære MOT fra. NBIM begrunnet 2026-stemmen med GVG 4.3 (aksjonærenes rett til å stemme over grunnleggende endringer). Texas Capital Bancshares fikk samme sak og samme bom.

**Til demo/jury (alle fra samme kjøring):**
- Alle 38 falske alarmer gikk til menneske. Ingen feil-MOT gikk rett ut. Av 30 treff gikk 9 rett ut og 21 til menneske.
- 11 av 28 bommer ble fanget av rutingen. De 17 andre fikk P(MOT) under 0,15 og gikk ut som «følg styret». Det er den svake siden: nye sakstyper uten historikk (eks. 3) blir ikke sett.
- Dell-møtet viser begge feilene side om side: agenten flagget feil sak (Michael Dell) og overså riktig sak (Texas-flyttingen).

Sjekk: `python3 -I arbeid/oppgave_2343/plukk.py` (lister alle TP/FP/FN med P(MOT), ruting og retningslinje). Full liste: `arbeid/oppgave_2343/liste.txt`.
