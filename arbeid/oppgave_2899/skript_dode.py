"""Case 1 (#2899): døde skript-henvisninger (.py/.sh) og REGEL.md i repo-dokumentene.
Leser alle .md i repoen utenom state/rapporter/ og arkiv/ (gamle tekster). `<arbeidsmappe>/x` = `arbeid/x`.
Bruk: python3 -I skript_dode.py [repo] [--inn]
  uten --inn: fil:linje<TAB>henvisning<TAB>fil i landsbyen (eller -) per død henvisning; siste linje = antall
  --inn:      bare landsby-stiene som løser henvisningene (til arbeid/verktoy/c1_henviste_filer.txt)"""
import os, re, sys
arg = [a for a in sys.argv[1:] if not a.startswith("--")]
REPO = arg[0] if arg else "."  # repo-roten; i landsbyen: gi stien til den lokale GitHub-repoen
L = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
filer = set()
for d, m, f in os.walk(REPO):
    m[:] = [x for x in m if x not in (".git", ".venv", "__pycache__")]
    for x in f: filer.add(os.path.relpath(os.path.join(d, x), REPO))
navn = {os.path.basename(f) for f in filer}
PFX = ["", "arbeid/", "arbeid/hack/", "arbeid/hack/c1/", "arbeid/hack/levering/", "arbeid/hack/c1/leveranse/", "arbeid/verktoy/"]
RX = re.compile(r"(?<![\w.-])((?:[\w.{},-]+/)*[\w.-]+(?:\.py|\.sh|REGEL\.md))(?![\w])")

def utvid(t):  # arbeid/oppgave_{a,b}/REGEL.md -> to stier
    m = re.search(r"\{([^}]*)\}", t)
    return [x for v in m.group(1).split(",") for x in utvid(t[:m.start()] + v + t[m.end():])] if m else [t]

def i_repo(t, base):
    return (any(os.path.normpath(os.path.join(p, t)) in filer for p in [base] + PFX)
            or ("/" not in t and t in navn))

def i_landsby(t, linje):
    ls = [os.path.normpath(os.path.join(p, t)) for p in PFX if os.path.isfile(os.path.join(L, p, t))]
    if not ls and "/" not in t:  # bart filnavn: let i oppgave-mappene som nevnes på samme linje
        ls = [f"arbeid/oppgave_{o}/{t}" for o in re.findall(r"oppgave_(\d{4})", linje)
              if os.path.isfile(os.path.join(L, f"arbeid/oppgave_{o}/{t}"))]
    return ls[:1]

dode, inn = [], set()
for rel in sorted(filer):
    if not rel.endswith(".md") or rel.startswith("state/rapporter/") or "/arkiv/" in rel: continue
    for nr, linje in enumerate(open(os.path.join(REPO, rel), encoding="utf-8", errors="replace").read().splitlines(), 1):
        linje = linje.replace("<arbeidsmappe>/", "arbeid/").replace("$R/", "").replace("$D/", "")
        for mt in RX.finditer(linje):
            tok = mt.group(1)
            if tok.startswith(("_", ".", "tmp/")) or tok == "py" or "astral.sh" in tok: continue  # nett-adresser og /tmp-kopier
            for t in utvid(tok):
                if i_repo(t, os.path.dirname(rel)): continue
                deler = t.split("/")  # «a.sh/b.py» = to filnavn
                if len(deler) == 2 and all(re.search(r"\.(py|sh)$", d) for d in deler) and all(i_repo(d, "") for d in deler): continue
                ls = i_landsby(t, linje)
                inn.update(ls)
                dode.append(f"{rel}:{nr}\t{t}\t{ls[0] if ls else '-'}")
if "--inn" in sys.argv:
    print("\n".join(sorted(inn)))
else:
    print("\n".join(dode)); print(f"# {len(dode)} døde henvisninger")
