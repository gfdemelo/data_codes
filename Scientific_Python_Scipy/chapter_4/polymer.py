#!/usr/bin/env python


import math, random

class Polymer:
	""" Representa um random-flight polímero em solução, em que este é tratado como uma sequência com segmentos orientados
	aleatoriamente; não há correlação entre a orientação de um segmento e outro."""

	def __init__(self, N, a):
		"""Inicia o polímero com N segmentos, cada um de comprimento a"""

		self.N, self.a = N, a
		self.xyz = [(None, None, None)]*N       # Guarda os vetores de posição do segmento em tuplas
		self.R = None                           # Vetor End-to-end
		self.make_polymer()                     # Constrói o polímero atribuindo posições dos segmentos

	def make_polymer(self):
		""" Calcula as posições do segmento, centro de massa e distância end-to-end para um random-flight polímero"""

		self.xyz[0] = x, y, z = cx, cy, cz = 0., 0., 0.		# Inicia o polímero na origem (0,0,0)
		for i in range (1, self.N):
			"""
			Uma forma de obter a localização do próximo segmento é pegar um ponto aleatório na superfície da esfera
			e usar o correspondente par de ângulos no sistema de coordenadas esféricas polares, theta e phi (em que 0 < theta < pi e 
			0 < phi < 2pi) para ajustar a distância em relação ao segmento anterior como:
			deltaX = a*sin(theta)*cos(phi)
			deltaY = a*sin(theta)*sin(phi)
			deltaZ = a*cos(theta)
			"""
                        # Pega uma orientação aleatoria para o próximo segmento
			theta = math.acos(2*random.random() -1)
			phi = random.random() * 2. * math.pi
                        # Adiciona o vetor de deslocamento para esse segmento
			x += self.a * math.sin(theta) * math.cos(phi)
			y += self.a * math.sin(theta) * math.sin(phi)
			z += self.a * math.cos(theta)
                        # Armazena o vetor e atualiza ou soma ao centro de massa
			self.xyz[i] = x, y, z
			cx, cy, cz = cx + x, cy +y, cz + z
                        # Cálculo da posição do centro de massa
			"""
			Nós calculamos a posição do centro de massa do polímero, e então deslocamos as coordenadas originais dos
			segmentos do polímero, de forma que eles sejam mensurados relativos a esse ponto (as coord. do segmeto terão origem
			no centro de massa)
			"""
			
		cx, cy, cz = cx / self.N, cy / self.N, cz / self.N
		# O vetor end-to-end é a posição do último segmento, uma vez que iniciamos na origem
		self.R = x, y, z
			
		# Recentraliza o polímero em seu centro de massa
		for i in range(self.N):
			self.xyz[i] = self.xyz[i][0] - cx, self.xyz[i][1] - cy, self.xyz[i][2] - cz
	def calc_Rg(self):
		""" Calcula e retorna o raio de rotação do polímero, Rg."""
	
		self.Rg = 0	
		for x, y, z in self.xyz:
			self.Rg += x**2 + y**2 + z**2
		self.Rg = math.sqrt (self.Rg / self.N)
		return self.Rg
 

if __name__=='__main__':
	polymer = Polymer(1000, 0.5)	# Polímero com 1000 segmentos e comprimento 0.5
	print(polymer.R)		# vetor end-to-end
	print(polymer.calc_Rg())

