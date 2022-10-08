"""
Vista de ambiente
@author: Luís Morgado
"""

import math

from ..erro import Erro, ErroParam
from ..ambiente.ambiente import Elemento
from .visualizador import AMARELO, Visualizador

#_____________________________________________________________

class VistaAmb(Visualizador):
	def __mostrar_elemento(self, posicao, elemento):
		"""
		Mostrar elemento numa posição excepto agente
		@param posicao: posição do elemento
		@param elemento: elemento a mostrar
		"""
		if elemento == Elemento.ALVO:
			self.alvo(posicao)
		elif elemento == Elemento.OBSTACULO:
			self.obstaculo(posicao)
		elif elemento == Elemento.VAZIO:
			self.vazio(posicao)  
 			
	def __mostrar_valor_posicao(self, pos, val, vmin, vmax):
		"""
		Mostrar posição com cor correspondente ao valor
		@param pos: posição
		@param val: valor
		@param vmin: valor mínimo
		@param vmax: valor máximo
		"""
		# Definir cor (R,G,B) com normalização de valor
		if   val > 0: cor = (0, (val / vmax) * 255, 0)
		elif val < 0: cor = ((val / vmin) * 255, 0, 0)
		else:		  cor = (0, 0, 0)
		# Mostrar posição com cor respectiva
		self.rect(pos, 0, cor, 0)
				
	def mostrar_elementos(self, elementos):
		"""
		Visualizar elementos do ambiente
		@param elementos: dicionário com elementos a mostrar {pos: elem}
		"""
		param = locals()
		try:
			for posicao, elemento in elementos.items():
				self.__mostrar_elemento(posicao, elemento) 
		except:
			raise ErroParam(Erro.PARAM_INV, param) from None
 				
	def mostrar_alvos_obst(self, elementos):
		"""
		Visualizar alvos e obstáculos
		@param elementos: dicionário com elementos a mostrar {pos: elem}
		"""
		param = locals()
		try:
			for posicao, elemento in elementos.items():
				if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
					self.__mostrar_elemento(posicao, elemento) 
		except:
			raise ErroParam(Erro.PARAM_INV, param) from None

	def mostrar_per_dir(self, per_dir):
		"""
		Mostrar percepção direccional
		@param per_dir: percepção direccional
		"""
		param = locals()
		try:
			for elem, _, pos in per_dir.values():
				self.__mostrar_elemento(pos, elem)
		except:
			raise ErroParam(Erro.PARAM_INV, param) from None
			
	def mostrar_valor(self, funcao_valor, escala=None):
		"""
		Visualizar função valor
		@param funcao_valor: dicionário com associações posição:valor
		@param escala: (mínimo, máximo)
		"""
		param = locals()
		try:
			if funcao_valor:
				if escala:
					vmin, vmax = escala
				else:
					vmax = max(funcao_valor.values())
					vmin = min(funcao_valor.values())
				# Mostrar valores em código de cores
				for estado, valor in funcao_valor.items():
					self.__mostrar_valor_posicao(estado.posicao, valor, vmin, vmax)
		except:
			raise ErroParam(Erro.PARAM_INV, param) from None
				
	def mostrar_politica(self, politica):
		"""
		Visualizar política
		@param politica: dicionário com associações posição:operador
					operador deve ter propriedade ang
		"""
		param = locals()
		try:
			for estado, accao in politica.items():
				self.vector(estado.posicao, 1, accao.ang)			   
		except:
			raise ErroParam(Erro.PARAM_INV, param) from None

	def mostrar_plano(self, estado_inicial, plano):
		"""
		Visualizar plano
		@param estado_inicial: estado inicial
		@param plano: sequência de operadores com propriedade ang
		"""
		param = locals()
		try:
			if plano:
				avanco = 1
				x, y = estado_inicial.posicao
				for oper in plano:
					ang = oper.ang
					self.vector((x, y), avanco, ang)
					dx = avanco * math.cos(ang)
					dy = -avanco * math.sin(ang)
					x += round(dx)
					y += round(dy)
		except:
			raise ErroParam(Erro.PARAM_INV, param) from None

	def mostrar_solucao(self, solucao):
		"""
		Visualizar solução de PEE
		@param solucao: sequência de nós com operadores com propriedade ang
		"""
		param = locals()
		try:
			if solucao:
				plano = [no.operador for no in solucao[1:]]
				self.mostrar_plano(solucao[0].estado, plano)
		except:
			raise ErroParam(Erro.PARAM_INV, param) from None

	def marcar_posicao(self, posicao, margem=2, cor=AMARELO, linha=1):
		"""
		Marcar posição
		@param pos: posição a marcar
		@param margem: margem em pixeis
		@param cor: cor RGB
		@param linha: espessura de linha (0 - preencher)
		"""
		param = locals()
		try:
			self.marcar([posicao], margem, cor, linha)
		except:
			raise ErroParam(Erro.PARAM_INV, param) from None

	def mostrar_estados(self, estados, margem=2, cor=AMARELO, linha=1):
		"""
		Mostrar conjunto de estados
		@param estados: conjunto de estados
		@param margem: margem em pixeis
		@param cor: cor RGB
		@param linha: espessura de linha (0 - preencher)
		"""
		param = locals()
		try:
			posicoes = {estado.posicao for estado in estados}
			self.marcar(posicoes, margem, cor, linha)
		except:
			raise ErroParam(Erro.PARAM_INV, param) from None


		
