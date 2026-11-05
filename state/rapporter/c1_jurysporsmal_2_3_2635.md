# Case 1 (#2635): sp. 2 og sp. 3 i JURY_SPORSMAL rettet til repo4-tall (BYTT-utgaven)

- leveranse/JURY_SPORSMAL.md sp. 2: blandede tall (finner 30, 35 falske, «alle 38» til menneske) → finner 32, 35 falske, 32 av dem til menneske, 3 uten menneske. Det siste er et ærlig funn: med repo4 går 3 falske MOT ut uten menneske (før 0).
- sp. 3: KI [0,36; 0,59]/[0,37; 0,59] → [0,40; 0,62] begge; repo4 - b2 +0,11 [0,01; 0,22] → +0,15 [0,04; 0,25]; «ikke som 0,476» → 0,512. Hybrid-sammenligningen (+0,04, +0,069, PR-AUC 0,525) er bare målt mot den frosne modellen og står nå merket slik; den er ikke målt på nytt for repo4.
- levering/JURY_SPORSMAL.md: sp. 2 var allerede repo4; sp. 3 fikk én setning om at repo4s 2026-tall var sett før regelen.
- Alle tall fra `leveranse/kilder/c1_repo4_tall_2592.md` (kald kjøring 17:03). Tallvakt: 22 filer, 175 påstander, 0 avvik. STÅR-reserven er ikke rørt.
- Ikke gjort: PR-AUC på MOT for repo4 finnes ikke i en kildefil, så den er ikke skrevet inn.
