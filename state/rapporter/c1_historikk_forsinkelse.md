# Case 1: hvor mye faller frossen agent hvis NBIMs stemmer blir kjent sent? (#2299, arkitekt)

**Svar: nesten ingenting.** Med forsinkelse 1–90 dager faller F1 på MOT med 0 til 0,03 på begge år, og alle KI for fallet
dekker 0. Historikken er verdt omtrent 0,19 F1, men verdien kommer fra NBIMs stemmer i *tidligere år*, ikke fra ferske
stemmer i samme sesong. Golvet 0,415 i JURY pkt. 7 måler ikke sen publisering (se nederst).

Skript: `arbeid/oppgave_2299/forsinkelse.py`. Det er en kopi av modellkoden i `oppgave_2044/train.py` (miks h2) med ett tillegg:
en stemme teller bare når møtedato < saksdato − N dager. Pakka og de frosne filene er ikke rørt.
Måler: v3 `--score mot` (MOT mot styret). Vinduet val = 2025. For 2024 importeres v3 uendret, og bare vinduet byttes til
«år == 2024», fordi v3 sitt «train» er alle år ≤ 2024. Egen F1 er sjekket mot v3 med assert på hver kjøring.
KI: klyngebootstrap over møter, 2000 trekk (1000 i kontrollen), parvis mot N=0.

- **A frossen:** modell, C og grense er som i den frosne agenten (valgt ved N=0). Bare sakene som predikeres får forsinket historikk.
  Det svarer til agenten slik den er levert.
- **B trent på nytt:** hele treningen bruker samme N, og C og grense velges på nytt.
- 2024: trent < 2024. C og grense velges på 2024 selv, med samme prosedyre som frossen bruker på 2025. Nivået er derfor
  optimistisk, og fallet fra N=0 er det som teller.

KP: forventet 0,520231 (frossen, val 2025, v3, C=3, grense 0,9188), fikk 0,520231. Uten historikk forventet 0,337
(`c1_ablasjon_v2`), fikk 0,336 (N=100000, B, 2025).

| N dager | 2025 A (frossen) | fall [KI] | 2025 B (ny trening) | fall [KI] | 2024 A (frossen) | fall [KI] | 2024 B (ny trening) | fall [KI] |
|---|---|---|---|---|---|---|---|---|
| 0 | **0,520** [0,40; 0,63] | – | – | – | **0,536** [0,41; 0,65] | – | – | – |
| 1 | 0,520 | 0 | 0,518 | −0,002 [−0,04; 0,03] | 0,536 | 0 | 0,522 | −0,015 [−0,12; 0,08] |
| 7 | 0,520 | 0 | 0,523 | +0,003 [−0,03; 0,03] | 0,536 | 0 | 0,507 | −0,029 [−0,15; 0,07] |
| 30 | 0,523 | +0,003 [0; 0,01] | 0,520 | 0 [−0,03; 0,03] | 0,536 | 0 | 0,507 | −0,029 [−0,13; 0,07] |
| 90 | 0,523 | +0,003 [0; 0,01] | 0,527 | +0,007 [−0,03; 0,04] | 0,536 | 0 | 0,512 | −0,024 [−0,07; 0,02] |
| *kontroll 365* | 0,552 | +0,032 [0; 0,07] | 0,529 | +0,009 [−0,04; 0,06] | 0,497 | −0,039 [−0,08; 0,00] | 0,488 | −0,048 [−0,12; 0,02] |
| *kontroll ingen historikk* | 0,299 | −0,221 [−0,34; −0,10] | 0,336 | −0,185 [−0,30; −0,07] | 0,253 | −0,283 [−0,41; −0,15] | 0,340 | −0,196 [−0,31; −0,07] |

PR-AUC (avvik) flytter seg like lite: 2025 0,473 → 0,472 (A, N=90), 2024 0,591 → 0,587.

**Verste N (1–90):** 2025 er N=1 B med 0,518 (−0,002). 2024 er N=7/30 B med 0,507 (−0,029). Begge KI dekker 0.

## Hvorfor så lite?
Agenten bruker tre historikknøkler: selskap, selskap+tekst og tekst. Et selskap har som regel ett møte i året. En
forsinkelse under ett år fjerner derfor nesten bare stemmer fra ekstraordinære møter og fra samme tekst i andre selskaper
samme vår, og de bærer lite. Først ved 365 dager faller 2024 (−0,04/−0,05), og selv da ikke 2025.

## Hva det betyr for JURY pkt. 7 og tabellen «Golv 0,415»
0,415 kommer fra `--hist 1` (`kilder/c1_enkle_regler_og_hist1.md`). Der får treningsradene historikk fra alle etiketter
før 2025, også sin egen og senere år (`lab = year < til_aar` uten datogrense, `oppgave_2044/train.py` hist_feats). Modellen
lærer dermed en historikk som er sterkere enn den den får på val. Det er en lekkasje i treningen, ikke et mål på sen publisering.
Det ærlige tallet når stemmene ikke er kjent løpende, er raden for N=90 eller N=365 over: **0,52 på 2025 og
0,49–0,54 på 2024**. Påstanden om «+0,07 fra løpende historikk» (arkitekt_2290 pkt. 3, 0,448 → 0,522) gjelder h1 mot h2, altså
lekkasje mot ingen lekkasje, ikke ferskhet.

**Anbefaling:** Speider og dommer (#1975 og #2255) bør bytte pkt. 7 til: «Kommer NBIMs stemmer først 90 dager etter
møtet, er F1 på MOT 0,523 på val 2025 og 0,512–0,536 på 2024; fallet er innenfor støy. Uten historikk faller den til
0,34.» Golvet 0,415 bør tas ut av tabellen, eller merkes «hist 1, lekker i trening». Agenten endres ikke.
Første dag med en uke til (arkitekt_2290 pkt. 3) går da ikke til å måle publiseringsforsinkelsen. Den risikoen er målt bort.

Filer: `arbeid/oppgave_2299/pred_<år>_N<N>_<A|B>.csv` (v3-format), `resultat_hoved.json`, `kjoring.log`, `kontroll.log`.
Kjør: `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2299/forsinkelse.py [--aar 2025 2024] [--lag 0 1 7 30 90]` (~6 min).
