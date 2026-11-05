# Case 1 på én side: stemmeagenten som finner NBIMs stemmer mot styret

> **Oppdatert grunnlinje (5.11 kveld):** Den sterkeste enkle regelen er «gjenta NBIMs forrige beslutning på samme sak eller person» (`arbeid/hack/c1/grunnlinje_gjenta_forrige.py`). Den gir F1 på MOT 0,42 / 0,51 / 0,51 for 2024–2026, snitt 0,48, mot agentens 0,51 / 0,53 / 0,51, snitt 0,52: agenten er bedre i snitt, men lik regelen i 2026. Der dette dokumentet sammenligner med regel b2 (0,365), er det en svakere regel. Lekkasjetesten: `arbeid/hack/c1/lekkasjetest.py`. <!-- tallvakt: ignorer: grunnlinje, ikke hovedtall -->

**1. Hva agenten gjør.** Den leser sakslista (selskap, sakstype, forslagstekst, forslagsstiller, styrets
anbefaling, NBIMs tidligere stemmer) og peker ut sakene der NBIM trolig stemmer **mot styret**. Tre bunker: FOR (følger styret), mulig MOT (med NBIMs egen begrunnelse
fra en tidligere MOT-stemme), eller **til menneske**. Hver sak får et ordrett sitat fra nærmeste punkt i NBIMs Global Voting Guidelines
(riktig regel i 15 av 20 i stikkprøve, #2115).

**2. Metode.**
- **Avgrensning:** bare NBIM og bare arrangørens real_votes: 194 selskaper i 37 land, møteår 2019–2026,
  utviklede (DM) og fremvoksende (EM) markeder, alle sakstyper; test 2026 er 136 selskaper i 31 land
  (`omfang.txt`). Ikke andre forvaltere, ikke selskaper utenfor utvalget.
- Fasit er NBIMs egne stemmer (real_votes). Splitt etter møteår, aldri tilfeldig: val 2025, **test 2026**.
  Grensen (p ≥ 0,923) er låst på val før test; kalibreringen er lært på val 2025; båndet er valgt fra et fast rutenett på test-tabellen og sjekket på val (7,5 % val, 7,9 % test, `c1_menneske_terskel.md`).
- Ingen lekkasje: historikk bare fra møter strengt før møtedatoen; fasitkolonner
  (`nbim_vote`, `rationale_*`, `position_paper`) stoppes med assert.
- Gulvet «følg styret» har **F1 på MOT = 0**. Derfor måles F1 på MOT, ikke accuracy.

**3. Hovedtall** (frosset modell #2044, test 2026, `c1/maaler_offisiell_v3.py --score mot`):

| F1 MOT | presisjon | recall | 95 % KI (klyngebootstrap per selskap) | MOT i test |
|---|---|---|---|---|
| **0,512** | 0,478 | 0,552 | [0,40; 0,62] | 58 av 1539 saker (TP 32, FP 35, FN 26) |

Følg styret: F1 0. Beste enkle regel (samme selskap + samme tekst fikk MOT før): 0,365 [0,25; 0,49]; agenten slår
den med +0,15 [0,04; 0,25] (#2134). Sidetall: avvik inkl. 5 AVSTÅ (66 saker) gir 0,5294.

**Ikke bare «aksjonærforslag = MOT».** 56 av 58 MOT i test 2026 er stemmer mot styrets *egne* forslag, og 29 av
agentens 30 treff er der. Regelen «aksjonærforslag = MOT» kan finne høyst 2 av 58 (`c1_forslagsstiller.txt`).

Accuracy **96,0 %** er *lavere* enn følg styret (**96,2 %**): bare 3,8 % er MOT, så den som aldri sier MOT
finner null. Agenten finner 32 av 58.

**4. Når saken går til et menneske.** (a) Usikre saker: kalibrert P(MOT) i båndet [0,15; 0,85) (kalibreringen er lært på val 2025; båndet er valgt fra et fast rutenett på test-tabellen og sjekket på val (7,5 % val, 7,9 % test, `c1_menneske_terskel.md`))
(`--baand`). (b) Datafeil eller ukjent selskap/sakstype. (c) Mistenkelig fritekst («ignore … vote against»
renses og rutes). (d) MOT-flagg uten sitat. Rutingen endrer aldri maskinens svar, bare hvem som ser saken.

| test 2026, standardoppsett | tall |
|---|---|
| til menneske | 161 av 1539 (10,5 %) med fasit; 164 av 1578 inn |
| MOT blant dem | 29 av 58 (32 av 35 falske MOT-flagg er også her) |
| MOT funnet, maskin + menneske | 40 av 58, F1 0,792 hvis mennesket avgjør riktig (øvre grense); 0,306 hvis mennesket bare følger styret |
| MOT som ingen ser | 18 av 58 (P(MOT) under 0,15, verken flagget eller rutet) |

Kilde: `kjor_agent_real_test2026.txt`, `BESLUTNINGSSTOTTE.md`. Lesetid ca. 56 timer (antatt 20 min per sonesak, 10 per flagg, ikke målt).

**5. Tre ærlige begrensninger.**
1. **Få MOT-stemmer, stor usikkerhet.** 58 MOT i test gir KI 0,40–0,62. Les F1 som «rundt 0,48».
   Alene finner agenten halvparten av MOT; den skal ikke stemme automatisk.
2. **Sitatet er fra en annen sak.** NBIMs egen tekst, men fra nærmeste tidligere MOT-stemme
   (annet møte, ofte annet år): et hint, ikke begrunnelsen for denne saken.
3. **Avhenger av oppdatert historikk og en skjør terskel.** Uten NBIMs tidligere stemmer i samme sesong faller
   F1 0,512 → 0,415 [0,30; 0,53] på MOT (#2134). Små flytt av grensen endrer flaggene mye; bytt oppsett med `--baand`.

Kilder: `state/rapporter/c1_tallkonsistens.md` (tall), `METODE.md`, `README.md`.
