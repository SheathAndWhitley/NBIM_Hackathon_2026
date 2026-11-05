# Case 1: hvor bommer frossen #2044 på stemmer MOT styret (#2569)

Kilde: `arbeid/oppgave_2496/full_{2024,2025,2026}_test.csv` mot arrangørens fil (sha 71ba51…). Målerens linje
«MOT mot styret» gjenskapt: F1 0,4545 / 0,5143 / 0,4762 (TP 30/45/30, FP 14/31/38, FN 58/54/28).
Kode: `arbeid/oppgave_2569/bommer.py` (gruppering), `siste.py` (regel), `boot.py` (KI). Rader: `rader.csv`.
«Historikk» = NBIMs stemmer i år før teståret (rullende, samme info som modellen har).

## Topp 3 mønstre (antall per år 2024/2025/2026)
1. **Agenten er i praksis en «samme tekst var MOT før»-detektor.** TP med tidligere MOT på samme
   tekst: 26/41/26 av 30/45/30. FN uten slik teksthistorikk: 37/48/23 av 58/54/28. Nye MOT-er
   (første gang NBIM sier MOT på teksten) fanges nesten aldri (TP 4/4/4).
   Mest styrevalg: FN DIRECTOR_ELECTION 28/34/13; uten teksthistorikk 22/34/11.
2. **Gamle MOT-er som NBIM har sluttet med gir FP, og de øker.** FP med tidligere MOT på teksten:
   12/24/22 av 14/31/38. FP på styrevalg 12/23/26, mest DM (FP DM 11/26/26 mot EM 3/5/12).
   Eks.: Colruyt FP 0/0/4, Dell 2/2/2, Nomad 2/2/1.
3. **Hele møter med flere MOT bommes samlet.** FN i møter med ≥2 sanne MOT: 30/35/11. Mest EM
   (FN EM 29/22/13), Kina 12/2/3 (Lepu Medical 6 i 2024), India 5/14/3, Fluence 0/8/0. Say-on-pay FN 11/4/0.

## Målt trekk: regel «siste stemme var FOR» (ingen terskel, ingen parameter)
Fjern MOT-flagget når NBIMs **siste** stemme på samme tekst i samme selskap i tidligere år var FOR.

| testår (val) | val frossen → regel | test frossen → regel | FP fjernet / TP tapt (test) |
|---|---|---|---|
| 2024 (2023) | 0,361 → 0,379 | 0,455 → 0,472 | 8 / 1 |
| 2025 (2024) | 0,536 → 0,559 | 0,514 → 0,531 | 11 / 2 |
| 2026 (2025) | 0,520 → 0,534 | 0,476 → **0,522** | 11 / 0 |

Bedre på alle tre val-årene, så valget er tatt på val. Testårene ble lest først etterpå.
Tre testår samlet: 0,485 → 0,510. Parvis bootstrap over møter (2000 trekk): +0,025, KI95 [+0,006; +0,044], P(>0) 0,99.
Liten effekt, men den har samme retning overalt og er nesten bare færre FP på styrevalg.

Prøvd, men ikke verdt det:
- *Møtesmitte*: senk grensen for andre saker i et møte der én sak er flagget. Beste q på val ga
  ingen gevinst eller ble dårligere (2023: 0,361 → 0,337). Sporet er lukket.
- *Legg til flagg når siste stemme var MOT* («paa»): bedre på val bare i 2023, dårligere i 2024 og 2025. Sporet er lukket.

## Til smed4/arkitekt (#2567/#2568), kan måles før 17:45
Legg regelen inn som etterbehandling i målebenken: `python3 -I arbeid/oppgave_2569/siste.py` kjører alle
tre årene på val og test (ca. 5 s). Som trekk i modellen: `siste_stemme_samme_tekst ∈ {MOT, FOR, ingen}`.
Merk: dette er etter frysen kl. 16. Det er et kandidattall og ikke hovedtallet, med mindre noen bestemmer det.
