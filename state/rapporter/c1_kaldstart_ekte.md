# Case 1: kaldstart.sh måler nå mot de ekte stemmene (dommer #2099, H3 tettet)

**Dom: GRØNN.** `bash arbeid/hack/c1/kaldstart.sh` fra tom tmp-kopi, 12.31:
`GRØNN F1_MOT 0.476190 REF 0.476190 AVVIK +0.000000 (grense 0.005) tid 31s`.
MOT mot styret TP 30 FP 38 FN 28, P 0,441, R 0,517, 58 i fasit. Det er de samme tallene som dommer #2090 fikk.

## Hva som var feil
1. Steg 4 målte med `c1/maaler.py` mot `data_v3/fasit.csv`, altså N-PX (REF 0,474).
2. Steg 1 kopierte ikke filene den ekte agenten trenger. Første kalde kjøring feilet derfor med `No module named 'c1_real'`. Kald start kl. 13 ville altså ha feilet, ikke bare målt feil.

## Rettet i `arbeid/hack/c1/kaldstart.sh`
- Steg 1 kopierer også c1_real.py, oppgave_2044/train.py, oppgave_2047/vern.py, oppgave_2046/case1_mot.py, data_off/real_test_input.csv og real_votes.csv til `$TMP/state/opplastet`. Det er samme liste som i smed3s `levering/fremmed.sh` (#2094). Jeg gjenbrukte den og skrev ingen ny vei.
- Steg 4 bruker `maaler_offisiell_v3.py <svar> test --data real --score mot` (landsbyens kopi, sha256[:10] 8b09c36e01) på både `_pred_uten_ruting.csv` (hovedtallet) og `pred_maaler.csv`. Begge gir 0,476190.
- Steg 5: REF står som standard på 0,476190 (#2090). `REF=` i miljøet overstyrer fortsatt.
- Kopien av train.py er byte-lik landsbyens (sha 772fb715). Ingen fil på agentens vei har landsbystien hardkodet.

## Merk
- Smed3s 0,4818 fra fremmed.sh (#2094) er F1 på **avvik** (v2-standard), ikke MOT. Begge tallene er riktige, men 0,476 er hovedtallet.
- Agenten ruter nå 228 av 1578 (14,4 %). c1_tall_likt.md sier 176 (11,2 %). Ulikheten kommer fra båndet/--til-menneske (standard 10 % av val) eller de nye rutingsgrunnene. Dette påvirker ikke F1, men tallet i juryfilene må sjekkes (#1952/#1975).
- Kjør kl. 13 (#1952): `bash arbeid/hack/c1/kaldstart.sh` fra hvor som helst. Ca. 30 s. `BEHOLD=1` beholder kopien.
