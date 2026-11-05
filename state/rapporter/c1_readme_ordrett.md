# Case 1: README i jury-zipen fulgt ordrett på tom mappe (#2416, smed2, 05.11 ca. 15.45)

**Resultat: GRØNN.** Alle stegene i rot-README virker som skrevet. HOVEDTALL F1 MOT = **0.476190**.

## Slik ble det gjort
- Zip bygd med `pakk_jury.sh` (den offisielle byggeren; bruker samme fremmed.sh-kjøring som jurypakke.py-oppskriften),
  i egne mapper: `C1_JURYBYGG=/tmp/s2_2416_bygg C1_JURYSTAGE=/tmp/s2_2416_stage sh arbeid/hack/levering/pakk_jury.sh /tmp/s2_2416.zip`
  -> 1,0 MB, 99 filer. Merk: bygd før kl. 16, så FROSNE_SHA256 er dagens filer («ikke frosset ennå»).
- Kopiert som `jurypakke_c1.zip` til tom `/tmp/s2_jury`, kjørt under `env -i` med egen HOME og PATH=/opt/homebrew/bin:/usr/bin:/bin
  (bare uv + system). uv-cachen på minien var varm (nedlasting ikke testet, se #2412).
- Ingen loggfil nevner <repo> (0 treff i steg 1–3, steg 4 og agentloggen).

## Steg for steg (linjenummer i rot-README.md i zipen)
| linje | steg | utfall |
|---|---|---|
| 13–15 | `unzip`, `cd c1_stemmeagent`, `sh KJOR.sh` | utgang 0. FRYSVAKT GRØNN (15 filer), HOVEDTALL 0.476190, TALLVAKT GRØNN. uv sync 1 s, kjøring 48 s |
| 23–24 | SCORE-linjer 0.481752, `ut/agent.csv` | stemmer; agent.csv har anbefaling, sitat, til_menneske |
| 26–28 | `sh arbeid/hack/levering/sjekk_treffsikkerhet.sh /tmp/c1_sjekk` | utgang 0. TP 30 FP 38 FN 28 TN 1443 STEMMER, sha256 LIK |
| 31 | `.venv/bin/python arbeid/hack/levering/kjor_agent.py --help` | virker |
| leveranse/README.md 52 | `uv run --project arbeid/kandidater/smed2_c1_mot ... --ut <mappe>` (sier «i repoet», men virker også i zipen) | utgang 0, samme SCORE 0.481752 |

## Småting som kan forvirre en fremmed (ingen er feil i kjøringen)
1. **README linje 23:** utskriften har også linja `IKKE HOVEDTALL ... {'F1': 0.5 ...}` før HOVEDTALL. README nevner bare SCORE-linjene.
   En jury kan lese «F1 0.5». Forslag: «Linja som starter med IKKE HOVEDTALL er en sjekk med test-fordelingen, ikke resultatet.»
2. **README linje 31 (Egne saker):** bare `--help`. Første naturlige forsøk med `"meeting_id":"X1","company_id":"C9"` gir
   `til_menneske=1`, «kan ikke vurderes: ikke heltall» (pent håndtert, men --help sier ikke at id-ene må være heltall).
   Med heltall virker det: `--sak '{"meeting_id":9000001,"item_no":3,"company_id":537900,"meeting_date":"2026-05-01","proposal_text":"Shareholder Proposal Regarding Report on Climate Lobbying","proposal_type":"SHAREHOLDER","proponent":"Shareholder","mgmt_rec":"AGAINST","country":"United States","market":"DM"}'`
   -> P(MOT) 0,52, til menneske, GVG 5.3.1. Forslag: legg ett slikt eksempel under linje 31.
3. **README linje 13:** forutsetter at fila heter `jurypakke_c1.zip` (standardnavnet i pakk_jury.sh). Lever med det navnet.
4. **README linje 9:** nedlasting på 1,5 GB uten cache er ikke testet her (varm cache); uten nett ble bevist i #2412.

## Neste
Kjør samme test på den endelige zipen etter frysen kl. 16 (da skal pakk_jury.sh sjekke sha256 mot state/c1_frys.json).
Kommando for gjentakelse: se «Slik ble det gjort» over; steg 1–3 i `env -i ... sh -c 'unzip -q jurypakke_c1.zip && cd c1_stemmeagent && sh KJOR.sh'`.
