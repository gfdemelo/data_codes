#!/usr/bin/env python3

import copy

class Time:
	"""Representa o tempo do dia.
	Atributos: hora, minuto, segundo"""

def print_time(t):
	print('(%.2d : %.2d : %.2d)' % (t.hora, t.minuto, t.segundo))	
	
def is_after(t1, t2):
	return (t2.hora, t2.minuto, t2.segundo) > (t1.hora, t1.minuto, t1.segundo)

def add_time(t1, t2):
#	if not valid_time(t1) or not valid_time(t2):
#		raise ValueError('tempo inválido')
	assert valid_time(t1) and valid_time(t2)
	return int_to_time(time_to_int(t1)+time_to_int(t2))

def time_to_int(t):
	minutos = t.hora *60 + t.minuto
	segundos = minutos *60 + t.segundo
	return segundos

def int_to_time(s):
	time=Time()
	minuto, time.segundo = divmod(s, 60)
	time.hora, time.minuto = divmod(minuto, 60)
	return time

def increment_modificadora(tempo, segundos):
	""" modifica os argumentos"""

	tempo.segundo += segundos

	if tempo.segundo >= 60:
		tempo.segundo -= 60
		tempo.minuto += 1
		increment_modificadora(tempo, 0)	
	
	if tempo.minuto >= 60:
		tempo.minuto -= 60
		tempo.hora += 1
	return tempo	

def increment_pura(t, segundos):
	""" função increment pura sem considerar a base 60 de time_to_int e int_to_time"""

	tiempo=Time()
	tiempo.hora = t.hora
	tiempo.segundo = t.segundo
	tiempo.minuto = t.minuto
	tiempo.segundo += segundos
	if tiempo.segundo >= 60:
		tiempo.segundo -= 60
		tiempo.minuto += 1
		return increment_pura(tiempo, 0)	
	if tiempo.minuto >= 60:
		tiempo.minuto -= 60
		tiempo.hora += 1
		return tiempo	

def increment(t, segundos):
	return(int_to_time(time_to_int(t)+segundos))	

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
time2=Time()
time2.hora=-1
time2.minuto=1
time2.segundo=30
print_time(add_time(time, time2))
