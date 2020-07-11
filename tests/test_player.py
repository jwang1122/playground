import unittest
from level2.card import *

class TestPlayer(unittest.TestCase):
    def test_getHandValue(self):
        john = Player("John")
        ACE = BlackJackCard("A", "Diamonds")
        h8= BlackJackCard("7", "Hearts")
        c8= BlackJackCard("7", "Clubs")
        
        john.addCardToHand(ACE)
        john.addCardToHand(h8)
        john.addCardToHand(c8)
        self.assertEqual(john.getHandValue(), 15)
        