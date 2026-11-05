# Case 1: robusthet på den endelige pakken fra kald start (#2783, smed3, 05.11 18:51–18:55)

Endelig zip per dommerens #1972 (c1_endelig_pakke_1930.md): `state/levering/c1_gronn/SISTE_GRONNE.zip` ->
`jurypakke_c1_1827_0e3b14b.zip`, sha256 98257a6e198fc617…1aae3c3. Sjekket kl. 18:53: ingen nyere zip i state/levering,
SISTE_GRONNE peker fortsatt på denne. Kald mappe `/tmp/rob2783`: unzip, frysvakt (19 filer GRØNN), `uv sync --frozen`
fra zipens uv.lock, agenten kjørt som KJOR.sh gjør (`env -i`, zipens .venv) men med `--csv <dårlig fil>`.
Skript: `sh arbeid/oppgave_2774/robust_zip.sh state/levering/c1_gronn/SISTE_GRONNE.zip /tmp/rob2783` (1 min).
Måling: zipens `maaler_offisiell_v3.py ... test --data real --score mot` på `ut/pred_maaler.csv`.

Akseptkrav: forståelig feilmelding eller samme 0,512, ingen stacktrace.

| Test | Hva er galt | Exit | Traceback | Utfall | F1 MOT (v3) | Godkjent |
|---|---|---|---|---|---|---|
| tom.csv | 0 byte | 0 | nei | «advarsel: inn-fila har ingen saker (bare overskrift); skriver tom agent.csv», 0 rader | nan (måleren, ingen rader) | ja |
| bare_overskrift.csv | bare kolonnelinja | 0 | nei | samme advarsel, 0 rader | nan | ja |
| uten_proposal_text.csv | kolonnen proposal_text mangler | 0 | nei | 1578 rader, alle til menneske («1578 som ikke kunne vurderes»), per rad «mangler felt: proposal_text», anbefaling = styret | 0,000 (ingen MOT-flagg, forventet) | ja |
| uten_mgmt_rec.csv | kolonnen mgmt_rec mangler | 0 | nei | ingen advarsel (valgfritt felt, mgmt_rec_raw brukes), 1578 rader | **0,512** | ja |
| latin1.csv | fila lagret som latin-1 (æøé) | 0 | nei | «advarsel: inn-fila er ikke UTF-8-tekst (invalid continuation byte, byte 203); prøver latin-1», 1578 rader; pred_maaler.csv sha d02cf88475bfee93 = frysen | **0,512** | ja |
| binaer.csv | 51 kB vilkårlige bytes | 0 | nei | UTF-8-advarsel, 400 «saker» alle til menneske som ikke kunne vurderes | nan (ingen gyldig id) | ja |

Resultat: 6 av 6 godkjent, identisk med #2755 (samme zip) og #2774. Ingen krasj, ingen traceback, ingenting å melde dommer.
Ingen endring gjort i pakken (modellfrys, etter 19:00-regelen).

Detalj: uten_mgmt_rec gir samme F1 som frossen, men pred_maaler.csv er ikke byte-identisk med frysen
(1378 rader ulike, 0 ulike i id/flagg): mgmt_rec inngår i trekk, så p-verdiene flytter seg litt uten at flaggene gjør det.

Hvis dommer legger en nyere zip (tekststopp #2549) i state/levering/c1_gronn/ før 19:30, kjør samme skript på den
og legg tabellen under her. Logger: `/tmp/rob2783/logg_*.txt`, ut: `/tmp/rob2783/ut_*/`.
