# Case 1: demoen godkjent fra kald kopi, med fire avvik i manuset (dommer2 #2240)

**Dom: GODKJENT.** Kald start er GRØNN, demoen gir samme tall som manuset, README-kallet virker. Manuset har fire små avvik som speider må rette (#1975).

## Kjørt (05.11 kl. 13.41, git 9012a58)
- `BEHOLD=1 bash arbeid/hack/c1/kaldstart.sh` -> `GRØNN F1_MOT 0.476190 REF 0.476190 AVVIK +0.000000`, 33 s, kopi /tmp/c1_kald.g9AtHN, måler v3 sha256[:10] 418a937e57.
- I kopiens rot, ordrett fra manuset: `bash arbeid/hack/c1/demo_saker_2026.sh` (18 s, exit 0) og `bash arbeid/hack/c1/demo_mangler_styret.sh` (exit 0). Siste linje: `HOVEDTALL maaler_offisiell_v3.py ... F1 MOT 0.476190`. Linja over den: `TP 30 FP 38 FN 28  P 0.4412  R 0.5172`.
- Fra landsbymappen: `bash arbeid/hack/c1/leveranse/kjor.sh` (57 s, exit 0), `TALLVAKT GRØNN`, `MOT mot styret ... F1 0.4762`.
- Frysvakta: `c1_frys.py sjekk` sier «ikke frosset ennå» (exit 0). Den sperrer altså ikke, men den er ikke prøvd mot frosne filer. Det gjør den først etter kl. 16 (#1972).

## Skjermen mot manuset (sak 1–7)
Seed 17 trekker de samme fem sakene. Sitatsaken er 2089132|3 (seed 0 av 71). Hver sak har samme agentsvar, samme rutingsgrunn og samme fasit som i manuset:
1 rå 0.91223 / sjanse 0.1912, går til menneske (usikker). 2 rå 0.2623 / 0.0075, går ikke til menneske. 3 rå 0.63559 / 0.0455, går til menneske (ukjent selskap). 4 rå 0.45061 / 0.0138, går ikke til menneske, og fasit er Against. 5 rå 0.257 / 0.0075, går til menneske (ukjent selskap), og fasit er Against. 6 MOT, rå 0.96994 / 0.5217, går til menneske med sitatet GVG 1.1. 7: med anbefaling går saken ikke til menneske. Uten anbefaling går den til menneske med samme grunn som i manuset.

## Avvik i manuset (DEMO_MANUS.md)
1. **Linje 78 og 81:** utdraget viser `score 0.0075`. Skjermen viser nå `rå 0.2623  sjanse for MOT 0.0075`, og i tillegg en linje `forslag: Approve Non-Financial Report` over. Utdraget bør byttes med det som faktisk vises.
2. **Linje 7–9 og 93:** manuset sier ikke at siste linje på skjermen er `HOVEDTALL ... F1 MOT 0.476190`, og heller ikke at 0,4818 rett over er et sidetall (avvik inkl. avstå). Juryen kan lese 0,4818 som hovedtallet. Én setning om dette bør inn.
3. **Linje 7:** «ca. 15 s». Målt 18 s, og skriptets egen kommentar sier 20 s. Det er lite, men tallet bør være det samme begge steder.
4. **Linje 91:** «målt med arrangørens måler». Kaldstart og README sier «måler v3, landsbyens kopi». Ordet må være det samme overalt. Måler-sha er 418a937e57, mens commit 58f2bd1 nevner v3 8b09c36e01. Det hører til #2238.

## Funn underveis (ordnet)
Første kalde start kl. 13.38 var **RØD**, med `ModuleNotFoundError: injeksjon_hoflig`. Smed3 (#2237) hadde lagt en ny import inn i den levende `c1_real.py`, men ikke i kaldstart.sh sin filliste. Det var rettet kl. 13.41, og andre kjøring er den som gjelder. Lærdom: endringer i `c1_real.py` må komme sammen med kaldstart.sh og fremmed.sh i samme steg. Ellers brekker kald start mellom stegene. `arbeid/` er gitignorert, så det finnes ingen historikk å rulle tilbake til.
