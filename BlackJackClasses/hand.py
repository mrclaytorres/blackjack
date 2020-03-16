from .deck import *

class Hand():

    def __init__(self):
        self.cards = [] # start with an empty list
        self.value = 0 # start with a zero value
        self.aces = 0 # keep track of aces

    def add_card(self, card):
        # card passed in
        # from Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]

        #track for aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1