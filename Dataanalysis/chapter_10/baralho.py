#!/usr/bin/env python

#Copas (hearts), Espada (Spades), Paus (Clubs), Ouro (Diamonds)
#valores do BlackJack

import numpy as np
import pandas as pd

suits = ['H','S','C','D']
card_val = (list(range(1,11))+[10]*3)*4
base_names = ['A'] + list(range(2,11)) + ['J','K','Q']
cards = []
for suit in suits:
	cards.extend(str(num) + suit for num in base_names)

deck = pd.Series(card_val, index=cards)
#print(deck)

def draw(deck, n=5):
	return deck.sample(n)

print('Mão de cinco cartas')
print(draw(deck))

get_suit = lambda card: card[-1]   #a ultima letra é o naipe
print('Duas cartas aleatórias de cada naipe:')
print(deck.groupby(get_suit, group_keys=False).apply(draw, n=2))
