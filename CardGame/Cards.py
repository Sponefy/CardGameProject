import random

from colored import fg, attr


class Card:

    def __init__(self, color, value, colorful):
        self.color = color
        self.value = value
        self.colorful = colorful

    def show(self):
        color_code = '\033[0m'

        if self.colorful is not True:
            if self.color == 0:
                color_code = '\033[91m'
            elif self.color == 1:
                color_code = '\033[92m'
            elif self.color == 2:
                color_code = '\033[93m'
            elif self.color == 3:
                color_code = '\033[94m'

        print(color_code + self.value + '\033[0m')


class FunctionCards(Card):

    def __init__(self, color, value, colorful):
        super().__init__(color, value, colorful)

    def perform_action(self):
        if self.value == '+2':
            self.plus_two()
        elif self.value == 'Ø':
            self.block()
        elif self.value == '+4':
            self.plus_four()
        elif self.value == '🏳‍🌈':
            self.chagne_color()
        elif self.value == '🔄':
            self.rotate()

    def plus_two(self):
        pass

    def block(self):
        pass

    def plus_four(self):
        pass

    def chagne_color(self):
        pass

    def rotate(self):
        pass


class Deck:

    def __init__(self):

        card_values = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10', '+2', 'Ø', '+4', '🏳‍🌈', '🔄']
        colored_cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '+2', 'Ø']
        function_cars = ['+2', 'Ø', '+4', '🏳‍🌈', '🔄']

        card_colors = ['s','h','d','c'] #spades, hearths, dimonds, clubs
        self.cards = []

        for i in range(4):
            for j in range(len(card_values)):
                colorful = True
                if card_values[j] in colored_cards:
                    colorful = False

                if card_values[j] in function_cars:
                    self.cards.append(FunctionCards(i, card_values[j], colorful))
                else:
                    self.cards.append(Card(i, card_values[j], colorful))

        random.shuffle(self.cards)

    def show(self):

        for card in self.cards:
            card.show()

    def get_card(self):
        card = self.cards[0]
        self.cards.pop(0)
        return card
