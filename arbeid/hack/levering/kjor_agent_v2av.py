"""#2896: kjor_agent.py med v2av-modellen (MODELL=v2av): c1_real_v2av.py i stedet for c1_real.py, ellers uendret.
Valgt av KJOR.sh når arbeid/hack/levering/MODELL inneholder v2av. Standard (frossen) er kjor_agent.py."""
import os, sys
HER = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HER)
import c1_real_v2av; sys.modules["c1_real"] = c1_real_v2av
import kjor_agent
if __name__ == "__main__":
    kjor_agent.main()
