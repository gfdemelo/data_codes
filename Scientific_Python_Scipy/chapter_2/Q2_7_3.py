#!/usr/bin/env python


def digit_sum(n):
	s_digits = list(str(n))
	dsum=0
	for s_digit in s_digits:
		dsum += int(s_digit)
	return dsum

def is_harshad(n):
	return not n % digit_sum(n)

print(is_harshad(42))
