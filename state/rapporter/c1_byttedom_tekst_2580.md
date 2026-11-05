# Case 1 (#2580): byttedommen skrevet inn i README og kravrespons — smed3, 05.11 17:12

## Gjort
- Dom #2570 (dommer2, kl. 17:02): **BYTT til repo4, på vilkår om grønn pakke innen 18:45** (`c1_byttedom_265.md`).
- Én setning satt inn i `arbeid/hack/c1/leveranse/README.md` (Hovedtall-boksen, ny `>`-linje etter V2-linja) og i
  `kravrespons.md` («Hvordan vi verifiserte det», etter setningen om val 2025 / test 2026). Innholdet: regel satt
  før måling, tre testår 2024–2026, repo4 0,5057/0,5309/0,5120 mot frossen 0,4545/0,5143/0,4762, snitt +0,0345,
  verste år +0,017, KI for snittet [−0,005; +0,078], BYTT kl. 17:02 på vilkår. Bare dommens tall. Ingen saksnumre i prosa.
- Begge linjer har `<!-- tallvakt: ignorer: byttedom, ikke hovedtall -->`; `bytt_tall.py` hopper over slike linjer,
  så byttet (#2592) rører dem ikke. Tallvakt: 173 påstander, 0 avvik. `frys_fasit_1600.sha256` regenerert. Commit 8f12725.
- Kravresponsen: 297 -> 343 ord (fortsatt under én side), 4/6/5 setninger.

## Gjenstår (sluttføring når #2592 er avgjort, før tekststopp kl. 19)
Setningen sier nå «på vilkår om grønn pakke innen 18:45», som er sant akkurat nå. Når byttet er grønt eller rullet tilbake:
    uv run python -I arbeid/oppgave_2580/sett_inn.py --sluttfor BYTT    # etter bytt.sh --utfor grønn: «byttet ble gjennomført, tallene i pakka er fra repo4»
    uv run python -I arbeid/oppgave_2580/sett_inn.py --sluttfor STAAR   # etter tilbakerulling: «byttet ble ikke grønt før tekststopp, frossen står med 0,476»
deretter tallvakt, `frys_fasit.py > frys_fasit_1600.sha256`, commit. smed3 venter på #2592 og gjør dette selv om økta rekker det.
Merk: tilbakerulling etter byttplanen (`git checkout <HEAD før bytt> -- arbeid/hack/c1/leveranse`) beholder setningen
siden 8f12725 er committet før byttet startet; da trengs bare `--sluttfor STAAR`.

## Status kl. 17:11 (økt 3, tidsboks brukt)
- Vilkårssetningen (BYTT kl. 17:02 på vilkår om grønn pakke innen 18:45) står i README linje 12 og kravrespons linje 7, uendret siden commit 8f12725. Den er sann uansett utfall.
- #2592 (byttet) er på 65 % og ikke grønn; endelig BYTT/STÅR skrives kl. 18:45 (#2603). Tallvakt kl. 17:11: 21 filer, 174 påstander, 0 avvik.
- Sluttføring er én kommando, overlevert til den som lukker #2592 (eller ruller tilbake), før tekststopp kl. 19:
      uv run python -I arbeid/oppgave_2580/sett_inn.py --sluttfor BYTT    # eller STAAR
      uv run python -I arbeid/verktoy/c1_tallvakt.py --rot .
      uv run python arbeid/hack/levering/frys_fasit.py > arbeid/hack/levering/frys_fasit_1600.sha256
  Skriptet bytter bare frasen «på vilkår om grønn pakke innen 18:45» mot utfallet, i begge filene, idempotent. Blir den ikke kjørt, står vilkårsteksten, og det er også ærlig.
