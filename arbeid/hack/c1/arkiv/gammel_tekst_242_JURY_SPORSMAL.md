# Fjernet fra levering/JURY_SPORSMAL.md (ordre #242, oppgave #2219)

Linje 23, 105-107, 110, 114-117 ordrett før endring:

Regelen «aksjonærforslag = MOT» kan derfor finne høyst 2 av 58. På Vanguard-data ga den 0,839, men det målte forslagstype, ikke vurdering.
- **H-B Pakka motsier seg selv om sitatene.** `levering/JURYSVAR.md:26`, `levering/METODE.md:62` og `c1/leveranse/BEGRENSNINGER.md:25`
  sier «Vanguard, ikke NBIM» og «1 av 30 begrunner». Det gjelder N-PX-agenten. `c1/DEMO_MANUS.md:53` og `c1_real.py:201` viser NBIM-begrunnelse og GVG.
  En jury som leser begge, ser en motsigelse.
- **H-D Kalibrering av p_mot på real_votes er ikke målt.** ECE 0,025 i `levering/METODE.md:58` er N-PX-modellen. #2109 (smed3) er åpen.
- **H-G Rutetabellen og flere tall teller 66 avvik, ikke 58 MOT.** `levering/BESLUTNINGSSTOTTE.md:5` kaller 66 «ekte MOT-stemmer».
  `c1/JURY_METODE.md:9` bruker «129 MOT-saker» fra N-PX, og `c1/JURY_METODE.md:29` sier at agenttallet «ikke er målt ennå», men
  det er målt (0,4762, `levering/README.md:27`).
- **H-H Hvorfor 2026 er svakere enn 2025 på real_votes** (0,476 mot 0,520). Forklaringen i `levering/JURYSVAR.md:35` gjelder N-PX-modellen.


## Svar 7 (gammel sone, avvik 66), byttet ut av speider
Med standarden (10 % sone nær grensen) leser forvalteren 13,3 saker per 100 og fanger 65 % av MOT mot 50 % for maskinen alene.
Presisjonen på flaggene går fra 0,47 til 0,77. 65 % er en øvre grense, fordi vi antar at mennesket avgjør sonen riktig. Med datafeil,
ukjente selskaper og injeksjon går 188 av 1578 saker (11,9 %) til menneske. Tidsbruken (62 timer) er en antagelse, ikke målt.
Kilde: `levering/BESLUTNINGSSTOTTE.md:21-26,37,43-45`. *Merk: tabellen teller avvik (66), ikke MOT (58).*
