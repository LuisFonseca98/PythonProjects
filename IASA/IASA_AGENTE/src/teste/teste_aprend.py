

from controlo_aprend.controlo_aprend_ref import ControloAprendRef
from sae import Simulador


controlo = ControloAprendRef()
Simulador(2,controlo,reiniciar=True).executar()

#n -> episodio
#Quando o agente chega ao alvo, ele chegou a convergencia, ou seja, definiu o melhor/otimo trajeto
# Q pode ser o valor de um conjunto de recompensas
#epsilon e o que permite o agente puder explorar ou executar a accao