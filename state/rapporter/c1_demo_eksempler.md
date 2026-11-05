# Case 1 demo: ett treff og én bom fra test 2026 (#2141, utvalg rettet #2160)

**Gjenskap begge utskriftene** (fra landsbymappen, ca. 15 s, ingen modellendring):

    bash arbeid/oppgave_2141/demo_treff_bom.sh [UTMAPPE]      # standard /tmp/c1_demo2141

Skriptet kjører den vanlige agenten (`levering/kjor_agent.py`, real_votes, smed2s MOT-modell #2044) på hele test 2026,
finner de **58 sakene der NBIM stemte MOT mot styret** (samme fasit som måler v3 «MOT mot styret»: nbim_vote MOT og
against_board 1), og teller treff som måleren: agenten sier MOT der styret ikke sier MOT. Agenten fanget **30**, bommet på **28**.
Måler v3 på samme helkjøring gir det samme: `MOT mot styret: TP 30 FP 38 FN 28, F1 0,4762`.
Ett treff og én bom trekkes med `random.Random(0).choice` på sorterte id-er, så sakene er ikke håndplukket.
Deretter kjøres agenten kaldt på bare de to sakene. Tallene (anbefaling, P(MOT), rå score, ruting) er like i hel- og enkeltkjøringen,
og to kalde kjøringer av hele skriptet gir byte-lik utskrift. Utskriften ligger i `arbeid/oppgave_2141/utskrift.txt`.

**Hva som ble rettet (#2160):** første versjon trakk fra 66 avvik fra styret (against_board 1), 33 fanget og 33 bommet.
De 8 ekstra var ikke MOT mot styret: 5 AVSTÅ og 3 der NBIM stemte FOR mot et styre som anbefalte MOT. Med rett utvalg
ble trekket nytt (samme seed-regel), så demoen viser nå to andre saker enn før.

Grensen er låst på val 2025: rå score ≥ 0,91885 gir MOT (kalibrert ca. 0,19). Saker med kalibrert P(MOT) i [0,15; 0,85) går til menneske.

## Utskrift

```
FRYSVAKT: ikke frosset ennå (<repo>/state/c1_frys.json finnes ikke)
fasit MOT mot styret i test 2026 (som måler v3): 58, fanget 30, bommet 28; trukket (seed 0): treff 2089132|3, bom 2114914|3

== TREFF: 2089132|3 TV TOKYO Holdings Corp. 2026-06-18 (Japan, DIRECTOR_ELECTION)
   forslag:     Elect Director Ishikawa, Ichiro
   agent:       MOT (styret FOR, mot styret 1)  kalibrert P(MOT) 0.5217  rå score 0.96994
   bånd:        til menneske 1  usikker: kalibrert P(MOT) 0.52 i båndet [0.15, 0.85)
   retningslinje: NBIM 1.1.1  «The board should guide company strategy and monitor management performance without conflicts of interest.»
   grunnlag:    BM25 43.7; type DIRECTOR_ELECTION: 74/277 tidligere MOT-begrunnelser i 1.1; nabo-begrunnelsen i 1.1; posisjonsnotat (fra nabo-begrunnelsen): Board independence (NBIM-PP2)
   grunn (NBIMs tidligere begrunnelse): «The board should guide company strategy and monitor management performance without conflicts of interest. A majority of shareholder-elected board members in a non-controlled company should be independent of management, dominant shareholders, and related third parties. In a majority-controlled compan»  [NBIMs begrunnelse 2023, TV TOKYO Holdings Corp.: «Elect Director Ishikawa, Ichiro»]
   fasit:       NBIM stemte Against (mot styret 1.0). NBIMs begrunnelse: The board should guide company strategy and monitor management performance without conflicts of interest. A majority of shareholder-elected board members in a non-controlled company should be independ

== BOM: 2114914|3 The Monogatari Corp. 2026-09-25 (Japan, DIRECTOR_ELECTION)
   forslag:     Elect Director Kato, Hisayuki
   agent:       FOR (styret FOR, mot styret 0)  kalibrert P(MOT) 0.1912  rå score 0.87246
   bånd:        til menneske 1  usikker: kalibrert P(MOT) 0.19 i båndet [0.15, 0.85)
   retningslinje: NBIM 0.0.3  «Our starting point when deciding how to vote is to support the board. We participate in electing the board and entrust it with running the company.»
   grunnlag:    følger styret: NBIMs utgangspunkt er å støtte styret
   fasit:       NBIM stemte Against (mot styret 1.0). NBIMs begrunnelse: The board should guide company strategy and monitor management performance without conflicts of interest. A majority of shareholder-elected board members in a non-controlled company should be independ
```

## Hvorfor bommen skjedde (én setning)

Japanske styrevalg går sjelden MOT (7 av 226 i test 2026), og selskapet har ingen egen nabo-begrunnelse som trekker opp,
så rå score 0,872 lå under den låste grensen 0,919 og agenten fulgte styret. Saken lå likevel i usikkerhetsbåndet
(P(MOT) 0,19) og ble **sendt til menneske**, så med ruting slått på stemmes den ikke blindt.

## Ærlige forbehold
- Bommen er rutet, men det gjelder ikke alle: 11 av 28 bommer i test 2026 gikk til menneske, 17 ble stemt FOR uten ruting.
  Flest bommer er styrevalg (13), så «annet fra ledelsen» (5) og revisor (4).
- Treffet har kalibrert P(MOT) 0,52 og går også til menneske. 21 av 30 treff er rutet; agentens sikre MOT (P ≥ 0,85) er få.
- Treffets sitat og retningslinjepunkt (NBIM 1.1.1) treffer NBIMs egen begrunnelse ordrett, fordi naboen er samme direktør
  i samme selskap i 2023 (TV TOKYO, Ishikawa). Det viser at oppslaget virker, men også at gjentatte saker er lette.
- Presisjonen er lav: 38 falske MOT mot 30 ekte (P 0,44). Demoen viser ett treff og én bom, ikke de falske alarmene.
- Frysvakta var ikke satt da utskriften ble laget (før kl. 16). Etter frysen bør skriptet kjøres på nytt; det sjekker frysen selv i første linje.
