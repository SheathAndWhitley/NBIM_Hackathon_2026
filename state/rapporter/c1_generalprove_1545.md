# Case 1: siste generalprøve med sluttsjekk.sh før frysen (#2423, smed4)

Kjørt 15:38–15:43, git 445e428, kald kopi /tmp/c1_sluttsjekk_smed4_2423. Ingen kodeendringer.

## Kjøring A: sluttsjekk.sh ordrett
- Utgangskode **4 (RØD)**, steg 1 frysvakt: `FRYSVAKT: ikke frosset ennå (state/c1_frys.json finnes ikke), --krev: STOPP`.
- Dette er ventet før kl. 16: skriptet krever frys. Ikke en feil i pakka, men det betyr at
  sluttsjekk.sh ikke kan gi grønt før frysen er tatt (riktig for 19:30).

## Kjøring B: samme skript, steg 1 kommentert ut (kopi i /tmp, repoet uendret)
- Utgangskode **0**. Siste linje: `SLUTTSJEKK GRØNN ... (256 s)`.
- HOVEDTALL: `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190` (P 0.4412, R 0.5172, TP 30 FP 38 FN 28, 58 MOT i fasit).
- TALLVAKT: **GRØNN** i kaldstart, i steg 3 og i ziptest (18 filer, 168 påstander, 0 avviker).
- Tallsjekk: 2417 tall i 18 filer, ingen uten kilde rapportert.
- Hovedtall kald kopi 0.476190 = kv hack_levert 0.476190 = zipen.
- Jury-zip: /tmp/jurypakke_c1.zip, 1.0 MB, 99 filer, 5/5 zip- og stisjekk. Merk: 8 tekstfiler nevner ~ (kjørestien leser dem ikke).
- Ziptest: sha256 ny prediksjonsfil = frossen fil (b113b545…3653): LIK.
- Steg 7 tekstavtrykk: `TEKSTAVTRYKK: ikke tatt ennå (state/c1_tekstavtrykk.json; tas kl. 16.03)` – bare info.

## Funn til arkitekt/dommer
1. GRØNN-linja lister «frysvakt» som ok selv når steg 1 er hoppet over; harmløst her, men linja er hardkodet.
2. Steg 5 skriver over standard /tmp/jurypakke_c1.zip – andre som bruker den fila samtidig får denne versjonen.
3. Ingen røde funn i selve pakka. Etter frysen 16:03 bør sluttsjekk.sh kjøres ordrett (kjøring A) og gi grønt.

Logger: arbeid/oppgave_2423/ (sluttsjekk.out, sluttsjekk_uten_frys.out, steg-loggene).

## Rettet i #2443 (smed4, commit b42f7f3)
- Funn 1: GRØNN-linja bygges nå av stegene som faktisk kjørte grønt (`ok <steg>` etter hvert steg), ikke hardkodet. Hovedtall og ziptest står også med.
- Funn 2: steg 5 lager egen mappe per kjøring med `mktemp -d /tmp/c1_jurypakke.XXXX` (eller bruker `$C1_JURYZIP`) og skriver stien ut før byggingen. Filnavnet i mappa er fortsatt `jurypakke_c1.zip`.
- Test: `bash -n` ok. Kopi uten steg 1 (arbeid/oppgave_2443/kopi/) ga utgang 0, 224 s: `SLUTTSJEKK GRØNN: kaldstart, tallvakt, tallsjekk, hovedtall, jury-zip, ziptest ok; HOVEDTALL F1 MOT 0.476190 = kv hack_levert = zipen (/tmp/c1_jurypakke.D6hq/jurypakke_c1.zip, 1.0M)`. Frysvakt er ikke med, siden steget ikke kjørte. Logg: arbeid/oppgave_2443/sluttsjekk_uten_frys.out.
