#!/usr/bin/env python


balance=100

def add_interest(rate):
	global balance
	balance += balance * rate/100

for year in range(4):
	add_interest(5)
	print('Balance after year {}: ${:.2f}'.format(year+1, balance))
