# Case 1: dom over tallene i de tre eksempelsakene og lim-inn-fanen (#2351, dommer)

**Dom: HOLDER.** Alle påstandene i `c1_tre_eksempler.md` (#2343) og de tre stikkprøvede radene i `c1_limfane_kontroll.md` (#2344)
stemmer med min egen telling. Ingen agentfiler er endret. Ingen rettelser nødvendig.

**Slik telte jeg (uten smed2s plukk.py):** egen kald kopi med `fremmed.sh /tmp/dommer2351` (tallvakt grønn, kl. 14.56),
og eget skript `arbeid/oppgave_2351/tell.py` (bare stdlib). Skriptet slår `kjor_agent_real_maskin_alene.csv` sammen med
real_votes 2026 (1578 rader, 1539 med against_board) og teller MOT mot styret som måler v3 gjør. Rutingen står ikke i
maskin_alene-fila (alle 1578 har konfidens 0,9, og p_avvik der er den rå scoren, ikke kalibrert P(MOT)). Den leste jeg
fra kopiens egen `agent.csv`, etter å ha bekreftet at kopien har samme avvik-flagg og samme rå score som leveransefila
på alle 1578 rader (0 avvik). Kopiens `pred_maaler.csv` har 188 rader med konfidens 0,5, likt leveransens.

| påstand | rapporten sier | min telling | dom |
|---|---|---|---|
| F1 på MOT, test 2026 | 0,476190 (TP 30, FP 38, FN 28) | 0,476190, TP 30 FP 38 FN 28 | holder |
| (a) falske alarmer til menneske | alle 38, ingen rett ut | 38 av 38 rutet, 0 rett ut | holder |
| (b) treff | 9 rett ut, 21 til menneske | 9 rett ut, 21 rutet, av 30 | holder |
| (c) bommer fanget av ruting | 11 av 28; de 17 andre under 0,15 | 11 av 28 rutet; 17 ikke rutet, alle med P(MOT) < 0,15 (maks 0,0896) | holder |
| til menneske totalt | 188 av 1578 (183 med fasit) | 188 av 1578; 183 blant de 1539 med fasit | holder |

**(d) de tre radene, lest fra kopiens agent.csv og real_votes 2026:**

| sak | styret / agent / NBIM | P(MOT) kalibrert (rå) | til menneske | retningslinje | NBIMs seksjon 2026 | dom |
|---|---|---|---|---|---|---|
| Pochteca 2068788\|4, 30.04.2026, sak 4 | FOR / MOT / MOT | 1,0 (0,99302) | nei | NBIM 3.1.1 «The company should have a robust nomination and election process …» | GVG 3.1 | holder |
| Dell 2085617\|1, 25.06.2026, sak 1 (Michael S. Dell) | FOR / MOT / FOR | 0,5217 (0,95551) | ja, båndet | NBIM 1.2.1 «Board decisions that are particularly vulnerable to conflicts of interest …» | (ingen, NBIM FOR) | holder |
| Dell 2085617\|11, sak 11 (Delaware→Texas) | FOR / FOR / MOT | 0,0138 (0,40616) | nei | NBIM 0.0.3 «Our starting point … is to support the board.» | GVG 4.3 | holder (rapporten runder til 0,014) |

Historikkpåstandene holder også: NBIM stemte MOT Pochtecas styrevalg 2019, 2020, 2021, 2022, 2023 og 2025 (teksten heter
«Elect or Ratify …» til 2021 og «Elect and/or Ratify …» fra 2022), med GVG 3.1 som begrunnelse 2020–2025. Michael Dell:
MOT 2019–2022, FOR 2023–2026. Delaware→Texas finnes tre ganger i data: Tesla 2024 FOR, Dell 2026 MOT, Texas Capital
Bancshares 2026 MOT. Texas Capital (2052809|13) fikk FOR fra agenten med P(MOT) 0,0 og ble ikke rutet, altså samme bom.

**Lim-inn-fanen, stikkprøve 3 rader** (`arbeid/oppgave_2344/fane_ti_saker.json` mot `cli_ti/agent.csv`, `cli_sak_tom/agent.csv`
og min kalde kopi): anbefaling, P(MOT), til menneske, rutingsgrunn og retningslinje er like i alle kilder.
- 2040176|5: MOT, 0,5217, rutet, «usikker … 0,52 i båndet», NBIM 3.3.1. Fane = CLI = kald kopi.
- 2035238|3: FOR, 0,0896, rutet, «ukjent selskap», NBIM 0.0.3. Fane = CLI = kald kopi.
- 9900001|1 (tom tekst): FOR, P(MOT) tom, rutet, «kan ikke vurderes: mangler felt: proposal_text». Fane = CLI (--sak).

**Merknad, ikke feil:** p_avvik i `kjor_agent_real_maskin_alene.csv` er rå modellscore (0,993 for Pochteca), ikke kalibrert P(MOT).
Den som vil lese ruting eller P(MOT) må bruke agent.csv eller pred_maaler.csv (konfidens 0,5 = rutet). Står alt i `_LES.md`-stilen allerede.

Bevis: `arbeid/oppgave_2351/` har `tell.py`, `fremmed.log`, `KJORING_kald.txt` og `agent_kald.csv`.
Kjør på nytt: `python3 -I arbeid/oppgave_2351/tell.py arbeid/hack/levering/kjor_agent_real_maskin_alene.csv arbeid/oppgave_2351/agent_kald.csv`
