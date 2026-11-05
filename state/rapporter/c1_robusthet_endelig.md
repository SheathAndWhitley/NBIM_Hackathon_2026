# Case 1: dårlige inndata mot den ENDELIGE jury-zipen fra kald kopi (#2803, smed3, 05.11 kl. 19:35)

Pakke: `state/levering/c1_gronn/jurypakke_c1_1902_cbae393.zip` (sha256 e6dae4988dbd2056…), den dommeren pekte ut som
endelig i #1972. Kald kopi: zipen kopiert til tom mappe `/tmp/c1_2803`, pakket ut, FRYSVAKT GRØNN (sha256 mot
FROSNE_SHA256.txt), eget miljø med `uv sync --frozen`. Hver inn-fil kjørt med kopiens eget python under `env -i`:
`kjor_agent.py --csv <fil> --ut <mappe>`. Inn-filene er bygd av de fem første radene i kopiens real_test_input.csv.
Skript: `arbeid/oppgave_2803/robusthet_endelig.py`. Ingen frosne filer endret (git status tom for levering/oppgave_2044).

| inndata | oppførsel | exit |
|---|---|---|
| tom fil (0 byte) | `advarsel: inn-fila har ingen saker (bare overskrift); skriver tom agent.csv`. agent.csv med bare overskrift. | 0 |
| bare overskrift | samme som over | 0 |
| ikke-UTF-8: latin-1 med æøå (5 saker, kjente id-er) | `advarsel: inn-fila er ikke UTF-8-tekst (invalid continuation byte …); prøver latin-1`. 5 rader, alle til menneske: «instruksjonslignende tekst i forslaget; felt avviker fra lagret sak (proposal_text)». æøå skrevet riktig tilbake i agent.csv (utf-8). Anbefaling FOR = styret, P(MOT) 0,0. | 0 |
| ikke-UTF-8: UTF-16 med BOM | leses som latin-1, blir 12 «rader» med tull. Alle til menneske: «kan ikke vurderes: mangler felt: meeting_id,item_no,company_id,…». Ingen sak avgjort. | 0 |
| ikke-UTF-8: tilfeldige bytes (0–255 ×4) | leses som latin-1, 8 «rader» med tull, alle til menneske med «mangler felt». | 0 |
| manglende kolonne proposal_text | 5 til menneske: «kan ikke vurderes: mangler felt: proposal_text». Anbefaling = styrets. | 0 |
| manglende kolonne mgmt_rec | 5 til menneske: «felt avviker fra lagret sak (mgmt_rec); modellen brukte lagret rad». | 0 |
| manglende kolonner id, company_id, meeting_date | 5 til menneske: «mangler felt: company_id,meeting_date» (id lages fra meeting_id\|item_no). | 0 |
| bare kolonnen id | 5 til menneske: «mangler felt: meeting_id,item_no,company_id,…». | 0 |
| ikke CSV (JSON-tekst) | tolkes som overskrift uten rader: samme advarsel som tom fil, tom agent.csv. | 0 |

Ingen av de ti kjøringene krasjet (ingen traceback, exit 0 på alle). Alt som ikke kan vurderes går til menneske med
forklart grunn, og anbefalingen faller tilbake på styrets. Samme oppførsel som i #2716/#2380 på den frosne koden,
pluss latin-1-fallbacken fra #2724 (c1_real.py linje 150–154), som nå er bekreftet i den endelige zipen.

## To ærlige merknader (ikke feil, ikke rettet: koden er frosset)
- Binært/UTF-16 gir ikke «pen feil» slik kommentaren i koden lover, men tull-rader som alle rutes til menneske. Utfallet
  er trygt (ingen sak avgjort), men meldingen sier «mangler felt» i stedet for «fila er ikke tekst».
- Norsk tekst flagges fortsatt som «instruksjonslignende» (vokabular-kuttet i injeksjon_hoflig.py, se #2716), ikke som ukjent språk.

## Reproduksjon
    D=/tmp/c1_x; mkdir -p $D && cp state/levering/c1_gronn/jurypakke_c1_1902_cbae393.zip $D/ && cd $D && unzip -q *.zip && cd c1_stemmeagent
    shasum -a 256 -c -q FROSNE_SHA256.txt && UV_PROJECT_ENVIRONMENT=$PWD/.venv uv sync --frozen --no-install-project -q
    python3 -I <repo>/arbeid/oppgave_2803/robusthet_endelig.py $D/c1_stemmeagent
