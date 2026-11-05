# STÅR-reserve (#2598): README.md og kravrespons.md med frossen 0,476

**#2640 (17:45):** jury-rettelsene fra #2637 (punktene merket STÅR/begge) er inne i alle fem filene her. README/kravrespons får dem fra reglene i `lag_staar.py`, ERLIG/JURY_SPORSMAL/MUNTLIG fra `arbeid/oppgave_2640/rett_staar.py` (kalles sist i `lag_staar_erlig.py`), så de overlever ombygging. Fem filer skal kopieres ved STÅR (MUNTLIG.md også, #2631), og `arbeid/oppgave_2631/staar_rest.py --skriv` tar KRAVRESPONS/EN_SIDE/GITHUB_README_UTKAST i levering/. Oppskrift med tider: `state/rapporter/c1_staar_ovelse.md`.

Bruk bare hvis repo4-zipen ikke er grønn innen 18:45 og dommeren sier STÅR.
Filene her er BYTT-utgaven i `arbeid/hack/c1/leveranse/` (slik den sto kl. 18:0x) med:
- alle hovedtall tilbake til frossen (0,476, P 0,44, R 0,52, TP 30 FP 38 FN 26→28, 188/1578 = 11,9 %, val 0,520,
  KI [0,36; 0,59], rader [0,37; 0,59], sidetall 0,482 [0,375; 0,580], 127/60/183 rutet kl. 12.54, TN 1443, acc 95,7 %,
  F1 0.4762 i utskriften, «pluss fire historikktrekk (repo4)» strøket fra modellbeskrivelsen),
- byttedommen sluttført ærlig: «Kandidaten besto regelen, men pakken med repo4 ble ikke grønn i tide,
  så den frosne agenten står med 0,476.»

Regenerer/sjekk mot gjeldende BYTT-tekst: `uv run python -I arbeid/oppgave_2598/lag_staar.py [--sjekk]`
(stopper hvis BYTT-teksten har endret seg så en erstatning ikke lenger finnes nøyaktig én gang).

Ta i bruk (etter dom STÅR): `cp arbeid/hack/c1/reserve_staar/{README.md,kravrespons.md} arbeid/hack/c1/leveranse/`,
deretter samme kjede som ellers (tallvakt, frys_fasit, pakk_jury). Ikke kjør `sett_inn.py --sluttfor` etterpå; dommen er alt sluttført her.
De 16 andre tekstene byttet rørte, rulles tilbake med `tilbake_fra_zip.sh` (#2593). Den tilbakerullingen gir
ERLIG_EVALUERING.md og JURY_SPORSMAL.md UTEN ærlighetsforbeholdet, så kopier deretter STÅR-utgavene herfra (#2625):
`cp arbeid/hack/c1/reserve_staar/{ERLIG_EVALUERING.md,JURY_SPORSMAL.md} arbeid/hack/c1/leveranse/`
(zip 2587 + STAAR-tekstene fra #2618 i § 7 og svar 20, klokkeslett 16:49–16:51; regenerer: `uv run python -I arbeid/oppgave_2625/lag_staar_erlig.py`).
Rekkefølge ved STÅR: tilbake_fra_zip.sh → cp de fire filene herfra → tallvakt, frys_fasit, pakk_jury.
