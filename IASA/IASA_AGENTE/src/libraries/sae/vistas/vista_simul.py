"""
Vista de Simulação
@author: Luís Morgado
"""

import os
import pygame
from .visualizador import BRANCO, PRETO
from .vista_amb import VistaAmb

#_____________________________________________________________

# Separação das áreas de visualização
SEP_X = 1
SEP_Y = 1

# Posição inicial da janela
POS_JAN_X = 10
POS_JAN_Y = 40

# Número de visualizadores e de separadores
NUM_VIS = 2
NUM_SEP_X = NUM_VIS + 1
NUM_SEP_Y = 2

#_____________________________________________________________

class VistaSimul:
	def __init__(self, modelo, escala):
		"""
		Iniciar vista
		@param escala: dimensão dos elementos do ambiente
		@param fps: taxa de actualização do ecrã
		"""
		self._modelo = modelo
		# Dimensões de visualização
		dim_vis_x = modelo.ambiente.dim_x * escala
		dim_vis_y = modelo.ambiente.dim_y * escala
		dim_jan_x = NUM_VIS * dim_vis_x + NUM_SEP_X * SEP_X
		dim_jan_y = dim_vis_y + NUM_SEP_Y * SEP_Y
		# Rectângulos das áreas de visualização
		self._rect_amb = (SEP_X, SEP_Y, dim_vis_x, dim_vis_y)
		self._rect_mod = (dim_vis_x + NUM_VIS * SEP_X, SEP_Y, dim_vis_x, dim_vis_y)
		# Iniciar janela e visualizadores
		self._iniciar_janela(POS_JAN_X, POS_JAN_Y, dim_jan_x, dim_jan_y)
		self._vista_amb = VistaAmb(dim_vis_x, dim_vis_y, escala, BRANCO)
		self._vista_mod = VistaAmb(dim_vis_x, dim_vis_y, escala, PRETO)

	@property
	def vista_mod(self):
		return self._vista_mod

	def _iniciar_janela(self, x, y, dim_x, dim_y):
		""""
		Iniciar janela de simulação
		"""
		os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
		pygame.display.set_caption("Simulador de ambiente")
		self.svis = pygame.display.set_mode((dim_x, dim_y))	
		self.svis.fill(PRETO)
		
	def actualizar(self):
		"""
		Actualizar visualização
		"""
		self._vista_amb.limpar()
		# Mostrar ambiente
		ambiente = self._modelo.ambiente
		self._vista_amb.mostrar_elementos(ambiente.elementos)
		self._vista_amb.agente(ambiente.posicao_agente,
							   ambiente.direccao_agente.value,
							   ambiente.colisao,
							   ambiente.recolha)
		# Mostrar percepção direccional
		if self._modelo.agente.controlo.mostrar_per_dir:
			self._vista_mod.limpar()
			self._vista_mod.mostrar_per_dir(ambiente.per_dir)
			self._vista_mod.marcar([ambiente.posicao_agente], linha=1)
		# Actualizar vistas
		self._vista_amb.actualizar(self.svis, self._rect_amb)
		self._vista_mod.actualizar(self.svis, self._rect_mod)


		
