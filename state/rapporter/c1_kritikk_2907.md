# Case 1 (#2917): kritisk lesing av forklarings-kandidaten #2907. GRØNN, ingen linjer må endres før 02:00

Arkitekt, 05.11 ca. 20:25. Kode lest: `arbeid/oppgave_2907/v2f_rull.py` (diff mot `hack/c1/leveranse/verktoy/v2_rull.py`) og `maal.sh`.
Regel: `c1_trekkliste_forklaringer.md` (strengt før dato, aldri år > til_aar, gjelder også treningsrader).

## Dom: GRØNN
| sjekk | resultat |
|---|---|
| Lekkasjetest #2915 på K3 (`--grunn 1,2,3,4`), år 2023–2026 | A egen dag: lekk −0,017 / −0,005 / −0,019 / +0,0005, 0 flagg snudd. B permutasjon: F1avvik 0,045 / 0,054 / 0,056 / 0,049 mot tilfeldig 0,059 / 0,036 / 0,063 / 0,039. **SAMLET GRØNN** |
| Uavhengig brute-force av trekk 1–4 (egen løkke, ikke kodens `merge_asof`), til_aar=2025, 2000 tilfeldige rader 2019–2026 (også treningsrader) | **0 avvik**. Rader med trekk > 0: 19 / 253 / 36 / 3 |

KP: #2915-testen er kjent RØD på to lekke kontroller og GRØNN på v2av (fra #2915). På K3: forventet GRØNN, fikk GRØNN.
Brute-force: forventet 0 avvik hvis koden følger regelen, fikk 0.

## Linje for linje (v2f_rull.py)
- **L71–78:** `rationale_section` leses bare inn i `RS` og brukes bare i `grunn_feats`. Den kommer aldri inn i `X`/`BRUKT`. Lekktest-greinene (L76, L78) er av når `--lekktest 0`. OK.
- **L82–88 `_asof`:** samme mønster som `hist_feats --hist 2`: `dropna` fjerner rader uten etikett, kumulativ sum per nøkkel og `merge_asof(..., allow_exact_matches=False)`. Det gir strengt før dato, så samme møte og samme dag er utelukket. OK.
- **L92 `lab = ok & year <= til_aar`:** stemmer med regelen. Ved valg på val (til_aar = T−1) ser ingen rad etiketter fra teståret. Treningsrader ser bare tidligere møter, aldri sin egen rad. OK, bekreftet av brute-force.
- **L93 `ind`:** `RS.isin(S) & y==1`, NaN utenfor `lab`. OK.
- **L95–98 trekk 1, 2, 3, 5:** nøkkel `person`/`CID`, maskert til riktig sakstype etterpå. Personnøkkelen er den samme `_navn()` som repoets `person`. OK.
- **L99–102 trekk 4:** bruker bare SAY_ON_PAY-etikett for (selskap, år−1), aldri forklaringen og aldri samme år. Hele fjoråret ligger før enhver dato i år. OK.
- **L106–108 `_GC`-cache:** nøkkelen er bare `til_aar`. Det holder, siden `RS` og `a.grunn` er faste i én kjøring. OK.
- **L133 og L142:** trekkene går inn i både LR- og LGBM-matrisen med samme `til_aar` som `hist_feats`. OK.

## Ikke lekkasje, men verdt å vite (ingen må fikses før 02:00, siden #2907 ikke er kandidat)
1. **Vakt-året 2023 er tilpasset på seg selv.** `maal.sh` tar 2023 fra `v2_2024_val.csv`. Den fila skrives med `pv_all` og grensen `t`, som er valgt for best F1 *på 2023* (L166–171, L186). Tallet for 2023 er dermed optimistisk, både for v2+av (0,3723) og for K1–K3. Sammenligningen mellom dem er rettferdig, fordi begge har samme skjevhet. Absoluttnivået og avstanden til frossen 2023 er det ikke. Dommeren bør vite dette når 2023 brukes som vakt (intet år −0,02).
2. **Docstringen (L7–8) sier fortsatt at `rationale_section` er forbudt.** `FORBUDT`-asserten (L29) dekker bare `BRUKT`, så den sier ikke ifra. Skal koden noen gang til juryrepoen, må L7–8 nevne `HIST_GRUNN` («lest bare fra tidligere møter»), ellers ser det ut som et regelbrudd. Utskriften på L74 gjør dette allerede i loggen.
3. **Steg 2 i byggeoppskriften (`--lekktest 1`, NaN for hele teståret, byte-like) er feil spesifisert.** Med `--hist 2` skal trekkene bruke forklaringer fra tidligere møter samme sesong, så testen må gi avvik. Smeden gjorde rett i å bytte til `--lekktest 2`. Til neste gang bør oppskriften peke på `c1_lekkasjetest.py`.
4. Effekt (ikke lekkasje): K1–K3 ligger −0,005 til −0,002 under v2+av. Ablasjonen #2919 (S4 0,5601, A-1 0,5604, selvrapportert) ligger også innenfor frøstøyen (sd ≈ 0,005 fra #2911). Det er ingen grunn til å gjenåpne sporet.

## Anbefaling til natt-dommen (#2874)
#2907 er lekkasjefri, men har ingen gevinst. Den skal ikke være kandidat. Ingen kodeendring trengs før 02:00.
Tar en senere kandidat i bruk `grunn_feats`, kan dommeren gjenbruke kommandoene under.

Kommandoer: `arbeid/oppgave_2917/lekktest_K3.txt` (full utskrift), `arbeid/oppgave_2917/brute.py` (kjøres etter
`v2f_rull.py <data> --hist 2 --testaar 2025 --grunn 1,2,3,4 --lekktest 3` i samme mappe).
