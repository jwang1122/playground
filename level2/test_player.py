import unittest
from card import *

class TestPlayer(unittest.TestCase):
    def test_getHandValue(self):
        john = Player("John")
        ACE = BlackJackCard(0, "Diamonds")
        h8= BlackJackCard(7, "Hearts")
        c8= BlackJackCard(7, "Clubs")
        
        john.addCardToHand(ACE)
        john.addCardToHand(h8)
        john.addCardToHand(c8)
        self.assertEqual(john.getHandValue(), 17)
        