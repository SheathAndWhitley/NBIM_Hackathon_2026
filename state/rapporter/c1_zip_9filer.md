# Case 1: de 9 manglende filene er nå i jury-zipen (#2448)

- `arbeid/hack/levering/pakk_jury.sh` (stien i oppgaven, `c1/leveranse/`, var feil) har fått én `kopier`-linje med de 8 filene fra
  `c1_manglende_filer.md` del (1). `DEMO_MANUS.md` var alt med (#2442). Ikke i c1_frys FILER, frysen er urørt. README/JURY ikke rørt.
- `menneske_tabell.py` er med som kode, de hardkodede stiene er ikke rettet (står i kommentaren i skriptet). Den nevner ~, som
  stisjekken i steg 5 viser (9 tekstfiler, ingen på kjørestien).
- Test 15:52: zip bygd i egen mktemp-mappe (C1_JURYBYGG/C1_JURYSTAGE), 112 filer, 1,1 MB. `unzip -l` viser alle 9.
  Utpakket i tom mappe: `sh KJOR.sh` exit 0, **HOVEDTALL 0.476190, TALLVAKT GRØNN**.
- Kjørt fra utpakket zip med `python3 -I` (ingen landsby-sti):
  - `treffsikkerhet.py`: TP 30 FP 38 FN 28 (P 0,4412, R 0,5172 → F1 0,476); konfidens ≥ 0,6: presisjon 1,00, recall 0,346
  - `treffsikkerhet_ki.py`: recall 51,7 % [39,1–65,2], ved ≥ 0,6 recall 34,6 % [15,8–55,0], samme som i rapportene
  - `sjekk_lekkasje.py svar … --data real`: OK, ingen lekkasjesignatur
  - `terskel_val_test.py` med zipens .venv (etter KJOR.sh): kjører, valgt t = 0,9188 val-optimal
