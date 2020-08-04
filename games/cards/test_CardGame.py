from unittest import TestCase, mock
from games.cards.CardGame import CardGame
from games.cards.DeckOfCards import DeckOfCards
from games.cards.Player import Player


class TestCardGame(TestCase):
    def setUp(self):
        self.card_game = CardGame()

    def test_create_card_game(self):
        self.assertEqual(len(self.card_game.lst_of_players), 4)

        for player in self.card_game.lst_of_players:
            self.assertIsInstance(player, Player)

        self.assertIsNotNone(self.card_game.num_of_cards)
        
    @mock.patch("builtins.print")
    def test_new_game(self, mocked_print):
        with mock.patch.object(DeckOfCards, "new_game") as mocked_new_game:
            self.card_game.new_game()

            self.assertTrue(mocked_print.called)  # Check if print was print all players
            mocked_new_game.assert_called_with()

        with mock.patch.object(DeckOfCards, "deal_one") as mocked_deal_one:
            self.card_game.deal_one()

            mocked_deal_one.assert_called_with()  # Check if deal_one was called

    def test_print_all_players(self):
        with mock.patch("games.cards.Player.print") as mocked_player_print:
            self.card_game.new_game()

            mocked_player_print.assert_called()
