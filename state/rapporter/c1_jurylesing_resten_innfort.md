# Case 1 (#2550): speiderens funn fra #2544 ført inn i JURY.md og ERLIG_EVALUERING.md

Bare tekst er endret, i `arbeid/hack/c1/leveranse/JURY.md` og `ERLIG_EVALUERING.md`. Det er ingen nye tall: hvert tall som er satt inn, står fra før i README eller i JURY_SPORSMAL sp. 19.
Tallvakt: 18 filer, 169 påstander, 0 avvik. Frysvakt: GRØNN, 17 filer uendret.

## Punkt for punkt
- **A1 (ført inn):** ERLIG § 3 sier nå at forskjeller under ~0,02 er «én-sak-støy». Lagt til at også V2s +0,040 er innenfor støyen med KI [−0,007; +0,095], og at forskjeller skal leses mot KI-et. I § 4 står nå «under 0,02, altså én-sak-støy».
- **A2 (ført inn):** JURY sier ikke lenger «låst på val 2025». Ny tekst: båndet er valgt fra et fast rutenett på test-tabellen og sjekket på val (7,5 %/7,9 %), og er altså ikke uavhengig av test.
- **A4 (ført inn):** nytt V2-punkt i «Hvorfor vi ikke jaget testtallet». Hybriden er ikke nevnt.
- **A5 (ført inn):** merknad etter [A]: v2 er andre kjøring av ablasjonen, ikke V2-varianten.
- **A6 (delvis):** JURY pkt. 8 bruker nå samme tidspunkt som BEGRENSNINGER (kontrollagenten, 05.11 kl. 13.37). README:11 (kl. 12.54) er ikke rørt, fordi den ligger utenfor oppgaven og er en annen kjøring med samme tall. Et felles tidspunkt etter frysen må komme fra sluttsjekken (#2538) eller den endelige kaldstarten (#1972).
- **A7 (ført inn):** «Én av de 16». Lista har nå sju punkter fordi A8 og A9 kom til, og teksten sier «Merk sju ting».
- **A8 (ført inn):** nytt punkt i § 6-lista: kaldstart.sh er den gamle kommandoen, og i dag gjør `kjor.sh` det samme.
- **A9 (ført inn):** nytt punkt i § 6-lista: «rundt 0,5» er for rundt, les 0,476 (0,36–0,59), under målet.
- **A10 (ført inn):** hakeparentes etter «NBIM publiserer stemmene løpende» som peker på forbeholdet i § 6. Overskriften i § 6 sier nå at teksten er ordrett med to unntak: dette, og B16.
- **B14 (ført inn):** «(forsøk 2363)» og «(sak 2366)» er strøket, og «dommeren» er byttet med «kontrollagenten».
- **B15 (ført inn):** «uten landsbystier» er byttet med «uten stier til utviklingsmappa».
- **B16 (ført inn):** «dommeren» er byttet med «kontrollagenten» på alle fem steder i ERLIG (også i den ordrette kravresponsen, med merknad) og i JURY.
- **B17 (hoppet over):** speideren satte lav prioritet. Teksten sier allerede «(i repoet, ikke i zipen)».
- **A3, B11–B13:** ikke min oppgave. De gjelder demo_utskrift.txt og tas av smed3 etter generalprøven.

## Grep over hele jury-pakka (smed|landsby|sak N|forsøk N|/Users)
- JURY.md og ERLIG_EVALUERING.md: **0 treff**. BEGRENSNINGER.md og kravrespons.md: 0 treff.
- `demo_utskrift.txt` (smed2, sak 2132, /Users): smed3 tar dette (A3, B11–B13).
- Kodekommentarer i `demo_vis.py`, `demo.sh`, `kjor.sh` og `spor_npx/*`: interne sporingsnumre i kode, ikke jurytekst. Jeg rørte dem ikke så tett på tekststopp.
- `README.md:57`: stien `arbeid/kandidater/smed2_c1_mot` er den frosne prosjektmappa (pyproject.toml/uv.lock står i frysen) og kan ikke gis nytt navn.
- `JURY_SPORSMAL.md` (sak 2417, `landsbyrapport:`) og `NESTE_VERSJON.md` (sak/forsøk NNNN, `landsbyrapport:`, «i landsbyen»): utenfor denne oppgaven, og andre har nylig rettet i dem (#2543). **Forslag til tekststoppen (#2549):** stryk «(sak 2417)» i JURY_SPORSMAL:53, og vurder om prefikset `landsbyrapport:` skal hete f.eks. `teamrapport:`.
- `kilder/` (53 filer): rå kildefiler som bevis. De beholdes ordrett, slik `kilder/LESMEG.md` beskriver.
