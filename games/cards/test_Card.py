from unittest import TestCase
from games.cards.Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card(2, "Heart")
        self.card2 = Card(14, "Club")  # 14 == "ACE"

    def test_init(self):
        self.assertIsInstance(self.card1, Card)
        self.assertIsInstance(self.card2, Card)

    def test_init_raise_errors(self):
        with self.assertRaises(ValueError) as context:
            Card(0, "Club")
            self.assertTrue("Value need to be 2-14" in context.exception)
        with self.assertRaises(ValueError) as context:
            Card(2, "Not suit")
            self.assertTrue("Value suit need to be Diamond,Spade,Heart,Club " in context.exception)

    def test_card_fields(self):
        self.assertEqual(self.card1.value, 2)
        self.assertEqual(self.card2.value, 14)

    def test_repr(self):
        self.assertEqual(self.card1.__repr__(), "2 of Heart")
        self.assertEqual(self.card2.__repr__(), "ACE of Club")
