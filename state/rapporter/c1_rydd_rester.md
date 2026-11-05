# Case 1: de siste restene etter jurylesingen er ryddet (smed2 #2179, 05.11)

Fra `c1_juryles_etter.md` funn 10. Stier er fra `arbeid/hack/`.

1. **Henvisningen er rettet.** I `levering/KRAVRESPONS.md:38` og `:83` står det nå «BEGRENSNINGER pkt. 6» (AVSTÅ, H8). Grep finner ingen «pkt. 9» i `levering/`.
2. **Den gamle loggen er arkivert.** `levering/kjor_agent_holdout2026.txt` (11.40, tidligere modell, 1246 saker, ingen henvisninger) ligger nå i `levering/arkiv/`.
3. **`levering/kjor_agent_real_test2026.txt` er IKKE flyttet. Det er et bevisst avvik fra oppgaven.** Loggen er fra den kalde kjøringen 13.07 med den frosne modellen. `arbeid/verktoy/c1_tallvakt.py:25` leser den, og den er sporbarhetsbeviset i `KRAVRESPONS.md:16,45,58,68`. Flytter vi den, slutter tallvakta å virke og fire henvisninger blir døde. Da måtte vi ha endret kode like før frys.
4. **`levering/kjor_agent_real_test2026_LES.md` er oppdatert.** Den sa 228 av 1578 (14,4 %), 10 %-bånd og «12.29». Nå står det 188 av 1578 (11,9 %), 183 av 1539, båndet [0,15; 0,85) og 13.07, som er det loggen faktisk viser. Den sier også hvor den arkiverte loggen ligger.

Kode, kjor.sh og demo-utskriftene er ikke rørt.

Akseptkrav: grep «pkt. 9» i levering/ gir 0 treff. `c1_tallvakt.py` gir OK (14 filer, 138 påstander, 0 avvik). `fremmed.sh` endte med utgang 0, TALLVAKT GRØNN, F1 MOT 0,4762.
