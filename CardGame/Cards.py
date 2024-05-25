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

        print(color_code + self.value + '\033[0m', end='')


class FunctionCard(Card):

    def __init__(self, color, value, colorful):
        super().__init__(color, value, colorful)

    def perform_action(self, players):
        if self.value == '+2':
            self.plus_two(players)
        elif self.value == 'Ø':
            self.block(players)
        elif self.value == '+4':
            self.plus_four(players)
        elif self.value == '🏳‍🌈':
            self.chagne_color(players)
        elif self.value == '🔄':
            self.rotate()

    def plus_two(self, players):
        pass

    def block(self, players):
        pass

    def plus_four(self, players):
        pass

    def chagne_color(self, players):
        pass

    def rotate(self):
        pass



