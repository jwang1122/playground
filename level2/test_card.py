import unittest
from card import *

class TestBlackJackCard(unittest.TestCase):
    def test_faces(self):
        c1 = BlackJackCard(1, "DIAMONDS")
        self.assertEqual(c1.getValue(), 11)
        c1 = BlackJackCard(9, "DIAMONDS")
        self.assertEqual(c1.getValue(), 9)
        c1 = BlackJackCard(11, "DIAMONDS")
        self.assertEqual(c1.getValue(), 10)
        c1 = BlackJackCard(13, "DIAMONDS")
        self.assertEqual(c1.getValue(), 10)

    
    def test_init(self):
        self.assertRaises(ValueError, BlackJackCard, -2, "DIAMONDS")        
        self.assertRaises(ValueError, BlackJackCard, 2, "DIAMOND")        
        self.assertRaises(ValueError, BlackJackCard, 14, "DIAMONDS")
    
    def test_EqualValue(self):
        c1 = BlackJackCard(11, "DIAMONDS")
        c2 = BlackJackCard(13, "HEARTS")
        self.assertEqual(c1==c2, True)
 