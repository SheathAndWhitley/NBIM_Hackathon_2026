# Case 1 #2896: v2+av (#2887) ligger klar i pakka og byttes med én fil. Standard er fortsatt frossen (smed, 05.11)

## Kommandoen dommeren kjører kl. 02, bare hvis dommen #2874 sier BYTT
```
bash arbeid/hack/c1/bytt_v2av.sh --bytt      # MODELL=v2av, github_synk, sha av ny FROSNE_SHA256.txt -> state/c1_BYTT
# så: oppdater tallene i dokumentene (se under), og
C1_TORR=1 bash arbeid/verktoy/c1_natt_push.sh   # må gi TØRR GRØNN før neste ekte push
```
Uten argument gjør skriptet ingenting (tørt). `--tilbake` setter modellen tilbake til frossen.

## Slik virker det
- Bryteren er fila `arbeid/hack/levering/MODELL`, med `frossen` (standard) eller `v2av`.
  - KJOR.sh (jury_kjor.sh) kjører `kjor_agent.py` eller `kjor_agent_v2av.py` og skriver linja `MODELL:`.
  - testaar.sh leser samme fil. `C1_MODELL=v2av` overstyrer den.
- Nye filer: `modell_v2av.py`, `c1_real_v2av.py`, `kjor_agent_v2av.py` og `av_regel.py` i `hack/levering/`, pluss `v2_rull.py` i `leveranse/verktoy/`.
  - `modell_v2av.py` er modell_repo4.py pluss SVD-trekket fra v2_rull.py, med k=48.
  - `c1_real_v2av.py` er c1_real.py pluss av-regelen, slik smed2 laget den i #2893. `av_regel.py` er byte-lik smed2s (sha d7db9bf0…).
- Ingen frosne filer er endret, verken i oppgave_2567/2575 eller i FROSNE_SHA256.txt.
- Modellvakt: github_synk.sh legger v2av-filene og MODELL inn i FROSNE_SHA256.txt bare når MODELL=v2av.
  - Et bytte endrer derfor FROSNE_SHA256.txt, og c1_natt_push.sh pusher ikke uten state/c1_BYTT.
  - Med frossen er lista uendret, så pushene i kveld blokkeres ikke. Prøvd på stagen: 6 linjer kommer til ved v2av.
- testaar.sh med v2av: v2_rull.py med k 32/64/48, deretter av-regel alle år (valgt på val T-1 i #2887, låst i REGEL.md). Ingen ny variant er målt.

## Kald kopi
Kjørt slik: github_synk.sh mot tom temp-repo, så `git archive HEAD` og casedata, i /tmp/c1_2896.

| modus | KJOR.sh | HOVEDTALL | tallvakt | testaar.sh |
|---|---|---|---|---|
| frossen (standard) | utgang 0, frysvakt grønn (14 filer) | 0,512000 | GRØNN | 0,5057 / 0,5309 / 0,5120, snitt 0,5162 = fasit |
| v2av | utgang 1 | **0,539130** (TP 31 FP 26 FN 27) | **RØD**: 150 gamle tall i 22 dokumenter | **0,5731 / 0,5667 / 0,5391, snitt 0,5596** = dom #2890 |

Skanningen ga 0 funn. FROSNE_SHA256.txt er lik GitHub-repoens i frossen modus.

## Det som gjenstår ved BYTT (ikke koding)
Tallvakta er rød i v2av-modus fordi README, JURYSVAR, BESLUTNINGSSTOTTE og de andre dokumentene fortsatt har repo4-tallene: 0,512, 161 til menneske, TP 32 FP 35. Det er riktig at den er rød, for den stopper en push med feil tall.
- Dokumentendringene finnes allerede i smed2s byttegren: `arbeid/oppgave_2893/natt-v2av.patch`, bare .md-delene.
- Nye tall å skrive inn: F1 0,539, P 0,544, R 0,534, TP 31 FP 26 FN 27, 135 av 1578 (8,6 %) og 132 av 1539 til menneske, testår snitt 0,5596.
- Patchen er laget mot en eldre HEAD. Jury-fiksene (#2897) kan derfor gi konflikter, og den bør brukes med `git apply --3way` eller for hånd.
