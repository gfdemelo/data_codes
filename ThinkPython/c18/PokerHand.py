#!/usr/bin/env python3

from __future__ import print_function, division

from cartas import Mao, Baralho


hist={}

class PokerMao(Mao):
    """Represents a poker hand."""

    def naipe_hist(self):
        """Builds a histogram of the naipes that appear in the hand.

        Stores the result in attribute naipes.
        """
        self.naipes = {}
        for card in self.cards:
            self.naipes[card.naipe] = self.naipes.get(card.naipe, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.naipe_hist()
        for val in self.naipes.values():
            if val >= 5:
                return True
        return False

    def valor_hist(self):
        """Builds a histogram of the naipes that appear in the hand.
                                                                         
        Stores the result in attribute naipes.
        """
        self.valor = {}
        for card in self.cards:
            self.valor[card.valor] = self.valor.get(card.valor, 0) + 1

    def check_poker(self, number=1):
       self.valor_hist()
       for val in self.valor.values():
            if val == number:
                  return True
       return False

    def has_pair(self):
         return self.check_poker(2)

    def has_twopair(self):
       if self.has_pair():
           pares=0
           for val in self.valor.values():
               if val >=2:
                   pares += 1
           if pares >=2:
               return True
       return False

    def has_trinca(self):
       return self.check_poker(3)
	
    def has_sequence(self):
       self.valor_hist()
       lista=[]
       for item in self.valor:
          lista.append(item)
       lista.sort()
       count=0
       if 10 in lista and 11 in lista and 12 in lista and 13 in lista and 1 in lista:
          return True     
       for i in range(len(lista)-1):
           if lista[i+1] - lista[i] ==0:
               del lista[i+1]
               #lista.pop(i+1)
           if lista[i+1] - lista[i] == 1:
               count += 1
           if count >= 4:
               return True
           if lista[i+1] - lista[i] > 1: 
               count=0
       return False
       
       
	
    def has_fullhouse(self):
       if self.check_poker(3) and self.check_poker(2):
           return True
       return False

    def has_quadra(self):
       if self.check_poker(4):
           return True
       return False

    def has_straightflush2(self):
       if self.has_flush() and self.has_sequence():
           return True
       return False


    def has_straightflush(self):
        self.valor_hist()
        self.naipe_hist()
        copa = PokerMao(); ouro= PokerMao(); paus= PokerMao(); espadas=PokerMao()
        lista_copa=[]; lista_ouro=[]; lista_paus=[]; lista_espadas=[];
        if self.has_flush():
            for val in self.cards:
                 if str(val).endswith('Ouros'):
                     ouro.add_card(val)
                     lista_ouro.append(val) 
                 if str(val).endswith('Copas'):
                     copa.add_card(val)
                     lista_copa.append(val) 
                 if str(val).endswith('Paus'):
                     paus.add_card(val) 
                     lista_paus.append(val) 
                 if str(val).endswith('Espadas'):
                     espadas.add_card(val) 
                     lista_espadas.append(val) 
            copa.sort()
            if len(lista_copa) >= 5:
                return copa.has_sequence()
            ouro.sort()
            if len(lista_ouro) >= 5:
                return ouro.has_sequence()
            paus.sort()
            if len(lista_paus) >= 5:
                return paus.has_sequence()
            espadas.sort()
            if len(lista_espadas) >= 5:
                return espadas.has_sequence()
        return False

    def has_highcard(self):
        self.valor_hist()
        if 1 in self.valor.keys():
            return 1
        else:
            return max(self.valor.keys()) 

    def classify(self):
        global hist
        a=self.has_highcard()                            
        hist['high card'] = hist.get('high card', 0) + 1
        if self.has_straightflush2():
           hist['straight flush'] = hist.get('straight flush', 0) + 1
    #       print(hist)
           return
        elif self.has_quadra():
           hist['quadra'] = hist.get('quadra', 0) + 1
     #      print(hist)
           return
        elif self.has_fullhouse():
           hist['full house'] = hist.get('full house', 0) + 1 
      #     print(hist)
           return
        elif self.has_flush():
           hist['flush'] = hist.get('flush', 0) + 1
       #    print(hist)
           return
        elif self.has_sequence():
           hist['sequence'] = hist.get('sequence', 0) + 1 
        #   print(hist)
           return
        elif self.has_trinca():
           hist['trinca'] = hist.get('trinca', 0) + 1 
         #  print(hist)
           return
        elif self.has_twopair():
           hist['two pair'] = hist.get('two pair', 0) + 1
         #  print(hist)
           return
        elif self.has_pair():
           hist['pair'] = hist.get('pair', 0) + 1
          # print(hist)
           return
        return


if __name__ == '__main__':
    for j in range(10000):
    # make a deck
       deck = Baralho()
       deck.shuffle()

    # deal the cards and classify the hands
       for i in range(7):
         hand = PokerMao()
         deck.move_cards(hand, 7)
         hand.sort()
         #print(hand)
         (hand.classify())
    inverse=dict()
    for item in hist:
        inverse.setdefault(hist[item], []).append(item)
    for item in inverse:
        print('%s   -   %.2f' % (inverse[item], item/hist['high card']*100))
    #print(sorted(inverse.items()))
