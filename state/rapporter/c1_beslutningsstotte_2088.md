# Case 1: beslutningsstøtten bygger nå på terskeltabellen (#2088, speider)

Fil: `arbeid/hack/levering/BESLUTNINGSSTOTTE.md`, skrevet om for en forvalter.

- Gamle N-PX-tall (#1995, 129 MOT av 1246, bare amerikansk say-on-pay) er fjernet. Nytt grunnlag: real_votes test 2026, 1539 saker, 66 MOT, alle markeder og sakstyper, frossen modell #2044.
- Hovedtabell per 100 saker med fire kolonner: maskin alene (4,6 leses, 50 % fanget), **i dag 10 % sone (13,3 leses, 65 % fanget, 23 av 66 oversett)**, vid (33,2 leses, 82 %), høy presisjon (1,9 leses, P 0,80, 36 % på test / 25 % på val). Pluss mellomting (15 % sone, 23 leses, 76 %).
- Hvert tall peker til `c1_terskeltabell.md` (#2084), `c1_bootstrap_f1.md` (#2086), `c1_agent_real_2053.md` eller `case1_svakheter_2082.md`. Falske flagg, oversett og timer er regnet om fra P, R og sone-% i tabellen (formel står i fila).
- Forbehold med: få MOT (KI 0,38–0,58), «fanget» er øvre grense, sonen blir 11 % på test, ekte rutingandel 11,2 %, historikk må være oppdatert (0,48 → 0,39), terskelen er skjør (0,92 → 0,83 gir F1 0,35).
- p_mot-avsnittet med gammel kalibrering (#2015, N-PX) er byttet ut: p_mot er rekkefølge, ikke prosent. Treffprosent- og kostnadstabellene fra N-PX (#2017, #2032) er fjernet; timer er regnet på nytt med samme antagelse (20/10 min).

**Hull funnet:** agenten kan bare velge andel til menneske (`--til-menneske`), ikke terskel. «Vid» og «høy presisjon» finnes bare i `terskeltabell.py`. Står ærlig i fila. Et `--oppsett`-flagg i `kjor_agent.py` ville gjøre de tre valgene ekte (forslag til smed, ikke gjort her).
