# Case 1 leveranse 1 (c1_v1): hel kjøring fra kald start, dommer #1952, 05.11 ca. 12:55

> **Eldre leveranse (v1, 05.11 kl. 12:55), ikke gjeldende.** Tallene under er fra den første modellen (#2044) og er erstattet. Gjeldende hovedtall står i `README.md` på rota av repoen og lages av `sh KJOR.sh` (linja `HOVEDTALL`). <!-- tallvakt: ignorer: eldre v1 -->

Hovedtall i v1 (eldre): F1 **0,4762 på MOT mot styret**, test 2026 (real_votes, 1539 saker med fasit, 58 MOT), TP 30 FP 38 FN 28. <!-- tallvakt: ignorer: eldre v1 -->
Frossen modell #2044 miks h2. Måler `arbeid/hack/c1/maaler_offisiell_v3.py --score mot` (sha256 8b09c36e01).

Gjenskap fra landsbymappen (ett av disse):

    bash arbeid/hack/c1/kaldstart.sh                 # kopierer, uv sync --frozen, kjører, måler, GRØNN/RØD
    sh arbeid/hack/levering/fremmed.sh /tmp/fremmed  # README-kallet; mål ut/pred_maaler.csv med v3 --score mot

Innhold:
- `kravrespons.md`: kravresponsen med ekte tall (også kopiert til `c1/leveranse/kravrespons.md`)
- `ut/`: agent.csv (1578 saker, sitat og ruting), pred_maaler.csv (sha256 2e061f0fb0da9267…), _pred_uten_ruting.csv, KJORING.txt, agent.log
- `kaldstart.log` (GRØNN, 52 s), `fremmed.log` (README-kallet, 32 s, identisk pred_maaler.csv)
- `kaldstart_forsok1_feil.log`: første forsøk 12:44, RØD (retningslinje_oppslag.py manglet i kopien, rettet 12:44)
- `hist_regel.py`: historikkregel-baselines (F1 MOT 0,091 og 0,145)
