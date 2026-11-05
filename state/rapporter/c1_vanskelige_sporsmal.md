# Case 1: de tre vanskeligste jury-spørsmålene, korte svar med kilde (speider, #2373, 05.11 kl. 15.10)

Ingen nye tall: hvert tall står i kilden i parentes. Stier under `arbeid/hack/c1/leveranse/` med mindre annet står.
Utvalgt fra de ti i `JURY_SPORSMAL.md`: dette er de tre der svaret må innrømme en svakhet, og der en kritisk jury kan felle oss hvis svaret er vagt.

## 1. «Dere bruker NBIMs stemmer fra samme sesong. Er ikke det lekkasje?»
Historikken bruker bare møter strengt før sakens dato, og brute force-sjekk på 400 tilfeldige rader ga 0 avvik (`ERLIG_EVALUERING.md:28-29`). Vi antar at stemmene er kjent løpende, og den antakelsen har ingen kilde i pakka (`JURY_SPORSMAL.md`, «Hull vi kjenner»). Uten den faller F1 på MOT fra 0,476 til 0,415 [0,30; 0,53], og det er golvet vi oppgir (`JURY.md`, Begrensninger pkt. 7; `kilder/c1_enkle_regler_og_hist1.md`). Også golvet slår den beste enkle regelen b2 (0,365) (`JURY.md`, tabellen «Slår dere noe enkelt?»).

## 2. «Målet var 0,5, dere har 0,476, og et nytt forsøk ga 0,500. Hvorfor ikke ta det?»
0,476 er testtallet til den frosne agenten: grensa er valgt på val 2025 (0,520), test 2026 er kjørt én gang, 95 % KI er [0,36; 0,59], og forspranget på regel b2 er +0,11 [0,01; 0,22] (`JURY.md`, «Les dette først» og tabellen; `kilder/c1_val_kaldstart.md`). Forsøket med nyeste historikk (A+B) ble valgt på val og godkjent i lekkasjesjekken, og på test ga det 0,500, men det er bare 1 treff mer og 3 falske MOT færre, godt innenfor støyen (bootstrap ±0,1) (`state/rapporter/c1_lekkasje_2363.md` pkt. 3; `state/rapporter/c1_beslutning_nyeste_historikk.md` pkt. 5–6). PR-AUC gikk ned fra 0,525 til 0,509, så rangeringen ble ikke bedre (samme kilder). Dommeren valgte det bort (#2366): gevinsten på val 2025 og val 2024 er ikke skilt fra støy, så den frosne agenten (#2044, 0,476) står som levert, og 0,500 er ført som verifisert, men ikke levert (`state/rapporter/c1_beslutning_nyeste_historikk.md` pkt. 8–10).

## 3. «Hva gjør agenten når den er usikker, og hvilke feil ser ingen?»
Den sender 188 av 1578 saker (11,9 %) til et menneske: kalibrert P(MOT) i [0,15; 0,85), ukjent selskap eller instruks i teksten (`state/rapporter/c1_til_menneske_tall.md`). Båndet ble valgt fra en tabell på test 2026 og bare sjekket på val, og det sier vi rett ut (`ERLIG_EVALUERING.md:44`). Den største svakheten er de stille bommene: 17 av 28 oversette MOT får P(MOT) ≤ 0,09 og når aldri et menneske, blant dem 0 av 7 MOT i USA (`kilder/c1_bommene.md`; `JURY.md`, Begrensninger pkt. 3–4). Derfor er agenten en sorteringshjelp og ikke en automatisk stemme, og å rute de stille bommene er første tiltak med én uke til (`JURY.md`, Juryspørsmål 2 og 3).

## Til den som oppdaterer etter frysen (#1975)
- Svar 2 er skrevet om etter dommen i #2366 (A+B valgt bort, `c1_beslutning_nyeste_historikk.md` pkt. 8–10). Hovedtallet 0,476 i svar 1 og 3 står uendret; ingen nye tall er lagt til (#2383).
- I svar 3 bruker jeg 188 av 1578. Måleren sier 183 av 1539 med fasit, og begge tallene er riktige (`c1_til_menneske_tall.md`). Bruk den samme nevneren overalt i ett og samme svar.
