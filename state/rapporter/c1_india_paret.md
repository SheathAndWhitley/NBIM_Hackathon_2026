# Case 1: er India-gevinsten mer enn tilfeldighet? Paret test (#2311, smed2)

**Hva:** Paret klyngebootstrap (10 000 trekk, seed 0) og paret permutasjon (bytt PÅ/AV innen hver klynge) av
F1 MOT-mot-styret (= v3 `--score mot`), India-bryter PÅ minus AV. Filer fra `arbeid/oppgave_2303/`. Klynge per
selskap og per møte, som i `c1_bootstrap_f1.md`. Test 2026 er ikke brukt.
**Skript:** `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2311/paret.py` (utdata `arbeid/oppgave_2311/ut.txt`).
Punkttallene er lik v3-måleren via `oppgave_2303/maal_aar.py` (2024: 0,5444 / 0,5363; 2025: 0,5618 / 0,5202).

| År | F1 PÅ | F1 AV | Δ | 95 % KI (selskap) | 95 % KI (møte) | PÅ taper | lik | perm p (selskap / møte) | rader som skiller |
|---|---|---|---|---|---|---|---|---|---|
| 2024 (holdt ut, trent <2024) | 0,544 | 0,536 | **+0,008** | [0,000; +0,028] | [0,000; +0,028] | 0,000 | 0,364 | 1,00 / 1,00 | **1** (riktig) |
| 2025 (regelen funnet her) | 0,562 | 0,520 | **+0,042** | [+0,009; +0,082] | [+0,009; +0,083] | 0,000 | 0,006 | 0,063 / 0,066 | **5** (alle riktige) |

## Slik leses det
- **Regelen snur få saker.** 2024: 1 sak. 2025: 5 saker i 5 ulike møter og selskaper. Alle er India, styret FOR, NBIM MOT
  (4 OTHER_MGMT, 1 styrevalg). Selskap 560207 er med begge år. Ingen snudd sak var feil.
- **«PÅ taper 0 %» er ikke bevis.** Bootstrap kan bare trekke de snudde sakene på nytt. Er alle riktige, kan PÅ aldri tape.
  Intervallet sier at regelen ikke gjorde skade i disse dataene, ikke at den vil virke.
- **Permutasjonen er den ærlige testen.** 2024: p = 1,0. Én sak kan ikke skille regel fra tilfeldighet.
  2025: p ≈ 0,06 (= 2/2⁵, fem riktige av fem). Det er ikke under 0,05, og 2025 er året regelen ble funnet på, så p-en er optimistisk.
- **Konklusjon:** Gevinsten er ikke vist å være mer enn tilfeldighet. Retningen er lik begge år og ingen snudde saker er feil,
  men det holdt-ut beviset er én sak. Forventet gevinst på nye data er liten (2024: +0,008) og usikker.
  Mitt råd til dommeren (#2297): ikke bytt agent ved frys på grunnlag av dette. Bruk det heller i juryen som et ærlig eksempel på en regel
  vi testet og valgte bort fordi beviset var for tynt.

**Dom (dommer2, #2315, 05.11 14:50): GODKJENT.** Kjørt på nytt fra kommandoen over: alle tall identiske (Δ, KI, perm p, antall snudde rader), v3-punkttallene stemmer (0,5444/0,5363, 0,5618/0,5202), treningsvinduet er år < valår, `--kun-val 1` stopper før test 2026, og India-regelen bruker ingen etiketter.
