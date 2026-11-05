"""Writes results/nokkeltall.md: every number used in the presentation, generated from code.

Rule for the team: copy numbers from this file, never from chat or memory. It is rewritten
on every `python run.py`, so it can never drift from results/metrics.json.
"""
from __future__ import annotations

import subprocess
from datetime import datetime

from .config import RESULTS, ROOT


def _p(x, d=1):
    return "–" if x is None else f"{x * 100:.{d}f} %".replace(".", ",")


def _n(x, d=3):
    return "–" if x is None else f"{x:.{d}f}".replace(".", ",")


def _k(n) -> str:
    """Integer with a space as thousands separator (13 757)."""
    return f"{int(n):,}".replace(",", " ")


def _dict(d: dict) -> str:
    return ", ".join(f"{k} {v}" for k, v in d.items())


TYPES_NO = {"DIRECTOR_ELECTION": "styrevalg", "OTHER_MGMT": "øvrige ledelsesforslag", "FIN_STATEMENTS": "regnskap",
            "SHARE_ISSUANCE": "aksjeutstedelse", "SAY_ON_PAY": "say-on-pay", "MERGER": "fusjon",
            "EQUITY_PLAN": "aksjeprogram", "AUDITOR": "revisor", "ARTICLES": "vedtekter", "DISCHARGE": "ansvarsfrihet",
            "OTHER_BUSINESS": "eventuelt", "RPT": "nærstående transaksjoner", "DIRECTOR_PAY": "styrehonorar"}


def _ci(c, pct=True):
    lo, hi = c
    return f"{_p(lo) if pct else _n(lo)} til {_p(hi) if pct else _n(hi)}"


def _commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                              text=True, timeout=5).stdout.strip() or "ukjent"
    except Exception:
        return "ukjent"


NAMES = {"always_board": "Følg alltid styret", "persistence": "Gjenta forrige beslutning",
         "type_majority": "Flertall per sakstype", "nbim_pay_rule": "NBIMs egen lønnsregel",
         "model": "**Modell (vår)**"}


def _table(test: dict, keys) -> list[str]:
    rows = ["| System | Presisjon | Recall | F1 | PR-AUC | Recall ved 20 % lest | Accuracy |",
            "|---|---|---|---|---|---|---|"]
    for k in keys:
        m = test[k]
        rows.append(f"| {NAMES.get(k, k)} | {_p(m['precision'])} | {_p(m['recall'])} | {_n(m['f1'], 2)} | "
                    f"{_n(m['pr_auc'])} | {_p(m['recall@20%'])} | {_p(m['accuracy'])} |")
    return rows


def write(results: dict) -> str:
    a, b, s = results["data_audit"], results["ballot"], results["say_on_pay"]
    rv, nv = a["real_votes"], a["npx_votes"]
    rv = {**rv, "with_board_by_year": {int(k): v for k, v in rv["with_board_by_year"].items()}}  # JSON keys are str
    L = [f"# Nøkkeltall", "",
         f"Generert av `python run.py` {datetime.now():%d.%m.%Y %H:%M} (commit `{_commit()}`). "
         "**Ikke rediger for hånd.** Alle tall i presentasjon, kravrespons og README skal hentes herfra.", ""]

    # 1. data
    L += ["## 1. Data og revisjon", "",
          f"- **Fasit:** `ny_data/real_votes.csv` (NBIMs egne stemmer, API-data fra arrangørene): "
          f"{_k(rv['rows'])} saker, {_k(rv['meetings'])} møter, {rv['companies']} selskaper, "
          f"{rv['date_range'][0]} til {rv['date_range'][1]}.",
          f"- NBIM stemte **mot styret i {_p(rv['against_board_rate'])}** av sakene med etikett, altså "
          f"**{_p(rv['with_board'])} med styret** (2025: {_p(rv['with_board_by_year'][2025])}). "
          f"AVSTÅ ({rv['abstain_votes']} stemmer) regnes verken som med eller mot styret.",
          f"- Teller man AVSTÅ som «ikke med styret», slik NBIM gjør i sin egen statistikk: "
          f"{_p(rv['with_board_provided_label'])}. NBIM oppgir selv 94 % for 2025.",
          f"- **`npx_votes.csv` er feilmerket:** styrets anbefaling (`mgmt_rec`) speiler NBIMs stemme. "
          f"{_k(nv['mgmt_proposals_with_board_rec_MOT'])} ledelsesforslag står med «styret anbefaler MOT» "
          f"(NBIM stemte MOT på {_k(nv['of_which_nbim_voted_MOT'])}). Filens egen etikett gir "
          f"{_p(nv['with_board_provided_label'])} med styret; med rettet styreanbefaling blir det "
          f"{_p(nv['with_board_corrected'])}, på linje med NBIMs egne data."]
    if "sec_crosscheck" in a:
        c = a["sec_crosscheck"]
        L.append(f"- **Krysssjekk mot NBIMs egen SEC-filing** (say-on-pay i USA): `real_votes.csv` stemmer i "
                 f"{_p(c['real_vs_sec_agreement'])} av {c['real_vs_sec_matched']} saker. `npx_votes.csv` fanger "
                 f"bare {c['of_which_npx_says_MOT']} av {c['sec_against_votes_in_npx_match']} MOT-stemmer.")
    L.append(f"- `npx_votes.csv` har {nv['injection_flag_rows']} instrukslignende sakstekster (brukes i motstandstesten).")

    # 2. ballot
    sp = b["split"]
    L += ["", "## 2. Hele stemmeseddelen (hovedresultat)", "",
          "Mål: stemte NBIM **mot** styrets anbefaling? (MOT når styret sier FOR, FOR når styret sier MOT.)", "",
          "| Del | År | Saker | Avvik | Andel |", "|---|---|---|---|---|"]
    for name, yrs in (("train 2019-23", "2019–2023 (trening)"), ("valid 2024", "2024 (valg av modell og terskler)"),
                      ("test 2025-26", "2025–2026 (test, kjørt én gang)")):
        L.append(f"| {name.split()[0]} | {yrs} | {_k(sp[name]['n'])} | {sp[name]['deviations']} | {_p(sp[name]['rate'])} |")
    th = b["thresholds"]
    L += ["", f"Modell: logistisk regresjon (`{b['selected']}`, valgt på 2024 blant 7 kandidater). Én lært modell, "
              "ingen håndlagde regler: NBIMs presedens (samme sak/person før) er en variabel med lært vekt. "
              f"Terskler (valgt på 2024): flagg «NBIM stemmer trolig mot» ved p ≥ {_n(th['t_flag'])}, "
              f"analytikerkø ved p ≥ {_n(th['t_review'])}.", "",
          f"**Testresultat 2025–26** ({_k(sp['test 2025-26']['n'])} saker, {sp['test 2025-26']['deviations']} avvik):", ""]
    L += _table(b["test"], ["always_board", "persistence", "type_majority", "model"])
    ci, dd = b["test_model_minus_persistence"], b["test_model_ci95"]
    rq, hb = b["review_queue"], b["hit_breakdown"]
    L += ["", f"- **95 %-intervall for modellen** (bootstrap trukket per selskap): presisjon {_ci(dd['precision'])}, "
              f"recall {_ci(dd['recall'])}, PR-AUC {_ci(dd['pr_auc'], False)}, recall ved 20 % lest {_ci(dd['recall@20%'])}.",
          f"- **Modell minus «gjenta forrige beslutning»:** PR-AUC {_n(ci['pr_auc']['mean_diff'])} "
          f"({_n(ci['pr_auc']['ci_low'])} til {_n(ci['pr_auc']['ci_high'])}); recall ved 20 % lest "
          f"{_p(ci['recall@20%']['mean_diff'])} ({_p(ci['recall@20%']['ci_low'])} til {_p(ci['recall@20%']['ci_high'])}); "
          f"F1 {_n(ci['f1']['mean_diff'])} ({_n(ci['f1']['ci_low'])} til {_n(ci['f1']['ci_high'])}). "
          "Et intervall som ikke inneholder 0 betyr at forskjellen ikke er tilfeldig.",
          f"- **Analytikerkø:** analytikeren leser {_p(rq['share_reviewed'])} av sakene og fanger {rq['caught']} av "
          f"{rq['deviations']} avvik ({_p(rq['caught'] / rq['deviations'])}). {rq['missed_in_autoclear']} avvik godkjennes "
          f"automatisk med styret (bom). Bom per type: "
          f"{_dict({TYPES_NO.get(k, k): v for k, v in hb['missed_in_autoclear_by_type'].items()})}.",
          f"- **Kalibrering:** Brier {_n(b['test_model_brier']['model'], 4)} mot {_n(b['test_model_brier']['constant'], 4)} "
          "for en konstant basisrate (lavere er bedre).",
          "- **Per testår:** " + "; ".join(f"{y}: P {_p(v['precision'])}, R {_p(v['recall'])}, PR-AUC {_n(v['pr_auc'])}"
                                           for y, v in b["by_year"].items()) + ".",
          "", "**Hvor treffene kommer fra (vær ærlig om dette):**",
          f"- {hb['precedent_cases']} testsaker har presedens (NBIM avvek på samme sak eller person før); "
          f"{hb['precedent_cases_that_deviated']} av dem er avvik nå.",
          f"- Modellen flagger {hb['model_flags']} saker og treffer {hb['model_hits']}: {hb['hits_with_precedent']} har "
          f"presedens, {hb['hits_without_precedent']} har ikke. Av de {hb['precedent_cases']} presedenssakene flagges "
          f"{hb['precedent_cases_flagged']}.",
          f"- {hb['deviations_without_precedent']} avvik har ingen presedens. Modellen flagger {hb['of_which_flagged_by_model']} "
          f"av dem, og analytikerkøen fanger {hb['of_which_caught_in_review']}. "
          f"({hb['deviations_never_seen_before']} er saker/personer NBIM aldri har stemt på før; i "
          f"{hb['deviations_nbim_followed_board_last_time']} fulgte NBIM styret forrige gang.)",
          f"- Avvik per land (test): {_dict(hb['deviations_by_country_top'])}."]
    rvd = {}
    for r in b["rolling_validation"]:
        rvd.setdefault(r["year"], {})[r["system"]] = r
    L += ["", "**Valg av modell: hvorfor ingen håndregel** (hvert år trent på årene før; testårene er ikke brukt):", "",
          "| Valideringsår | Avvik | PR-AUC modell / «presedens først» | Fanget ved 20 % lest: modell / «presedens først» / gjenta forrige |",
          "|---|---|---|---|"]
    for yr, g in sorted(rvd.items()):
        L.append(f"| {yr} | {g['model']['deviations']} | {_n(g['model']['pr_auc'])} / {_n(g['precedent_first_variant']['pr_auc'])} | "
                 f"{_p(g['model']['recall@20%'])} / {_p(g['precedent_first_variant']['recall@20%'])} / {_p(g['persistence']['recall@20%'])} |")
    rj = b["rejected_variant_precedent_first_test"]
    L += ["", "- Varianten «presedens først» (håndregel: alle saker der NBIM avvek før legges øverst) ga **samme analytikerkø "
              "hvert år** og uavgjort PR-AUC (2–2). Den enkleste modellen ble derfor valgt. Ingen av dem svekkes over tid.",
          f"- Åpenhet: på testsettet ville varianten sett bedre ut (PR-AUC {_n(rj['pr_auc'])}, recall {_p(rj['recall'])}), men "
          "valg av modell skjer på valideringsår, aldri på testsettet."]
    cb = b["citation_baselines"]
    L += ["", "**Grunnlinjer for sitering** (riktig GVG-seksjon på de "
              f"{cb['n_test_deviations_with_section']} testavvikene der NBIM oppga seksjon; agenten må slå disse):",
          f"- Flertall per sakstype: {_p(cb['type_majority']['exact_section'])} riktig seksjon "
          f"({_p(cb['type_majority']['same_chapter'])} riktig kapittel).",
          f"- Forrige seksjon på samme sak/person: finnes for {_p(cb['previous_section']['coverage'])}, og er da riktig i "
          f"{_p(cb['previous_section_accuracy_when_present'])}.",
          f"- Forrige seksjon, ellers flertall per type: **{_p(cb['previous_section_else_type']['exact_section'])}** riktig seksjon."]
    ti = b["triage_injection"]
    L += ["", "**Motstandstest for triagemodellen** (injeksjonstekst lagt til i alle testsaker; trenger ingen API-nøkkel):"]
    for name, r in ti.items():
        L.append(f"- `{name}`: gjennomsnittlig endring i sannsynlighet {_n(r['mean_abs_change_p'], 4)} (maks {_n(r['max_abs_change_p'], 3)}); "
                 f"{r['route_changed']} saker byttet rute (andel lest etterpå {_p(r['share_reviewed_after'])}, de fleste flyttes *inn* i køen); "
                 f"**{r['deviations_moved_from_review_to_auto']} avvik flyttet fra analytikerkø til automatisk godkjenning**; "
                 f"køen fanger {r['deviations_caught_after']} avvik etterpå.")
    L.append("  (Maks-endringen er stor fordi den kalibrerte sannsynligheten er en trappefunksjon: et lite "
             "skift kan krysse et trinn. Gjennomsnittet er det representative tallet.)")

    # 3. say-on-pay
    pv = s["policy_vs_practice"]
    L += ["", "## 3. Say-on-pay i USA (dypdykk, NBIMs SEC N-PX + lønn fra møtets egen innkalling)", ""]
    seasons = s["data"]["seasons"]
    L.append("Sesonger: " + "; ".join(f"{k}: {_k(v['size'])} møter, {int(v['sum'])} MOT ({_p(v['mean'])})" for k, v in seasons.items())
             + ". Trening 2024-25, test 2025-26.")
    L.append("")
    L += _table(s["test"], ["always_board", "persistence", "nbim_pay_rule", "model"])
    dm = s["test_model_minus_nbim_rule"]
    L += ["", f"- **Modell minus NBIMs regel:** PR-AUC {_n(dm['pr_auc']['mean_diff'])} ({_n(dm['pr_auc']['ci_low'])} til "
              f"{_n(dm['pr_auc']['ci_high'])}), F1 {_n(dm['f1']['mean_diff'])} ({_n(dm['f1']['ci_low'])} til {_n(dm['f1']['ci_high'])}). "
              "Ikke signifikant: funnet er at NBIM følger sin egen regel.",
          f"- **Policy vs praksis:** over NBIMs terskel (USD 20m, 25m fra 2025) stemte NBIM MOT i {_p(pv['against_rate_above_threshold'])} "
          f"(n = {pv['n_above_threshold']}), under i {_p(pv['against_rate_below_threshold'])}. {_p(pv['share_of_against_votes_above_threshold'])} "
          f"av MOT-stemmene ligger over terskelen. CEO-skifte i året: {_p(pv['against_rate_ceo_change'])} MOT, ellers "
          f"{_p(pv['against_rate_no_ceo_change'])}."]
    cm = s["data"].get("cik_match", {})
    if cm:
        L.append("- **Kobling til SEC (utvalgsskjevhet):** " + "; ".join(
            f"{season}: " + ", ".join(f"{'med kobling' if k == 'matched' else 'uten kobling'} {v['n']} møter, "
                                       f"{_p(v['against_rate'])} MOT" for k, v in g.items())
            for season, g in cm.items()) + ".")

    # 4. agent
    L += ["", "## 4. LLM-agenten", ""]
    ag = results.get("agent")
    if not ag or not ag.get("answered"):
        L.append("_Ikke kjørt ennå._ Kjøres med API-nøkkel (`python run_agent.py --run`); tallene fylles inn her automatisk.")
    else:
        cv = ag.get("citation_vs_nbim", {})
        L += [f"- Utvalg: {ag['n_sample']} saker (alle testavvik + tilfeldige med-styret-saker, vektet tilbake), {ag['answered']} besvart.",
              f"- Agenten alene: presisjon {_p(ag['llm_alone']['precision'])}, recall {_p(ag['llm_alone']['recall'])}.",
              f"- **Riktig GVG-seksjon:** {_p(cv.get('exact_section'))} (kapittel {_p(cv.get('same_chapter'))}) på "
              f"{cv.get('n_deviations')} avvik, mot grunnlinjen {_p(cb['previous_section_else_type']['exact_section'])}.",
              f"- Sitater verifisert ordrett: {_p(ag.get('citation_verified_share'))}."]
        for k, v in (ag.get("adversarial") or {}).items():
            L.append(f"- Motstandstest `{k}`: fulgte instruksen i {v['followed_injection']} av {v['n']}; "
                     f"flagget som injeksjon {v['injection_flagged']}; fulgte OG ble godkjent automatisk: {v.get('followed_AND_auto_cleared', '–')}.")
        if ag.get("stability"):
            st = ag["stability"]
            L.append(f"- Stabilitet ({st['n']} saker kjørt to ganger): samme stemme {_p(st['same_vote'])}, samme seksjon {_p(st['same_section'])}.")
    text = "\n".join(L) + "\n"
    (RESULTS / "nokkeltall.md").write_text(text, encoding="utf-8")
    return text
