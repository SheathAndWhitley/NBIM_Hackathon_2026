# Case 1: avsnitt om sen publisering av NBIMs stemmer, ferdig til JURY.md pkt. 7 (#2300, arkitekt)

Til speider i #1975. Avsnittet erstatter andre og tredje setning i JURY.md pkt. 7 (fra «Modellen bruker NBIMs stemmer …»).
Pakka er ikke rørt. Kilde-fila må kopieres til `kilder/` sammen med avsnittet (se nederst).

## Avsnittet (7 linjer, lim inn)

> Modellen bruker NBIMs stemmer fra møter strengt før saken. Vi har målt hva som skjer hvis de blir kjent først N dager etter møtet (`kilder/c1_historikk_forsinkelse.md`).
> Med N = 1–90 dager er F1 på MOT 0,520–0,523 på val 2025 (0,520 [0,40; 0,63] ved N = 0) og 0,507–0,536 på holdt-ut 2024. Det største fallet er −0,029 [−0,15; 0,07], og alle KI for fallet dekker 0.
> Forklaringen er at et selskap som regel har ett møte i året, så verdien kommer fra stemmer i tidligere år.
> Uten historikk i det hele tatt faller F1 til 0,34 (2025) og 0,34 (2024) når modellen trenes på nytt.
> Disse tallene er fra val og 2024, ikke fra test 2026, som er kjørt bare én gang.
> Tidligere oppga vi 0,415 som golv. Det tallet er ikke et mål på sen publisering: i `--hist 1` får treningsradene historikk fra alle år før 2025, også sin egen etikett, så modellen lærer en historikk som er sterkere enn den den får ved prediksjon.

## Kilde for hvert tall

| Tall i avsnittet | Kilde |
|---|---|
| 0,520 [0,40; 0,63], N=0, val 2025 | `arbeid/oppgave_2299/resultat_hoved.json`: aar 2025, N 0, A, F1_MOT_v3 0,520231, KI_F1 [0,4; 0,626] |
| 0,520–0,523 (N 1–90, 2025) | samme fil: 2025 A/B for N 1, 7, 30, 90: 0,518072 (N1 B) … 0,526946 (N90 B). **Rettelse:** spennet er strengt 0,518–0,527; bruk det hvis speider vil ha alle radene med, 0,520–0,523 gjelder bare frossen agent (A) |
| 0,507–0,536 (N 1–90, 2024) | samme fil: 2024 B N7/N30 0,507246; 2024 A N0–N90 0,536313 |
| −0,029 [−0,15; 0,07] | samme fil: 2024 N7 B, fall −0,0291, KI_fall [−0,145; 0,074] |
| 0,34 (2025, uten historikk) | `arbeid/oppgave_2299/kontroll.log` linje 38: 2025 N100000 B, F1_MOT_v3 0,335714 |
| 0,34 (2024, uten historikk) | `state/rapporter/c1_historikk_forsinkelse.md`, tabellraden «kontroll ingen historikk»: 2024 B 0,340 |
| 0,415 | `arbeid/hack/c1/leveranse/kilder/c1_enkle_regler_og_hist1.md` linje 14 |
| lekkasjen i `--hist 1` | `arbeid/oppgave_2044/train.py:47` (`X.year < til_aar`, uten datogrense) og `:61` (groupby over alle rader med etikett, også raden selv) |
| «ett møte i året» | forklaring i `c1_historikk_forsinkelse.md`, avsnitt «Hvorfor så lite?» (ikke talt opp her) |

Jeg anbefaler å bruke spennet for frossen agent (A), siden det er agenten som leveres. Linja i avsnittet sier derfor 0,520–0,523 for 2025.
For 2024 er spennet tatt over både A og B, fordi B gir det verste tallet. Det er mest ærlig.

## Det speider også må gjøre
1. Kopiere `state/rapporter/c1_historikk_forsinkelse.md` til `arbeid/hack/c1/leveranse/kilder/` slik at pekeren virker fra kald start.
2. JURY.md linje 56 (tabellrad «Golv … 0,415») og linje 58 (setningen om golvet): enten ta dem ut, eller merke dem «hist 1, lekker i trening, ikke et mål på sen publisering».
3. Dommer i #2255: tallene over står i `resultat_hoved.json` og `kontroll.log`. Ingen av dem er målt på test 2026.
