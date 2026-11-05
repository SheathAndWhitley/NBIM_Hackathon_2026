# Case 1: én kommando for sluttsjekken kl. 19.30 (#2330)

Kommandoen dommeren kjører i #1972 (fra landsbymappen, etter frysen kl. 16):

    bash arbeid/hack/levering/sluttsjekk.sh

Siste linje er `SLUTTSJEKK GRØNN: ...` (utgang 0) eller `SLUTTSJEKK RØD: <grunn>` (utgang 4).
Kjøringen stopper ved første røde steg. Fulle logger ligger i `/tmp/c1_sluttsjekk_logg.XXXX`, og stien skrives ut.

## Steg (bare kall til skript som finnes fra før)
1. Frysvakt: `c1_frys.py sjekk --krev` (ikke frosset gir rødt).
2. Kald kopi: `fremmed.sh /tmp/c1_sluttsjekk` (har egen frysvakt og tallvakt, skriver HOVEDTALL).
3. Tallsjekk: `c1_tallsjekk.py --bare-ikke --feil` (et tall i pakka uten kilde gir rødt).
4. HOVEDTALL fra steg 2 skal være lik verdien i kv `hack_levert`. Steget leser `tavle.py levert`
   og kjører den lagrede `kmd` på `sti`. Tallene sammenlignes som tekst, med 6 desimaler.

## Prøvekjøringer 14:41
- Ekte, uten flagg: **RØD**, som ventet før frysen: `FRYSVAKT: ikke frosset ennå (state/c1_frys.json finnes ikke), --krev: STOPP`. Utgang 4, 0 s.
- Med midlertidig frys (`C1_FRYS=/tmp/...json`, laget med `c1_frys.py frys`, slettet etterpå): **GRØNN** på 50 s.
  Frysvakt 10/10 filer like. Tallvakt i kopien grønn (163 påstander, 0 avvik). Tallsjekk: 2213 tall, alle har kilde.
  HOVEDTALL 0.476190 = kv hack_levert 0.476190.
- `bash -n`: ok.

Vil du prøve før kl. 16, lag en midlertidig frys og sett `C1_FRYS` på samme måte. Den ekte `state/c1_frys.json` blir ikke rørt.
Forholdet til `c1_etterfrys.sh` (#2187): det skriptet kjører alle stegene og skriver en rapport. Det sjekker ikke tallsjekken
med --feil og heller ikke kv hack_levert. sluttsjekk.sh gir én linje, en utgangskode og har disse to stegene i tillegg.
