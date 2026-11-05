# Case 1: utkast til juryavsnitt om frøfølsomhet (#2935, ikke lagt i repoen)

Status: utkast. Dommeren avgjør ved 02-dommen om det skal inn i README. Kilder: c1_plattformavvik.md (#2918),
c1_frospredning_tidsvekt_av.md (#2920), c1_frosnitt_v2av.md (#2926). c1_frossen_frospredning.md (#2933) finnes ikke ennå.
Når den kommer, byttes linja merket [#2933] ut med snitt (sd) og min–maks for frossen over 5 frø.

## Avsnittet (12 linjer, til README under «Mac og Linux gir litt ulikt tall»)

**Hvor sikkert er 0,512?** Agenten bruker en modell med litt tilfeldighet når den trenes (LightGBM-«frøet»).
Vi har trent den frosne agenten på nytt med tre andre frø, uten å endre noe annet. Da ble F1 MOT for 2026
0,531, 0,530 og 0,571 i stedet for 0,512. Linux-tallet 0,520 ligger inne i det samme spennet.
Hva det betyr i saker: 2026 har 58 stemmer mot styret, og én sak som havner på andre siden av grensen flytter
F1 med omtrent 0,005–0,01. Spennet 0,51–0,57 tilsvarer altså noen få saker, ikke en annen agent.
Ærlig lest: forskjeller under ca. ±0,02 mellom to varianter kan være tilfeldighet. Derfor krever vi +0,02 i snitt
over tre testår før vi bytter modell, og vi måler nye kandidater med 5 frø (sd for snittet 0,005–0,009).
[#2933: den frosne agenten med 5 frø: snitt X (sd Y), min–maks A–B.]
Hvorfor vi oppgir 0,512 og ikke 0,571: modellen ble frosset kl. 16 før vi så testtallet. Å velge det frøet som
gir best testtall, er å velge etter fasiten. Det blåser opp tallet og sier ingenting om neste år. 0,512 er det
laveste av de fire kjøringene vi har. Hovedtallet er altså ikke pyntet. Tallet forvalteren bør regne med, er
«rundt 0,51–0,57». Tallet vi lover, er 0,512.

## Notater til dommeren
- Kontrollpunkt: 0,512 / 0,5312 / 0,5303 / 0,5714 og TP 32 FP 35 FN 26 sjekket mot c1_plattformavvik.md og README linje 29.
  KP: forventet 0,512 i README, fikk 0,512.
- «0,005–0,01 per sak» er et overslag fra #2926 (≈0,005 per år med ~90 MOT) og #2918 (1–2 rader ≈ 0,008). Det er ikke målt
  per rad for 2026.
- Setningen «laveste av de fire» må sjekkes på nytt når #2933 kommer. Hvis et frø gir under 0,512, skriv «i nedre del».
- Gammel bootstrap-KI [0,36; 0,59] i c1_seed_frossen.md gjelder en eldre modell (#2044) og er derfor ikke brukt her.
