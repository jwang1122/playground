from card import *

deck = Deck()

for i in range(Deck.NUMCARDS):
    print(i, ":", deck.nextCard())
print()

deck.shuffle()

for j in range(Deck.NUMCARDS):
    print(j, ":", deck.nextCard())
print()
