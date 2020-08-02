from unittest import TestCase, mock
from games.cards.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck_cards = DeckOfCards()
        self.deck_shuffle = DeckOfCards()

    def test_nums_of_card_in_deck(self):
        self.assertEqual(len(self.deck_cards.deck), 52)

    def test_deal_one(self):
        top_card_on_deck = self.deck_cards.deal_one()
        self.assertEqual(str(top_card_on_deck), "2 of Diamond")

    def test_new_game(self):
        self.deck_shuffle.new_game()  # New game will shuffle the deck
        self.assertTrue(self.deck_cards.deck != self.deck_shuffle.deck)  # Not the same order in deck

    @mock.patch('builtins.print')
    def test_show(self, mock_print):
        self.deck_cards.show()
        results_expected = ""
        for card in self.deck_cards.deck:
            results_expected += str(card) + "\n"

        mock_print.assert_called_with(results_expected)
