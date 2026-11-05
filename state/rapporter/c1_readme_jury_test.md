# Case 1: README fulgt ord for ord som jurymedlem (#2328)

Kopi av `arbeid/hack/levering/` i tom `/tmp/jury2328/`, deretter README.md steg for steg. Kjørt 05.11 ca. 14.42–15.05, før frys.

| steg i README | resultat | avvik / merknad |
|---|---|---|
| `sh arbeid/hack/levering/fremmed.sh /tmp/fremmed` fra kopien av levering/ | **AVVIK** | stien finnes ikke (utgang 127). Med `sh levering/fremmed.sh`: rot blir `/`, «FRYSVAKT RØD» (utgang 4). levering/ alene er ikke selvbærende |
| samme fra landsbymappen | ok | TALLVAKT GRØNN, HOVEDTALL 0.476190, 188 av 1578 til menneske, 31 s |
| `sh arbeid/hack/levering/sjekk_treffsikkerhet.sh` fra kopien av levering/ | **AVVIK** | «AGENTEN FEILET» (utgang 2): leter etter `//arbeid/kandidater/smed2_c1_mot` |
| samme fra roten av kald kopi | ok | TP 30 FP 38 FN 28 TN 1443, STEMMER, sha LIK, 5 s |
| Egne saker `--csv` (i kald kopi) | ok | 2 saker gir agent.csv. Skriver også testtallene for 2026 til skjermen, noe som forvirrer (står nå i README) |
| Egne saker `--sak '{"utsteder": ..., "cusip": ...}'` | **AVVIK** | feil feltnavn. Gir utgang 0, men «kan ikke vurderes: mangler felt», FOR og til menneske. Byttet ut med et eksempel som er prøvd og virker (FOR, NBIM 0.0.3) |
| `bash arbeid/hack/c1/leveranse/kjor.sh` | ok, uklart | F1 0.4762 vises, men siste linje er `SCORE 0.481752` (sidetall). Står nå i README |
| `menneske_tabell.py arbeid/oppgave_2132/agent.csv` | ok | tabellen er lik README. Bare fra landsbymappen |
| `robusthet_frossen.py --ut state/rapporter/c1_robusthet_frossen.md` | **AVVIK (farlig)** | kommandoen skriver over den offisielle rapporten. Endret til `--ut /tmp/c1_robusthet.md`. Kjørt mot /tmp: utgang 0, basis F1 0.4762, 11 s |
| `rare_saker.py --ut DIR` | ok | utgang 0, 20 rader, 95 s. Endret til konkret `/tmp/c1_rare` |
| `svartid.py --n 100` | ikke kjørt | tar ca. 10 min. Dommer #2292 dømmer svartidene |
| lenker: TREFFSIKKERHET.md, kravrespons.md, BEGRENSNINGER.md | ok | finnes i både landsbymappen og den kalde kopien |
| gjenskapingsskripter (2132, 2144, 2257, 2259, menneske_tabell, kjor.sh, demo.sh) i kald kopi | avvik (dokumentert) | kopieres ikke av fremmed.sh, så de virker bare fra landsbymappen. Står nå i README |
| demo/README | uklart | sa ikke hvor `demo.sh` skal kjøres fra. Rettet |

## Rettet (bare tekst, ingen frosne filer)
- README.md: ny boks «Hvor du står»: kjør fra repo-roten, levering/ alene er ikke nok, og hva feilen ser ut som. Et prøvd `--sak`-eksempel med påkrevde felt. kjor.sh-linja forklart. Robusthet skriver til /tmp i stedet for over rapporten. Merknad om at gjenskapingsskriptene bare finnes i landsbymappen.
- demo/README.md: demo.sh kjøres fra landsbymappen.
- Etter endringen gir fremmed.sh fortsatt TALLVAKT GRØNN (17 filer, 166 påstander, 0 avvik). c1_frys sjekk: ikke frosset ennå. Kjører `arbeid/hack/c1/c1_frys.py` gir «finnes ikke»; den ligger i `arbeid/verktoy/`.

## Ikke rettet (forslag)
- Viktigst: får juryen bare `levering/`, virker ingenting. Enten må pakka juryen får være hele repoet, eller så bør fremmed.sh-utdataene (/tmp/fremmed) leveres som en egen zip med README i roten. Dette må den som pakker kl. 19.30 avgjøre (#1972, #2330).
- Målerutskriften sier «ruting (konfidens < 0.6): 183 til menneske». Det er den gamle regelen og stemmer ikke med båndet [0,15; 0,85). Teksten kommer fra måleren, som jeg ikke rører.
- Commit: ikke mulig, fordi arbeid/ og state/ er git-ignorert. Endringene ligger på disk.

## Rettinger etter testen (#2339, 05.11 14.47–14.50)
- `fremmed.sh` og `sjekk_treffsikkerhet.sh`: rotsjekk først. Kjøres de fra `levering/` alene, stopper de nå med
  «FEIL STED: fant ikke repo-roten …», sier hvor man skal stå og viser til README (utgang 6). Før ga de villedende
  «FRYSVAKT RØD» (4) og «AGENTEN FEILET» (2). Ingen av skriptene står i c1_frys.py FILER; agent, modell og data er urørt.
- README.md, boksen «Hvor du står»: beskriver den nye feilmeldingen.
- Tekstrettingene fra #2328 (prøvd `--sak`-eksempel, kjor.sh-linja, robusthet til /tmp, demo/README) står.

Ny gjennomgang i tom mappe (`/tmp/jury2339`, `/tmp/jury2339k`), alt grønt:
| steg | resultat |
|---|---|
| `sh levering/fremmed.sh` fra kopi av bare levering/ | FEIL STED, utgang 6 (klar melding, som ventet) |
| `sh levering/sjekk_treffsikkerhet.sh` samme sted | FEIL STED, utgang 6 |
| `sh arbeid/hack/levering/fremmed.sh /tmp/jury2339k` fra landsbymappen | utgang 0, HOVEDTALL 0.476190, TALLVAKT GRØNN, 35 s (kjørt to ganger, også etter README-endringen) |
| `sjekk_treffsikkerhet.sh` i kald kopi | utgang 0, TP 30 FP 38 FN 28 TN 1443 STEMMER, sha LIK |
| `--sak` (README-eksempelet) i kald kopi | utgang 0, FOR, NBIM 0.0.3 |
| `--csv` (2 saker) i kald kopi | utgang 0, agent.csv med 2 rader |

Står igjen (ikke min avgjørelse): om juryen får hele repoet eller bare /tmp/fremmed som zip (#1972, #2330).
Målerens tekst «konfidens < 0.6: 183» er urørt (måleren er frossen). Ingen commit: arbeid/ og state/ er git-ignorert.
Sikkerhetskopi av skriptene før endring: /tmp/fremmed.sh.f2339, /tmp/sjekk.f2339.
