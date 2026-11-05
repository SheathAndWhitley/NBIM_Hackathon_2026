# Name that LLM: oppstartsplan fra fredag 06.11 morgen (#2525)

Én side som samler planene fra før. Detaljene ligger i `ntl_startplan.md` (#2506) og `ntl_forste_forsok.md` (#2510). Ingenting startes før fristen kl. 20 i dag.
KP: forventet beste offentlige 0,586, fikk 0,586 (ntl_lora_resultat.md:44, ref 57968608). Forventet snitt 3B+1,5B 0,6212 nestet, fikk 0,6212 (ntl_3b_innsending.md:11).

## Dette vet vi fra før
- **Beste offentlige:** 1,5B-LoRA, **0,586** (#1621). Raav uten LoRA ga 0,487. **Beste lokale:** snitt av 3B og 1,5B, **0,6212 nestet** (#1634). Det er ikke sendt inn.
- **Gapet:** nestet → offentlig er målt bare én gang, **−0,025 (±0,03)**. Mål 0,65 offentlig ≈ **0,675 nestet**, altså +0,054 over det beste vi har. Plass 10 sto på 0,707 (03.11).
- **Lukkede spor (sporsjekk: 15 treff, ingen nye lukkinger):** overflatestil, funksjonsord, tokenizer-n-gram, NCD, trio-temperatur og parvis trio-logit lå alle under støy (#1491). Sentrering/ungarsk ga 0,5705 lokalt men bare 0,342 offentlig (#1546). Gaggle-rader ga ikke løft i kjeden (#1485), men er ikke testet i LoRA.
- **Åpne spor:** snittkjernen (#1765, lagt bort for hackathonet), 7B (uprøvd: 3B stoppet ved 66 % av poolen), flere frø (uprøvd).
- **7B-kost (UKONTROLLERT anslag):** QLoRA 4-bit gir ca. 400 tok/s. 66 % av poolen tar ca. 1010 min, som er over grensa på 540 min per økt. Derfor kjører vi bare 25 % av poolen, ca. 7,5 t GPU av 30 t per uke.
- **Lærdom fra Case 1:** måler med sha først, så svarformat, kaldstart, frys per innsending og tallvakt. Hver oppgave får egen måler (#2139-feilen: oppgaver uten egen måler falt til den globale).

## Kl. 08: dommeren setter opp måleren før noe forsøk
`tavle maaler --oppgave <id>` med `arbeid/name_that_llm/maaler/maaler.py --uten-sann` (sha 8733327407) på hver NTL-oppgave. dommer2 kjører `ntl_frys.py` og kaldstart offline. Uten frys blir det ingen innsending.

## De tre første oppgavene (start samtidig fredag morgen)
| # | Hvem | Oppgave | Akseptkrav | Kost |
|---|---|---|---|---|
| A | smed | Snittkjerne 3B+1,5B (#1765) via `arbeid/oppgave_1618/bygg.py` | SJEKK i kjerneloggen ≥ 0,575 **og** nestet ≥ 0,618 hos dommeren. Da 1 innsending, forventet 0,59–0,60 offentlig. Gir også måling nr. 2 av gapet. | 90 min, ca. 51 min GPU |
| B | smed2 | Qwen2.5-7B QLoRA trinn 1 på fast utvalg av 25 % av Open Pool | Etter 10 min: < 250 tok/s gir stopp. SJEKK > 0,5665 betyr fortsett. Under 0,55 stopper 7B. Mellom 0,55 og 0,5665 er det uavgjort til C er målt. | 30 min å bygge, ca. 7,5 t GPU |
| C | smed3 | Trinn 2 for 1,5B med nytt frø, snittet med gammel OOF | Nestet rapportert mot 0,6109. ≥ +0,008 betyr at gevinsten er varians: flere frø gjør jobben og B nedprioriteres. < +0,003 betyr at mangfoldet er ekte og B prioriteres. Ingen innsending. | 60 min, ca. 30 min GPU |

## Slik måler vi mot 0,65
- **Hovedtall:** nestet balansert treffsikkerhet fra `arbeid/oppgave_1618/blend.py` på forsøkets OOF. Forventet offentlig er nestet − 0,025, til A gir måling nr. 2. Deretter bruker vi snittet av de to gapene.
- **Sannhet:** bare offentlig Kaggle-score teller som målt. Maks 5 innsendinger per dag, og dommeren godkjenner hver. Bare forsøk med nestet ≥ beste − 0,003 sendes.
- **Stopp-punkt fredag kl. 14:** står ikke 7B (SJEKK i trinn 1) over grensa, går vi over til data: Gaggle-supersettet som trinn 1-data for LoRA (#1484).
- **Ærlig:** A gir ca. +0,010. Bare B kan nå 0,65, og den sjansen anslår jeg til ca. 25 %. Står vi under 0,62 offentlig søndag, melder vi det til guden med tall, i stedet for å bruke flere uker.
