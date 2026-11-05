# Case 1 på én slide: finner agenten når NBIM stemmer mot styret?

**Problem.** NBIM følger styret i 96 % av sakene. Verdien ligger i de få stemmene **mot styret**: dem må en
forvalter finne før generalforsamlingen. «Følg styret» får 96,2 % accuracy og finner **null** av dem¹.

**Data og avgrensning.** NBIMs egne stemmer (real_votes): 13 757 saker, 194 selskaper, 37 land, 2019–2026,
utviklede (DM) og fremvoksende (EM) markeder, alle sakstyper². Splitt etter møteår: tren 2019–2024, val 2025,
**test 2026** (testmodellen trent på 2019–2025, kjørt én gang) (1539 saker med fasit, 58 MOT)³.

**Metode.** Logistisk regresjon + LightGBM (snitt av rangene) på forslagstekst (TF-IDF), sakstype, forslagsstiller,
styrets anbefaling, land/marked og NBIMs *tidligere* MOT-stemmer
(bare møter før møtedatoen; fasitkolonner stoppes med assert). Grense låst på val før test³; menneskebåndet valgt på test-tabellen og sjekket på val.

| test 2026, frosset modell #2044 | F1 på MOT | presisjon | recall | accuracy |
|---|---|---|---|---|
| Følg styret (gulvet) | **0** | – | 0 | 96,2 % |
| Beste enkle regel (samme selskap + tekst fikk MOT før) | 0,365 | | | |
| **Agenten** | **0,512** [0,40; 0,62] | 0,478 | 0,552 | 96,0 % |

Agenten finner 32 av 58 MOT (TP 32, FP 35, FN 26)¹ og slår beste enkle regel med +0,15 [0,04; 0,25]⁴.

**Usikre saker går til et menneske.** Kalibrert P(MOT) i [0,15; 0,85), ukjent selskap/sakstype, datafeil,
mistenkelig fritekst eller MOT uten sitat: 161 av 1539 saker (10,5 %), der ligger 32 av 58 MOT⁵.
Rutingen endrer aldri maskinens svar. Hver sak får et ordrett sitat fra NBIMs Global Voting Guidelines.

**Ærlig begrensning.** 18 av 58 MOT-stemmer får P(MOT) under 0,15 og blir **verken flagget eller sett av et
menneske**⁵. Agenten er beslutningsstøtte, ikke en autopilot: den stemmer aldri selv.

Kilder (alt under `arbeid/hack/levering/` om ikke annet står):
¹ `TREFFSIKKERHET.md:12-18` (måler `c1/maaler_offisiell_v3.py --score mot`, KI: klyngebootstrap per selskap, #2095)
² `omfang.txt` (laget av `omfang.py` fra `state/opplastet/20261105_114241_real_votes.csv`)
³ `METODE.md:10-21`, `kjor_agent_real_test2026.txt:3,8`
⁴ `state/rapporter/c1_jury_slaar_enkelt.md` (#2134)
⁵ `BESLUTNINGSSTOTTE.md:12,20,26`, `kjor_agent_real_test2026.txt:23`

Dashboardet er demoen: `bash arbeid/hack/c1/leveranse/demo.sh` (ekte agent på holdout-saker, ikke håndplukket).
