import random


class Player:
    def __init__(self, name, amount, num_cards=5):
        self.name = name
        self.amount_money = amount
        self.player_hand = []
        self.num_cards_on_hands = num_cards

    def set_hand(self, new_cards):
        """
            Set new Cards for player
            check if length new_cards are valid to number card in hand depending on the game
        """
        if len(new_cards) == self.num_cards_on_hands:
            self.player_hand = new_cards
        else:
            print("Each player must receive a number of cards depending on the game")

    def get_card(self):
        # Get random card from player hand
        if len(self.player_hand):
            random_card = random.choice(self.player_hand)
            self.player_hand.pop(self.player_hand.index(random_card))
            return random_card

    def add_card(self, card):
        # Add card
        self.player_hand.append(card)

    def reduce_amount(self, amount):
        # Reduce amount from player
        if self.__check_amount(amount):
            self.amount_money -= int(amount)

    def add_amount(self, amount):
        # Add amount from player
        if self.__check_amount(amount):
            self.amount_money += int(amount)

    def __check_amount(self, amount):
        """ Check if amount is valid """
        try:
            if int(amount) <= 0:
                print("Sorry, input must be a positive integer, try again")
            else:
                return True
        except TypeError:
            print("Amount need to be type int.1")
            return
        except ValueError:
            print("Sorry, invalid input must be a number")

    def print(self):
        """ Print
            --- Player ---
            Name:
            Amount:
            Cards:
        """
        print(f"--- Player ---\nName: {self.name}\nAmount: {self.amount_money}\nCards: {self.player_hand}")
