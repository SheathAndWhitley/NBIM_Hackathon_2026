# Case 1: demo-manuset har nå de tre ekte sakene, under 3 min (#2267)

- `arbeid/hack/c1/DEMO_MANUS.md` skrevet om: måltall, treff Mobimo (agent.csv linje 276), bom LOTTE Chemical (linje 89), til menneske Kura Sushi (linje 15), avslutning. 359 ord leses høyt, ca. 2:30.
- Bommen vises ærlig og med sin farlige side: P(MOT) 0,09, FOR uten menneske. Av 28 oversette MOT gikk 17 FOR fra maskinen alene, 11 til menneske; alle 38 falske MOT gikk til menneske.
- Alle tall målt på nytt kl. 14.0x: `arbeid/oppgave_2267/maaling.txt` (måler v3 sha 418a937e57: TP 30 FP 38 FN 28, F1 0,4762, 183 rutet av 1539) + `telling.py` (ruting per feiltype). Tallkilde-tabell nederst i manus.
- Sitatene sjekket maskinelt: alle tre finnes ordrett i agent.csv. agent.csv er lik kald kopi /tmp/fremmed (sha f0444a47…).
- Forrige 5-min-manus med tilfeldige saker (seed 17) ligger som `DEMO_MANUS_5min_tilfeldige.md`.
- Ærlig merknad: Mobimos retningslinjesitat (5.2.1, årsrapport) passer dårlig, står i manus som svar hvis spurt. «96 av 100» er avrundet fra følg-styret 96,2 % (c1_demo_etter_rydding.md), ikke fra min egen utskrift.
