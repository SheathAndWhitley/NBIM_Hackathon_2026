# Case 1: dom over huskeregel-grunnlinja fra smed2 (#2350) – HOLDER

Dommer, 05.11 kl. 15.05, oppgave #2354. Dom: **HOLDER.** Alle fire tall i `c1_huskeregel.md` er reprodusert fra kald kopi og målt av meg med måler v3, og regelen bruker ingen informasjon som ikke er kjent før møtedatoen.

## Hva jeg gjorde
1. Kald kopi: `huskeregel.py` kopiert alene til tom mappe under `/tmp`, kjørt med `python3 -I` fra `/tmp` (2,5 s, exit 0). Utskriften er tegn for tegn lik `arbeid/oppgave_2350/kald_ut.txt`, og de fire `regel_*.csv` er byteidentiske med smed2s (`cmp`).
2. Egen måling, uten skriptets `maal()`: `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py <fil> <vindu> --data real --score mot`. Måler-sha 418a937e57, data 71ba5135e7, 13 757 rader.

| Variant | Vindu | F1 MOT | P | R | TP/FP/FN | smed2 |
|---|---|---|---|---|---|---|
| A selskap + sakstype | val 2025 | 0,254237 | 0,1765 | 0,4545 | 45/210/54 | 0,2542 ✓ |
| A selskap + sakstype | test 2026 | **0,243243** | 0,1513 | 0,6207 | 36/202/22 | 0,2432 ✓ |
| B selskap, alle saker | val 2025 | 0,161538 | 0,0925 | 0,6364 | 63/618/36 | 0,1615 ✓ |
| B selskap, alle saker | test 2026 | **0,125000** | 0,0683 | 0,7414 | 43/587/15 | 0,1250 ✓ |

Frossen #2044 i samme kjøring: val 0,5202, test 0,4762 (lik `hack_levert`).

## Lekkasjesjekk
- Historikken bygges bare av rader med kjent `nbim_vote`, og oppslaget bruker `meeting_date` **strengt før** sakens dato. Datoene er ISO (`YYYY-MM-DD`, alle 13 757 rader), så strengsammenligningen er riktig. Eget møte brukes aldri; 33 selskap+dato-par med flere meeting_id samme dag ekskluderes også (konservativt).
- Løpende historikk (stemmer fra samme vindusår ved tidligere møter): jeg kjørte regelen om med historikk **bare fra år før vinduet**. Alle tolv tall ble identiske (TP/FP/FN uendret for A og B, val og test). Regelen bruker altså i praksis ingen stemmer fra testvinduet; spørsmålet om løpende historikk er irrelevant for grunnlinja.
- `mgmt_rec` tom tolkes som FOR, samme som måler v3. Styret MOT gir alltid «følg styret», ingen MOT-flagg fra regelen der.
- Ingen trening, ingen terskel, ingen valg på test: regelen er skrevet før måling, med A og B begge rapportert.

## KI-tallene
Diff-KI-ene (frossen minus regel, parret klyngebootstrap per selskap, `arbeid/oppgave_2103/diff_ki.py`) kom ut identiske i min kjøring: A test +0,233 [+0,118; +0,335], B test +0,351 [+0,240; +0,462], regelen vinner i 0 av 2000 trekk. Jeg har ikke revidert diff_ki.py på nytt i denne dommen (godkjent i #2103).

## Til speider (én setning til jurypakka)
> Den beste huskeregelen vi fant («stem MOT der NBIM stemte MOT mot styret sist gang i samme selskap og sakstype») gir F1 0,243 på test 2026 og 0,254 på val 2025 mot agentens 0,476 og 0,520, en forskjell på +0,23 [95 % KI +0,12; +0,34] på test, verifisert av dommeren fra kald kopi med måler v3 (`state/rapporter/c1_huskeregel_dom.md`).

## Småting (ikke rettingskrav)
- Forsøk #1172 og #1173 står som selvrapporterte på tavla fordi #2350 ikke har egen måler. Tallene er bekreftet her; jeg lar dem stå uendret for å ikke røre målere én time før frys.
- Skriptet har absolutte stier til landsbyen (`LAND = <repo>`). Det er greit for en intern grunnlinje, men det hører ikke inn i jury-zipen uten omskriving.
