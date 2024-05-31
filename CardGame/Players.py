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
        self.hand.cards.append(self.deck.get_card())

    def show_hand(self):
        for card in self.hand.cards:
            card.show()
            print(' ', end='')
        print()

    def player_turn(self):
        self.show_hand()
        card_index = input('Wybierz kartę: ')
        self.play_card(card_index)

    def check_hand_for_card(self, current_card):
        playable_cards = False

        counter = 0

        for card in self.hand.cards:
            if not (current_card.color != card.color and current_card.value != card.value and card.colorful):
                counter += 1

        if counter > 0:
            playable_cards = True
        else:
            print("Automatycznie dobrano kartę")

        return playable_cards

