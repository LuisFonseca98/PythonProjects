from sae import Controlo, Simulador


class ControloTeste(Controlo):
    def processar(self, percepcao):
        print("processar")


controlo = ControloTeste()
Simulador(1, controlo).executar()
