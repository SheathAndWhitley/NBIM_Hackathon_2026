# Case 1: demo-manus (5 min), saker trukket tilfeldig fra test 2026 (#2070, 05.11 kl. 12.20). ELDRE, SKAL IKKE LESES HØYT: gjeldende er DEMO_MANUS.md

**Eldre versjon (sak 2659):** sakstabellen og rutingstallene under er fra den eldre frosne modellen (#2044 miks h2, F1 0,476). Levert modell er repo4, F1 MOT 0,512 [0,40; 0,62], TP 32 FP 35 FN 26 (`arbeid/oppgave_2659/maaling.txt`); gjeldende demo er `DEMO_MANUS.md`. Hovedtallene i «» under er oppdatert til repo4.

Agenten: `arbeid/hack/levering/kjor_agent.py`, standard real_votes (smed2 #2044, miks h2 + NBIM-sitat + menneskebånd: kalibrert P(MOT) i [0,15, 0,85), ukjent selskap, injeksjon, datafeil).
Tall i {KLAMMER} kan endre seg ved modellfrys kl. 16 (#1975). Verdien i parentes er målt 05.11 kl. 12.20,
ruting og P(MOT) kontrollert mot agenten etter menneske-vaktene 05.11 kl. 13.10 (#2177).

Gjenskap alt (ca. 15 s, fra landsbymappen, kald start):

    bash arbeid/hack/c1/demo_saker_2026.sh /tmp/c1_demo2026

**Slik ble sakene valgt (ikke håndplukket):** alle 1539 saker i test 2026 med fasit, sortert på id.
`numpy.random.default_rng(seed).choice(1539, 5)` for seed 0, 1, 2, … til trekket hadde minst 2 saker der
NBIM stemte mot styret og minst 1 sak agenten sender til et menneske. Seed 0–16 holdt ikke kravet,
**seed 17** var den første som gjorde det. Sitatsaken (sak 6) er trukket for seg med seed 0 blant de
{N_AGENT_MOT} (71) sakene der agenten selv går mot styret, fordi agenten bare siterer når den sier MOT.
Kode: `arbeid/hack/c1/demo_trekk_2026.py`.

---

## 0:00–0:40 Problemet og måltallet
«NBIM stemmer med styret i om lag 96 % av sakene i 2026. Å alltid følge styret gir høy treffprosent,
men finner null stemmer mot. Vi måler derfor én ting: hvor godt agenten finner stemmene MOT styret,
F1 på MOT, på 2026, et år modellen aldri har sett. F1 er ett tall fra 0 til 1 som både teller hvor mange
MOT-stemmer agenten finner, og hvor ofte den har rett når den sier MOT. Følg styret: F1 0. Agenten: F1 {F1_TEST} (0,512).»
«Spør dere om agenten er 97 % treffsikker: nei. Treffprosenten er 95,7 %, litt under følg styret (96,2 %). 97,4 % er bare andelen riktige FOR-saker. Hovedtallet er F1 0,512 på MOT: agenten finner 32 av 58 stemmer mot styret, og 48 % av flaggene er ekte. Høy treffprosent betyr ingenting når 96 av 100 saker uansett er FOR.» (#2210, se JURY_SPORSMAL.md S0)

## 0:40–2:40 Fem tilfeldige saker fra 2026, slik de kom ut

| # | Sak (id) | Agent | rå score (sjanse for MOT) | Til menneske | Fasit: NBIM stemte |
|---|---|---|---|---|---|
| 1 | Hainan Jinpan, kapitalendring/vedtekter (`2056685\|7`), Kina | FOR | {S1} (0,912; 19 %) | **ja**, usikker: sjanse for MOT 19 %, mellom 15 og 85 % | For |
| 2 | Arbonia AG, ikke-finansiell rapport (`2041102\|2`), Sveits | FOR | {S2} (0,262; 0,8 %) | nei | For |
| 3 | Eximbank, ansvarsforsikring for styret (`2039527\|11`), Vietnam | FOR | {S3} (0,636; 5 %) | **ja**, ukjent selskap (ingen NBIM-stemmer før møtet) | For |
| 4 | Nomad Foods, valg av James E. Lillie (`2084542\|6`) | FOR | {S4} (0,451; 1 %) | nei | **Against** (bom) |
| 5 | Klarna, emisjon uten fortrinnsrett (`2089598\|12`), UK | FOR | {S5} (0,257; 0,8 %) | **ja**, ukjent selskap (ingen NBIM-stemmer før møtet) | **Against** (bom, men til menneske) |

Si dette, kort:
- «Tre av fem er riktige FOR. Sak 1 har rå score 0,912, rett under grensen der agenten sier MOT ({GRENSE}, 0,919), så
  agenten sier FOR. Sjansen for MOT er 19 %. Alt mellom 15 og 85 % regnes som usikkert, og saken går til et menneske. Mennesket ville sett at
  NBIM stemte For.» Sak 3 og 5 går også til et menneske, fordi NBIM aldri har stemt i selskapet før.
- «Sak 4 og 5 er ekte stemmer mot styret, og agenten bommer på begge. Det er ærlig: agenten finner
  halvparten av MOT-stemmene i 2026 (recall, andelen av MOT-stemmene den finner: {R_TEST}, 0,52), og her traff vi de to den mister. Klarna (sak 5)
  er et ukjent selskap og går til et menneske likevel; Nomad (sak 4) går rett igjennom som FOR.»
- «Hva NBIM selv skrev: sak 5 Klarna: *"Existing shareholders should have the right to approve share
  issuances in order to prevent the dilution of ownership without their prior consent."* Sak 4 Nomad:
  *"Shareholders should have the right to seek changes to the board when it does not act in their
  best interest."* I hele 2026 er det bare 2 MOT-stemmer på emisjoner, for få til å si hvor godt agenten fanger den sakstypen.»
  {BYTT HVIS FRYSEN ENDRER SAK 4/5: si hva som skjedde, ikke pynt}
- «Rå score er en rangering (snitt av plasseringen i to modeller), ikke en sannsynlighet. Agenten oversetter
  derfor scoren til en sjanse for MOT, lært på fasiten fra 2025 (kalibrering): rå 0,91 i sak 1 er bare 19 % sjanse for MOT.»

## 2:40–3:40 Sak 6: når agenten sier MOT, med NBIMs egne ord
**TV TOKYO Holdings, 18.06.2026, valg av styremedlem Ishikawa Ichiro (`2089132|3`), Japan.**
Trukket med seed 0 blant agentens egne MOT-saker.

- Agent: **MOT** styret, rå score {S6} (0,970), sjanse for MOT 52 %, **sendt til menneske** (usikker: mellom 15 og 85 %).
- Sitat (punkt GVG 1.1), NBIMs begrunnelse fra 2023 for samme styremedlem i samme selskap:
  *«The board should guide company strategy and monitor management performance without conflicts of
  interest. A majority of shareholder-elected board members in a non-controlled company should be
  independent of management, dominant shareholders, and related third parties.»*
- Fasit: NBIM stemte **Against**, med samme begrunnelse.
- Si ærlig: sitatet er hentet fra en tidligere sak (alltid tidligere år, annet møte), aldri fra fasit.
  At det er ordrett likt fasit, kommer av at NBIM bruker faste standardtekster: 999 NBIM-begrunnelser
  har bare 19 ulike tekster (`c1/kilder/nbim_begrunnelser.csv`). Sitatet forklarer svaret, modellen bruker det ikke til å gjette.

## 3:40–4:30 Menneske i loopen
- «Forvalteren velger hvor usikker en sak må være før et menneske ser den (innstillingen `--baand`, standard: sjanse for MOT
  mellom 15 og 85 %). Oversettelsen til sjanse lærer vi på 2025 og bruker uendret på 2026: {N_RUTET} saker (repo4: 161 av 1539, 10,5 %; eldre frossen: 183)
  går til et menneske.»
- I tillegg går saker fra ukjent selskap (sak 3 og 5), med datafeil, en skjult instruks i sakteksten (injeksjon, f.eks. «ignorer retningslinjene») eller MOT uten sitat til et menneske.
- «Sak 1 og 6 viser hvorfor: agenten var i tvil, og sa det, i stedet for å gjette.»
- **Sak 7: styrets anbefaling mangler (#2157).** Samme ekte sak som sak 2 (Arbonia, `2041102|2`), kjørt to
  ganger med `--sak`, én gang med `mgmt_rec` og én gang med den tom (`mgmt_rec` og `mgmt_rec_raw` = ""):

      bash arbeid/hack/c1/demo_mangler_styret.sh      # ca. 10 s

      == 2041102|2 Arbonia AG 2026-04-24: styret anbefaler For
         agent: FOR (styret lest som FOR, mot styret 0)  score 0.0075
         til menneske: 0  grunn: -
      == 2041102|2 Arbonia AG 2026-04-24: styrets anbefaling mangler
         agent: FOR (styret lest som FOR, mot styret 0)  score 0.0075
         til menneske: 1  grunn: styrets anbefaling mangler: antatt FOR, sjekk innkallingen;
                                 felt avviker fra lagret sak (mgmt_rec); modellen brukte lagret rad

  Si: «Uten styrets anbefaling vet ikke agenten hva "mot styret" betyr. Den gjetter ikke stille: den
  antar FOR, sier det, og sender saken til et menneske med grunnen. Her så den i tillegg at feltet
  avviker fra saken den har lagret.» Ærlig: saken finnes i historikken, så modellen brukte den lagrede
  raden og scoren er lik. Rutingen er det som endres, ikke modellen.

## 4:30–5:00 Tallene, ærlig
- Test 2026, målt én gang med vår egen måler (`maaler_offisiell_v3.py`): F1 MOT {F1_TEST} (0,512, 95 %-usikkerhetsintervall 0,40–0,62), presisjon {P_TEST} (0,48: når agenten sier MOT,
  har den rett 48 % av gangene), recall {R_TEST} (0,55: den finner 55 % av MOT-stemmene): {TP} treff, {FP} falske MOT, {FN} bommet MOT av 58 (repo4: 32, 35, 26, kald kjøring sak 2596; eldre frossen: 30, 38, 28).
- Følg styret: F1 0. MOT-grensen og usikkerhetsbåndet er valgt på 2025, aldri justert på 2026.
- «Én kommando fra kald start: `bash arbeid/hack/c1/demo_saker_2026.sh`.»

---

### Sjekkliste etter modellfrys (#1975)
1. Kjør `bash arbeid/hack/c1/demo_saker_2026.sh` på frosset modell; bytt alle {KLAMMER} med utdata.
2. Trekket (seed 17) avhenger av rutingen. Endrer frysen hvilke saker som rutes, kan en annen seed bli
   første som holder kravet. Bruk da den nye seeden og de nye sakene. Ikke behold seed 17 for å få penere saker.
3. Endrer frysen sak 4/5 til treff: si det, og si at det er etter frysen.
