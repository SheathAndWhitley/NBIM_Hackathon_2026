# Case 1: robusthetstallene fra #2380 ført inn i ERLIG_EVALUERING.md (smed3 #2386, 05.11 kl. 15.25)

**Resultat: nytt § 5 i `arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md`. Akseptkravet holder: `fremmed.sh` i tom /tmp-mappe gir HOVEDTALL 0.476190 og TALLVAKT GRØNN (167 påstander stemmer, 0 avviker). Ingen frosne filer endret.**

## Hva som er skrevet
- Tallene fra #2380 er like som #2063/#2071 i utfall: 16 av 16 testtyper gir samme krasj/MOT/menneske/uten grunn, ingen krasj.
  Derfor én kort passasje om at testen er gjentatt på dagens pakke fra kald kopi, med kilde.
- Det som faktisk er annerledes, står ærlig med: rutingsgrunnen «nær grensen» heter nå «usikker: kalibrert P(MOT) i båndet»,
  og høflighetsvakta legger «instruksjonslignende tekst i forslaget» på fem oppdiktede forslag som før hadde én grunn.
  Ingen sak rutes annerledes. Svakheten (misvisende grunn på ekte, uvanlige forslag) er nevnt.
- Gammelt § 5 (detaljer fra kravresponsen) er nå § 6, og henvisningen «(se § 5)» i § 2 er rettet til § 6.
- Kilder lagt i pakka: `leveranse/kilder/c1_robusthet_kald_2380.md` (rapporten fra #2380) og
  `leveranse/kilder/c1_robusthet_kald_2380_tabell.md` (full tabell per testtype).

## Én ting å vite om tallvakta
Første kjøring ble RØD: jeg skrev «F1 0,476190 på MOT mot styret», og tallvakta sammenligner med målerens fire desimaler (0.4762).
Rettet til «F1 0,476 på MOT mot styret (0,476190 med seks desimaler i fremmed.sh-utskriften)». Andre kjøring GRØNN.
Lærdom for andre som skriver i pakka: skriv hovedtallet med tre eller fire desimaler på linjer med «F1 ... MOT».

## Kjøring
`rm -rf /tmp/c1_kald_2386 && sh arbeid/hack/levering/fremmed.sh /tmp/c1_kald_2386` (uv sync 0 s, kjøring 29 s). Logg: `/tmp/fremmed_2386.log`.
Frosne filer (lista i `arbeid/verktoy/c1_frys.py`): `git status --short` tom.
