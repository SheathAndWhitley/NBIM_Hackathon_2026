# Case 1 (#2875): likhet til tidligere MOT-forslag finner ikke flere nye MOT-er. Ingen bytte

Idé (#2569): agenten fanger nesten bare MOT der samme tekst var MOT før. Kan likhet (ikke eksakt treff) til forslag NBIM
stemte MOT på i tidligere år hente inn de nye MOT-ene? Regelen sto i `arbeid/oppgave_2875/REGEL.md` før målingen.
Trekket legges på lederen midt+av (#2703): p' = p_avvik + w·sim, samme k, deretter av-regelen. w ∈ {0, .05, .1, .2, .3}
velges på val T-1. Offisiell måler `maaler_aar.py --score mot`.

| F1 MOT | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 | mot frossen |
|---|---|---|---|---|---|---|
| frossen repo4 | 0,3535 | 0,5057 | 0,5309 | 0,5120 | 0,5162 | – |
| leder midt+av (w=0) | 0,3736 | 0,5083 | 0,5276 | 0,5424 | 0,5261 | +0,0099 |
| v1 tfidf 1-2-gram (w valgt 0/0/0) | 0,3736 | 0,5083 | 0,5276 | 0,5424 | 0,5261 | +0,0099 |
| v2 MiniLM (w valgt 0/0,2/0) | 0,3736 | 0,5083 | **0,5119** | 0,5424 | 0,5209 | +0,0047 |

**Dom etter #265/#281: STÅR.** Ingen av variantene når +0,02 i snitt. v1 blir identisk med lederen fordi val-året
valgte w=0 alle tre år, siden hver w>0 gjorde val dårligere. v2 valgte w=0,2 én gang (val 2024: 0,541 → 0,551), og så
falt test 2025 med 0,016 mot lederen. Det er støy på val som ikke holdt på test.
Variant «bare ny tekst» (w·sim bare der selskap+tekst mangler historikk) er verre på val i alle år og for alle w>0
(f.eks. 2025: 0,541 → 0,35 ved w=0,2). Den er rapportert som innsikt og var ikke kandidat.

Hvorfor (diagnose bare på 2023, `diag2023.log`): 552 rader med ny tekst, bare 25 sanne MOT. AUC p_avvik 0,781, sim alene
0,734, p+0,3·sim 0,801. Rangeringen blir litt bedre, men med 25 positive flytter det nesten ingen saker over terskelen.
Det lille som flyttes, er generiske styrevalg-tekster som ligner gamle MOT-er. Selskapsvis MOT-andel (AUC 0,62-0,65)
er svakere enn sim.

Lekkasjesjekk: sim for en rad i år Y bruker bare forslag fra år < Y. tfidf-vokabularet er tilpasset bare på tekster fra år < Y.
MiniLM er forhåndstrent uten fasit. MOT-settet er nbim_vote=MOT og mgmt_rec≠MOT, alt fra tidligere år. w velges på val T-1
og aldri på test. k i midt bruker antallet rå-flagg på test, ikke fasit (som #2703). Vakt-året 2023 er in-sample for w-valget
(sagt i REGEL), og w=0 der uansett.
Vær obs: 2024 og 2025 er både test-år og val-år for neste test-år (rullende), slik det også var i #2701/#2703.

Spor lukket: tekstlikhet til tidligere MOT som tillegg til p_avvik, både tfidf og MiniLM. Gjenåpnes bare med ny grunn,
f.eks. likhet til NBIMs rationale-tekster fra tidligere år (smed3 #2876 ser på retningslinjer).
Kode: `arbeid/oppgave_2875/likhet.py` (`python3 likhet.py --ny`, MiniLM: `--emb` med dommer_k44-venv), ca. 10 s / 60 s.
