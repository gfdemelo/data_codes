#!/usr/bin/env python3


prefixes='JKLMNOPQ'
suffix='ack'

for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		print(letter+'u'+suffix)
	else:
		print(letter+suffix)


