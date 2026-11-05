# Case 1: reserveplan når sluttsjekken blir RØD etter kl. 19 (#2524)

Grunnene under er de faktiske `rod`-linjene i `arbeid/hack/levering/sluttsjekk.sh`. Utgang 4 = rød.
Loggmappa står i RØD-linja (`$LOGG`). **Eier av alt etter 19:00: dommer** (kjøreplanens regel 2). dommer2 kjører
ziptesten av reservezipen, fordi den skal sjekkes av en annen enn den som bygde den.

**Reservezip (R)**, i denne rekkefølgen:
1. `state/levering/c1_gronn/SISTE_GRONNE.zip`, SHA i `c1_gronn/SHA256.txt` (fylles av #2522 / sluttsjekk 18:30 og 19:00).
2. Finnes den ikke: siste kjente grønne fra i dag er `/tmp/c1_jurypakke.Oait/jurypakke_c1.zip`, 16:26,
   SHA256 `07417d5e56b6fa4c3e5f3f01b43415a910eeceaa70344e333e2f83d7d2c5da91`, 149 filer, ziptest GRØNN 0.476190
   (logg `/tmp/c1_sluttsjekk_logg.ULpU`). Bygd før commit 9994f16 (JURY_SPORSMAL 14-18 mangler der).
3. Eldre reserve: `/tmp/c1_jurypakke.kP4i/jurypakke_c1.zip` (16:13, SHA `13e23f4a…aa7f0`).

Sjekk R før bytte (1–2 min, dommer2): `shasum -a 256 R` mot linja over, og
`sh arbeid/hack/levering/test_jury_zip.sh R $(mktemp -d)` → `ZIPTEST GRØNN … 0.476190`.

| RØD-grunn (tekst i RØD-linja) | Hva dommeren gjør (kommando) | Lever i stedet | Siste bytte |
|---|---|---|---|
| `frysvakt (utgang N)` | Modellfil rørt etter frys. `python3 -I arbeid/verktoy/c1_frys.py sjekk` viser fila; `git checkout <frys-commit> -- <fil>` (commit i c1_frys.json), så `bash arbeid/hack/levering/sluttsjekk.sh` | R, hvis ny kjøring ikke er grønn | Rett til 19:25, bytt til R 19:30 |
| `kaldstart fremmed.sh (utgang N)` | `tail -30 $LOGG/2_fremmed.txt`. Miljøfeil (uv/nett/disk): `df -h /tmp`, kjør sluttsjekken én gang til. Kodefeil: `git revert <siste commit>` | R | Ett omforsøk; ikke grønn 19:25 → R |
| `TALLVAKT RØD … mangler .venv eller pred_maaler.csv` | Kald kopi ufullstendig: `rm -rf /tmp/c1_sluttsjekk_ny; bash arbeid/hack/levering/sluttsjekk.sh /tmp/c1_sluttsjekk_ny` (egen mappe, sletter ikke andres) | R | 19:25 |
| `TALLVAKT RØD (utgang N): k tall avviker` | `grep ^AVVIK $LOGG/3_tallvakt.txt` viser fil:linje. Rett tallet eller `git revert` commiten som innførte det, kjør sluttsjekken | R (tallene der er tallvakt-grønne) | Retting til 19:20 (sluttsjekk tar ca. 3–5 min), ellers R |
| `TALLVAKT RØD i fremmed.sh, men grønn i steg 3` | Uforklart, ikke rett i blinde: `diff <(grep AVVIK $LOGG/2_fremmed.txt) <(grep AVVIK $LOGG/3_tallvakt.txt)`; skriv på tavla | R | Straks (19:30 senest) |
| `tallsjekk (utgang N): tall uten kilde` | `python3 -I arbeid/verktoy/c1_tallsjekk.py --bare-ikke --feil` viser tallene; `git revert` av tekstcommiten | R | 19:20, ellers R |
| `kv hack_levert mangler` / `ga ingen SCORE` | `uv run python tavle.py levert` viser kv; skriv den ikke om etter 19:00. Hovedtallet står i fremmed.sh-loggen | R, og si ærlig i til-guden at kv-sjekken var rød | 19:30 |
| `HOVEDTALL X fra kald kopi != Y i kv hack_levert` | Modell eller måler endret: behandles som frysvakt (raden over). Aldri endre kv for å få likhet | R (0.476190) | 19:30 |
| `pakk_jury.sh (utgang N): ingen zip` | `tail -20 $LOGG/5_pakk.txt` (oftest død peker / manglende fil i kilder/). `git revert` av siste tekstcommit, kjør på nytt | R | 19:25 |
| `ziptest (utgang N)` eller `HOVEDTALL i zipen != kald kopi` | `tail -30 $LOGG/6_ziptest.txt`. Ny zip er brukket: ikke reparer, lever R | R | Straks |
| `7 tekstavtrykk` | Aldri rødt (bare info/ADVARSEL). Les `TEKSTAVTRYKK:`-linja: listen over endrede filer skal stemme med `git log --since=16:00 --name-only`. Ingen handling | Ny zip er OK | – |
| Tid/maskin tom (ingen grønn etter 19:00) | Lever R med SHA. En sjekket eldre pakke slår en usjekket ny | R | **19:50** absolutt |

**Etter bytte (dommer):** `cp R state/levering/c1_gronn/` hvis den ikke ligger der, `shasum -a 256 >> SHA256.txt`,
`ln -sf <navn> state/levering/c1_gronn/SISTE_GRONNE.zip`, så `uv run python tavle.py til-guden "Case 1 levert: <sti>,
SHA256 <…>, git <HEAD R ble bygd fra>, F1 MOT 0,476190; sluttsjekk 19:00 var RØD på <grunn>, reserve brukt" --av dommer`.
Ærlig: oppgi at R mangler endringene etter at den ble bygd (for nr. 2: JURY_SPORSMAL 14-18).

**Anbefaling nå (før 18:30):** kopier zip nr. 2 til `state/levering/c1_gronn/` (oppgave #2522, smed4), fordi /tmp-mapper
fra mktemp kan forsvinne og ingen står i c1_gronn ennå (sjekket 16:35: mappa finnes ikke).
