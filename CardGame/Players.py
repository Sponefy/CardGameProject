from Cards import Card, FunctionCard
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

    # sprawdzenie czy gracz ma kartę, którą może zagrać
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


class Bot(Player):

    def __init__(self, hand, deck):
        super().__init__(hand, deck)

    def play_random_card(self, current_card, next_player):
        random_card = None

        for card in self.hand.cards:
            if not (current_card.color != card.color and current_card.value != card.value and card.colorful):
                random_card = card
                break
            elif not card.colorful:
                random_card = card
                break

        if isinstance(random_card, FunctionCard):
            random_card.perform_action(self, next_player)

        if random_card is None:
            self.draw_card()
            return current_card
        else:
            self.hand.cards.remove(random_card)
            return random_card













