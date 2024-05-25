from Cards import Card
from Deck import Deck


class Player:

    def __init__(self, hand, deck):
        self.hand = hand
        self.deck = deck

    def play_card(self, i):
        card = self.hand.cards[i]
        self.hand.cards.pop(i)
        return card

    def draw_card(self):
        self.hand.append(self.deck.get_card())

    def show_hand(self):
        for card in self.hand.cards:
            card.show()
            print(' ', end='')
        print()

    def player_turn(self):
        self.show_hand()
        card_index = input('Wybierz kartę: ')
        self.play_card(card_index)


