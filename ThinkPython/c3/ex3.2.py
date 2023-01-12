#!/usr/bin/env python3


def do_twice(f, v):
	f(v)
	f(v)

def print_spam(v):
	print('spam')

def print_twice(bruce):
	print(bruce)
	print(bruce)

def do_four(print_twice, v):
	print_twice(v)
	print_twice(v)




do_twice(print_spam, 'spam')
print(' ')
do_four(print_twice, 'spam')
