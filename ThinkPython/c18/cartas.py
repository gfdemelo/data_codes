#!/usr/bin/env python3

import random

class Cartas:
	"""Representa cartas de um baralho padrão
	Atributos: 
		naipe: inteiro 0-3
		valor: inteiro 1-13 """

	#Atributos de Classe (não estão associados a nenhum método)
	nomes_naipe = ['Copas', 'Ouros', 'Paus', 'Espadas']
	nomes_valor = [None, 'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
	
	
	def __init__(self, naipe=0, valor=2):
		self.naipe = naipe		#Atributos de instância
		self.valor = valor

	def __str__(self):
		return '%s de %s' % (Cartas.nomes_valor[self.valor], Cartas.nomes_naipe[self.naipe])

	def __lt__(self, other):
		t1 = self.naipe, self.valor
		t2 = other.naipe, other.valor
		return t1 < t2


class Baralho:
	"""Representa um baralho"""

	def __init__(self):
		self.cards = []
		for naipe in range(4):
			for valor in range(1,14):
				card = Cartas(naipe, valor)
				self.cards.append(card)
	
	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return repr(res)#'\n'.join(res)

	def add_card(self, carta):
		self.cards.append(carta)
	
	def pop_card(self, i=-1):
		return self.cards.pop(i)

	
	def shuffle(self):
		#print('Rodando baralho.shuffle')
		random.shuffle(self.cards)


	def sort(self):
		self.cards.sort()

	
	def move_cards(self, mao, num):
		for i in range(num):
			a=random.randint(0, len(self.cards)-1)
			mao.add_card(self.pop_card(a))
		return mao

	def deal_hands(self, num_mao, num_cartas):
		lista=[]
		for i in range(num_mao):
			mao=Mao(self)
			a=self.move_cards(mao, num_cartas)
			lista.append(str(a))
		return lista


class Mao(Baralho):
	""" Representa uma mão de cartas de um baralho"""
	
	def __init__(self, label=''):
		self.cards = []
		self.label = label




c=Baralho() 
hand=Mao(c)
print(c.deal_hands(5, 5))

