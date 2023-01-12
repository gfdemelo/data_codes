#!/usr/bin/env python3

import datetime

class Cliente:
	""" Uma classe que representa um cliente de banco"""
	
	def __init__(self, nome, endereço, nascimento):
		self.nome = nome
		self.endereço = endereço
		self.nascimento = datetime.strptime(nascimento, '%Y-%m-%d')
		self.senha = '1234'

	def idade(self):
		"""Calcula a idade do cliente"""
	
		today = datetime.today()
		try:
			aniversario = self.nascimento.replace(year=today.year)
		except ValueError:
			aniversario = self.nascimento.replace(year=today.year, day=self.nascimento.day-1) #caso a data seja 29 Fev
	
		if aniversario > today:
			return today.year - self.nascimento.year - 1
		return today.year - self.nascimento.year
