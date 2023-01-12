#!/usr/bin/env python



def dot_product(v1,v2):
	"""Calcula o produto escalar, a.b= soma(a_i,b_i)"""

	v1_v2=0
	for i in range(len(v1)):
		v1_v2 += v1[i]*v2[i]
	return v1_v2
	
def cross_product(v1,v2):
	"""Calcula o produto vetorial, a x b = [a_2b_3 - a_3b_2, a_3b_1 - a_1b_3, a_1b_2 - a_2b_1]"""

	v1_v2=[v1[1]*v2[2]-v1[2]*v2[1],v1[2]*v2[0]-v1[0]*v2[2],v1[0]*v2[1]-v1[1]*v2[0]]
	return v1_v2
	
def scalar_triple(v1,v2,v3):
	""" Calcula a.(bxc)"""

	return dot_product(v1,cross_product(v2,v3))

def vector_triple(v1,v2,v3):
	""" Calcula a x (b x c)"""

	return cross_product(v1,cross_product(v2,v3))		



a=[1,2,3]
b=[3,4,5]
c=[7,8,9]
print(dot_product(a,b))
print(cross_product(a,b))
print(scalar_triple(a,b,c))
print(vector_triple(a,b,c))
