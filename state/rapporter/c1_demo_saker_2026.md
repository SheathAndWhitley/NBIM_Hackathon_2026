# Case 1: demo-saker trukket tilfeldig fra test 2026 (speider #2070)

Manus: `arbeid/hack/c1/DEMO_MANUS.md` (5 min). Gjenskap: `bash arbeid/hack/c1/demo_saker_2026.sh` (15 s, kald start, verifisert 12.20).
Trekk: `arbeid/hack/c1/demo_trekk_2026.py`. Gammelt utkast (N-PX, VAL 2025): `DEMO_MANUS_npx_utkast.md`.

**Trekk:** 1539 saker med fasit i test 2026, `default_rng(seed).choice(1539, 5)`. Krav: ≥2 fasit MOT, ≥1 rutet.
Seed 0–16 forkastet, **seed 17** OK: 2056685|7, 2084542|6, 2089598|12, 2041102|2, 2039527|11.
Kald kjøring på bare de 5 ga identisk utdata med kjøringen på hele 2026.

| sak | agent | score | menneske | fasit |
|---|---|---|---|---|
| Hainan Jinpan, vedtekter | FOR | 0,912 | ja (nær grense 0,919) | For |
| Arbonia, ikke-fin. rapport | FOR | 0,262 | nei | For |
| Eximbank, styreforsikring | FOR | 0,636 | nei | For |
| Nomad Foods, styrevalg | FOR | 0,451 | nei | **Against (bom)** |
| Klarna, emisjon uten fortrinnsrett | FOR | 0,257 | nei | **Against (bom)** |

Funn:
1. Ærlig og ubehagelig: agenten bommer på begge MOT i trekket (recall 0,50 på hele 2026, så det er ikke rart).
   Ingen av de 5 får NBIM-sitat, fordi sitat bare gis ved MOT. Sitatet vises derfor med en egen trukket sak
   (seed 0 blant de 71 agent-MOT): TV TOKYO, styrevalg, MOT 0,970, GVG 1.1-sitat fra NBIMs begrunnelse i 2023, fasit Against.
2. `p_mot` i agent.csv er et rangsnitt (logreg ⊕ LightGBM, train.py l. 92), ikke en kalibrert sannsynlighet.
   Står det «P(MOT)» i JURY.md eller UI-et, er det feil. Manus kaller det MOT-score.
3. Emisjon uten fortrinnsrett (Klarna) har en tydelig NBIM-policy, men modellen gir den 0,26. Kandidat for feilanalysen (#2072).
4. Seed 17 avhenger av rutingen. Etter frysen må trekket kjøres på nytt, og den nye første gyldige seeden brukes (står i sjekklista).
