class Card:
    faces = ("ZERO", "ACE", "TWO", "THREE","FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK","QUEEN", "KING")
    suits = ('DIAMONDS', "CLUBS", "SPADES", "HEARTS")

    # constructor
    def __init__(self, face, suit):
        # instance variables    
        self.face = face
        self.suit = suit
        pass

    def __repr__(self):
        return "(" + str(self.face) + "," + self.suit + ")"

    def getValue(self):
        return # your code goes here

    def __eq__(self, other):
        return # your code goes here

c = Card(4, "DIAMONDS")
print(c)