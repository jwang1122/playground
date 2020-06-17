class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        self.value = int(face) if face.isnumeric() else 1 if face=="A" else 11 if face=="J" else 12 if face=="Q" else 13

    def __repr__(self):
        return " of ".join((self.face, self.suit))
    
    def getValue(self):
        return self.value

faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spades", "Clubs", "Hearts", "Diamonds"] 

cards = [Card(s,f) for s in suits for f in faces ]

print(cards)
print(len(cards))

card = cards[12]
print(f"card {card} has value {card.getValue()}")
card = cards[0]
print(f"card {card} has value {card.getValue()}")

from random import shuffle
shuffle(cards)
print(cards)
card = cards[25]
print(f"card {card} has value {card.getValue()}")
