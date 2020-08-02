from unittest import TestCase, mock
from games.cards.CardGame import CardGame
from games.cards.DeckOfCards import DeckOfCards


class TestCardGame(TestCase):
    def setUp(self):
        self.card_game = CardGame()

    @mock.patch("builtins.print")
    def test_new_game(self, mocked_print):
        with mock.patch.object(DeckOfCards, "new_game") as mocked_new_game:
            self.card_game.new_game()

            self.assertTrue(mocked_print.called)  # Check if print was print all players
            mocked_new_game.assert_called_with()

        with mock.patch.object(DeckOfCards, "deal_one") as mocked_deal_one:
            self.card_game.deal_one()

            mocked_deal_one.assert_called_with()  # Check if deal_one was called
