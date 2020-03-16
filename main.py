from BlackJackClasses.card import Card
from BlackJackClasses.deck import Deck
from BlackJackClasses.hand import Hand
from BlackJackClasses.chip import Chips

playing = True

test_deck = Deck()
test_deck.shuffle()
# print(test_deck)

# Define a Player
test_player = Hand()

#Deal one card from the deck Card(suit, rank) object
pulled_card = test_deck.deal()
print(pulled_card)

test_player.add_card(pulled_card)
test_player.value
print(test_player.value)