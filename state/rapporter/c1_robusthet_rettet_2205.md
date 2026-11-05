# Case 1: robusthetsfunnene fra #2202 rettet og testet med 10 nye rare filer (#2205)

**Status:** Ingen krasj. Alle rare saker får enten et gyldig svar (FOR/MOT/AVSTÅ) eller går til menneske. Test 2026 gir samme resultat som før, tall for tall.

**Rettet her (bare i agent-laget, `arbeid/hack/levering/c1_real.py`, modellen er ikke rørt):**
- Svakheten #2202 lot stå: styret «Kanskje» skrev `KANSKJE` som stemme i agent.csv. Nå står det `anbefaling=TIL MENNESKE` når
  styrets verdi ikke er FOR/MOT/AVSTÅ, både for vurderte saker og for saker som ikke kunne vurderes (ny konstant `GYLDIG`). Rutingen var allerede på plass fra #2202.
- De tre stille gjennomslagene fra #2202 (ukjent land, dato 2099 og «Kanskje») var allerede rettet i #2202, og de er sjekket på nytt her.

**Nye rare filer (utfordrer-vinkel: filformat, ikke feltverdier), `arbeid/oppgave_2205/saker/`:**

| sak | utfall |
|---|---|
| 21 bare header | 0 saker, rc 0 |
| 22 BOM i header | lest riktig, FOR, maskin |
| 23 kolonnen proposal_type mangler | menneske: «mangler felt» |
| 24 samme id to ganger | første vurderes, den andre går til menneske som «duplikat» |
| 25 mgmt_rec «against» (små bokstaver) | lest som MOT, svar MOT (følger styret) |
| 26 item_no «1.0» | menneske: «ikke heltall» (strengt, men trygt) |
| 27 dato med klokkeslett | menneske: «ugyldig møtedato» (strengt, men trygt) |
| 28 dato 1990 | menneske: ukjent selskap og dato utenfor perioden |
| 29 fasitkolonne nbim_vote i inndata | hele fila avvises med vilje, rc 1: «inn-saken har fasitfeltet «nbim_vote»; fjern det» (lekkasjevern, ikke krasj) |
| 30 semikolon som skilletegn | menneske: «mangler felt» (fila blir ikke lest feil i stillhet) |

**Kontroll:** Full kjøring på test 2026 (1578 saker) gir `pred_maaler.csv` byte-lik med kjøringen etter #2202. I agent.csv er id, anbefaling, mot_styret, til_menneske og p_mot like: 0 avvik.
Måleren i denne kjøringen gir F1 0,4818 (TP 33, FP 38, FN 33), samme som før endringen. Kravet sier 0,476. Det tallet er ikke gjenskapt
her (antakelig en annen kjøring eller et annet vindu), men endringen flytter ingen prediksjoner.

**Kjente svakheter (ikke rettet, bevisst):** `1.0` og ISO-dato med klokkeslett går til menneske i stedet for å normaliseres.
Semikolonfil blir ikke tolket, den rutes. En fil med fasitkolonne stoppes helt i stedet for at kolonnen fjernes.

**Gjenskap:** `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --csv arbeid/oppgave_2205/saker/<sak>.csv --ut /tmp/u`
(versjonen før endringen ligger i `/tmp/c1_real_for_2205.py`. `arbeid/` er git-ignorert, så det ble ingen commit.)
