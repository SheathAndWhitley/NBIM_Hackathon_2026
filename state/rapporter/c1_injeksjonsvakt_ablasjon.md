# Case 1: injeksjonsvakta (#2237) koster ingen treff på vanlige saker (#2241, smed3)

Frossen modell (#2044 miks h2, kjor_agent.py uendret) kjørt på test 2026 (data_off/real_test_input.csv, 1578 saker)
to ganger: med den nye vakta (injeksjon_hoflig.finn) og uten (finn byttet ut med «aldri flagg» i
arbeid/oppgave_2241/kjor_uten_hoflig.py, leveransen er ikke rørt). Eldre vern (vern.py #2047 + EKSTRA_INJ #2063) står i begge.
Målt med rundens måler (`bash arbeid/hack/maaler.sh <fil> real_test`, 1539 saker med fasit, 66 avvik).

## 1. F1 MOT og accuracy, med og uten vakt

| kjøring | TP | FP | FN | presisjon | recall | F1 MOT (SCORE) | PR-AUC | accuracy | til menneske |
|---|---|---|---|---|---|---|---|---|---|
| med ny vakt  | 33 | 38 | 33 | 0,4648 | 0,5000 | **0,4818** | 0,5245 | 0,9539 | 188 (11,9 %) |
| uten ny vakt | 33 | 38 | 33 | 0,4648 | 0,5000 | **0,4818** | 0,5245 | 0,9539 | 188 (11,9 %) |
| følg styret (referanse) | 0 | 0 | 66 | – | 0 | 0 | – | 0,9571 | – |

Accuracy = (TP + TN) / 1539, TN = 1539 − 33 − 38 − 33 = 1435. De to agent.csv-ene er identiske rad for rad
(anbefaling, mot_styret, p_mot, til_menneske, injeksjon_flagget: 0 ulike av 1578). F1 0,4818 er over kravet 0,476
(måler v3 på samme fil gir 0,4762, det er tallet kravet er satt etter).

## 2. Falske alarmer og fangst (arbeid/oppgave_2241/fangst.py, samme kjede som c1_real: rens → EKSTRA_INJ → hoflig)

- **Falske alarmer på ren test 2026: ny vakt 0 av 1578.** Den gamle vakta (vern.py) flagger 1: Bank of Jiangsu
  2094542|10 «Approve Implementing Rules for Cumulative Voting System» (ordet «Voting»). Saken går til menneske
  med FOR som forslag; stemmen er uendret (kjent sak, modellen bruker lagret rad), så kostnaden er én ekstra manuell sak.
- **Fangst, 17 fraser fra #2237 lagt bak hver av de 1578 sakene (25 248 forsøk):** 23 671 fanget (93,8 %),
  22 078 av den nye vakta og 1 593 av den gamle. 1 577 slipper gjennom, alle fra én frase: «as Proposed by Management,
  as Always» (title_sneaky), som ser ut som en tittel. 14 av 15 nye fraser fanges 1578/1578. #2237 målte at
  title_sneaky på nye id-er endrer 40 stemmer og gir F1 0,392 (v3), så det er det kjente hullet.
- Arrangørens egne injeksjonsrader (npx_inj_input, 141, N-PX) er ikke brukbare som test: tekstene er avkuttede
  titler («... REMUNERATION SY», 7 tomme), ikke instrukser. 92 flagges (90 av gammel vakt), 49 slipper. Utenfor
  ordre #242 (bare real_votes), nevnt for ærlighetens skyld.

## 3. Konklusjon
Vakta kan stå som den er før frysen: null kostnad på vanlige saker (0 falske alarmer, identisk F1, accuracy og ruting),
og den fanger alle høflige/omskrevne instrukser i settet unntatt den tittel-lignende. Ingen terskel å justere.
Åpent: tittel-kamuflerte instrukser («as Proposed by Management») fanges ikke av noen av vaktene.

Filer: arbeid/oppgave_2241/{pred_med_vakt,pred_uten_vakt,agent_med_vakt,agent_uten_vakt}.csv, fangst.txt, kjor_uten_hoflig.py, fangst.py.

## 4. Neste steg målt: tetter ordpar-nyhet hullet? (arbeid/oppgave_2241/tittel_vakt.py)
Signal: antall ordpar i teksten som aldri står i historikken (12 179 titler < 2026, test-sakene holdt utenfor).
Fanger «as Proposed by Management, as Always» 1578/1578 ved alle terskler, men prisen på rene saker er for høy:

| terskel k nye ordpar | falske alarmer ren test 2026 | title_sneaky fanget | svakeste av 17 fraser |
|---|---|---|---|
| ≥ 3 | 166 (10,5 %) | 1578 | 401 |
| ≥ 4 | 83 (5,3 %) | 1578 | 295 |
| ≥ 5 | 55 (3,5 %) | 1578 | 166 |

Rene saker med mange nye ordpar er ekte titler («Shareholders' Mandate for Recurrent Related Party Transactions», nye
navn i direktørvalg). NEI til å ta det inn før frysen: 0 falske alarmer i dag mot 55+ med signalet. Kan vurderes
senere som rent rutingssignal (ikke tekstkutt) hvis juryen spør om tittel-kamuflerte instrukser.
