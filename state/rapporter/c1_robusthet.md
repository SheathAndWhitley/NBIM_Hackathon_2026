# Case 1: robusthetstest av den frosne agenten på ødelagt input (#2716, smed3)

Kjørt 05.11 kl. 18:12–18:18 fra kald kopi i /tmp (bygd med fremmed.sh sin filliste, 21 frosne filer
med frysens sha256 fra state/c1_frys.json 17:18:18, eget uv-miljø, `env -i`). Koden er ikke endret.
Hver inn-fil kjørt med `kjor_agent.py --csv <fil> --ut <mappe>`. Inn-filene er laget av de fem første
radene i test 2026 (Fraser & Neave, møte 2031740).

| input | hva som ble gitt | oppførsel | exit |
|---|---|---|---|
| tom fil (0 byte) | `01_tom.csv` | `advarsel: inn-fila har ingen saker (bare overskrift); skriver tom agent.csv`. agent.csv med bare overskrift. | 0 |
| bare overskrift | `01b_bare_overskrift.csv` | samme som over | 0 |
| manglende kolonne | `proposal_text` fjernet, 5 saker | alle 5 til menneske: `kan ikke vurderes: mangler felt: proposal_text`. Anbefaling = styrets (FOR), P(MOT) tom. | 0 |
| ukjent selskap | company_id 999999999, meeting 9999999 | til menneske: `ukjent selskap: ingen NBIM-stemmer for selskapet før møtedatoen`. De to kjente sakene i samme fil svart normalt (FOR, P 0,007 / 0,000). | 0 |
| dublett-id | sak 2031740\|1 to ganger | første kopi svart normalt (FOR, P 0,000); andre til menneske: `kan ikke vurderes: duplikat: 2031740\|1 er sett før i samme fil`. | 0 |
| tekst med æøå, kjent id | «Godkjenn årsregnskapet og styrets forslag om utbytte på kr 3,50 pr. aksje – Blåøyd Fjørfe ASA» på 2031740\|1 | til menneske: `instruksjonslignende tekst i forslaget; felt avviker fra lagret sak (proposal_text)`. æøå skrevet riktig tilbake i agent.csv (utf-8). | 0 |
| tekst med æøå, ny id | to norske forslag på nytt møte 9999998 | begge til menneske med `instruksjonslignende tekst i forslaget`, anbefaling FOR = styret. | 0 |

Ingen av de sju kjøringene krasjet (ingen traceback, exit 0 på alle). Alt som ikke kan vurderes går til
menneske med grunn, og anbefalingen faller tilbake på styrets.

## Funn som juryen bør høre fra oss, ikke oppdage selv

Norsk tekst flagges som «instruksjonslignende». Det er ikke vern.py (engelske instrukser) eller
EKSTRA_INJ-regexen som slår til, men injeksjon_hoflig.py: den bygger vokabular av NBIMs historikk (engelsk)
og kutter teksten der ordene blir ukjente. Målt direkte i kald kopi:
- «Godkjenn årsregnskapet» alene: ikke flagget
- «Godkjenn årsregnskapet og styrets forslag om utbytte …»: kuttet ved posisjon 9 (etter «Godkjenn»)
- «Velg Kåre Bø som styremedlem»: kuttet ved posisjon 13
- «Approve dividend of kr 3,50 per share» (engelsk, men «kr 3,50» er ukjent): kuttet ved posisjon 8

Konsekvens: fremmedspråk og tall-/valutaformat utenfor historikken går til menneske, som er riktig
utfall, men rutingsgrunnen sier «instruksjonslignende tekst» der den burde sagt «ukjent språk/vokabular».
Modellen ser bare den kuttede teksten («Godkjenn», «Velg»), og P(MOT) blir 0,0. Ingen sak ble stille
avgjort av modellen. Ikke rettet: koden er frosset.

## Én setning til juryen

Agenten krasjer ikke på tom fil, manglende kolonne, ukjent selskap, dublett eller norsk tekst: hver sak
som ikke kan vurderes går til et menneske med en forklart grunn, og anbefalingen faller tilbake på
styrets, målt fra kald kopi av den frosne pakka etter frysen kl. 17:18.

## Reproduksjon

    sh arbeid/hack/levering/fremmed.sh /tmp/kald   # eller pakk ut jury-zipen
    cd /tmp/kald && .venv/bin/python arbeid/hack/levering/kjor_agent.py --csv <ødelagt.csv> --ut /tmp/ut_x

Inn-filene ble laget av de fem første radene i arbeid/hack/c1/data_off/real_test_input.csv
(skript i rapportens kjøring, /tmp-kopiene er ryddet etter oppgaven).
