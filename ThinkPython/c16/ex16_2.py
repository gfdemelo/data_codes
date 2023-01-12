#!/usr/bin/env python3

import copy, datetime

class Time:
	"""Representa o tempo do dia.
	Atributos: hora, minuto, segundo"""

def print_time(t):
	print('(%.2d : %.2d : %.2d)' % (t.hora, t.minuto, t.segundo))	
	
def is_after(t1, t2):
	return (t2.hora, t2.minuto, t2.segundo) > (t1.hora, t1.minuto, t1.segundo)

def add_time(t1, t2):
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

def mul_time(t, n):
	""" multiplica objeto Time t por um número n"""
	novo=Time()
	a=time_to_int(t)
	novo=int_to_time(a*n)
	return novo
	
def increment(t, segundos):
	return(int_to_time(time_to_int(t)+segundos))	

def valid_time(t):
	if t.hora < 0 or t.minuto < 0 or t.segundo < 0:
		return False
	if t.minuto >=60 or t.segundo > 60:
		return False
	return True

#Dia da semana
def dia_da_semana():
	d=dict()
	d['Sunday']='Domingo'
	d['Monday']='Segunda-feira'
	d['Tuesday']='Terça-feira'
	d['Wednesday']='Quarta-feira'
	d['Thursday']='Quinta-feira'
	d['Friday']='Sexta-feira'
	d['Saturday']='Sábado'
	hoje=datetime.date.today()
	dia=hoje.strftime('%A')
	print(d[dia])


#aniver=input('Digite o dia do seu aniversário no formato Mês-Dia-Ano: ')

def tempo_aniver():
	a='01-09-1993'
	r=datetime.datetime.strptime(a, '%m-%d-%Y')
	hoje=datetime.datetime.today()
	b=r.replace(year=hoje.year)
	if b < hoje:
		idade=abs(r.year-hoje.year)
		print('Você têm ', idade, 'anos')		
		c=b.replace(year=hoje.year+1)
		delta=c-hoje
		print('O tempo até o próximo aniversário é: ', delta)	
	else:
		idade=abs(r.year-hoje.year)-1
		print('Você têm ', idade, 'anos')		
		delta=b-hoje
		print('O tempo até o próximo aniversário é: ', delta)	
tempo_aniver()	



time=Time()
#time.hora=9
#time.minuto=59
#time.segundo=30
#time2=Time()
#time2.hora=2
#time2.minuto=2
#time2.segundo=24




