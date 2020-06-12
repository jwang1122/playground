import random

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
        return "(" + Card.faces[self.face] + " of " + self.suit + ")"

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


class Deck:
    NUMFACES = 13
    NUMSUITS = 4
    NUMCARDS = 52
    SUITS = ('DIAMONDS', "CLUBS", "SPADES", "HEARTS")
    def __init__(self):
        # initialize data - stackOfCards - topCardIndex
        self.topCardIndex = 51
        self.stackOfCards = []

        for i in range(len(Deck.SUITS)):
            for j in range(Deck.NUMFACES):
                self.stackOfCards.append(BlackJackCard(j+1, Deck.SUITS[i]))

    def __repr__(self):
        pass

    def setTopCardIndex(self, n):
        # setter
        pass

    def setStackOfCards(self,cards):
        # setter
        pass

    def shuffle(self):
        random.shuffle(self.stackOfCards)
        self.topCardIndex = 51

    def getCard(self):
        return self.topCardIndex

    def size(self):
        return 52

    def numCardsLeft(self):
        return 0

    def nextCard(self):
        self.topCardIndex -= 1
        return self.stackOfCards[self.topCardIndex]

class Player:
    def __init__(self):
        pass
    
    def addCardToHand(self, card):
        pass

    def getHandValue(self):
        return 9

    def hit(self):
        value = self.getHandValue()
        if value >= 20:
            return False
        if value <= 10:
            return True
        answer = input("Do you want to hit? (y or n): ")
        return True if answer=='y' else False

