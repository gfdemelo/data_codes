#!/usr/bin/env python3

import copy


class Time:
	"""Representa o tempo do dia.
	Atributos: hora, minuto, segundo"""

	def __init__(self, hora=0, minuto=0, segundo=0):
		self.hora = hora
		self.minuto = minuto
		self.segundo = segundo

	def __str__(self):
        	return '(%.2d : %.2d : %.2d)' % (self.hora, self.minuto, self.segundo)
	
	def time_to_int(self):
        	minutos = self.hora *60 + self.minuto
        	segundos = minutos *60 + self.segundo
        	return segundos

	def increment(self, segundos):
        	return(int_to_time(self.time_to_int()+segundos))	

	def is_after(self, other):
		#return (t2.hora, t2.minuto, t2.segundo) > (t1.hora, t1.minuto, t1.segundo)
		return self.time_to_int() > other.time_to_int()

	def add_time(self, other):
		return int_to_time(self.time_to_int() + other.time_to_int())
	
	def __add__(self, other):
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(other)

	def __radd__(self, other):
		""" É invocado quando o objeto Time aparece do lado direito do operador +"""
		return self.__add__(other)
	
	def __lt__(self, other):
		return (self.hora, self.minuto, self.segundo) < (other.hora, other.minuto, other.segundo)

def int_to_time(s):
	time=Time()
	minuto, time.segundo = divmod(s, 60)
	time.hora, time.minuto = divmod(minuto, 60)
	return time

def print_attributes(s):
	for attr in vars(s):
		print(attr, getattr(s, attr))


def valid_time(t):
	if t.hora < 0 or t.minuto < 0 or t.segundo < 0:
		return False
	if t.minuto >=60 or t.segundo > 60:
		return False
	return True


time=Time()
time.hora=9
time.minuto=59
time.segundo=30
time2= Time(1, 30)
time3 = Time(1,30)
print(time.__lt__(time2))
#print(sum([time, 133, time3]))
#print_attributes(time)
