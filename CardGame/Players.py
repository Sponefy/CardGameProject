class Player:

    def __init__(self, deck):
        self.hand = []
        self.deck = deck

    def play_card(self, i):
        card = self.hand[i]
        self.hand.pop(i)
        return card

    def draw_card(self):
        self.hand.append(self.deck.get_card())

    def show_hand(self):
        for card in self.hand:
            print(card, end='')
