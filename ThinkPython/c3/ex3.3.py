#!/usr/bin/env python3




def do_four(f):
	f()
	f()
	f()
	f()

def print1():
	print('+ - - - - + - - - - + - - - - +', end=' ');print()

def print2():
	print('|         |         |         |', end=' '); print()

def print_grid():
	print1()
	do_four(print2)
	print1()
	do_four(print2)
	print1()
	do_four(print2)
	print1()
	do_four(print2)
	print1()	

print_grid()





