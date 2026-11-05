# Arkitekt #1942 (avbrutt ved hack-omstart): NBIMs egne stemmer finnes åpent i SEC N-PX

Casen (05.11): to NBIM-caser, juryvurdert (30 % problemforståelse, 30 % evaluering, 20 % forklarbarhet, 20 % robusthet). Frist fre 06.11 kl. 12.

**Funn (case 1, stemmeagent):** Norges Bank (CIK 1374170) leverer selv N-PX til SEC (2024, 2025, 2026),
fordi 13F-forvaltere må rapportere say-on-pay-stemmer. Altså NBIMs EKTE stemmer som åpen fasit, ikke en amerikansk
erstatningsforvalter. Arrangøren sier NBIM-databasen er stengt; de har trolig ikke sett dette.
- Hentet og parset: `arbeid/arkitekt/hack1942/parse_nbim.py`, `nbim_votes.csv` (4857 stemmer, rådata i `data/`).
- Mot styret: 2024 13,3 % (251/1882, mye «ONE YEAR» frekvensstemmer), 2025 7,0 % (113/1621), 2026 7,8 % (106/1354).
  Gulv = «alltid som styret»: recall MOT 0. KP: casen sier 94 % med styret i 2025, vi fikk 93,0 % på say-on-pay. OK.
- Naturlig tidssplitt: tren 2024, valider 2025, test 2026.
- I tillegg: 11 PX14A6G (exempt solicitations) fra Norges Bank = NBIMs skriftlige begrunnelser, kan siteres.
- Vær obs: noen rader har styret=AGAINST (f.eks. Snowflake) — sjekk feltet før målet defineres.

SEC svarer med generisk User-Agent (200 OK). Anbefaling: velg case 1 med NBIMs egne N-PX-stemmer som fasit.
