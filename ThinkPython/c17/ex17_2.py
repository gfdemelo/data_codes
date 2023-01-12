#!/usr/bin/env python3



class Kangoroo:
	""" classe"""
	
	def __init__(self):
		"""Inicializa um objeto Kangoroo
		Atributos: pouch_contents"""

		self.pouch_contents=[]

	def put_in_pouch(self, other):
		return self.pouch_contents.append(other)

	def __str__(self):
		for i in range(len(self.pouch_contents)-1):
			print (repr(self.pouch_contents[i]))


kanga=Kangoroo()
kanga.put_in_pouch('kanga')
kanga.put_in_pouch('roo')
roo=Kangoroo()
kanga.put_in_pouch(roo)
print(kanga)		
		
