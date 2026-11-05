# Case 1: stier, kommandoer og lenker i jury-zipen (#2687)

Zip: `state/levering/c1_gronn/jurypakke_c1_1744_7efa4da.zip` (= SISTE_GRONNE.zip), pakket ut i tom `/tmp`-mappe.
Dokumenter: `README.md` (zip-rot), `arbeid/hack/c1/leveranse/README.md`, `leveranse/JURY.md`, `leveranse/kravrespons.md`.
Skript: `arbeid/oppgave_2687/stier.py` (alle `…`- og [](…)-stier mot zip-innholdet).

## Kommandoer: alle virker fra kald kopi
- `sh KJOR.sh`: EXIT 0, FRYSVAKT GRØNN (19 filer), HOVEDTALL 0.512000, TALLVAKT GRØNN.
- `kjor_agent.py --help`: OK. Eksempelet `--sak '…' --ut ut_egen`: p_mot 0,5417, til_menneske 1, NBIM 5.3.1, som README sier.
- `sh arbeid/hack/levering/sjekk_treffsikkerhet.sh /tmp/…`: TP 32 FP 35 FN 26 TN 1446 STEMMER, sha256 LIK.
- `ut/agent.csv` lages som lovet.

## Lenker
- docs.astral.sh/uv, astral.sh/uv/install.sh, nbim.no GVG, nbim.no position-papers: 200.
- `https://vd.nbim.no/` (leveranse/README.md:64) svarte ikke fra minien (timeout, ingen header). Kan være at den blokkerer roboter; bør sjekkes i nettleser.

## Brudd: stier som ikke finnes i zipen
1. `leveranse/README.md:28`: `state/opplastet/20261105_114240_npx_votes.csv` står i datatabellen med sha256, men fila er ikke i zipen. Juryen kan ikke sjekke summen. (Brukes ikke i hovedtallet; enten si «ikke med i zipen» eller ta raden ut.)
2. `leveranse/README.md:30`: `arbeid/hack/c1/arkiv/gammel_data/` finnes ikke i zipen. Teksten sier «De ligger i …» som om de er med.
3. `leveranse/README.md:72`: `c1/hent_npx.py` og `c1/baseline.py` (kreditering) er ikke i zipen. Si at de bare ligger i repoet.
4. `leveranse/README.md:19, 36, 42–46` og `JURY.md:9`: `kjor.sh` / `levering/fremmed.sh` / `hack/maaler.sh`. kjor.sh finnes, men virker ikke i zipen (fremmed.sh og maaler.sh mangler). README:39–40 sier det ærlig, men JURY.md:9 sier tallene er fra «kald kjøring med `kjor.sh`», uten forbeholdet. Mindre brudd.

## Linjehenvisninger som ikke støtter teksten (ikke stier, men jeg fant dem på veien)
5. `JURY.md:28`: «Agenten får 96,0 % (`kilder/TREFFSIKKERHET.md:16`)». Linje 16 der sier **95,7 %** (1473 av 1539), altså eldre tall. 96,0 % står i leveranse/README.md:31.
6. `JURY.md:29`: «agenten gir F1 0,482 på avvik (`kilder/c1_bootstrap_f1.md:6`)». 0,482 er den eldre frosne modellen. Levert repo4 gir 0,529 på avvik (README:17, KJOR-utskrift SCORE 0.529412).

## Tall i kravresponsen som er i strid med resten (utenfor oppgaven, bør til smed2/smed4)
7. `kravrespons.md:10`: «0,512 ligger **under** målet vårt på 0,5». Feil: 0,512 er over 0,5.
8. `kravrespons.md:7`: «95 %-intervall [0,36; 0,59]». Alle andre steder står [0,40; 0,62] for repo4.

Alle andre linjehenvisninger og henvisninger til avsnitt jeg sjekket (TREFFSIKKERHET, c1_val_kaldstart:23, c1_tiltak1_malt:18–19,25, c1_feil_stabilitet:23, c1_repo4_tall_2592:3–5, ERLIG § 2/§ 7, BEGRENSNINGER pkt. 4/6/7/8, JURY_SPORSMAL sp. 18/19/20 og «Hull vi kjenner», beslutning_nyeste pkt. 8–10, README «Datakilder»/«AI-verktøy») finnes og stemmer.
Ikke rettet noe selv.
