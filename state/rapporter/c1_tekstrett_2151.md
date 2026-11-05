# Case 1: to tekstsvar rettet i 1-siden og kravresponsen (speider #2151, 05.11 kl. 13.15)

## Rettet
1. `arbeid/hack/levering/EN_SIDE.md:23-24`: «standard 10 % av val-sakene, justerbart med `--til-menneske PROSENT`»
   → «Usikre saker: kalibrert P(MOT) i båndet [0,15; 0,85), låst på val 2025 (`--baand`; den gamle prosentregelen
   fås med `--til-menneske PROSENT`)». Totalen 188 av 1578 (11,9 %) sto allerede riktig på linje 26.
2. `arbeid/hack/c1/leveranse/kravrespons.md:4` (samme feil i jury-1-sideren, funnet underveis): «bånd ... standard 10 %
   ... 228 av 1 578 (14,4 %)» → «kalibrert P(MOT) i båndet [0,15; 0,85) ... 188 av 1 578 (11,9 %)».
3. `arbeid/hack/c1/leveranse/kravrespons.md:20`, krav 14 (hva vi trenger videre): én setning om lesetilgang (API) til
   NBIMs stemmedatabase med flere års stemmer og begrunnelser.
4. `arbeid/hack/c1/leveranse/kravrespons.md:20`, krav 20 (praksis mot policy): én setning. Vi har bare målt det indirekte:
   GVG-punktet agenten siterer er samme seksjon som NBIM selv oppga i 86 % av MOT-sakene 2026 (#2106). Det er ikke testet
   om NBIM stemmer slik retningslinjene sier i saker der de følger styret.
Ingen nye tall om hovedtallet. fremmed.sh er ikke rørt.

## Tallvakta
- Mot kald kjøring (#2127): `python3 -I arbeid/verktoy/c1_tallvakt.py --svar /tmp/c1_kald6_2127/ut/pred_maaler.csv --kjoring /tmp/c1_kald6_2127/ut/KJORING.txt`
  → **GRØNN**, utgang 0: F1 0,4762, TP 30 FP 38 FN 28, til menneske 188 av 1578; 13 filer, 129 påstander, 0 avvik.
- Uten argumenter er vakta **RØD** (22 avvik, alle «til menneske 188/183, måleren sier 228/223»). Grunnen er at standardloggen
  `arbeid/hack/levering/kjor_agent_real_test2026.txt` (12:38) er fra før det kalibrerte båndet og sier 228 (14,4 %).
  Teksten i pakka er riktig; loggen i repoet er gammel. **Må rettes før 19:30** (ny agentkjøring som skriver loggen, eller
  vakta peker på kald kopis KJORING.txt). fremmed.sh kjører vakta på kopiens egen kjøring og blir derfor grønn. Eier: #2150 (arkitekt).
