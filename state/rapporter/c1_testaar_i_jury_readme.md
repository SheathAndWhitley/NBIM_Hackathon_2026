# Case 1: testårskommandoen står nå i JURY.md og README (#2742)

- Ny blokk i `arbeid/hack/c1/leveranse/JURY.md` (rett under «Slik målte vi») og `README.md` (rett etter sitatblokken med hovedtall):
  kommandoen `bash arbeid/hack/c1/leveranse/verktoy/testaar.sh` kopiert ordrett fra #2733 (kald kopi), og forventet siste linje
  `F1 MOT mot styret: 2024 0.5057  2025 0.5309  2026 0.5120  snitt 0.5162`, kopiert fra en kjøring av `--rask` kl. 18:22.
- Linjene med TP/FP/FN per år er tatt ut av teksten med vilje: tallvakta leser 2024-linja som en påstand om hovedtallet (88 MOT mot 58).
  Bare sluttlinja står, og den viser tre testår og snittet.
- Tallvakt (`arbeid/verktoy/c1_tallvakt.py`): 32 filer, 0 avvik. Ingen frosne filer er rørt.
- Til #2740/#2549: zipen må bygges på nytt for at endringen skal komme med.
