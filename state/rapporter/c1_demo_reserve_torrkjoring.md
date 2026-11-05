# Case 1: demo-reserven tørrkjørt 15:55, klar for 16:05 (#2461, arkitekt)

Kommandoliste for 16:05: `arbeid/oppgave_2461/KOMMANDOER_1605.md` (kjernen: `sh arbeid/hack/levering/demo/reserve/lag_reserve.sh; echo "utgang $?"`).

## Tørrkjøring mot pakka slik den står nå (testmodus, ingenting overskrevet)
- Testfrys av dagens filer: `C1_FRYS=/tmp/c1_frys_test2461.json c1_frys.py frys` → 17 filer, 0,03 s.
- `C1_FRYS=… C1_RESERVE_UT=/tmp/c1_reserve_test2461 lag_reserve.sh` → **utgang 0, TEST GRØNN, 109 s**.
  5/5 sha `LIK FRYS`, `FRYSVAKT GRØNN: 17 filer`, `HOVEDTALL F1 MOT … 0.476190`. Logg: /tmp/c1_reserve_test2461.log.
- KP: forventet 0.476190 (levert hovedtall, #2322), fikk 0.476190. kjor_agent.py dedc9406…87e2, som i #2322.
- Ekte kjøring nå (før frysen): `RESERVE STOPP: frysvakta er ikke grønn`, gammel reserve (13:18) urørt. Riktig.

## Hva tok tid / merk
- Tid 109 s mot 67 s i #2322: maskinen er travel (mange agenter). Sett av 2–3 min.
- Frysvakta teller nå 17 filer (var 10 i #2322): frysliste utvidet siden. Den ekte frysen kl. 16 må gi samme 17, ellers sjekk c1_frys.py.
- Ingen feil. levering/, reserven og state/c1_frys.json ikke rørt.
