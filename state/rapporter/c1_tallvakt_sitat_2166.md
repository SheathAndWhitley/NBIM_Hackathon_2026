# Case 1: tallvakt og sitatkontroll etter rettingene (#2166, dommer2, 05.11 kl. 13.10)

**Dom: 0 avvik i tallvakta og 0 sitatfeil.** Én utdatert fil som tallvakta ikke fanger, se under.

## Tallvakta
- Kald kopi `sh arbeid/hack/levering/fremmed.sh /tmp/d2_2166`: utgang 0, F1 MOT 0,476190, TP 30 FP 38 FN 28 (58 MOT, 66 avvik),
  til menneske 188 av 1578 (11,9 %) og 183 av 1539 (11,9 %). `13 filer, 129 påstander stemmer, 0 avviker`, TALLVAKT GRØNN.
- Samme resultat i landsbyen (`python3 -I arbeid/verktoy/c1_tallvakt.py`): 0 avvik. De 22 menneske-avvikene fra #2156 er borte.
- Demoen (`c1/leveranse/demo_utskrift.txt`) teller riktig: 58 MOT mot styret, 30/38/28, F1 0,4762, 183 av 1539 til menneske.

## Avvik som tallvakta ikke ser (eier: smed2, #2159)
- `arbeid/hack/levering/kjor_agent_real_test2026_LES.md:10` sier «228 av 1578 (14,4 %)» og «223 av 1539 (14,5 %)».
  Riktig nå: **188 av 1578 (11,9 %)** og **183 av 1539 (11,9 %)**. Linja nevner ikke «menneske», så regexen i vakta hopper over den.
- `levering/c1_v1/` (kravrespons.md:4, ut/KJORING.txt og loggene) har 228/14,4 %. Det er den gamle v1-pakka. Den må merkes «eldre» eller holdes utenfor juryens pakke.

## Sitatkontrollen
- `python3 -I arbeid/oppgave_2166/alle_sitat.py /tmp/d2_2166/ut/agent.csv`: 1578 rader, alle har retningslinje-sitat, 74 MOT, 0 MOT uten sitat.
  **15 unike sitater, alle 15 står ordrett** både på NBIMs nettside (rå html) og i PDF-en.
- `arbeid/oppgave_2166/nummer.py`: nummeret er utledet fra h3/h4 i html-en og stemmer for alle 15. Det gjelder også de 8 som ikke ble sjekket i #2143
  (1.2.1, 2.1.1, 2.3.1, 3.2.1, 4.2.1, 5.1.2, 5.2.1, 6.3.1). For 6.2.5 er ledd 5 bekreftet i #2143.
- Demoutskriften har nå 1.1.1 og 3.1.1. Den gamle feilen 3.1.8 er borte (0 treff).

## Viktig
#2152 (nye menneske-vakter) er ikke ferdig. Når den og #2162 har kjørt, endres 188/183 igjen.
Da må `c1_tallvakt.py` kjøres på nytt, helst via `fremmed.sh` (#2155).
