# Case 1: stikkprøve av 20 sitater fra hele agenten (#2006, dommer2): 10/20 OK, og 0/10 på MOT-sakene

**Kjøring fra kald start.** `kjor_agent.py` (sha 1a04fe9e0086) er kjørt fra landsbymappen til den tomme mappa `/tmp/d2_2006/ut`, ikke fra smedens mappe. Hovedtallet stemmer: F1 **0,4743** (tp 83, fp 138, fn 46). 119 saker (9,6 %) går til menneske. Sitatlaget er smed3s `agent.py` (sha 5dd8af85ae2f).
**Utvalget.** Skriptet er `arbeid/oppgave_2006/stikk.py`, med seed 2006 og id-ene i `utvalg.json`. Utvalget er lagdelt: 10 tilfeldige av agentens 221 MOT og 10 av 1 025 FOR. Et rent tilfeldig utvalg ville gitt 2 MOT og 18 FOR og skjult feilen.

## Svar
| kontroll | utvalg (20) | hele settet (1 246) |
|---|---|---|
| Sitatet finnes ordrett i kilden (Vanguard US-policy feb 2025, også i SAI) | **20/20** | 1 246/1 246 |
| Sitatet står i punktet det oppgir | 20/20 | 1 246/1 246 |
| Punktet passer til stemmen | 10/20 (FOR 10/10, MOT 0/10) | ca. 1 025 av 1 246 |
| Begrunnelsen passer til saken | 10/20 (FOR 10/10, MOT 0/10) | **MOT 0/221** |
| **Hele raden OK** | **10/20 = 50 %** | vektet etter settet ≈ 82 %, men **0 % av MOT** |

Ingen sitater er diktet opp. Feilen er at sitat og stemme ikke henger sammen.

## Hovedfeilen: sitatet motsier MOT-stemmene
- Modellen (smed2 lgbm) og sitatagenten (smed3) gir hver sin stemme. Sammenslåingen i `kjor_agent.py` tar stemmen fra modellen og sitat og grunn fra sitatagenten. Sitatagenten sier **FOR i 1 246/1 246 saker**. Derfor bærer alle 221 MOT-stemmer sitatet *«… generally will support those that enhance long-term shareholder returns»* og grunnen *«ingen varselsignal i saken»*. Begrunnelsen sier altså det motsatte av stemmen. Kolonnen `sitatagent_anbefaling` viser FOR rett ved siden av MOT.
- Holdout 2026 består bare av Say-on-Pay-saker (kategori `SECTION 14A SAY-ON-PAY VOTES`, 1 246/1 246). Da er ett punkt for alle saker forventet, og det er ikke en egen feil. For MOT finnes det riktige punkter i samme kapittel:
  - `PIII / Say on Pay / ¶3`: lønn og resultat henger ikke sammen → *«a fund may vote against a pay-related proposal»*.
  - `¶4`: strukturfeil → samme formulering.
  - `¶5`: lav støtte over tid → styret må vise at det har tatt hensyn.
  - `¶8–¶18`: varselsignaler.
- Det som faktisk forklarer MOT, står allerede i 90 av 221 MOT-grunner: *«merk: fondet stemte MOT lønnssaken <dato i fjor>»*. Men det står etter «ingen varselsignal», så setningen motsier seg selv.
- 5 av 10 MOT i utvalget er også MOT i fasiten (Maplebear, Netflix, IQVIA, Exelixis, CRISPR). Uansett utfall er begrunnelsen feil for alle 10.

## Andre forbehold
- Kilden er **Vanguards** policy, ikke NBIMs. Fasiten er NBIMs stemmer (`forvalter` NORGES BANK). Juryteksten må si dette, slik #1994 og BEGRENSNINGER pkt. 7 allerede gjør.
- Sitatet er avkortet med «…» før *«It may also vote for compensation proposals that reflect improvements …»*. Det endrer ikke meningen, siden begge delene trekker mot FOR.

## Enkel retting (forslag til smed #1998, før modellfrys kl. 16)
Når modellen sier MOT, skal `kjor_agent.py` ikke bruke sitatagentens FOR-grunn. Bruk i stedet `PIII / Say on Pay / ¶3`, og skriv grunnen som «modellen ser risiko for avvik (p_mot X); fondet stemte MOT i fjor» når den merknaden finnes. Ellers skriv «policy åpner for MOT ved svak lønn/resultat-kobling; må vurderes av menneske». Sett `sitatagent_anbefaling` ≠ `anbefaling` som et synlig flagg. Sjekk deretter på nytt: andel MOT-rader med «ingen varselsignal» skal være 0.

## Tabell (20 saker)
| # | utsteder | agentens stemme | fasit NBIM | ordrett | riktig punkt | begrunnelse passer | rad |
|---|---|---|---|---|---|---|---|
| 1 | Maplebear Inc. | MOT (p 0.3667) | MOT | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR; historikk-merknad om MOT i fjor finnes | **FEIL** |
| 2 | Moderna, Inc. | MOT (p 0.1143, menneske) | FOR | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR | **FEIL** |
| 3 | Neogen Corporation | MOT (p 0.4872) | FOR | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR; historikk-merknad om MOT i fjor finnes | **FEIL** |
| 4 | Netflix, Inc. | MOT (p 0.4872) | MOT | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR; historikk-merknad om MOT i fjor finnes | **FEIL** |
| 5 | Conagra Brands, Inc. | MOT (p 0.3667) | FOR | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR; historikk-merknad om MOT i fjor finnes | **FEIL** |
| 6 | IQVIA Holdings Inc. | MOT (p 0.4872) | MOT | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR; historikk-merknad om MOT i fjor finnes | **FEIL** |
| 7 | Lucid Group, Inc. | MOT (p 0.3667) | FOR | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR | **FEIL** |
| 8 | Exelixis, Inc. | MOT (p 0.7) | MOT | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR | **FEIL** |
| 9 | Mercury Systems, Inc. | MOT (p 0.3667) | FOR | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR; historikk-merknad om MOT i fjor finnes | **FEIL** |
| 10 | CRISPR Therapeutics AG | MOT (p 0.3667) | MOT | ja | nei (¶6 «generally will support»; ¶3/¶4 sier «may vote against») | nei: «ingen varselsignal», sitatagenten sa FOR; historikk-merknad om MOT i fjor finnes | **FEIL** |
| 11 | First American Financial Corporation | FOR (p 0.0303) | FOR | ja | ja (¶6) | ja (generisk) | OK |
| 12 | Mueller Industries, Inc. | FOR (p 0.0172) | FOR | ja | ja (¶6) | ja (generisk) | OK |
| 13 | MercadoLibre, Inc. | FOR (p 0.0152) | FOR | ja | ja (¶6) | ja (generisk) | OK |
| 14 | Yum! Brands, Inc. | FOR (p 0.0303) | FOR | ja | ja (¶6) | ja (generisk) | OK |
| 15 | Allison Transmission Holdings, Inc. | FOR (p 0.0172) | FOR | ja | ja (¶6) | ja (generisk) | OK |
| 16 | IDEX Corporation | FOR (p 0.0152) | FOR | ja | ja (¶6) | ja (generisk) | OK |
| 17 | Stifel Financial Corp. | FOR (p 0.1) | FOR | ja | ja (¶6) | ja (generisk) | OK |
| 18 | Alcoa Corporation | FOR (p 0.0303) | FOR | ja | ja (¶6) | ja (generisk) | OK |
| 19 | Emerson Electric Co. | FOR (p 0.1) | FOR | ja | ja (¶6) | ja (generisk) | OK |
| 20 | BlackLine, Inc. | FOR (p 0.0303) | FOR | ja | ja (¶6) | ja (generisk) | OK |
Kommando: `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/d2_2006/ut && python3 -I arbeid/oppgave_2006/stikk.py /tmp/d2_2006/ut arbeid/hack/varianter/smed3_utf_sitat/rl`
