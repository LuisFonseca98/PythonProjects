


from pee.control_delib.controlo_delib import ControloDelib
from plan.plan_pee.plan_pee import PlanPEE
from sae import Simulador

"""
TERMINAR = 't'
INICIAR = 'i'
PAUSA = 'p'
EXECUTAR = 'e'
VELOCIDADE = 'v'
"""
planeador = PlanPEE()
controlo = ControloDelib(planeador)

Simulador(1,controlo).executar()