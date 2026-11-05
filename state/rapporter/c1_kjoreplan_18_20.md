# Case 1: kjøreplan 18–20 med reserve hvis kaldstarten feiler (#2548)

Regel: **vi leverer alltid en zip som har vært grønn.** Det er bedre å levere en eldre grønn zip enn en nyere zip som ikke er testet.

## Tidsplan
| Kl. | Hvem | Hva | Ferdig når |
|---|---|---|---|
| 18:00 | smed (#2538) | `bash arbeid/hack/levering/sluttsjekk.sh` fra ren tilstand: tallvakt, frysvakt, pakk_jury, test_jury_zip, lagre_gronn | ZIPTEST GRØNN F1 MOT 0.476190, ny linje i `state/levering/c1_gronn/SHA256.txt`, rapport `c1_sluttsjekk_1800.md` med HEAD og SHA |
| 18:00–19:00 | smed2/smed4, dommer2, speider | Bare tekstrettinger som allerede er på tavla (#2543–#2547). Ingen nye tall. Hver commit: tallvakt 0 avvik og frys_diff LIK | Hver commit grønn |
| **19:00** | alle | **TEKSTSTOPP.** Etter dette blir ingen filer i `arbeid/hack/c1/leveranse` endret. Ser noen en feil etter 19:00, skriver de den i BEGRENSNINGER i neste versjon, ikke i pakka | — |
| 19:00–19:15 | smed (#2549) | Sjekk at `git status --short arbeid/hack` er tom (se #2554 hull 2), så bygg zip på nytt fra HEAD, sluttsjekk.sh, lagre ved siden av reserven | `c1_tekststopp_19.md` med HEAD og SHA |
| 18:30 / 19:15–19:30 | dommer (#1972) | Kaldstart av **19:00-zipen** (`test_jury_zip.sh` i tom mappe, tom HOME). Sjekk tall mot tavla og tidssplitten. Skriv e-postutkastet `epost_utkast_hackathon.md` med filnavn og SHA på den zipen som blir levert | Endelig pakke = én navngitt fil + SHA, kl. 19:30 |
| 19:30–20:00 | ingen | Buffer. Ingen bygging. Bare reserveregelen under gjelder | — |

#1972 kan starte kl. 18:30 med 18:00-zipen som prøve. Da er kaldstartveien testet før 19:00-zipen kommer, og 19:15-kjøringen blir en ren gjentakelse.

## Reserven
- **Reservefila er den zipen #2538 lagrer kl. 18:** `state/levering/c1_gronn/jurypakke_c1_18MM_<HEAD>.zip`, der SHA står på linja fra 18:xx i `SHA256.txt`. #2538 skriver fullt navn og SHA i `c1_sluttsjekk_1800.md`. Det navnet er reserven, og ikke noe annet.
- **Ikke pek på `SISTE_GRONNE.zip`.** Lenka flytter seg hver gang noen lagrer en grønn zip. Den har flyttet seg tre ganger mellom 16:33 og 16:42. Reserven skal angis med filnavn og SHA.
- Før 18:00 er reserven den siste grønne nå: `jurypakke_c1_1642_bf0d3f8.zip`, SHA256 `83c3fdb6caaa84bb516e8c98ade07a67fa8352e871335ce8871e0f37ac62d3f8`. Den kom fra HEAD bf0d3f8 kl. 16:42.
- Sjekk før levering: `shasum -a 256 <fil>` skal gi samme SHA som i rapporten. Hvis SHA er ulik, er fila ikke reserven.

## Hvis noe feiler
| Feil | Hva vi leverer |
|---|---|
| 18:00-sjekken er rød | #2538 retter bare det som feilet og kjører på nytt. Reserven er 16:42-zipen til en ny grønn er lagret |
| Teksten blir ikke ferdig til 19:00 | Det blir stopp likevel. Det som er grønt i HEAD kl. 19:00, blir pakka |
| 19:00-zipen er rød, eller den ikke er lagret innen 19:20 | Lever **18:00-reserven**. Ingen ny bygging etter 19:20 |
| Kaldstarten i #1972 er rød på 19:00-zipen | Kjør reserven fra 18:00 kaldt (målt 57 s i #2554): `sh arbeid/hack/levering/test_jury_zip.sh state/levering/c1_gronn/<reservefil>.zip /tmp/reserve_$(date +%H%M)`. Den var grønn i test_jury_zip kl. 18, så hvis den er grønn nå, leverer vi den. Avviket skrives i e-postutkastet |
| Loggen sier `Failed to download` / `dns error` | Det er nettet, ikke zipen: kaldtesten har tom uv-buffer og laster ned pakker. Kjør samme zip nettfritt med maskinens buffer (målt 68 s, grønn i #2554): `sh arbeid/oppgave_2554/test_jury_zip_utennett.sh <zip> /tmp/reserve_utennett`. Grønn der = zipen er god |
| Begge er røde kl. 19:30 | Det er maskinen eller testen som er feil, ikke zipene. Lever 18:00-reserven med SHA. Dommeren skriver hva som feilet og når testen var grønn |

Siste frist for tekstendringer er **kl. 19:00**. Siste frist for å bygge zip er **kl. 19:20**. Kl. 19:30 er valget gjort, og det står i e-postutkastet som ett filnavn og én SHA.

## Prøvd i #2554 (16:45, arkitekt)
- Reserveveien kjørt på 16:42-zipen i tom /tmp-mappe: SHA stemte, ZIPTEST GRØNN, F1 MOT 0.476190, TP 30 FP 38 FN 28 TN 1443, **57 s** fra start til grønn.
- Hull 1 (rettet over): kaldtesten trenger nett. Med nettet sperret blir den rød på 6 s (`Failed to download pandas`). Nettfri variant med maskinens uv-buffer er grønn på 68 s.
- Hull 2: samme HEAD gir ikke samme innhold. bf0d3f8 ga 1642-zip `83c3fdb6…` og 1644-zip `ec8e04b8…`, og 6 tekstfiler er ulike (JURY_SPORSMAL, NESTE_VERSJON, LESMEG, to nbim_repo-filer, JURYSVAR). Pakka bygges fra arbeidstreet, ikke fra commiten, så ucommittede endringer kommer med og HEAD i filnavnet stemmer ikke. **Retting:** før byggingen kl. 18:00 og 19:00 skal `git status --short arbeid/hack` være tom. Hvis ikke, commit eller vent før `sluttsjekk.sh`. Reserven angis alltid med filnavn og SHA, aldri med HEAD alene.
- Hull 3: `state/` er git-ignorert, så reservezipen finnes bare på disk i `state/levering/c1_gronn/`. Ikke rydd den mappa før levering.
