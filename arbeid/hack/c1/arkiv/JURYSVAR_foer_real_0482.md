# Case 1: svar på de 6 vanskeligste jury-spørsmålene (metode og evaluering, #2066)

Alle tall har kilde i hakeparentes. [M] = `state/rapporter/c1_mot_modell_smed2.md`,
[A] = `state/rapporter/c1_mot_ablasjon.md`, [K] = `state/rapporter/hack_c1_kaldstart_smed3.md`,
[AG] = `state/rapporter/c1_agent_real_2053.md`, [F] = `state/rapporter/case1_hvilken_fasit.md`, [#n] = forsøk n på forsøkstavla.
Data: NBIMs egne stemmer (real_votes). Test 2026 har 1 539 saker, hvorav 66 MOT [M].

**1. «Lekker framtida inn? Hvordan er splitten?»**
Vi trener til og med 2024, velger C og grense på 2025 og kjører test 2026 én gang [M, #1037]. Historikken bruker bare møter strengt *før* sakens dato (`arbeid/oppgave_2044/train.py:43-47`).
NBIMs begrunnelser (`rationale_text`, `position_paper` m.fl.) er forbudt som input, og en assert stopper kjøringen hvis de brukes [M].
`position_paper` ble fanget som lekkasje underveis: når feltet er satt, er 97,5 % av sakene MOT [M].

**2. «Hvorfor F1 på MOT og ikke accuracy?»**
MOT er bare 66 av 1 539 testsaker [M], så den som aldri sier MOT får 95,7 % riktig (1 − 66/1 539).
Vår modell har faktisk *lavere* accuracy: 95,4 % (33 riktige og 38 falske flagg ut fra P 0,465 / R 0,50 / 71 flagget [M]). Den finner likevel halvparten av avvikene.
Det er avvikene forvalteren trenger hjelp med, og F1 på MOT måler nettopp om vi finner dem (recall) og om flaggene stemmer (presisjon).

**3. «Hvorfor gir følg styret 0, og er ikke det en stråmann?»**
Følg styret sier aldri MOT. Da er treffene 0, recall 0 og F1 0 [#1034 val 2025, målt med offisiell måler; AG test 2026].
Det er gulvet, ikke en løsning. De ekte sammenligningene er «alltid MOT», som gir 0,082 [#1035], og streng historikk, som gir 0,386 [#1038].
Vår valgte modell gir 0,482 [#1037]. Agenten fra kald start gir det samme tallet, 0,4818 [#1046].

**4. «0,482 med KI 0,37–0,58: er det mer enn støy?»**
Ja mot gulvene. Nedre grense 0,37 ligger over 0 og over 0,082 [M, #1035]. Mot målet 0,5 kan vi ikke skille oss ut [M].
Med 66 MOT-saker i test er forskjeller under omtrent ±0,05 støy [A]. Derfor velger vi aldri modell på test, bare på val 2025 (0,522) [M].
Val ligger høyere enn test, så vi rapporterer test som hovedtall [M].

**5. «Hva viser ablasjonen, hva bærer modellen?»**
Historikken bærer modellen. Uten selskapshistorikk faller F1 til 0,372 (diff −0,109, KI −0,169 til −0,050), og uten all historikk til 0,282 (−0,199) [A, #1042].
Tekst, forslagstype, stiller og land endrer F1 bare innenfor ±0,05, så de er ikke signifikante [A]. Noen fjerninger ser bedre ut på test (type 0,504), men de er dårligere på val. Derfor står full modell [A].
Det betyr at agentens begrunnelse først viser selskapets tidligere MOT-stemmer og deretter sitatet fra NBIMs retningslinjer [A].

**6. «Hva med selskaper uten historikk?»**
Delmengden er liten: 69 saker, 8 MOT og 7 selskaper i test [K]. En selskapsblind modell gir 0,471 på helheten [#1044], og med eget historikktrekk blir det 0,500 [#1045].
På de 8 sakene finner den første 2 og den andre 4 [K]. KI er 0–0,55 og 0–0,91, så tallene kan ikke rangere metoder [K].
Svaret vårt: modellen virker uten company_id, men usikre saker om nye selskaper sendes til et menneske [K, AG].

## Svakheter, sagt rett ut
- Vi når ikke målet. 0,482 er under 0,5, og KI 0,37–0,58 dekker begge [M].
- 0,482 forutsetter at NBIMs stemmer tidligere i samme sesong er kjent (løpende historikk). Uten den antakelsen er tallet 0,386 [#1038].
- Halvparten av MOT-sakene blir ikke funnet (recall 0,50), og 38 av 71 flagg er feil [M].
- Ruting hjelper bare hvis mennesket er godt. Uten de rutede sakene er F1 0,634, og 0,746 er en øvre grense som antar at mennesket treffer på alle 176 rutede saker [AG].
- Modellen tar snitt av rangene over sakene som scores sammen. Da flytter én ny sak grensen litt (0,91885 mot 0,91886) [AG]. Det er ikke etikettlekkasje, men testsakene er ikke helt uavhengige av hverandre.
- Ved skrivetid (12:15) står forsøkene #1037–#1046 som *selvrapportert* på tavla. Bare følg styret (#1034) er målt med rundens måler, og omåling skjer i #2062. Tallene her kan altså endre seg etter dommerens kontroll.
- Hvordan vi tolker N-PX-feltet er utledet fra dataene, ikke fra dokumentasjonen. Derfor brukes N-PX aldri som hovedtall [F].
