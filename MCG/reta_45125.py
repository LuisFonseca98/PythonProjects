# -*- coding: utf-8 -*-
"""
Created on Tue May 08 18:34:24 2018

@author: Luis Carlos
"""
from ponto_45125 import *

"""A classe Reta representa uma reta. A classe ErroPontosCoincidentes
é uma exceção (deriva de Exception) que é lançada quando se tenta definir
uma reta com dois pontos coincidentes."""
class ErroPontosCoincidentes(Exception):
    """exception"""
class Reta:
    """Inicializa os atributos origem e destino com os argumentos respetivos.
    Inicializa o atributo vetor_diretor com o vetor que aponta de origem para
    destino e tem comprimento 1"""
    def __init__(self,origem,destino):
        self.origem = origem
        self.destino = destino
        vetor_diretor= Ponto3D.subtrai_ponto(destino,origem)
        if(vetor_diretor.comprimento() <= (10.0)**(-10)):
            raise ErroPontosCoincidentes
        else:
             self.vetor_direcao = vetor_diretor.versor()
    """Retorna uma string constituída por Reta(o, d, v), onde o é a conversão
    para string do atributo origem, d do atributo destino e v do atributo
    vetor_diretor."""
    def __repr__(self):
        return "Reta(" + str(self.origem) + str(self.destino) +str(self.vetor_direcao) +  ") )"
    """Retorna o destino da reta"""
    def get_destino(self):
        return self.destino

    """Retorna o destino da reta"""
    def get_origem(self):
        return self.origem

    """Retorna o vetor diretor da reta"""
    def get_vetor_diretor(self):
        return self.vetor_direcao
if __name__ == '__main__':
    # teste ao construtor
    p1 = Ponto3D(0.0, 0.0, 0.0)
    p2 = Ponto3D(1.0, 2.0, 3.0)
    r1 = Reta(p1, p2)
    print("Até aqui não foram lançadas exceções.")

    # teste à exceção ErroPontosCoincidentes
    try:
        r2 = Reta(p2, p2)
    except ErroPontosCoincidentes:
        print("Ao tentar definir-se a reta r2 = Reta(p2, p2)")
        print("foi lançada a exceção ErroPontosCoincidentes.")
        print("A execução foi interrompida. r2 não ficou definida.")

    # teste a __repr__
    print(r1)

    # teste a get_origem
    print(r1.get_origem())

    # teste a get_destino
    print(r1.get_destino())

    # teste a get_vetor_diretor
    print(r1.get_vetor_diretor())
