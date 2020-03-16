class Chips():

    def __init__(self, total = 100):
        self.total = total # Chips on hand
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet