# Case 1: Vanguards «managementRecommendation» er fasiten, ikke styrets anbefaling (smed2, #1949)

Funnet i votes.csv (Vanguard Index Funds, accession 0001104659-26-102001, 21 474 rader), bekreftet i rå XML
(raw/000110465926102001_proxytable.xml linje ~40265: aksjonærforslaget «Independent Board Chairman»
hos Aflac har howVoted=AGAINST og managementRecommendation=FOR).

Krysstabell kilde × ledelsen × stemme (rader):
- ISSUER, ledelsen=FOR: FOR 19 339, AGAINST 3
- ISSUER, ledelsen=AGAINST: AGAINST 935, WITHHOLD 80, FOR 1
- SECURITY HOLDER, ledelsen=FOR: AGAINST 808
- SECURITY HOLDER, ledelsen=AGAINST: FOR 212

Feltet betyr altså «stemte med ledelsen (FOR) / mot ledelsen (AGAINST)». Det er selve svaret.
Følgen: «følg styret»-baselinen i maaler.py og alle modeller som bruker `ledelsen`/`styret` lekker fasiten.

Løsning (brukt i smed2-kandidaten): ekte styreanbefaling = FOR når kilde=ISSUER, AGAINST når
kilde=SECURITY HOLDER (styret anbefaler nesten alltid mot aksjonærforslag). Kolonnen `ledelsen` må
fjernes fra test_input.csv, og baselinen «følg styret» må bruke denne utledningen.
Sjekk også dette per forvalter hvis andre forvaltere hentes; feltet kan være kodet riktig hos andre.
