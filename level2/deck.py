class Deck:
    NUMFACES = 13
    NUMSUITS = 4
    NUMCARDS = 52

    def __init__(self):
        # initialize data - stackOfCards - topCardIndex
        self.topCardIndex = 51
        self.stackOfCards = []

        # loop through suits
		# loop through faces
		# add in a new card

    def __repr__(self):
        return 
    def setTopCardIndex(self, n):
        # setter
        pass

    def setStackOfCards(self,cards):
        # setter
        pass

    def shuffle(self):
        # shuffle the deck
        # reset variables as needed
        pass

    def getCard(self):
        return self.topCardIndex

    def size(self):
        return 52

    def numCardsLeft(self):
        return 0

    def nextCard(self):
        self.topCardIndex -= 1
        return self.stackOfCards[self.topCardIndex]