# #2875 regel fastsatt FØR måling (smed, 05.11 ~19:45)
Kandidat «likhet»: lederen midt+av (#2703) med ett nytt trekk lagt på p_avvik.
1) sim(rad) = høyeste tfidf-cosinus (ord 1-2-gram, sublinear_tf, min_df=2, vokabular tilpasset BARE tekster fra år < radens år)
   mellom radens proposal_text og alle forslag i år < radens år der NBIM stemte MOT og styret ikke sa MOT.
   Bare fortid, ingen fasit fra radens eget år. injection_flag=1 utelates.
2) p' = p_avvik + w*sim. Midt-terskel som #2703 (samme k, toppen k etter p'), deretter av-regelen (#2701).
3) w velges per testår T på val T-1 (repo4_T_val, fasit y{T-1}) fra {0, 0.05, 0.1, 0.2, 0.3}; lik score -> minste w.
   På val brukes k = antall rå-flagg i val (ingen midt, den trenger et år før). w=0 er nøyaktig lederen midt+av.
4) Testår 2024/25/26 én gang med offisiell måler oppgave_2567/maaler_aar.py --score mot.
5) Vakt-år 2023 = repo4_2024_val med w valgt på 2023 selv (in-sample, sagt åpent; optimistisk vakt).
Bytteregel #265/#281 mot frossen repo4 (0,5057/0,5309/0,5120, 2023 = repo4_2024_val rå):
snitt testår >= +0,02 og intet år (2023-2026) < -0,02. Rapporteres også mot lederen midt+av (0,5581).
Ingen varianter teller. Variant «bare ny tekst» (w*sim bare der samme selskap+tekst ikke har historikk) rapporteres som innsikt, ikke kandidat.

## Variant 2, skrevet FØR måling (etter at tfidf ga w=0 på val alle år, ~19:55)
Identisk regel som over, bare sim = høyeste cosinus i all-MiniLM-L6-v2 (lokal, normaliserte embeddinger) mot
MOT-mot-styret-forslag i år < radens år. Samme w-rutenett, samme valg på val T-1, samme bytteregel og vakt-år.
Dette er siste variant i #2875; ingen flere justeringer etter at tallene er sett.
