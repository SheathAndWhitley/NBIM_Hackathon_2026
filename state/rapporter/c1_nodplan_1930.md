# Case 1 (#2688): nødplan hvis kald start av endelig pakke (#1972) feiler kl. 19:30

Arkitekt, 05.11 kl. 17:45–18:00. Ingen frosne filer eller leveranse-tekster rørt.

## Reservene på disk (sjekket 17:55)
Kopiert ut av /tmp i dag, fordi /tmp ryddes under diskryddingen (#2683): `state/levering/c1_gronn/reserve_staar/` (SHA256.txt ligger der).

| Rang | Fil | sha256 | Hva |
|---|---|---|---|
| 1 | `state/levering/c1_gronn/SISTE_GRONNE.zip` -> `jurypakke_c1_1744_7efa4da.zip` | `e48426cd…cda031` | Siste grønne BYTT-pakke (0,512). Står den, er den svaret. |
| 2 | `state/levering/c1_gronn/reserve_staar/jurypakke_staar_2640.zip` | `32de94c3…ae417d7` | **STÅR-zip**, frossen modell 0,476 + rettede tekster. Tørrkjørt GRØNN i #2640 kl. 17:37: tallvakt 0 avvik, ZIPTEST GRØNN, HOVEDTALL 0.476190, TP 30 FP 38 FN 28 TN 1443. 167 filer. |
| 3 | `state/levering/c1_gronn/jurypakke_c1_1701_frossen_2587.zip` (= reserve_staar/jurypakke_c1_2587.zip) | `af3dd758…7d3e` | Frossen pakke 17:01, 0,476, *gamle* tekster uten jury-rettelsene. Siste skanse. |

Underlag for å bygge STÅR på nytt (samme mappe): `bytte2572_c1_frys.json` (d45ed794…), `bytte2572_head.txt`.

## Beslutningstre kl. 19:30
1. **Tall avviker** (HOVEDTALL ≠ 0.512 eller tallvakt rød) og retting tar over 5 min: lever **rang 1** (17:44-zipen) hvis den er yngre enn tekststoppen og fortsatt grønn; ellers rang 2.
2. **Avhengighet/kode feiler** (uv sync, import, KJOR.sh exit ≠ 0) i BYTT-pakken: lever **rang 2** (STÅR, annen modellkode, samme miljø som frys kl. 16).
3. **Disk full (ENOSPC)**: frigjør plass først (punkt «Disk» under), så kjør testen på nytt. Ikke bytt pakke for en diskfeil; pakken er ikke feil.
4. Alt rødt kl. 19:45: lever **rang 2 uten ny test** (den er tørrkjørt grønn), si det ærlig i følgebrevet: «testet grønn 17:37, ikke rekjørt etter 19:30».

## Kommandoer
Test en ferdig zip fra kald start (ca. 60 s, krever ledig disk, se under):
```
sh arbeid/hack/levering/test_jury_zip.sh <ZIP> /tmp/nod_test     # siste linje: ZIPTEST GRØNN: HOVEDTALL ...
```
Lag STÅR-zipen på nytt (bare hvis rang 2 mangler, ca. 3 min, oppskrift `c1_staar_ovelse.md` + `c1_staar_rettelser_2640.md`):
```
R=state/levering/c1_gronn/reserve_staar
python3 -I arbeid/oppgave_2598/lag_staar.py --sjekk                      # må si LIK
sh arbeid/hack/c1/bytte/tilbake_fra_zip.sh <repo> $R/jurypakke_c1_2587.zip $R/bytte2572_c1_frys.json
cp arbeid/hack/c1/reserve_staar/{README,kravrespons,ERLIG_EVALUERING,JURY_SPORSMAL,MUNTLIG}.md arbeid/hack/c1/leveranse/
python3 -I arbeid/oppgave_2631/staar_rest.py --skriv
python3 -I arbeid/verktoy/c1_tallvakt.py                                  # 0 avvik
python3 -I arbeid/hack/levering/frys_fasit.py > arbeid/hack/levering/frys_fasit_1600.sha256
sh arbeid/hack/levering/pakk_jury.sh /tmp/jurypakke_c1_staar.zip && sh arbeid/hack/levering/test_jury_zip.sh /tmp/jurypakke_c1_staar.zip
```
Merk: dette skriver over BYTT-tekstene i landsbyen. Gjøres bare etter dom fra dommeren, helst i en kald kopi.

## Disk: den mest sannsynlige feilen
**KP: forventet ZIPTEST GRØNN på rang 2 kl. 17:55, fikk ENOSPC.** Min test av STÅR-zipen fylte disken (1,2 GB -> 0): test_jury_zip.sh bruker tom HOME og tom uv-buffer, så uv laster ned og installerer hele miljøet på nytt. Etter at jeg slettet min testmappe: 396 MB ledig. Testen ga derfor ikke dom; rang 2 står på #2640-tørrkjøringen.
- Krav før 19:30: **minst 2 GB ledig** (`df -h /`). Under det feiler kald start uansett pakke.
- Rask plass: `rm -rf /tmp/jurytest_zip* /tmp/staar_ovelse_2631 /tmp/staar_kald /tmp/b2572tree` (testkopier, ikke leveranser), deretter diskvakta.
- Ikke slett noe i `state/levering/c1_gronn/`.

## Hvem gjør hva
| Når | Hvem | Hva |
|---|---|---|
| nå–19:00 | smed (#2683) | Disk over 5 GB. Ikke rør `state/levering/c1_gronn/`. |
| 19:00 | smed (#2549) | Tekststopp-zip, legges i c1_gronn og SISTE_GRONNE peker dit. |
| 19:30 | dommer (#1972) | Kald start av SISTE_GRONNE. Grønn: ferdig. Rød: velg etter beslutningstreet over, én linje på tavla. |
| 19:30–19:40 | smed3 | Retter feilen *eller* tester rang 2 med `test_jury_zip.sh` i `/tmp/nod_test`. |
| **19:45** | dommer | **Siste tidspunkt for å bytte.** Står det ikke en grønn pakke da, leveres rang 2 som den er. |
| 19:45–20:00 | ordfører | Pakken som er valgt legges der guden henter den, sha i tavla. |

## Anbefaling
Rang 2 (`reserve_staar/jurypakke_staar_2640.zip`, sha 32de94c3…) er reserven. Viktigste tiltak nå er disken, ikke pakken: under 1 GB ledig feiler kald start uansett.
