# Case 1 (#2631): øvelse på byttet til STÅR i kald kopi, med tid per steg

Kald kopi: /tmp/staar_ovelse_2631 (42 MB, rsync av c1 uten arkiv, levering, verktøy, oppgave_2044/2046/2047/2103/2274/2598/2618/2625, kandidatens låste miljø, state/c1_frys.json). Egen git-baseline i kopien. leveranse/ og levering/ i landsbyen er ikke rørt av meg (alle mine kommandoer kjørte med rot i kopien; endringene der kl. 17:19–17:23 er andres commits #2592/#2635/#2639).

## Dom: kjeden i LES.md er RØD som den står. Grønn etter to rettelser. Totalt 3 min 27 s maskintid.

| Steg | Kommando (i kopien) | Utgang | Tid |
|---|---|---|---|
| 0a | `lag_staar.py --sjekk` (reserve = BYTT-tekst?) | LIK | 0 s |
| 0b | `lag_staar.py` (bygg README/kravrespons STÅR) | OK | 0 s |
| 0c | `lag_staar_erlig.py /tmp/jurypakke_c1_2587.zip` | OK, lik git | 0 s |
| 1 | `tilbake_fra_zip.sh KOPI zip2587 /tmp/bytte2572_c1_frys.json` | OK, 24 filer tilbake, frysvakt grønn | 3 s |
| 2a | `lim_inn.py --variant STAAR --sluttfor` (som oppgaveteksten sier) | **AVVIST**, utgang 1: «--sluttfor gjelder bare BYTT» | 0 s |
| 2b | `lim_inn.py --variant STAAR` | OK, men gir IKKE reserve-utgaven (§ 7-overskrift og repo4-rad mangler) | 0 s |
| 3 | `cp reserve_staar/{README,kravrespons,ERLIG_EVALUERING,JURY_SPORSMAL}.md leveranse/` | OK | 0 s |
| 5 | `c1_tallvakt.py --rot KOPI` | **RØD: 15 avvik** (MUNTLIG.md, KRAVRESPONS.md, GITHUB_README_UTKAST.md) | 0 s |
| 8 | `pakk_jury.sh` | **RØD** (tallvakt i fremmed.sh) | 42 s |
| 10 | `cp reserve_staar/MUNTLIG.md leveranse/` (femte fil, LES.md nevner fire) | OK | 0 s |
| 12 | `arbeid/oppgave_2631/staar_rest.py --rot KOPI --skriv` (45 erstatninger i KRAVRESPONS/EN_SIDE/GITHUB_README_UTKAST) | OK | 0 s |
| 18 | `c1_tallvakt.py --rot KOPI` | **GRØNN**, 177 påstander, 0 avvik | 0 s |
| 19 | `pakk_jury.sh /tmp/jurypakke_staar_2631.zip` | GRØNN, 146 filer | 64 s |
| 20 | `test_jury_zip.sh` | GRØNN, HOVEDTALL 0.476190, TP 30 FP 38 FN 28 TN 1443 | 59 s |
| 21 | `frys_diff.sh zip2587 ny fasit` | 15 avvik, ventet: 4 STÅR-tekster ENDRET + 11 filer laget etter zip 2587 | 1 s |

Sum alle kjørte steg inkl. de røde rundene: 207 s. Ren STÅR-kjede uten feilrunder (1, 3, 10, 12, 18, 19, 20): ca. 2 min 10 s. Tenketid kommer i tillegg; under 10 min holder med stegene under.

## Funn
1. **Oppgavetekstens kommando er feil.** `lim_inn.py --variant STAAR --sluttfor` avvises av skriptet. STÅR-utfallet er `cp` av reserve_staar-filene (LES.md). `lim_inn.py --variant STAAR` alene gir heller ikke reserveteksten: lag_staar_erlig.py gjør tre erstatninger til (§ 7-overskrift, repo4-raden, «Den frosne modellen er levert uendret»). Bruk cp, ikke lim_inn.
2. **LES.md mangler MUNTLIG.md.** Den er laget etter zip 2587 (#2632), har BYTT-tall, og tilbake_fra_zip.sh rører den ikke. reserve_staar/MUNTLIG.md finnes. Fem filer skal kopieres, ikke fire.
3. **Tre tekster dekkes verken av zipen eller reserven:** `levering/KRAVRESPONS.md` og `EN_SIDE.md` (usporet, holdt utenfor zipen i #2587) og `GITHUB_README_UTKAST.md` (laget etter zipen, #2606). Alle tre har BYTT-tall og gjør tallvakta rød, som stopper pakk_jury. `arbeid/oppgave_2631/staar_rest.py` reverserer dem (omvendt bytt_tall.py + KI, sidetall, HOVEDTALL-utskrift, accuracy, og én eksplisitt linje KRAVRESPONS:12 som hoppregelen «#2044» ellers skjermer). Tallvakt 0 avvik etterpå. Tekstene er interne (ikke i zipen) unntatt GITHUB_README_UTKAST som ligger i levering/ og blir med i zipen.
4. **Reserven må regenereres etter hver BYTT-tekstendring.** `lag_staar.py --sjekk` var LIK kl. 17:1x i kopien, men #2639 (17:23) endret README/ERLIG etterpå. Sjekk rett før bruk (resultat nå står nederst). Hvis den stopper på «fant 0 treff», må regelen i lag_staar.py oppdateres før STÅR.
5. frys_diff mot zip 2587 gir 15 avvik ved STÅR, ikke «bare EN_SIDE/KRAVRESPONS» som tilbake_fra_zip.sh sier: 11 filer er laget etter zipen (MUNTLIG, kilder/*, LAGET, GITHUB_README_UTKAST, EN_SIDE, KRAVRESPONS) og 4 er STÅR-tekstene. Det er ventet, ikke rødt.

## STÅR-oppskrift (etter dom STÅR kl. 18:45), fra landsbymappen
```
python3 -I arbeid/oppgave_2598/lag_staar.py --sjekk                      # må si LIK, ellers oppdater reglene først
sh arbeid/hack/c1/bytte/tilbake_fra_zip.sh <repo> /tmp/jurypakke_c1_2587.zip /tmp/bytte2572_c1_frys.json
cp arbeid/hack/c1/reserve_staar/{README,kravrespons,ERLIG_EVALUERING,JURY_SPORSMAL,MUNTLIG}.md arbeid/hack/c1/leveranse/
python3 -I arbeid/oppgave_2631/staar_rest.py --skriv                      # KRAVRESPONS, EN_SIDE, GITHUB_README_UTKAST
python3 -I arbeid/verktoy/c1_tallvakt.py                                  # skal gi 0 avvik
python3 -I arbeid/hack/levering/frys_fasit.py > arbeid/hack/levering/frys_fasit_1600.sha256
sh arbeid/hack/levering/pakk_jury.sh /tmp/jurypakke_c1_staar.zip && sh arbeid/hack/levering/test_jury_zip.sh /tmp/jurypakke_c1_staar.zip
```
Merk: tilbake_fra_zip.sh legger tilbake frysfila fra 16:00 (17 filer). Ny frys fra #2592 (17:18) overskrives, det er meningen ved STÅR. Logger: /tmp/staar_2631_logg/, tider: /tmp/staar_2631_tider*.tsv, zip: /tmp/jurypakke_staar_2631.zip.
Resultat av lag_staar.py --sjekk kl. 17:25 i landsbyen: README.md: fant 0 treff (skal være 1) for: P 0,48, R 0,55 (TP 32 FP 35 FN 26). Følg styret gir 0. Valgt på val 20
