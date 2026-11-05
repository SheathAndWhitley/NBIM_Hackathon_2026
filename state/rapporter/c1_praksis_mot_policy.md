# Case 1 (#2331, smed2): følger NBIM sine egne retningslinjer? Praksis mot policy i tall

**Setning til kravresponsen:** Der NBIMs Global Voting Guidelines gir en regel som kan avgjøres fra saksteksten alene, stemte NBIM som regelen tilsier i 81 av 82 saker (98,8 %). Over de 13 327 avgitte stemmene 2019–2026 der policy-stemmen kan avledes (13 423 avgitt, 96 uten regel og uten styreanbefaling) er samsvaret 94,9 %, og fra 2020 viser 99,3 % av de 569 MOT-stemmene mot styret til et eget GVG-avsnitt (2019 har ingen publiserte begrunnelser).

Skript: `uv run python arbeid/oppgave_2331/praksis_mot_policy.py`, utskrift i `arbeid/oppgave_2331/utskrift.txt`. Bare lesing og telling av `state/opplastet/20261105_114241_real_votes.csv` (samme ekte stemmer som agenten), ingen modell, frossen #2044 er ikke rørt.

## Hvordan policy-stemmen settes
- **Regelstyrt (82 saker):** et «We will (not) support»-punkt i GVG som kan avgjøres fra forslagsteksten, forslagsstilleren og markedet: 5.2.4 («other business» → MOT), 6.1.5/6.1.6 (utstedelse uten fortrinnsrett over 20 % DM / 30 % EM → MOT, ellers FOR), 6.2.7 (poison pill → MOT), 6.2.8 (fjerne anti-takeover/supermajoritet → FOR), 3.1.4/3.1.5 (staggered/declassify), 1.3.5 (skille styreleder og CEO → FOR), 3.1.8 (flertallskrav → FOR), 3.1.11 (proxy access → FOR).
- **Utgangspunkt (13 245 saker):** NBIM 0.0.3 «Our starting point when deciding how to vote is to support the board», så policy-stemmen er styrets anbefaling.
- Tatt ut: 334 saker uten avgitt stemme (Do Not Vote, frekvensvalg) og 96 uten regel og uten styreanbefaling (brasilianske stemmeseddelspørsmål). AVSTÅ teller som avvik.

**Les tallet ærlig:** 94,9 % er høyt fordi utgangspunktet er «støtt styret». Det er nettopp de 5 % avvikene som er casen. Den egentlige policytesten er de regelstyrte sakene (98,8 %) og om MOT-avvikene har en GVG-begrunnelse.

## Per forslagstype (de 12 største)
| forslagstype | saker | samsvar med policy | regelstyrte (samsvar) | avvik MOT | avvik AVSTÅ | avvik FOR | MOT-avvik med GVG-begrunnelse |
|---|---:|---:|---:|---:|---:|---:|---:|
| DIRECTOR_ELECTION | 6543 | 94,6 % | 0 | 336 | 18 | 1 | 88 % (294/336) |
| AUDITOR | 1091 | 97,7 % | 0 | 25 | 0 | 0 | 80 % (20/25) |
| FIN_STATEMENTS | 816 | 99,0 % | 0 | 4 | 4 | 0 | 75 % (3/4) |
| DISCHARGE | 759 | 85,0 % | 0 | 114 | 0 | 0 | 73 % (83/114) |
| DIVIDEND | 650 | 99,2 % | 0 | 0 | 5 | 0 | - |
| OTHER_MGMT | 620 | 94,5 % | 7 (100 %) | 34 | 0 | 0 | 97 % (33/34) |
| SAY_ON_PAY | 550 | 91,8 % | 0 | 45 | 0 | 0 | 87 % (39/45) |
| DIRECTOR_PAY | 379 | 99,5 % | 0 | 2 | 0 | 0 | 50 % (1/2) |
| EQUITY_PLAN | 375 | 98,1 % | 0 | 7 | 0 | 0 | 71 % (5/7) |
| ARTICLES | 337 | 89,9 % | 0 | 28 | 5 | 1 | 100 % (28/28) |
| SHARE_ISSUANCE | 334 | 97,9 % | 13 (92 %) | 6 | 1 | 0 | 83 % (5/6) |
| ROUTINE | 311 | 99,0 % | 0 | 0 | 3 | 0 | - |

Per regel: 5.2.4 «other business» 44/44 MOT, 6.2.8 13/13, 6.1.5 12/13, 3.1.5 5/5, 1.3.5 3/3, 6.2.7 2/2, 3.1.8 1/1, 3.1.11 1/1.

MOT-avvik uten GVG-begrunnelse er **bare 2019** (92 MOT, 0 % med begrunnelse; 2020: 94 %, 2021–2026: 100 %). Det er hull i hva NBIM publiserte i 2019, ikke stemmer uten grunnlag. De lavere andelene i tabellen (DISCHARGE 73 %) kommer derfra.

## Konkrete saker der praksis avviker fra policy
1. **Hansa Biopharma 2023 (Sverige):** FOR utstedelse av inntil 20 % uten fortrinnsrett (hovedforslag), men MOT alternativet på inntil 10 %. GVG 6.1.5 setter grensen ved 20 % i DM, og samme par fikk FOR/FOR i 2021, 2022, 2024 og 2025. Det eneste regelstyrte avviket, og det er ikke internt konsistent.
2. **TCC Group Holdings 2020–2022 (Taiwan):** AVSTÅ på 16 rutinesaker (regnskap, utbytte, vedtekter; 5+5+6 over tre år) der styret anbefalte FOR. GVG har bare «support / not support», ingen avstå-regel, og ingen begrunnelse er publisert.
3. **H. Lundbeck 2020–2024 (Danmark):** AVSTÅ på 8 gjenvalg av styremedlemmer (Holmqvist, Levin, Rasmussen) år etter år. 6 av 8 viser til GVG 2.1 (styrets sammensetning), de to fra 2020 har ingen begrunnelse. Policyen sier enten støtte eller ikke støtte, så avståelsen er avviket, ikke mangel på grunn.
4. **HP 2022, PACCAR 2022, The Hartford 2025:** MOT aksjonærforslag om lavere terskel for å kalle inn ekstraordinær generalforsamling, uten publisert begrunnelse. GVG 4.2 er positiv til aksjonærers rett til å kalle inn møter (4.2.4 støtter skriftlig vedtak ved 50 %), men har ingen tallgrense for innkalling. Dette er et skjønn som går mot aksjonærrettighetene policyen ellers støtter, ikke et brudd på en konkret regel.
5. **Volkswagen 2019:** MOT ansvarsfrihet for 31 styremedlemmer (pluss 3 valg og 3 revisorsaker), uten publisert begrunnelse. Innholdet passer GVG 3.2.10 (ansvarsfrihet nektes ved alvorlig uro over styrets handlinger og søksmål), så dette er et dokumentasjonshull, ikke et avvik i sak.

## Avgrensning
- De fleste MOT-reglene (uavhengighet, oppmøte, mangfold, lønnsstruktur) trenger fakta som ikke står i dataene. De sakene havner under «utgangspunkt», så et MOT der regnes som avvik fra utgangspunktet selv om det kan følge en regel. Kolonnen med GVG-begrunnelse viser at det gjelder nesten alle.
- Regex-reglene er satt opp for hånd. Dommeren (#2334) reproduserte skriptet fra kald kopi, talte uavhengig og spotsjekket alle regelstyrte saker: holder. Eksempel 2 og 3 og 13 327-setningen er rettet av dommeren etter dom, se state/rapporter/c1_praksis_dom.md. Regelstyrte saker: n = 82, så 98,8 % hviler på få saker.
