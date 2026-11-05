"""#2572 bytte steg 2: legg modell_repo4.py og stemmeagent/ inn i c1_frys.py FILER og fremmed.sh sin kopier-liste.
pakk_jury.sh og frys_fasit.py leser FILER selv, så de følger med. Kjøres fra landsbymappen. Idempotent."""
import glob
F = "arbeid/verktoy/c1_frys.py"; s = open(F).read()
nye = ["arbeid/hack/levering/modell_repo4.py"] + sorted(glob.glob("arbeid/hack/levering/stemmeagent/*.py"))
anker = '    "arbeid/hack/levering/c1_real.py",'
assert anker in s
if nye[0] not in s:
    s = s.replace(anker, anker + "\n" + "\n".join(f'    "{f}",  # #2572 bytte til repo4' for f in nye)); open(F, "w").write(s)
F = "arbeid/hack/levering/fremmed.sh"; s = open(F).read()
a = "kopier arbeid/hack/levering/kjor_agent.py \\\n"
assert a in s
if "modell_repo4.py" not in s:
    s = s.replace(a, a + "  arbeid/hack/levering/modell_repo4.py arbeid/hack/levering/stemmeagent \\\n"); open(F, "w").write(s)
print("FILER og fremmed.sh oppdatert:", nye)
