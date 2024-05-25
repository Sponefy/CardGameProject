import random

from Cards import Card, FunctionCard


class Deck:

    def __init__(self):
        self.cards = []

    def create_new_deck(self):
        card_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '+2', 'Ø', '+4', '🏳‍🌈', '🔄']
        colored_cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '+2', 'Ø']
        function_cars = ['+2', 'Ø', '+4', '🏳‍🌈', '🔄']

        self.cards = []

        for _ in range(2):
            for i in range(4):
                for j in range(len(card_values)):
                    colorful = True
                    if card_values[j] in colored_cards:
                        colorful = False

                    if card_values[j] in function_cars:
                        self.cards.append(FunctionCard(i, card_values[j], colorful))
                    else:
                        self.cards.append(Card(i, card_values[j], colorful))

        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def show(self):

        for card in self.cards:
            card.show()

    def get_card(self):
        card = self.cards[0]
        self.cards.pop(0)
        return card

    def get_starting_card(self):
        for card in self.cards:
            if not isinstance(card, FunctionCard):
                self.cards.remove(card)
                return card

    def add_card(self, card):
        self.cards.append(card)