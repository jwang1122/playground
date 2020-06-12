class Card:
    faces = ("ZERO", "ACE", "TWO", "THREE","FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK","QUEEN", "KING")
    suits = ('DIAMONDS', "CLUBS", "SPADES", "HEARTS")

    # constructor
    def __init__(self, face, suit):
        # instance variables 
        if face<1 or face>13:
            raise ValueError("Invalid Card Face!")  
        if suit not in Card.suits:
            raise ValueError("Invalid Card Suit!") 
        self.face = face
        self.suit = suit
        pass

    def __repr__(self):
        return "(" + str(self.getValue()) + "," + self.suit + ")"

    def getValue(self):
        return self.face

    def __eq__(self, other):
        return self.getValue() == other.getValue()

class BlackJackCard(Card):
    def getValue(self):
        if(self.face == 1):
            return 11
        elif(self.face > 9):
            return 10
        return self.face

if __name__ == '__main__':
    c1 = Card(4, "DIAMONDS")
    print(c1)
    c2 = Card(4, "HEART")
    if(c1 == c2):
        print("Same")
    else:
        print("Different")
