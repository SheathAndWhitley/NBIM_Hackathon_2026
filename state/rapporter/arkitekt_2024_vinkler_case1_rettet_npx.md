# Arkitekt #2024: vinkler, gulv og tak for Case 1 på den rettede NPX-fila
Fil: `arbeid/hack/CASE/20261105_114301_npx_votes.csv` (49 006 rader med fasit, split_year 2024/25/26 på møtedato).
Mål: F1 på against_board=1, høyere er bedre. Test 2026: 634 MOT av 16 488 (3,8 %). Kode: `arbeid/oppgave_2024/kp_*.py`.
**Viktigst:** 302 av 634 MOT i 2026 er aksjonærforslag. Der gir regelen «Shareholder → MOT» P 1,000 R 0,476 F1 **0,645** alene,
over vår nåværende 0,47 (som er målt på et annet og mindre sett, så tallene kan ikke sammenlignes).
Grunnen er hvordan feltet er kodet: SEC-filene våre har selv `managementRecommendation=FOR` på aksjonærforslag som styret er imot
(sjekket: Constellation, «Circular Economy for Packaging», i `c1/data/raw/000102140824004999_proxyvote.xml`). Så «mot styret» på
aksjonærforslag er nesten bare en kodeeffekt. **Rapportér F1 for Management og Shareholder hver for seg.** Det ærlige, vanskelige tallet er Management-MOT (332 i 2026, 2,1 %).

## Omformulering (steg 0)
1 snu tida:     gjelder. Let ikke etter «hvorfor MOT», men etter hva NBIM stemte sist i samme selskap på samme tekst. Nøkkelen (selskap, tekst uten navn) dekker 30,7 % av 2026: Mgmt P 0,754 R 0,148.
2 primal-dual:  gjelder sterkt. Klassifiser møtet (har det minst én MOT?) og deretter punktet i møtet. 234 av 332 Mgmt-MOT (70 %) har en annen MOT i samme møte.
3 invarianter:  etiketten er (stemme ≠ anbefaling). Snus anbefalingen, snus etiketten, og det er hele aksjonærforslag-effekten. Avstå teller som MOT (739 Mgmt-rader). Det må stå i JURY.md.
4 grov nøkkel:  (land, forslagstype) som rate fra 2024-25. Med terskel ≥ 0,3: Mgmt P 0,631 R 0,196. Det er den billigste sterke nøkkelen.

## Gulv og tak (stoppregel)
Gulv: følg styret F1 0. Aksjonærforslag → MOT: F1 0,645 (2026) og 0,610 (val 2025). Under det taper modellen mot én linje.
Tak (anslag): aksjonærdelen perfekt + Mgmt P=R=0,5 gir F1 0,74. Mgmt P=R=0,7 gir F1 ca. 0,84. Over 0,85 krever det sannsynligvis lekkasje.
Støy: 634 positive gir standardfeil på F1 ca. ±0,02. Forskjeller under 0,02 er støy, så ingen tuning under det.
Stoppregel: en metode dør hvis Mgmt-F1 på val 2025 (valgt på 2024) ikke slår land×type-nøkkelen.
KP: er aksjonærforslag-effekten en kodeeffekt? Forventet `managementRecommendation=FOR` i vår egen SEC-råfil for Constellation «Circular Economy», fikk FOR (howVoted AGAINST). OK. MOT-andel 3,95 % (1936/49006). Mot gammelt sett ikke sammenlignbart (holdout 65 MOT av 1544).

## Tre ikke-standard metoder (BOLKER.md finnes ikke: rangert etter Mgmt-avstand, det svakeste stedet)
Alle terskler under er valgt på 2026 = UKONTROLLERT for valg. Første steg for smeden er å velge dem på nytt på val 2025.
M1 Stemmegivning mellom nøkler (trukket vinkel: «ensemble og stemmegivning»)   SH | (selskap,tekst) | land×type≥0,3:
   alt F1 **0,734** (P 0,881 R 0,629), Mgmt F1 0,402 (P 0,642 R 0,292). «2 av 3» er dårligere: 0,680. Hver flagget sak kan forklares med én nøkkel, og det er god beslutningsstøtte. 20 min.
M2 Møte-først (dual)   Steg 1: P(møtet har Mgmt-MOT) fra land, antall punkter, selskapets historikk og n_funds (n_funds 3-4 gir 15-26 % MOT, mot 3 % ved 1).
   Steg 2: punktet i møtet med høyest typerate. Treffer 70 %-strukturen over. UKONTROLLERT, 40 min.
M3 Sitat fra nøkkelen   Bruk nabosaken (samme selskap/tekst eller land×type) som begrunnelse. «Stemte MOT på samme forslag i 2025» er et sitat juryen forstår, og LLM-en trengs ikke. Gir Mgmt R ≤ 0,148 alene, mest for #45 og robusthet. 30 min.
Ikke gjort: sjekke om n_funds og injection_flag er lov å bruke (84 injiserte rader, MOT-rate 1,2 %; det er motstandstestens rader og skal holdes utenfor trening).

