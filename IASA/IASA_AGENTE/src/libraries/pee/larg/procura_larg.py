

"""
Classe que representa a procura em largura
Este tipo de procura, usa a estrategia de controlo,
que permite explorar primeiro os nos mais antigos
"""



from pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO
from pee.mec_proc.procura_grafo import ProcuraGrafo


class ProcuraLarg(ProcuraGrafo):

    def _iniciar_fronteira(self):
        return FronteiraFIFO()