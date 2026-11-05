# Case 1 (#2130, speider): sitatkildene. Alle 18 GVG-punkter agenten siterer står ordrett på nbim.no i dag. 8 av 20 gamle begrunnelser avviker fra dagens tekst

**Kort:** Alle 18 unike `retningslinje_id`-sitatene i `agent.csv` står ordrett på nbim.no (hentet 05.11 kl. 12:47) og i PDF-en fra 2024. Det gjelder alle 1 578 rader, og 1 504 av dem er `NBIM 0.0.3`. Vår lokale kopi `punkter.jsonl` stemmer: alle 140 NBIM-GVG-punkter står ordrett på nettsiden. Den andre sitattypen er kolonnen `sitat`: NBIMs egne begrunnelser fra 2020-2025, 20 unike. Av dem stemmer 12 med dagens GVG-tekst og -punkt. **8 avviker**, fordi NBIM skrev dem etter en eldre versjon av retningslinjene. Teksten er ekte NBIM-tekst fra arrangørens `real_train.csv`, men en jurymedlem som slår opp på nbim.no i dag finner den ikke ordrett.

**Metode.** Nettsiden og PDF-en er hentet på nytt med curl (`/tmp/sp2130/raa/`). Sammenligningen normaliserer mellomrom, typografiske apostrofer og orddeling i PDF-en. Skript: `python3 -I arbeid/oppgave_2130/sjekk_kilder.py <gvg.html> <gvg2024.txt> arbeid/hack/c1/retningslinjer/punkter.jsonl arbeid/oppgave_2106/agent.csv` og `sjekk_begrunnelser.py <gvg.html> <gvg2024.txt> <agent.csv>`. Svarfila er `arbeid/oppgave_2106/agent.csv` (smed2 #2106, test 2026), som har `retningslinje_*`-kolonnene. Pakkens `.md`-filer siterer ingen NBIM-punkt-id ordrett. De viser til «GVG 1.1»-begrunnelser (DEMO_MANUS.md:53, JURY_SPORSMAL.md:51), og det er sitattype B under.

**Nummerering.** `prinsipp.delpunkt` er NBIMs egen nummerering: overskriftene «1. Board independence» → «1. Independence of the board» gir 1.1. Ledd-nummeret til slutt (`.2` i 1.1.2) er **vårt** og står ikke på nbim.no. Pakka bør si «NBIM GVG 1.1, 2. avsnitt» eller presisere at leddet er vår telling.

## A. Agentens retningslinjesitat (`retningslinje_id` / `retningslinje_sitat`), 18 unike
Kilde-URL for alle: https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/ (PDF 2024: https://nbim.no/contentassets/01a7ee19b5d84a73a67a365e76a0fb01/global-voting-guidelines2024.pdf)

| sitat | kilde-URL | punkt | stemmer/avviker |
|---|---|---|---|
| NBIM 0.0.3 «Our starting point when deciding how to vote is to support the board. We partici…» | nbim.no GVG | 0.0 «Voting principles», ledd 3 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 1.1.2 «A majority of shareholder-elected board members in a non-controlled company shou…» | nbim.no GVG | 1.1 «1. Independence of the board», ledd 2 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 1.2.1 «Board decisions that are particularly vulnerable to conflicts of interest should…» | nbim.no GVG | 1.2 «2. Independence of main committees», ledd 1 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 1.3.1 «The board should exercise objective judgement on corporate affairs and be able t…» | nbim.no GVG | 1.3 «3. Separation of chairperson and CEO», ledd 1 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 2.1.1 «Board members should devote sufficient time to fulfil their responsibilities eff…» | nbim.no GVG | 2.1 «1. Time commitment», ledd 1 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 2.3.2 «The board should ensure that it can bring a broad range of perspectives and appr…» | nbim.no GVG | 2.3 «3. Diversity», ledd 2 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 3.1.3 «The company should establish reasonable procedures for shareholders to include p…» | nbim.no GVG | 3.1 «1. Board nomination and election», ledd 3 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 3.2.4 «We will also take into consideration unsatisfactory financial and strategic perf…» | nbim.no GVG | 3.2 «2. Board decisions and conduct», ledd 4 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 3.2.13 «We will not support the re-election of a director, or the entire board, if the c…» | nbim.no GVG | 3.2 «2. Board decisions and conduct», ledd 13 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 3.3.2 «A substantial proportion of annual remuneration should be provided as shares tha…» | nbim.no GVG | 3.3 «3. CEO remuneration», ledd 2 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 4.2.1 «Shareholders should in certain circumstances have the opportunity to raise issue…» | nbim.no GVG | 4.2 «2. Shareholder meeting», ledd 1 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 4.3.1 «The right to vote on fundamental changes affecting the company is a basic right…» | nbim.no GVG | 4.3 «3. Governing documents», ledd 1 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 5.1.2 «Excessive non-audit-related fees represent a potential conflict of interest and…» | nbim.no GVG | 5.1 «1. Auditor», ledd 2 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 5.2.1 «The board should use the annual report to present a fair, sensible and clear ass…» | nbim.no GVG | 5.2 «2. Financial statements», ledd 1 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 5.2.4 «We will not support an agenda item if the information disclosed is insufficient…» | nbim.no GVG | 5.2 «2. Financial statements», ledd 4 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 6.2.1 «When evaluating corporate transactions, we will also consider whether there is s…» | nbim.no GVG | 6.2 «2. Mergers, acquisitions and other corporate transactions», ledd 1 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 6.2.5 «Anti-takeover measures are generally not in the interest of shareholders, and th…» | nbim.no GVG | 6.2 «2. Mergers, acquisitions and other corporate transactions», ledd 5 | stemmer ordrett (nett ja, PDF 2024 ja) |
| NBIM 6.3.3 «For each material transaction, the board should disclose the transaction date, t…» | nbim.no GVG | 6.3 «3. Related party-transaction», ledd 3 | stemmer ordrett (nett ja, PDF 2024 ja) |

Sjekket i tillegg: hver rad i agent.csv har nøyaktig samme tekst som punktet i punkter.jsonl (`agent_lik` = sann for alle 18), og ingen id mangler i kilden.

## B. NBIMs tidligere begrunnelser (`punkt` / `sitat`, 74 rader, 20 unike)
Kilde: arrangørens NBIM-stemmedata (`arbeid/hack/c1/data_nbim/real_train.csv`, kolonnen rationale). Teksten sjekket setning for setning mot nbim.no-GVG i dag.

| sitat (begynnelse, eksempel-sak) | kilde-URL | punkt | stemmer/avviker |
|---|---|---|---|
| «Board decisions that are particularly vulnerable…» (Arbonia 2022, 7 rader) | nbim.no GVG | 1.2 | stemmer |
| «Board members should devote sufficient time…» (Lundbeck 2021, 6) | nbim.no GVG | 2.1 | stemmer |
| styrevalg/nominasjon (Aguas Andinas 2022, 7) | nbim.no GVG | 3.1 | stemmer |
| styrets beslutninger (Rain Industries 2025, 1) | nbim.no GVG | 3.2 | stemmer |
| CEO-lønn (Arbonia 2022, 11) | nbim.no GVG | 3.3 | stemmer |
| aksjonærmøte (PACCAR 2020, 1) | nbim.no GVG | 4.2 | stemmer |
| vedtekter (S.F. Holding 2022, 2) | nbim.no GVG | 4.3 | stemmer |
| revisor (Burgan Bank 2025, 3) | nbim.no GVG | 5.1 | stemmer |
| anti-takeover (Tesla 2020, 1) | nbim.no GVG | 6.2 | stemmer |
| uavhengighet + komiteer (Colruyt 2024, 1; Consun 2024, 2) | nbim.no GVG | 1.1 / 1.2 (+1.2/1.3 i samme tekst) | stemmer i innhold, setter sammen flere punkt. Én setning har gammel kommasetting («shareholders, and related») |
| «A majority of shareholder-elected board members…» (Kura Sushi 2021, 10; NMDC 2024, 1) | nbim.no GVG | 1.1 | **avviker i tegnsetting**: «dominant shareholders, and related third parties» mot «…shareholders and related…» i dag |
| «…balance of competencies and backgrounds» (Link & Motivation 2023, 2) | nbim.no GVG | 2.3 | **avviker i ett ord**: i dag «competences» |
| «…failed to act on … sought to circumvent shareholder proposals …» (Telecom Egypt 2024, 1) | nbim.no GVG | 3.2 | **avviker litt**: i dag «a shareholder proposal», «consideration» |
| «The roles of chairperson and CEO should not be held by the same individual. Where a company founder combines both roles…» (LOTTE 2023, 6) | nbim.no GVG | 1.3 | **avviker**: dagens tekst er «We believe shareholders are best served when the chairperson and CEO roles are held by different individuals». Grunnleggerunntaket står ikke lenger der |
| «We will not support an agenda item if the information disclosed is insufficient…» (Aguas Andinas 2020, «Other Business», 8) | nbim.no GVG | 5.2 | stemmer i innhold. I dag fortsetter setningen med «, e.g. …» |
| «…legal action, misstatements or goodwill write-offs…» (Varroc 2025, 1) | nbim.no GVG | 5.2 | **avviker**: i dag «misstatements, material goodwill write-offs, or material legal actions against the board» |
| «Mergers, acquisitions … should maximise shareholder returns. When evaluating…» (TSURUHA 2025, 1) | nbim.no GVG | 6.2 | **avviker**: i dag «We will not support mergers … that do not create long-term value», og 6.2.1 er omformulert |
| «Transactions between related parties should be avoided unless … demonstrably beneficial…» (Burgan Bank 2025, 2) | nbim.no GVG | 6.3 | **avviker**: i dag «carried out on market terms and be clearly beneficial», med ny opplysningsliste (6.3.3) |

**Lesning:** B-sitatene er ekte NBIM-tekst, men de er NBIMs *begrunnelse* fra det året, ikke dagens retningslinje. Pakka må kalle dem «NBIMs begrunnelse <år>», slik `sitat_kilde` allerede gjør, og ikke «GVG-sitat». A-sitatet er det som kan slås opp ordrett i dag.

## C. Andre funn i kilden
- **Versjon.** nbim.no i dag er nyere enn PDF-en fra 2024. 14 av 140 punkter står ikke i PDF-en eller er endret der, blant annet 5.3.7-5.3.10 (nye «will not support»-regler for bærekraftsforslag og Say on Climate), 2.2.3 og 1.3.2-1.3.3 («may not support» for styreleder som også er CEO). Ingen av agentens 18 punkter er berørt. Siter likevel nettsiden med hentedato, ikke PDF-en fra 2024.
- **To feilplasserte lokale id-er (ikke brukt av agenten):** `NBIM 2.3.6` («Internationally agreed standards…») er bildeteksten til et figurbilde på nettsiden, ikke et punkt under 2.3 Diversity. `NBIM 3.3.13` («The protection of shareholder rights…») er innledningen til «Shareholder protection» (før prinsipp 4), ikke 3.3 CEO-lønn.
- Posisjonsnotatene (NBIM-PP) og Vanguard-punktene siteres ikke av agenten i dag og er ikke sjekket her.

## Forslag til smed-oppgaver
1. **(smed2, liten)** I pakka og demoen: merk B-sitatene «NBIMs begrunnelse <år> (eldre GVG-versjon)», og la `retningslinje_sitat` (A) være sitatet som vises som «NBIMs retningslinje». Gjelder DEMO_MANUS.md:53, JURY_SPORSMAL.md:51 og KRAVRESPONS rad 30.
2. **(smed2, liten)** Skriv i README/METODE: «kilde: nbim.no/…/global-voting-guidelines/, hentet 05.11.2026. Punkt = NBIMs prinsipp.delpunkt, siste tall er vår avsnittstelling».
3. **(speider/smed, liten)** Rett `lag_retningslinjer.py`: ta bort `NBIM 2.3.6` (bildetekst) og flytt `NBIM 3.3.13` til `NBIM 4.0.1` (innledning). Agentens prediksjon påvirkes ikke, men BM25 kan i dag treffe dem.
