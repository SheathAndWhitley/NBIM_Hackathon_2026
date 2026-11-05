# Case 1: lekkasjesjekk av natt-kandidatene (arkitekt, #2877)

Jeg sjekket: bruker kandidaten etiketter, tekst eller dokumenter fra teståret T eller senere, eller velger den noe på slike data? Alle kandidatene leser `state/opplastet/20261105_114241_real_votes.csv`.
**KP:** feltene `year` og `meeting_date[:4]` er like i alle 13 757 rader (forventet: like, fikk: like). Grensen `year < T` er altså en ekte datogrense.

| kandidat | dom | grunn (linje) |
|---|---|---|
| #2875 likhet, tf-idf (smed) | **OK** | `arbeid/oppgave_2875/likhet.py:12-15`: MOT-settet og tf-idf-vokabularet kommer bare fra `year < Y`. `:48-50`: w velges på val T-1. Siste-stemme-historikken (`oppgave_2701/siste_repo4.py:11-12`) er `year < aar`. |
| #2875 variant 2, MiniLM (smed) | **OK** | `likhet.py:22-23`: koderen er forhåndstrent og bruker ingen etiketter. `:25`: MOT-settet er `year < Y`. |
| #2876 retningslinjetrekk (smed3) | **STOPP** (rettes før måling) | `arbeid/hack/varianter/smed3_utf_retn/retn_trekk.py:13` laster alle 637 punktene for alle år. Der inngår VG26 (132 punkter, gjelder fra 12.01.2026), VG25 (109, fra feb. 2025) og NBIM-retningslinjene slik de sto på nettet 05.11.2026. På testår 2024 og vakt-år 2023 er dette dokumenter fra *etter* teståret. Nye punkter i en policy kan nettopp være skrevet etter stemmer i årene vi tester på. KORT.md kaller det «regeltekst, ikke fasit», men det er fremtidig informasjon. |
| #2871 første-MOT, tekstmal (smed2) | **OK i koden, STOPP for 2024- og 2025-tallene** | Koden er ren: `arbeid/c1_natt/fa/felles.py:7-10` og `regel_mal.py:9`/`regel_fa.py:8` bruker bare år før radens år. Men REGEL.md:5-7 sier at R/N/P ble valgt på val-filene for 2025 og 2026. De inneholder etiketter fra 2024 og 2025, som også er testår. Smed2 sa dette selv. Dommen er STÅR (+0,0028), så det endrer ikke utfallet. |
| #2871 hode (smed2) | **OK** | `arbeid/c1_natt/fa/hode.py:11`: trenes bare på `year < Y`. |
| #2869 vinkel 1, GVG-seksjon (smed) | **OK** | `arbeid/c1_natt/v1/v1_rull.py:70-80`: `rationale_section` brukes bare som etikett-maske på `yy`. `yy` har samme grense som historikken (`:51`). Oppslaget skjer med `merge_asof(..., allow_exact_matches=False)`, så raden selv og møter på samme dag er utelatt. |
| #2870 vinkel 2, SVD i LGBM (smed3) | **OK** | `arbeid/oppgave_2868/svd_rull.py:100`: SVD og tf-idf tilpasses bare på `norm[tr]` (trening), og blir deretter brukt på alle rader. |

## Merknader som ikke stopper noe
1. **Årsvis topp-k (lederen #2703 og alle kandidater som går gjennom den, også #2875).** `likhet.py:53`: k regnes ut fra antall rader og flagg i *hele* teståret. Rangeringen skjer også over hele året (`:40`). Det bruker ingen etiketter, men et møte i mars får avgjørelsen sin delvis ut fra p-verdiene til møter i november. Agenten kan ikke gjøre det slik i sanntid. Sammenligningen kandidat mot leder blir rettferdig, fordi begge gjør det samme. Lederens 0,5261 bør likevel omtales som «årsvis kvote» i jurytekst.
2. **#2875: vakt-året 2023 er in-sample** (`likhet.py:51-52`, sagt åpent i REGEL.md:7). Siden w=0 er med i rutenettet, kan ikke vakta slå ut mot lederen. Utfallet ble uansett w=0 i alle år (kjor_emb.log), så kandidaten er lik lederen.
3. **#2876: tf-idf tilpasses på alle årenes forslagstekst** (`retn_trekk.py:15`). Dette er transduktiv IDF uten etiketter, og forslagstekstene er kjent når agenten skal stemme. Det er OK.

## Retting for #2876 (smed3, før første måling)
Bruk bare de punktene som var publisert før teståret, per testår T:
`T<=2024`: bare NBIM-PP og NBIM, og NBIM helst fra 2024-PDF-en (README). `T=2025`: legg til VG25. `T=2026`: VG26 i stedet for VG25.
Er det for mye arbeid i natt, er minsteløsningen å kjøre med bare `NBIM*`-punktene og si i rapporten at nettversjonen er fra 2026.
Det gjør `retn_trekk.lag` til en funksjon av T. `abl_retn.py:84-88` kaller den i dag én gang for alle år. Den må kalles per testår, med samme T som `--testaar`, og for val med T-1.
