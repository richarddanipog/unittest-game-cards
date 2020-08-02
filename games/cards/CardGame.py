import random
from games.cards.Player import Player
from games.cards.DeckOfCards import DeckOfCards


class CardGame(DeckOfCards):

    def __init__(self, num_of_cards=5):
        DeckOfCards.__init__(self)
        amount_player = random.randint(5000, 10000)  # Random amount between 5000-10000
        self.num_of_cards = num_of_cards
        self.lst_of_players = \
            [
                Player("Richard", amount_player, num_of_cards),
                Player("Ricky", amount_player, num_of_cards),
                Player("Shay", amount_player, num_of_cards),
                Player("Ori", amount_player, num_of_cards)
            ]

    def new_game(self):
        """ Start a new game """
        self.__init__()
        super().new_game()
        for _ in range(self.num_of_cards):  # Distribute cards to each player
            for player in self.lst_of_players:
                card = super().deal_one()
                player.add_card(card)

        for player in self.lst_of_players:  # Print all player
            player.print()

