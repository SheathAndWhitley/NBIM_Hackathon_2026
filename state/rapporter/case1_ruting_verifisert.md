# Case 1: rutingstallene til smed2 (#1955) kontrollert fra kald start, med variant b (dommer2 #1995)

**Kort fortalt:** smed2s tall reproduseres bit for bit, men de gjelder den gamle modellen med lekkasje. På variant b er gevinsten fra det symmetriske båndet omtrent halvparten så stor. Ved 10 % ruting stiger maskinens MOT-presisjon fra 0,38 til 0,43, ikke til 0,50. Det skjeve båndet holder seg: system-F1 er 0,65 mot smed2s 0,66. **Til juryen skal variant b-tallene under brukes, ikke tallene fra #1955.**

## Metode
- Rå score fra frosset variant b (`oppgave_1993/train_v3_g.py`, `PVP_DAGER=100`, `--drop s_float,g_sbc_vs_float,s_lonn_vs_storr`, 5 frø). Val er trent på 2024 og predikert på 2025. Test er trent på 2024+2025 og predikert på 2026.
- Kjørt fra kald start: `env -i`, tom mappe og nohup (`arbeid/oppgave_1995/kald.sh /tmp/rut1995`).
- Rutingskoden har jeg skrevet på nytt selv (`ruting_b.py`), etter oppskriften i `ruting.py` og `ruting_skjev.py`. Alt låses på val 2025 og skrives til `laast_paa_val.json` før test leses: isotonisk kalibrering, grense, bånd og c i det skjeve båndet. Test er kjørt én gang.
- Grensen er den samme som i hovedtallet (#1993), 0,183297. Test-F1 uten ruting blir 0,474, akkurat som hovedtallet, så kjeden stemmer. Med smed2s rutenett for grensen (0,182675) flytter tallene seg høyst ±0,02.
- Systemtallene forutsetter at mennesket avgjør alle rutede saker riktig, så de er en **øvre grense**.

## Steg 0: reproduksjon av #1955 som den står
Jeg kjørte `ruting.py` og `ruting_skjev.py` i en kopi i /tmp, med `env -i`. Alle testtallene i `case1_ruting.md` ble identiske: grense 0,2031, ECE 0,013, rader for 0/5/10/20 % og skjev c* = +0,25/+0,75/+1,00. **Tallene er altså ekte for modellen de ble kjørt på.** Den modellen er `ruting.raa()`, med alle kjennetegn, også `s_float` og PvP med 20 dagers grense. Det er den lekkende fullvarianten fra `case1_lekkasjefri.md`, ikke variant b.

## Test 2026 ved 10 % ruting (val 2025 i parentes)
| | smed2 #1955 (full) | **variant b (dommer2)** | avvik |
|---|---|---|---|
| uten ruting: P / R / F1 | 0,379 / 0,574 / 0,457 | 0,376 / 0,643 / 0,474 | R +0,07 |
| **symmetrisk bånd:** rutet | 125 (10,0 %) | 119 (9,6 %) | |
| MOT hos mennesket | 22 av 129 | 18 av 129 | −4 |
| maskinens MOT-presisjon | **0,500** (0,416) | **0,427** (0,366) [0,35, 0,50] | **−0,07** |
| maskinens MOT-recall | 0,626 (0,486) | 0,658 (0,546) [0,57, 0,74] | +0,03 |
| systemets presisjon / recall | – / 0,690 | 0,481 / 0,705 | |
| system-F1 | 0,625 | 0,572 (0,535) [0,50, 0,63] | −0,05 |
| **skjevt bånd:** c* valgt på val | +0,75 | +0,50 | |
| MOT hos mennesket | 36 av 129 | 28 av 129 | |
| maskinens P / R | 0,633 / 0,409 | 0,556 / 0,545 | |
| systemets P / R | – / 0,574 | 0,654 / 0,643 | |
| **system-F1** | **0,658** (0,630) | **0,648** (0,617) [0,58, 0,71] | −0,01 |

[ ] = 95 % klyngebootstrap på test med selskap (cusip) som klynge, 2000 trekk.

Kalibrering (isotonisk, tilpasset på val): snitt p på test er 0,117 mot faktisk MOT-andel 0,104, og ECE er 0,025. smed2 fikk 0,013. Litt svakere, men den holder fortsatt.

Ved 5 og 20 %, test (variant b): symmetrisk gir maskin-P 0,405 / 0,500 og system-F1 0,524 / 0,674. Skjevt gir system-F1 0,555 (c = +0,75) / 0,820 (c = +1,00). Alle tallene står i `arbeid/oppgave_1995/ruting_b.txt`.

## Avvik og dom
1. **Symmetrisk 10 %, presisjon 0,38 → 0,50: holder ikke for variant b.** Det riktige tallet er 0,38 → 0,43 (+0,05), og på val bare +0,02. smed2 advarte selv om at testgevinsten var større enn val-gevinsten. Variant b bekrefter at forventningen bør ligge i den nedre enden. Recall holder seg (0,66).
2. **Skjevt 10 %, system-F1 0,66: holder** (0,65). Men c* blir +0,50 og ikke +0,75, og hele gevinsten forutsetter at mennesket avgjør riktig.
3. Ved 20 % ligger c* fortsatt på kanten av rutenettet (+1,0), og maskinens recall faller da til 0,11 på val. Mennesket gjør da nesten alt arbeidet. Det bør ikke selges som maskinens fortjeneste.
4. Ingen tegn til juks: grense, bånd og c er låst på val før test leses, og test er lest én gang. Svakheten er at #1955 ble kjørt på den lekkende modellen og en egen kopi av feature-oppsettet (`ruting.raa`), ikke på `train_v3.py`-utfallet direkte.

## Til agenten og juryen
Bruk variant b med grense 0,1833. Anbefalt ruting er 10 %, symmetrisk. Mennesket ser cirka 120 saker i året, og 18 av dem er MOT. Maskinens MOT-presisjon blir 0,43 og recall 0,66. Vil man ha best mulig kombinert system, kan man velge skjevt bånd med c = +0,50. Da blir system-F1 0,65, men bare som øvre grense.

Forsøk: #1026 (symmetrisk, system-F1 0,572) og #1027 (skjevt, 0,648). Kommando: `rm -rf /tmp/rut1995 && env -i HOME=$HOME PATH=/usr/bin:/bin nohup bash arbeid/oppgave_1995/kald.sh /tmp/rut1995 > /tmp/rut1995.log 2>&1` (cirka 1 min).
