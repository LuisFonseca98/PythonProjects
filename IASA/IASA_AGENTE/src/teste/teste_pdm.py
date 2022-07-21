

from pee.control_delib.controlo_delib import ControloDelib
from plan.plan_pdm.plan_pdm import PlanPDM
from sae import Simulador


planPDM = PlanPDM()
controlo = ControloDelib(planPDM)

Simulador(3,controlo).executar()