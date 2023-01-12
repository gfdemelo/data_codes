#!/usr/bin/env python

class BankAccount:
	""" Uma classe que representa uma conta de banco"""

	corrente = '$'

	def __init__(self, cliente, numero_conta, saldo=0):
		""" Inicia a classe BankAccount com um cliente, número de conta e saldo da conta"""

		self.cliente = cliente
		self.numero_conta = numero_conta
		self.saldo = saldo
		assert self.Luhn_algorithm(numero_conta), 'O número da conta é inválido'
			

	def deposito(self, quantidade):
		"""Quantidade depositada na conta"""

		if quantidade > 0:
			self.saldo += quantidade
		else:
			print('Quantidade de depósito inválida: ', quantidade)

	def saque (self, quantidade):
		""" Quantidade a ser sacada, considerando que há fundos suficientes"""

		if quantidade > 0:
			if quantidade > self.saldo:
				print('Saldo insuficiente')
			else:
				self.saldo -= quantidade
		else:
			print('Quantidade inválida para saque: ', quantidade)

	def check_saldo(self):
		"""Imprime o saldo da conta"""

		print('O saldo da conta %d é %s%.2f' % (self.numero_conta, self.corrente, self.saldo))


	def Luhn_algorithm(self, numero_conta):
		""" Verifica se o número da conta é válido"""

		a=list(str(numero_conta))
		b=a[::-1]
		for i in range(1, len(b)):
			if i%2:
				b[i] = str(int(b[i])*2)
				if int(b[i]) > 9:
					c=list(b[i])
					b[i] = str(int(c[0]) + int(c[1]))
		for i in range(len(b)):
			b[i] = int(b[i])				
		
		if not sum(b) % 10:
			return True
		return False 

class SavingsAccount(BankAccount):
	""" Uma classe qu representa a poupança do cliente"""
	
	def __init__(self, cliente, numero_conta, taxa_juros, saldo=0):
		""" Inicia a poupança"""

		self.taxa_juros = taxa_juros
		super().__init__(cliente, numero_conta, saldo) #super chama o __init__ da classe base
		
	def add_juros(self):
		""" Adiciona o juros a conta a uma taxa taxa_juros"""

		self.saldo *= (1. + self.taxa_juros / 100)


class CurrentAccount(BankAccount):
	"""Representa a conta corrente"""

	def __init__(self, cliente, numero_conta, taxa_anual, limite_transf, saldo=0):
		"""Inicia a conta corrente"""

		self.taxa_anual = taxa_anual
		self.limite_transf = limite_transf
		super().__init__(cliente, numero_conta, saldo)

	def saque(self, quantidade):
		""" Quantidade a ser sacada se fundos existem e são suficientes e a quantidade é menor que o limite de transferencia"""
	
		if quantidade <= 0:
			print('Quantidade para saque invalida: ', quantidade)
			return

		if quantidade > self.saldo:
			print('Fundos insuficientes')
			return

		if quantidade > self.limite_transf:
			print('%s%.3f excede o limite de transferencia de %s%.3f' % (self.corrente, quantidade, self.corrente,self.limite_transf))
			return
	
		self.saldo -= quantidade
	
	def aplicar_taxa_anual(self):
		"""Descontar a taxa anual da conta corrente"""

		self.saldo = max(0., self.saldo - self.taxa_anual)
















