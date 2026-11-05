# Case 1 natt: er +0,02 over støy? Parret bootstrap over selskaper (arkitekt #2889)

Kommando: `uv run python arbeid/c1_natt/stoytest.py frossen <svarmappe>` (4000 trekninger, frø 2889, under 1 s). Selskapene trekkes på nytt innen hvert år, og de samme selskapene brukes for begge kandidatene. Den bruker samme F1 MOT-telling som `maaler_aar.py`. Punkttallene stemmer med de pinnede (frossen 0,5057/0,5309/0,5120).
| A = frossen, B = | snitt-diff 2024-26 | 90 %-intervall | sd | andel ≤ 0 | andel ≥ +0,02 |
|---|---|---|---|---|---|
| #2701 «av» (prøven) | +0,0135 | [+0,0070, +0,0214] | 0,0044 | 0,0 % | 8,8 % |
| #2887 v2av (annen modell) | +0,0434 | [+0,0151, +0,0714] | 0,0169 | 0,4 % | 90,8 % |
- Støyen avhenger av hvor ulik kandidaten er frossen. #2701 bare fjerner flagg, så sd er 0,004 og +0,0135 er en ekte, men liten gevinst (under regelens +0,02). For en ny modell som v2av er sd 0,017. Da er ±0,028 bare støy (90 %), og +0,02 alene er IKKE over støy. v2av sitt +0,043 er det, med nedre grense +0,015.
- Hvert år for seg har mye bredere intervall (v2av sitt 2023-vaktår er [-0,022, +0,044]), så vakten på -0,02 per år slår lett ut på støy.
- Bootstrapen dekker bare utvalget av testselskaper. Spredning fra tilfeldige frø kommer i tillegg (#2886).
- Bruk i 02:00-dommen (#2874): skriv snitt-intervallet ved siden av BYTT/STÅR. Regelen er låst og endres ikke av dette.
