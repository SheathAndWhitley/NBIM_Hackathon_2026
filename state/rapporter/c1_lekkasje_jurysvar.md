# Case 1 (#2746): lekkasje-effekten skrevet inn i pakka

- `c1/leveranse/KANDIDATER.md`: nytt underavsnitt «Effekt av samme-dags-fiksen (#2744)» under lekkasjesjekken: per år 0,5057→0,4973, 0,5309→0,5153, 0,5120→0,5636; snitt 0,5162→0,5254 (+0,009). 0/0/1 flagg endret på berørte rader; flytt skyldes nytt C/grense-valg. Kvalifiserer ikke etter #265. Levert modell står.
- `c1/leveranse/JURY_SPORSMAL.md`: nytt sp. 24 «Er det lekkasje i historikktrekkene?», kort svar med de samme tallene.
- Kilde kopiert: `c1/leveranse/kilder/c1_lekkasje_effekt.md`.
- Idempotent rettskript: `arbeid/oppgave_2746/rett.py` (kjør på nytt hvis jury-zipen bygges fra en eldre kopi).
- Tallvakt: 196 påstander, 0 avvik. Ingen modellendring.
- Merk for #2740 (smed2): zipen må bygges etter denne commiten for å få med sp. 24.
