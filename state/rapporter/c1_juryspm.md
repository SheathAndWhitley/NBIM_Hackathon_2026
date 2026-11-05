# Case 1: ti vanskelige jury-spørsmål med ærlige svar fra målte tall (#2318, arkitekt)

Gjelder levert agent = frossen #2044 miks h2 (`levering/kjor_agent_real_maskin_alene.csv`, forsøk #1046), test 2026 på real_votes.
**KP:** forventet 0,476190 (#2242), fikk `SCORE 0.476190`, TP 30 FP 38 FN 28 av 58 MOT
(`python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/hack/levering/kjor_agent_real_maskin_alene.csv test --data real --score mot`, sha 418a937e57, kjørt 14:40).
Hvert svar har maks 3 setninger og en kilde. India-svaret (6) må snus hvis dommer #2297 / paret test #2311 tar regelen inn før kl. 16.

**1. Har dere lekkasje fra fasit inn i modellen?**
Forbudte felt (`nbim_vote*`, `rationale_*`, `funds_disagree`, `position_paper`) stoppes med assert i `oppgave_2044/train.py`; `position_paper` ble tatt ut fordi den var 97,5 % MOT når satt. Sakstypen lekker ikke: uten den gir test 0,500 mot 0,476, differanse +0,024 [−0,012; +0,062] (#2103, forsøk #1108/#1109). Kilde: `c1_lekkasje_v3.md`.

**2. Er tidssplitten ekte, eller har dere tunet på 2026?**
Trening ≤ 2024, C og grense (0,9188) valgt på val 2025, test 2026 kjørt én gang med låst grense (`oppgave_2044/train.py`, `c1_lekkasje_v3.md`). Bedre testtall vi så i ettertid ble ikke tatt inn: «uten sakstype» 0,500 (#1109) og t4e 0,529 (#1033) ble valgt bort fordi de ikke vant på val (#2103, #2242). Frysvakta tar sha256 av modell, prediksjoner og agent kl. 16 (#2142).

**3. Hvorfor er F1 på MOT bare 0,476?**
MOT er sjeldent: 58 av 1539 saker i test (3,8 %), og «følg styret» gir F1 0 (v3-måleren over). Bommene samler seg: hele styrer straffes i ett møte, selskaper med bare FOR før gir 0 av 7 truffet, og India ga 0 av 14 på val (`c1_feilanalyse_mot.md`, #2067). 17 av de 28 bommene har agenten P(MOT) under 0,09, så de er modellens bom og ikke noe en terskel fikser (#2293).

**4. Hvor sikkert er tallet?**
95 % KI er [0,36; 0,59] med klyngebootstrap over selskaper, og val 2025 er 0,520 [0,41; 0,63] (#2095, `c1_lekkasje_v3.md`). Med 58 MOT er «rundt 0,5 ± 0,12» den ærlige lesningen. Forskjellen 2025→2026 er innenfor støy, og årsaken er ikke målt (JURYSVAR spm. 9).

**5. Er agenten bedre enn følg styret, når treffprosenten er lavere?**
Treffprosent 95,39 % mot 95,71 % for følg styret, men følg styret finner 0 MOT og agenten 30 av 58 (#2220, #2242, v3 over). Mot den sterkeste enkle regelen (b2, samme selskap og tekst fikk MOT før, 0,365) vinner modellen +0,11 [0,01; 0,22] parret (#2134, `c1_enkle_regler_og_hist1.md`).

**6. India-regelen ble funnet på val. Er ikke det å tilpasse til val?**
Jo: regelen (styreleder = daglig leder i India) løfter val 2025 fra 0,520 til 0,562, men den ble funnet ved å lese val-bommene, så det tallet er optimistisk (#1156, `c1_india_bryter.md`). På holdt-ut 2024 er gevinsten 0,536 → 0,544 med v3, og den hviler på én snudd sak (`c1_india_bryter.md`, #2303; 0,5743 i #1157 er intern avviks-F1, ikke v3 MOT). Derfor er den ikke i levert agent før paret test (#2311) og dommer #2297 sier ja, og vi har ikke sett på 2026 med regelen.

**7. Hvorfor ikke ta inn flere trekk som ga mer på val?**
Kravet vårt er «bedre begge år»: tiltak 1 ga +0,026 på 2025 men −0,015 på 2024, og person-trekkene alene +0,007 / −0,018, så sporet er lukket (`c1_tiltak1_person_ablasjon.md`, #2296). Ingen del vant begge år.

**8. Hva gjør mennesket i loopen, og hjelper det?**
188 av 1578 saker (11,9 %) går til menneske med skriftlig grunn, og alle 38 falske MOT-flagg ligger der; saker maskinen svarer alene på har 0 falske MOT (P 1,0, F1 0,514) (#2293). Gjør mennesket de rutede sakene riktig blir F1 0,828, følger det bare styret 0,269; sannheten ligger mellom, og de 17 trygge bommene ser ingen (#2132, JURYSVAR spm. 7, #2293).

**9. Hva skjer med nye selskaper, tomme felt eller rare inndata?**
Nye selskaper uten historikk: F1 0,375 (−0,101), og 99,4 % går til menneske; tom tekst eller tomme nøkkelfelt gir 0 MOT og 100 % til menneske i stedet for gjetting (#2144, `c1_robusthet_frossen.md`). Rare saker krasjer ikke (utgang 0 fra kald kopi, #2264), og svartid er 5,5 s per sak fra kald start eller 0,04 s per sak i en liste, uten nett (#2259, `c1_svartid.md`).

**10. Bruker agenten NBIMs stemmer som ikke var kjent ennå?**
Den bruker bare stemmer fra møter før saksdatoen, og NBIM publiserer stemmene fem dager før møtet fra 2021 (`c1_nbim_publisering.md`). Kommer stemmene først 90 dager etter møtet, er F1 0,523 på 2025 og 0,512–0,536 på 2024, fall innenfor støy; uten historikk faller den til 0,25–0,34 (#2299, `c1_historikk_forsinkelse.md`). Gamle 0,415 («hist 1») er ikke et golv for sen publisering, fordi den lekker i treningen (#2306).

## Avvik funnet underveis (til speider #1975 / dommer2 #2255)
- `agent.csv` sier nå 71 MOT mot styret, ikke 74 (3 er FOR mot styrets MOT); KRAVRESPONS linje 60 må rettes (#2309).
- 0,4818 (#2263, ablasjon) er avviks-F1 (66 avvik), ikke MOT-F1; må ikke stå som hovedtall.
- 0,415 står fortsatt som golv i minst fem filer (#2306).
