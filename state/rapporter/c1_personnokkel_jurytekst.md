# Case 1 (#2505): personnøkkel-funnet er skrevet inn i jurytekstene

- Dommen på #2496 er GODKJENT (`state/rapporter/c1_personnokkel_dom.md`, dommer #2503).
- `JURY_SPORSMAL.md` pkt 13: én setning om at personnøkkelen gir +0,049 på 2026, men −0,037 på 2024 og +0,001 på 2025, med KI som dekker null begge år, og derfor ikke er tatt inn.
- `NESTE_VERSJON.md`: punktet om personnøkkelen på tidligere år sier nå «KI dekker null i 2024 og 2025» og peker på `kilder/` i stedet for `landsbyrapport:`.
- Rapporten og dommen er kopiert til `kilder/` med en kopinote øverst. pakk_jury.sh tar med hele leveranse/, så den trengte ingen endring.
- Funn underveis: tallsjekken i sluttsjekken var RØD på fire interne saksnumre (sak 2485/2490/2495/2496) i nye avsnitt i NESTE_VERSJON fra andre agenter. Jeg fjernet numrene, ingen tall i innholdet er endret.
- Sjekker: tallvakt 0 avvik, frysvakt GRØNN (17/17), sluttsjekk GRØNN F1 MOT 0.476190 = zipen, frys_fasit LIK (129 filer). Commit 0d0dc9f; NESTE_VERSJON og fasiten kom i HEAD via 8ed8ac3/04b76c0 (#2504, #2508) med samme innhold.
