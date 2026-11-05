# Dom (#2334): praksis-mot-policy-tallene fra smed2 (#2331) HOLDER, to eksempelsaker rettet

**Dom: holder.** Hovedtallene og setningen til kravresponsen er reprodusert fra kald kopi og talt uavhengig. To av fem eksempelsaker var upresise og er rettet i `state/rapporter/c1_praksis_mot_policy.md` (merket der). Speider kan føre tallet inn i jurypakka (#2342).

## Hva jeg gjorde
- Kopierte skript og `state/opplastet/20261105_114241_real_votes.csv` (sha256 71ba5135…) til tom mappe, kjørte med `python -I`. Utskriften er identisk med smed2s `arbeid/oppgave_2331/utskrift.txt`.
- Egen telling uten smed2s kode (pandas, bare kolonnene nbim_vote, mgmt_rec, year, rationale_section).
- Leste alle 82 regelstyrte saker per regel, og de 14 sakene med nøkkelord (poison pill, supermajority, written consent, special meeting) som reglene ikke fanger.

## Tallene i setningen
| påstand | min telling | holder |
|---|---|---|
| regelstyrte 81/82 = 98,8 % | 81/82, eneste avvik Hansa Biopharma 2023 | ja |
| 13 327 saker, samsvar 94,9 % | 13 423 avgitt, minus 96 uten regel og uten styreanbefaling = 13 327; 12 643 samsvar | ja, med presisering |
| fra 2020: 569 MOT mot styret, 99,3 % med GVG-avsnitt | NBIM MOT der styret sa FOR, år ≥ 2020: 569, 565 med GVG (4 uten: Samsung SDI, SFA Semicon, ENCE, Mobimo, alle 2020) | ja |
| 2019 har ingen publiserte begrunnelser | 0 av 1 504 rader i 2019 har rationale_text eller rationale_section | ja |

Presisering gjort: «13 327 avgitte stemmer» var 13 423 avgitte minus 96 uten policy-stemme. Setningen sier nå dette eksplisitt.

Rå «følg styret»-samsvar uten regler er 94,4 % (12 581/13 325). Reglene løfter det 0,5 poeng, så 94,9 % er ikke pyntet av regelvalget.

## Eksempelsakene
1. Hansa Biopharma 2023: holder (FOR på 20 %, MOT på 10 %, FOR/FOR i 2021, 2022, 2024, 2025).
2. TCC Group Holdings: 16 AVSTÅ holder, men de er fordelt 2020/2021/2022 (5/5/6), ikke bare 2020. **Rettet.**
3. H. Lundbeck: 8 AVSTÅ 2020–2024 holder, men «uten begrunnelse» stemte ikke: 6 av 8 har GVG 2.1, bare 2020-paret mangler. **Rettet.**
4. HP 2022, PACCAR 2022, Hartford 2025: holder. Merk at styret også anbefalte MOT, så i skriptets eget mål teller de som samsvar; rapporten sier selv at det er skjønn, ikke regelbrudd.
5. Volkswagen 2019: 31 ansvarsfrihet + 3 valg + 3 revisor holder (pluss 1 aksjeutstedelse som ikke er nevnt), ingen begrunnelse.

## Reglene
Ingen feilfangst i de 82 regelstyrte sakene. Regelsettet er konservativt: det tar ikke med «written consent» (GVG 4.2.4) og «ratify supermajority», men alle de 14 ufangede nøkkelordsakene ville enten gitt samsvar eller er skjønn, så 98,8 % er ikke løftet av utvalget. n = 82 er lite, og rapporten sier det.

## Avgrensning
Tallet sier hvor ofte NBIM stemte som den mekanisk avledede policy-stemmen. Det sier ikke at MOT-stemmene var riktige, bare at nesten alle fra 2020 peker på et GVG-avsnitt. Kravresponsen må holde seg til den formuleringen.
