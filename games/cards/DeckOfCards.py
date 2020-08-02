import random
from games.cards.Card import Card

TYPES_CARD = ["Diamond", "Spade", "Heart", "Club"]
ACE_FACES = {"Jack": 11, "Queen": 12, "King": 13, "ACE": 14}


class DeckOfCards:
    def __init__(self):
        # init the deck with all cards
        self.deck = self.__build_deck()

    def __shuffle(self):
        # Shuffle the deck
        random.shuffle(self.deck)

    def deal_one(self):
        # Take one card from the top of the deck
        return self.deck.pop(0)

    def new_game(self):
        # Init the deck
        self.__init__()
        self.__shuffle()

    def show(self):
        # Print all card in deck
        all_cards = ""
        for card in self.deck:
            all_cards += str(card) + "\n"
        print(all_cards)

    def __build_deck(self):
        # First - create regular cards [(2,Diamond), (3,Diamond), (4,Diamond), (5,Diamond), (6,Diamond),....]
        regular_cards = [Card(num, suit) for suit in TYPES_CARD for num in range(2, 11)]

        # second - create regular cards [(Jack,Diamond), (Jack,Spade), (Jack,Heart), (Jack,Club), (Queen,Diamond),....]
        faces_cards = [Card(v, suit) for k, v in ACE_FACES.items() for suit in TYPES_CARD]

        return regular_cards + faces_cards