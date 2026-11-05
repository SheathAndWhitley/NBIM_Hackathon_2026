# Case 1: demo-manuset (DEMO_MANUS.md) kjørt ordrett med tidtaking (#2433, smed2, 05.11 ca. 15.45)

**Resultat: alle tall, saker og sitater i manuset stemmer med en kald kjøring.** Men tre ting må rettes før demoen (se under).
Manuset ligger i `arbeid/hack/c1/DEMO_MANUS.md` (ikke i leveranse/; det finnes ingen DEMO*-fil der).
Bygget før frysen kl. 16 (FRYSVAKT «ikke frosset ennå»). Ingen kodeendring. demo.sh skriver over `leveranse/demo_utskrift.txt`;
jeg tok kopi før og la den tilbake etterpå (ny utskrift: `/tmp/s2_2433_demo_utskrift_ny.txt`).

| steg | kommando | virker | avvik | sekunder |
|---|---|---|---|---|
| 0 | `pakk_jury.sh /tmp/s2_2433.zip` (som #2416) | ja, 1,0 MB, 99 filer | – | 71 |
| 0b | i zipen: `sh KJOR.sh` (env -i, varm uv-cache) | ja, FRYSVAKT GRØNN, HOVEDTALL 0.476190, TALLVAKT GRØNN | – | 104 |
| 0c | i zipen: `sh arbeid/hack/c1/leveranse/demo.sh` | **NEI**, utgang 1 | `fremmed.sh` (og `vis_manussaker.py`, DEMO_MANUS.md) er ikke med i zipen. demo.sh virker bare fra repoet | 0 |
| 1 | `sh arbeid/hack/levering/fremmed.sh /tmp/s2_2433_fremmed` (manus: «start ved 0:00, tar 42 s») | ja, HOVEDTALL 0.476190, TALLVAKT GRØNN | **tar 103 s, ikke 42 s** (kjor_agent 75 s av dem) | 103 |
| 1b | agent.csv sha | `1543706f…` som manuset sier | – | – |
| 2 | `python3 -I arbeid/oppgave_2329/vis_manussaker.py /tmp/…/ut/agent.csv` | ja | Mobimo l.276 p 1.0/0, LOTTE l.89 p 0.0896/0, Kura l.15 p 0.5833/1, GVG 5.2/1.1, båndtekst og alle tre sitater ordrett likt. Viser ikke NBIMs fasit (det gjør demo.sh med real_votes) | 0,03 |
| 3 | `sh arbeid/hack/c1/leveranse/demo.sh /tmp/s2_2433_fremmed` (gjenbruker kopien) | ja | demo_utskrift.txt **lik linje for linje** utenom tidsstempelet i linje 1 | <1 |
| 4 | tallene i manus (`telling.py`) | ja | TP 30 FP 38 FN 28, F1 0,4762, P 0,441, 183/1539 = 11,9 %, FN maskin 17/menneske 11, FP maskin 0/menneske 38: alt likt | <1 |
| 5 | tekst som leses høyt | – | 349 ord i «» (manus sier 404 inkl. sitater) = 2:25 ved 145 ord/min; med pauser ca. 2:45 | ~150–165 |

## Passer det i tidsramma (under 3 min)?
Opplesingen passer (ca. 2:25–2:45). **Det live-kjørte passer ikke:** fremmed.sh tar 103 s, men Mobimo skal på skjermen ved 0:35.
Startes den ved 0:00, er radene først klare ved ca. 1:45.

## Forslag til speider (#1975), i rekkefølge
1. **Kutt den kalde kjøringen ut av de 3 minuttene:** kjør `fremmed.sh /tmp/c1_kald` *før* demoen begynner. Live kjøres bare
   `demo.sh /tmp/c1_kald` (gjenbruker kopien, under 1 s) og eventuelt `vis_manussaker.py` (0,03 s). Rett «tar 42 s» til «ca. 100 s, kjøres før demoen».
   Avslutningssetningen «Én kommando fra kald start gir de samme radene» står fortsatt (vis tidsstempelet i demo_utskrift linje 1).
2. Skriv i manuset at demo.sh og vis_manussaker bare finnes i repoet, ikke i jury-zipen (eller ta med fremmed.sh + vis_manussaker.py i zipen; det er kodeendring, så ikke før frysen uten dom).
3. Manusets skjermkommando peker på `arbeid/oppgave_2329/vis_manussaker.py`; demo.sh bruker `arbeid/hack/c1/vis_manussaker.py`. Bruk én sti (den i hack/c1).
4. Ordtallet i manuset (404) stemmer ikke med det jeg teller (349 i «»); tida blir uansett under 3 min.

Etter frysen må agent.csv-sha (`1543706f…`) og linje 15/89/276 sjekkes på nytt (manusets egen «Etter modellfrys»-regel).
Filer: `/tmp/s2_2433_jury/` (zip-kjøring, kjor.log, demo_zip.log), `/tmp/s2_2433_fremmed.log`, `/tmp/s2_2433_vis.txt`, `/tmp/s2_2433_demo_utskrift_ny.txt`.

## Rettet i DEMO_MANUS.md (#2441, speider, 05.11 ca. 15.50, før frysen)
- Forslag 1: «start fremmed.sh ved 0:00, tar 42 s» er fjernet. Ny linje 5: `fremmed.sh /tmp/c1_kald` kjøres *før* demoen (ca. 100 s, målt 103 s); live bare `demo.sh /tmp/c1_kald` (<1 s) og `vis_manussaker.py` (0,03 s). Avslutningen viser tidsstempelet i demo_utskrift linje 1. Lagt til at demo.sh, fremmed.sh og vis_manussaker.py bare finnes i repoet, ikke i jury-zipen (forslag 2, bare som tekst).
- Forslag 3: én sti, `arbeid/hack/c1/vis_manussaker.py` (den gamle `arbeid/oppgave_2329/...` er ute).
- Forslag 4: ordtallet er 341 ord i «» i de fem opplesningsblokkene (min telling, `split()` på tekst mellom «»; smed2 fikk 349 med annen telling). Ca. 2:20 ved 145 ord/min, ca. 2:40 med pauser. Under 3 min.
- Saker, tall og sitater er ikke rørt. Ingen kode endret. «Etter modellfrys»-sjekken (sha og linje 15/89/276) gjenstår i #1975.
