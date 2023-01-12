#!/usr/bin/env python

iban_lengths={line.split()[0]:int(line.split()[1]) for line in open('iban.txt').readlines()}

print(iban_lengths)
