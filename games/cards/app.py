from games.cards.CardGame import CardGame


def check_who_won_round(lst_cards):
    """ Check witch player won the round """
    curr_winner = lst_cards[0]
    print(curr_winner[1])
    for i in range(1, len(lst_cards)):
        print(lst_cards[i][1])
        for j in range(i, len(lst_cards)):
            if curr_winner[1].value < lst_cards[j][1].value:
                curr_winner = lst_cards[j]
            elif curr_winner[1].value == lst_cards[j][1].value:
                if type_cards[curr_winner[1].suit] < type_cards[lst_cards[j][1].suit]:
                    curr_winner = lst_cards[j]
    return curr_winner


def start_game():
    print("\n<---- Game Start ---->")
    for round_game in range(1, 6):
        print(f"Round {round_game}")
        amount_on_table = 0
        cards_on_table = {}

        for player in card_game.lst_of_players:
            cards_on_table[player] = player.get_card()  # Get card from each player
            player.reduce_amount(100 * round_game)  # Reduce amount from player
            amount_on_table += 100 * round_game  # Collect money from each player on round

        print("Cards on table: ")
        lst_cards = list(cards_on_table.items())
        round_winner = check_who_won_round(lst_cards)

        print("\nThe winner in this round is: ")
        round_winner[0].add_amount(amount_on_table)
        print(round_winner[0].name, "\n")

    biggest_amount = 0
    the_winner = None
    for player in card_game.lst_of_players:  # Check who is the winner
        if biggest_amount < player.amount_money:
            biggest_amount = player.amount_money
            the_winner = player

    print("***** THE WINNER IS *****")
    print(f"""{the_winner.name} with amount of {the_winner.amount_money} """)


card_game = CardGame(5)
card_game.new_game()
type_cards = {"Diamond": 1, "Spade": 2, "Heart": 3, "Club": 4}
play_game = "y"
while play_game == "y":
    start_game()
    play_game = input("\nPlay Again, Insert Y else game will stop: ").lower()
    if play_game == "y":
        card_game.new_game()
