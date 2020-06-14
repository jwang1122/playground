import unittest
from card import *

class TestBlackJackCard(unittest.TestCase):
    def test_faces(self):
        c1 = BlackJackCard(0, "DIAMONDS")
        self.assertEqual(c1.getValue(), 11)
        c1 = BlackJackCard(8, "DIAMONDS")
        self.assertEqual(c1.getValue(), 9)
        c1 = BlackJackCard(9, "DIAMONDS")
        self.assertEqual(c1.getValue(), 10)
        c1 = BlackJackCard(12, "DIAMONDS")
        self.assertEqual(c1.getValue(), 10)
        c1 = Card(0,"Diamonds")
        c2 = Card(1, "Hearts")
        self.assertEqual(c2>c1, True)
        c1 = Card(12,"Diamonds")
        c2 = Card(11, "Hearts")
        self.assertEqual(c2>c1, False)
        self.assertEqual(c1+c2, 25)
    
    def test_EqualValue(self):
        c1 = BlackJackCard(11, "DIAMONDS")
        c2 = BlackJackCard(13, "HEARTS")
        self.assertEqual(c1==c2, True)
 