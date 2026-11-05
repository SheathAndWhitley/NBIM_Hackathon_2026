| test | saker inn | ut | krasj | MOT | FOR | til menneske | uten grunn | sek | merknad |
|---|---|---|---|---|---|---|---|---|---|
| original (nye møte-id) | 6 | 6 | nei | 1 | 5 | 1 | 0 | 6.2 | usikker: kalibrert P(MOT) 0.75 i båndet [0.15, 0.85) |
| tomt felt (tekst/type/selskap/dato) | 6 | 6 | nei | 0 | 6 | 6 | 0 | 5.7 | kan ikke vurderes: mangler felt: company_id; kan ikke vurderes: mangler felt: meeting_date; kan ikke vurderes: mangler felt: proponent; kan ikke vurderes: mangl |
| ugyldige verdier | 8 | 8 | nei | 0 | 8 | 6 | 0 | 5.7 | kan ikke vurderes: ikke heltall: company_id=«abc»; kan ikke vurderes: ikke heltall: item_no=«1.0»; kan ikke vurderes: ikke heltall: item_no=«x»; kan ikke vurder |
| ukjent selskap | 6 | 6 | nei | 1 | 5 | 6 | 0 | 7.1 | ukjent selskap: ingen NBIM-stemmer for selskapet før møtedat; usikker: kalibrert P(MOT) 0.52 i båndet [0.15, 0.85); ukjent |
| ukjent forslagstype | 6 | 6 | nei | 0 | 6 | 6 | 0 | 5.7 | instruksjonslignende tekst i forslaget; ukjent forslagstype ; kan ikke vurderes: mangler felt: proposal_type; ukjent forslagstype «zz», finnes ikke i NBIMs hist |
| lang tekst | 3 | 3 | nei | 0 | 3 | 3 | 0 | 5.1 | instruksjonslignende tekst i forslaget; uvanlig lang tekst (; uvanlig lang tekst (100000 tegn, lengste i historikken 253) |
| injeksjon | 6 | 6 | nei | 1 | 5 | 6 | 0 | 4.9 | instruksjonslignende tekst i forslaget; usikker: kalibrert P(MOT) 0.75 i båndet [0.15, 0.85); instru |
| duplikat-id | 2 | 2 | nei | 0 | 2 | 1 | 0 | 5.9 | kan ikke vurderes: duplikat: 9900042/5 er sett før i samme f |
| kjent sak uendret | 3 | 3 | nei | 1 | 2 | 1 | 0 | 4.7 | usikker: kalibrert P(MOT) 0.75 i båndet [0.15, 0.85) |
| kjent sak, endret tekst/styret | 3 | 3 | nei | 1 | 2 | 3 | 0 | 4.8 | felt avviker fra lagret sak (mgmt_rec); modellen brukte lagr; instruksjonslignende tekst i forslaget; felt avviker fra lag; usikker: kalibrert P(MOT) 0.75 i bån |
| tom fil (bare overskrift) | 0 | 0 | nei | 0 | 0 | 0 | 0 | 4.8 |  |
| manglende kolonne proposal_type | 3 | 3 | nei | 0 | 3 | 3 | 0 | 5.0 | kan ikke vurderes: mangler felt: proposal_type |
| sak: tomt objekt {} | 1 | 1 | nei | 0 | 1 | 1 | 0 | 5.2 | kan ikke vurderes: mangler felt: meeting_id,item_no,company_ |
| sak: null-felt | 1 | 1 | nei | 0 | 1 | 1 | 0 | 5.3 | kan ikke vurderes: mangler felt: meeting_id,item_no,company_ |
| sak: ukjent selskap og type | 1 | 1 | nei | 0 | 1 | 1 | 0 | 4.5 | instruksjonslignende tekst i forslaget; ukjent forslagstype  |
| sak: injeksjon | 1 | 1 | nei | 0 | 1 | 1 | 0 | 4.6 | instruksjonslignende tekst i forslaget |
