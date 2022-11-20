import unittest

from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self) -> None:
        self.cardgame = CardGame()
        self.card_1 = Card("Spades", 1)
        self.card_2 = Card("Hearts", 12)
        self.cards = [self.card_1, self.card_2]
        return

    def test_check_for_ace(self):
        self.assertEqual(self.cardgame.check_for_ace(self.card_1), True)

    def test_highest_card(self):
        self.assertEqual(self.cardgame.highest_card(self.card_1, self.card_2), self.card_2)

    def test_cards_total(self):
        self.assertEqual(self.cardgame.cards_total(self.cards), "You have a total of 13")
        