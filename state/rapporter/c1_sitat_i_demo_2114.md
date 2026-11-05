# Case 1 (#2114, smed2): retningslinja som avgjør står i agentens svarfil og vises i demoen, kjørt fra kald kopi

**Kort:** Svarfila `agent.csv` (test 2026) har feltene `retningslinje_id`, `retningslinje_sitat` og `retningslinje_grunnlag`
for hver sak (fra #2106). `demo.sh` viser dem nå for tre saker: én MOT riktig, én MOT bom og én rutet til menneske.
Hovedtallet er uendret: **F1 MOT 0,476190** (kaldstart.sh, måler v3, avvik +0,000000).

## Kommandoer (12:46-12:48)
```
sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_demo_2114        # fremmed.sh kald kopi + agent + demo_vis under env -i, 37 s
env -i HOME=$HOME PATH=/opt/homebrew/bin:/usr/bin:/bin:$HOME/.local/bin bash arbeid/hack/c1/kaldstart.sh   # GRØNN, 52 s
```
- sha256 på svarfila fra kald kopi (`/tmp/c1_demo_2114/ut/agent.csv`):
  `55a53eecf608d80034d3bba90f7e7bc75cacd91dc83e17858af7b1551fb27920`, byte-lik den varme kjøringen i #2106.
- kaldstart.sh: `GRØNN F1_MOT 0.476190 REF 0.476190 AVVIK +0.000000` (TP 30, FP 38, FN 28, 58 MOT i fasit v3).
- Demoens egen telling på real_votes (1539 saker med fasit, 66 MOT) gir F1 0,4818. Det er samme tall som før #2114
  (demo #2093). Forskjellen mot 0,476 er fasitutvalget (måler v3 har 58 MOT), ikke modellen.

## Endring
Bare `arbeid/hack/c1/leveranse/demo_vis.py`: sak 3 er nå «MOT bom» (agenten MOT, ikke rutet, NBIM fulgte styret) i stedet
for en FOR-sak, og hver sak skriver `RETNINGSLINJE <id>: «sitat»` + grunnlag. Det gamle sitatet heter nå
«tidligere NBIM-begrunnelse», fordi det er en begrunnelse fra et tidligere år, ikke selve retningslinja.
Sakene trekkes fortsatt med seed 0, ikke håndplukket. Full utskrift: `arbeid/hack/c1/leveranse/demo_utskrift.txt`.

## De tre sakene
1. **MOT riktig**: 2087754|4 PT Solusi Sinergi Digital, «Approve Auditors and Authorize Board to Fix Their Remuneration».
   Agent MOT (score 0,99). **NBIM 5.1.2**: «Excessive non-audit-related fees represent a potential conflict of interest
   and should be avoided.» NBIM stemte Against med begrunnelse fra GVG 5.1. Treff.
2. **Rutet til menneske**: 2089598|4 Klarna Group, «Ratify Ernst & Young LLP as Auditors». Agent FOR (score 0,25),
   til menneske fordi selskapet er ukjent (ingen NBIM-stemmer før møtedatoen). **NBIM 0.0.3**: «Our starting point
   when deciding how to vote is to support the board.» NBIM stemte For.
3. **MOT bom**: 2091877|2 Meidensha Corp., «Elect Director Miida, Takeshi». Agent MOT (score 0,97), ikke rutet.
   **NBIM 1.1.2** (uavhengighet), fordi NBIM stemte mot samme person i 2023. NBIM stemte For i 2026.
   Ærlig lesning: sitatet er plausibelt, men historikken slo feil. Høy score er ikke nok til å være sikker, og
   rutingen fanger ikke denne typen bom (8 slike blant de ikke-rutede MOT-bommene i kategorien).
