# Case 1 (#2640): jury-rettelsene (#2637) limt inn i STÅR-reserven, tørrkjørt grønn i kald kopi

Kilde: `c1_jury_rettelser.md`. Alle punkter merket STÅR eller begge er inne i `arbeid/hack/c1/reserve_staar/`:
1b, 2a, 3a, 3b, 4a, 4c (ERLIG + JURY_SPORSMAL), 4d, 4e, 4f, 4g, 4h (S-varianten), 5a, 5c, 5e. Ingen nye tall.

## Slik overlever de ombygging
- README/kravrespons: reglene i `arbeid/oppgave_2598/lag_staar.py` er skrevet om til å gå fra dagens BYTT-tekst (#2639) til STÅR-teksten med rettelsene. `--sjekk` sier LIK for begge. BYTT-spor-sjekken hopper nå over alle linjer merket `tallvakt: ignorer` (3a nevner 0,512 og 0,529 som sidetall).
- ERLIG/JURY_SPORSMAL/MUNTLIG: `arbeid/oppgave_2640/rett_staar.py` (idempotent, nøyaktig-én-gang-erstatninger). `lag_staar_erlig.py` kaller den til slutt.
- kravrespons i BYTT har fortsatt den korte dom-setningen (#2639 rørte den ikke); STÅR-utgaven sluttfører den med «ikke reprodusert fra kald start før fristen».
- `LES.md` oppdatert: fem filer kopieres (MUNTLIG også), staar_rest.py for de tre tekstene utenfor.

## Tørrkjøring i kald kopi (/tmp/staar_ovelse_2631, nullstilt og synket 17:38)
tilbake_fra_zip (zip 2587) → cp 5 filer fra reserve_staar → staar_rest.py --skriv (45) → tallvakt: **GRØNN, 177 påstander, 0 avvik**
→ pakk_jury (146 filer) → test_jury_zip: **FRYSVAKT GRØNN, TALLVAKT GRØNN, ZIPTEST GRØNN, HOVEDTALL 0.476190, TP 30 FP 38 FN 28 TN 1443**.
Zipen inneholder rettelsene (5 av 5 README-setninger, 3 av 3 ERLIG-setninger funnet). Logger: `/tmp/staar_2640_logg/`, zip `/tmp/jurypakke_staar_2640.zip`.
FRYS AVVIK 11 fra tilbake_fra_zip er filer laget etter zip 2587, som i #2631 (ventet).

## Uhell, rettet
Min første kjede i kopien ble avbrutt (rsync av 20 GB verktoy-mappe drept), og `cp reserve_staar/* leveranse/` kjørte da i landsbyen kl. 17:34 i stedet for i kopien.
Kl. 17:35 var de fem filene i `c1/leveranse/` tilbake lik HEAD (BYTT-tekst, 0,512) – trolig satt tilbake av en annen agent. Sjekket 17:44: alle fem lik HEAD, BYTT-spor til stede, ingen STÅR-dom. Ingen varig skade, men si fra om noen så rare tall i leveranse/ 17:34–17:35.

## Ikke gjort
- Utdraget i README (begge utgaver) viser `MOT mot styret: TP …`-linja fra måler v3; KJOR-utskriften i #2631 hadde bare `HOVEDTALL …`-linja. 5e følger BYTT-ordlyden. Smed2 avgjør om 5f/5e skal peke på HOVEDTALL-linja i stedet.
