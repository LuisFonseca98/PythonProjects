from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.recolher import Recolher
from sae import Simulador


#explorar = Explorar()
#controlo = ControloReact(explorar)

recolher = Recolher()#inicializo o comportamento
controlo = ControloReact(recolher)#o controlo reativo necessita de conhecer o recolher
Simulador(2, controlo).executar()#e feita uma simulacao com este comportamento
