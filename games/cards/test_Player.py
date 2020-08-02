from unittest import TestCase, mock
from games.cards.Player import Player
from games.cards.Card import Card


class TestPlayer(TestCase):

    def setUp(self):
        self.player1 = Player("rich", 5000, 5)
        with mock.patch.object(Card, '__init__', return_value=None) as mocked_card_init:
            self.cards = []
            for val, suit in [(3, "Diamond"), (8, "Diamond"), (2, "Heart",), (6, "Club"), (11, "Heart")]:
                self.cards.append(Card(val, suit))
                mocked_card_init.assert_called_with(val, suit)

    def tearDown(self):
        pass

    def test_set_hand(self):
        self.player1.set_hand(self.cards)

        self.assertListEqual(self.player1.player_hand, self.cards)

    @mock.patch("builtins.print")
    def test_set_hand_failed(self,mocked_print):
        with mock.patch.object(Card, '__init__', return_value=None) as mocked_card_init:
            new_card = Card(10, "Spade")
            mocked_card_init.assert_called_with(10, "Spade")
            self.cards.append(new_card)
            self.player1.set_hand(self.cards)

            mocked_print.assert_called_with("Each player must receive a number of cards depending on the game")

    def test_get_card(self):
        self.player1.set_hand(self.cards)
        card = self.player1.get_card()

        self.assertIsInstance(card, Card)
        self.assertTrue(len(self.player1.player_hand) == 4)

    def test_add_card(self):
        with mock.patch.object(Card, '__init__', return_value=None) as mocked_card_init:
            new_card = Card(10, "Spade")
            mocked_card_init.assert_called_with(10, "Spade")
            self.player1.add_card(new_card)

            self.assertTrue(len(self.player1.player_hand) != len(self.cards))
            self.assertNotEqual(self.player1.player_hand, self.cards)

    def test_reduce_amount(self):
        self.player1.reduce_amount(3000)

        self.assertTrue(self.player1.amount_money == 2000)

    @mock.patch("builtins.print")
    def test_reduce_amount_value(self, mocked_print):
        self.player1.reduce_amount(-1500)

        mocked_print.assert_called_with("Sorry, input must be a positive integer, try again")

    @mock.patch("builtins.print")
    def test_reduce_amount_type(self, mocked_print):
        self.player1.add_amount("Not a Number")

        mocked_print.assert_called_with("Sorry, invalid input must be a number")

    def test_add_amount(self):
        self.player1.add_amount(200)

        self.assertTrue(self.player1.amount_money == 5200)

    @mock.patch("builtins.print")
    def test_add_amount_value_negative(self, mocked_print):
        self.player1.add_amount(-1500)

        mocked_print.assert_called_with("Sorry, input must be a positive integer, try again")
        # with self.assertRaises(ValueError) as context:
        #     self.player1.reduce_amount(-1500)
        #     self.assertTrue("Amount need to be positive value." in context.exception)

    @mock.patch("builtins.print")
    def test_add_amount_value(self, mocked_print):
        self.player1.add_amount("Not a Number")

        mocked_print.assert_called_with("Sorry, invalid input must be a number")
        # with self.assertRaises(TypeError) as context:
        #     self.player1.reduce_amount("1000")
        #     self.assertTrue("Amount need to be type int." in context.exception)

    @mock.patch("builtins.print")
    def test_print(self, mocked_print):
        self.player1.print()

        mocked_print.assert_called_with("--- Player ---\nName: rich\nAmount: 5000\nCards: []")
