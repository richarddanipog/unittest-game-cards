ACE_FACES = {14: "ACE", 13: "King", 12: "Queen", 11: "Jack"}
TYPES_CARD = {"Diamond": 1, "Spade": 2, "Heart": 3, "Club": 4}


class Card:
    def __init__(self, value, suit):
        if 1 >= value or value >= 15:
            raise ValueError("Value need to be 2-14")
        elif suit not in TYPES_CARD:
            raise ValueError("Value suit need to be Diamond, Spade, Heart, Club ")
        else:
            self.value = value
            self.suit = suit

    def __repr__(self):
        """ Print card value of suit """
        val = ACE_FACES.get(self.value) if ACE_FACES.get(self.value) else self.value
        return f"{val} of {self.suit}"  # value of suit


