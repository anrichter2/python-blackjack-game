from .Card import Card, suits, ranks
import random

# Deck class object containing 52 card class objects with methods for shuffling the deck and dealing one card at a time.
class Deck:
    def __init__(self):
        self.avail_cards = []
        for suit in suits:
            for rank in ranks:
                self.avail_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.avail_cards)

    def deal_card(self):
        return self.avail_cards.pop()