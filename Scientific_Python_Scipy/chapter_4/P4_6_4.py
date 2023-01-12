#!/usr/bin/env python

import string, pylab
s=string.whitespace


class Experiment:
	"""Interpreta dados de conc. e tempo de uma reação para obtenção da contante de arrehnius"""

	def __init__(self, t=[], c=[]):

		self.t = t
		self.c = c
		self.x2, self.y2, self.sqrt, self.product =[], [], [], []

	def lista_dados(self,filename):
		for line in open(filename, 'r'):
			if not line.startswith('#'):
				b=line.strip().split(s)
				for item in b:
					b=item.split()
					self.t.append(float(b[0]))
					self.c.append(float(b[1]))
		
	def transformation_data(self):#, x, y):
		for i in range(len(self.t)):
			self.x2.append(self.t[i])
			self.y2.append(1/self.c[i])
		
	def linear_regression(self): #x, y):
		for i in range(len(self.t)):
			self.sqrt.append(self.x2[i]**2)
			self.product.append(self.x2[i]*self.y2[i])
		m = (pylab.mean(self.product) - pylab.mean(self.x2)*pylab.mean(self.y2)) / (pylab.mean(self.sqrt) - (pylab.mean(self.x2)**2))
		c = pylab.mean(self.y2) - m*pylab.mean(self.x2)
		return m,c	

arquivos = ['caa-40.txt','caa-50.txt','caa-60.txt','caa-70.txt','caa-80.txt']
k=[]
T=[313.15,323.15,333.15,343.15,353.15]

if __name__=='__main__':
	for item in arquivos:
		dados =Experiment(t=[], c=[]) 
		a = dados.lista_dados(item)
		b = dados.transformation_data()
		c = dados.linear_regression()
		k.append(pylab.log(abs(c[0])))
	#regressao de m para obter energia de ativacao
	reg = Experiment(t=k , c=T) 
	d = dados.transformation_data()
	e = dados.linear_regression()  	
	print('A energia de ativação é : %.14f mol/J ' % (e[0]*8.314))
