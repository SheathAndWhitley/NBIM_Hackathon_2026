# Case 1: hva slags saker MOT-stemmene er (sak 2181)

smed2, 05.11. Test 2026, samme definisjon som måler v3 `--score mot` (nbim_vote MOT og against_board 1, injeksjonsrader ute). Agentens treff er fra den frosne svarfila `arbeid/hack/levering/kjor_agent_real_maskin_alene.csv` (miks h2, maskin alene).

**Kommando** (fra rotmappa i repoet, bare stdlib): `python3 -I <arbeidsmappe>/oppgave_2181/mot_sakstyper.py`

```
test 2026: 1539 saker, 58 MOT mot styret, agenten fant 30

| sakstype (forslag fra) | MOT | saker | MOT-andel | agenten fant |
|---|---|---|---|---|
| styrevalg (styret) | 26 | 729 | 3,6 % | 14 |
| øvrige (styret) | 11 | 571 | 1,9 % | 5 |
| revisor (styret) | 7 | 130 | 5,4 % | 3 |
| andre styresaker (styret) | 6 | 87 | 6,9 % | 1 |
| annen sak / eventuelt (styret) | 6 | 6 | 100,0 % | 6 |
| styrevalg (aksjonærforslag) | 2 | 10 | 20,0 % | 1 |
| andre (aksjonærforslag) | 0 | 6 | 0,0 % | 0 |

øvrige (styret), MOT per type: [('ARTICLES', 3), ('SAY_ON_PAY', 3), ('SHARE_ISSUANCE', 2), ('RPT', 1), ('EQUITY_PLAN', 1), ('FIN_STATEMENTS', 1)]
forslagsstiller: [('Management', 56), ('Shareholder', 2)] av saker: [('Management', 1523), ('Shareholder', 16)]
land (MOT): [('Japan', 7), ('United States', 7), ('Indonesia', 7), ('Switzerland', 4), ('India', 4)]
selskaper med flest MOT: [('Texas Capital Bancshares, Inc.', 3), ('Nomad Foods Limited', 3), ('PT Solusi Sinergi Digital Tbk', 3), ('LOTTE Chemical Corp.', 2), ('Burgan Bank KPSC', 2)]
```

## Funn
- 56 av 58 MOT er styrets egne forslag (bekrefter speiderens sak 2172). De 2 aksjonær-MOT er begge **styrevalg med kandidat foreslått av aksjonærer**, ikke klassiske ESG-forslag. De 6 øvrige aksjonærforslagene fikk ingen MOT.
- Styrevalg er 28 av 58 MOT. «Annen sak/eventuelt» får MOT hver gang (6 av 6), og agenten finner alle.
- Svakest: revisor (3 av 7) og «andre styresaker» (1 av 6). Der ligger mye av de 28 som ikke ble funnet.
- Spredt geografisk: Japan, USA og Indonesia har 7 hver.
- Lagt inn i `arbeid/hack/levering/BESLUTNINGSSTOTTE.md` som ny seksjon «Hva slags saker MOT-stemmene er» (før Robusthet). `c1_tallvakt.py`: OK (139 påstander, 0 avvik).
- Rettet underveis: første utkast hadde 28 styrevalg som rent styret-tall. Krysstabellen viste at 2 av dem er aksjonærforslag, så tabellen deler dem nå.
