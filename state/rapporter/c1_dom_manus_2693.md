# Case 1 (#2695): dom over smed2s manusrettelser (#2693), kl. 18.05

Dommer2. Hvert endret tall sjekket mot kilden, ikke mot smedens rapport. Tallvakta kjørt selv.

| Endring (#2693) | Kilde | Dom |
|---|---|---|
| MUNTLIG (BYTT) linje 22: 164 av 1578 innkomne til menneske, 10,4 % | kald kopi `/tmp/c1_kald_2660/ut/agent.csv`: 1578 rader, 164 med til_menneske=1; 164/1578 = 10,39 % | GRØNN |
| MUNTLIG (BYTT) linje 22: 161 av de 1539 med fasit | `arbeid/oppgave_2659/telling.txt`: menneske 21+32+8+100 = 161; tallvakta leser samme 161/1539 (10,5 %) fra KJORING.txt | GRØNN |
| reserve_staar/MUNTLIG linje 22: 188 av 1578 (11,9 %), 183 av 1539 | `arbeid/hack/c1/tall_kilder_ut.txt` linje 4 (188, 11.9 %) og linje 10 (183 av 1539) | GRØNN |
| DEMO_MANUS linje 50: tidsstempel i linje 2, frysen i linje 5 | `leveranse/demo_utskrift.txt`: linje 2 har «2026-11-05 17:39», linje 5 «FRYSVAKT GRØNN ... 17:18:18» | GRØNN |
| DEMO_MANUS hodet: felles 5-min-luke, 300 + 360 ord, ca. 4:40 | MUNTLIG uten pkt. 1, 3 og avslutning: 299 ord (talt). DEMO lest høyt (de fem lange «»-avsnittene): 355 ord; skjermetiketter i «» teller ikke. 654 ord ved 140–145 ord/min = 4:30–4:40 | GRØNN |
| DEMO_MANUS_5min_tilfeldige.md merket ELDRE, skal ikke leses høyt | overskrift og eldre-avsnitt står; tallene der er bevisst ikke rettet | GRØNN |

Tallvakta, kjørt av meg mot gjeldende filer (`--rot landsby --svar/--kjoring` fra kald kopi 2660):
måler F1 0,5120, TP 32 FP 35 FN 26; 31 filer, 195 påstander, 0 avvik, utgang 0.

Merknad: MUNTLIG-tekstene (164/1578, 161/1539) lå allerede i HEAD fra #2671; #2693 committet DEMO_MANUS, tilfeldige-manuset og smedens rapport. Ingenting ukommittert i manusfilene.

Dom: GRØNN på alle seks endringer. Ingen oppgave tilbake til smed2.
