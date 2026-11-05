# Case 1: figur for juryen, rullende F1 MOT per år, frossen mot personnøkkel (sak 2497)

**Figur:** `arbeid/oppgave_2497/c1_personnokkel_rullende.png`, laget av `arbeid/oppgave_2497/lag_figur.py`.
Skriptet leser tallene rett fra tabellen i `state/rapporter/c1_personnokkel_rullende.md` (sak 2496), ingen tall
skrevet for hånd. Det stopper (assert) hvis tabellen ikke har tre år med uten, + person og KI.

Innhold: år 2024–2026 på x (val-år under), F1 MOT på y. Blå = frossen (0,4545 / 0,5143 / 0,4762),
oransje = + personnøkkel (0,4179 / 0,5155 / 0,5254). Strek = 95 % KI for person − uten
(−0,037 [−0,133; +0,058], +0,001 [−0,042; +0,050], +0,049 [+0,016; +0,090]) lagt på «uten»-punktet.
Stiplet linje: «følg styret» = 0. Tittel og fotnote sier «ikke hovedtall»; hovedtallet er frossen 2026 = 0,4762.

**Hvor:** Hele `c1/leveranse/` (også `kilder/`) står i frysfasiten, så en ny fil der ville gitt `NY` i frys_diff.
Figuren ligger derfor i `arbeid/oppgave_2497/`.

**Peker:** én linje i `arbeid/hack/c1/leveranse/NESTE_VERSJON.md` rett under sak 2496-punktet.

**Sjekker:** tallvakta på NESTE_VERSJON.md før og etter: 0 avvik (2 påstander om hovedtallet).
`frys_diff.sh --kilde`: FRYS AVVIK 1, ENDRET NESTE_VERSJON.md. Fila var alt endret og ikke committet av andre
(sak 2490, 2496, 2495/2498-punktene) før min linje. Jeg har ikke regenerert fasiten og ikke committet
NESTE_VERSJON.md, fordi endringene er andres. Den som dømmer/committer tekstene (#2500) må regenerere fasiten.

Kjør på nytt: `uv run python arbeid/oppgave_2497/lag_figur.py`
