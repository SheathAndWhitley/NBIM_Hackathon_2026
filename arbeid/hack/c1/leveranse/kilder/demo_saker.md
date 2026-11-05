# Case 1: tre demosaker fra den frosne agenten (miks h2, test 2026)

Kjøring: `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut arbeid/oppgave_2260/full` (standardkjøring, bånd [0,15; 0,85), 5,7 s). `pred_maaler.csv` har sha256 `b113b545…3653`, samme som den frosne fila. Ingen modellendring.

**Valgregel (ingen håndplukking):** `arbeid/oppgave_2260/velg.py` går gjennom `agent.csv` i filrekkefølge og tar den FØRSTE saken av hver type. Treff og bom: første blant saker maskinen avgjorde selv (`til_menneske 0`), så de tre sakene er ulike. Til menneske: første sak med `til_menneske 1`. MOT mot styret som i måler v3 (hovedmålet): fasit `nbim_vote MOT` og `against_board 1`; agent `anbefaling MOT` der styret ikke sier MOT.

Ærlig merknad: den aller første bommen i fila (linje 39, H. Lundbeck, «Reelect Lars Erik Holmqvist as Director», agent MOT, P 0,52) ble sendt til menneske, og den aller første treffen (linje 15) er menneskesaken under. Ingen av dem er valgt bort for å se penere ut; de faller bare i menneskekategorien.

## Treff: riktig MOT mot styret, avgjort av maskinen

`agent.csv` linje 276. Agentens faktiske utskrift, ordrett (alle felt i raden):

```
id: 2041367|21
company: Mobimo Holding AG
meeting_date: 2026-03-31
proposal_text: Transact Other Business (Voting)
styret: FOR
anbefaling: MOT
mot_styret: 1
p_mot: 1.0
til_menneske: 0
rutingsgrunn: 
punkt: GVG 5.2
sitat: We will not support an agenda item if the information disclosed is insufficient to make an informed decision.
sitat_kilde: NBIMs begrunnelse 2021, Mobimo Holding AG: «Transact Other Business (Voting)»
sitat_likhet: 1.4
injeksjon_flagget: 0
raa_score: 0.99844
retningslinje_id: NBIM 5.2.1
retningslinje_sitat: The board should use the annual report to present a fair, sensible and clear assessment of the company. The report should be reflective of the prior year, and include material risk factors.
retningslinje_grunnlag: BM25 1012.0; type OTHER_BUSINESS: 33/33 tidligere MOT-begrunnelser i 5.2; nabo-begrunnelsen i 5.2; regler i seksjonen et menneske bør sjekke: 5.2.3, 5.2.4
```

**Fasit (real_votes, ikke sett av agenten):** Switzerland, OTHER_BUSINESS, styret For, NBIM stemte **Against** (against_board 1.0). NBIMs begrunnelse: «We will not support an agenda item if the information disclosed is insufficient to make an informed decision.»

## Bom: NBIM stemte MOT, agenten sa FOR, avgjort av maskinen (falsk negativ)

`agent.csv` linje 89. Agentens faktiske utskrift, ordrett (alle felt i raden):

```
id: 2048411|10
company: LOTTE Chemical Corp.
meeting_date: 2026-03-20
proposal_text: Amend Articles of Incorporation (Office Term)
styret: FOR
anbefaling: FOR
mot_styret: 0
p_mot: 0.0896
til_menneske: 0
rutingsgrunn: 
punkt: 
sitat: 
sitat_kilde: 
sitat_likhet: 
injeksjon_flagget: 0
raa_score: 0.855
retningslinje_id: NBIM 0.0.3
retningslinje_sitat: Our starting point when deciding how to vote is to support the board. We participate in electing the board and entrust it with running the company.
retningslinje_grunnlag: følger styret: NBIMs utgangspunkt er å støtte styret
```

**Fasit (real_votes, ikke sett av agenten):** South Korea, ARTICLES, styret For, NBIM stemte **Against** (against_board 1.0). NBIMs begrunnelse: «The right to vote on fundamental changes affecting the company is a basic right of shareholders. This includes the right to approve changes to the company’s governing documents.»

## Til menneske: usikker sak (her var MOT riktig)

`agent.csv` linje 15. Agentens faktiske utskrift, ordrett (alle felt i raden):

```
id: 2033470|1
company: Kura Sushi, Inc.
meeting_date: 2026-01-28
proposal_text: Elect Director Tanaka, Kunihiko
styret: FOR
anbefaling: MOT
mot_styret: 1
p_mot: 0.5833
til_menneske: 1
rutingsgrunn: usikker: kalibrert P(MOT) 0.58 i båndet [0.15, 0.85)
punkt: GVG 1.1
sitat: The board should guide company strategy and monitor management performance without conflicts of interest. A majority of shareholder-elected board members in a non-controlled company should be independent of management, dominant shareholders, and related third parties. In a majority-controlled company, at least a third of board members should be independent.
sitat_kilde: NBIMs begrunnelse 2021, Kura Sushi, Inc.: «Elect Director Tanaka, Kunihiko»
sitat_likhet: 1.4
injeksjon_flagget: 0
raa_score: 0.98125
retningslinje_id: NBIM 1.1.1
retningslinje_sitat: The board should guide company strategy and monitor management performance without conflicts of interest.
retningslinje_grunnlag: BM25 43.7; type DIRECTOR_ELECTION: 74/277 tidligere MOT-begrunnelser i 1.1; nabo-begrunnelsen i 1.1; posisjonsnotat (fra nabo-begrunnelsen): Board independence (NBIM-PP2)
```

**Fasit (real_votes, ikke sett av agenten):** Japan, DIRECTOR_ELECTION, styret For, NBIM stemte **Against** (against_board 1.0). NBIMs begrunnelse: «The board should guide company strategy and monitor management performance without conflicts of interest. A majority of shareholder-elected board members in a non-controlled company should be independent of management, dominant shareholders, and related third parties. In a majority-controlled company, at least a third of board members should be independent. We will not support the re-election of a director, or the entire board, if the company has experienced material failures in the oversight, management or disclosure of social risks.»
## Hva sakene viser (for demoen)

- **Treff (Mobimo, «Transact Other Business»):** P(MOT) 1,0, ikke til menneske. NBIM-sitatet (punkt GVG 5.2) er NBIMs egen begrunnelse fra 2021 for samme selskap og samme forslagstekst, og er ordrett lik 2026-begrunnelsen. Modellen kjenner igjen en fast NBIM-praksis (33 av 33 tidligere OTHER_BUSINESS-MOT i 5.2). Svakhet: retningslinjesitatet (NBIM 5.2.1, om årsrapporten) passer dårlig til «annen sak»; sitatet fra begrunnelsen er det som bærer.
- **Bom (LOTTE Chemical, «Amend Articles of Incorporation (Office Term)»):** P(MOT) 0,09, under båndet, så maskinen sa FOR uten å spørre et menneske. NBIM stemte MOT med begrunnelsen om aksjonærenes rett til å stemme over vedtektsendringer. Agentens begrunnelse er bare utgangspunktet «støtt styret». Dette er typen feil båndet ikke fanger: lav sikkerhet for MOT, men feil. Det er 28 slike FN i test 2026 (R 0,517).
- **Til menneske (Kura Sushi, «Elect Director Tanaka, Kunihiko»):** kalibrert P(MOT) 0,58 i båndet [0,15; 0,85), så saken går til et menneske med forslag MOT og sitat om styreuavhengighet (GVG 1.1, posisjonsnotat NBIM-PP2). NBIM stemte MOT, så forslaget til mennesket var riktig.

## Kontroll og sammenheng

- De tre radene, og hele `agent.csv`, er identiske med den kalde kopien `/tmp/fremmed/ut/agent.csv` (kjøring 13:14, `pred_maaler.csv` sha `b113b545…3653`).
- Bommen er representativ for den farlige feiltypen: i test 2026 gikk **alle 38 falske MOT (FP) til menneske**, men av **28 oversette MOT (FN) gikk bare 11 til menneske; 17 ble FOR fra maskinen alene**, som LOTTE-saken (13 av 28 FN er styrevalg). Maskinen tar altså feil i stillhet bare i retning «følg styret».
