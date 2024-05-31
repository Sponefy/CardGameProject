import random




class Card:

    def __init__(self, color, value, colorful, game):
        self.color = color
        self.value = value
        self.colorful = colorful
        self.game = game

    def show(self):
        color_code = '\033[0m'

        if self.colorful is True:
            if self.color == 0:
                color_code = '\033[91m' # czerwony
            elif self.color == 1:
                color_code = '\033[92m' # zielony
            elif self.color == 2:
                color_code = '\033[93m' # żółty
            elif self.color == 3:
                color_code = '\033[94m' # niebieski

        print(color_code + self.value + '\033[0m', end='')


class FunctionCard(Card):

    def __init__(self, color, value, colorful, game):
        super().__init__(color, value, colorful, game)

    def perform_action(self, player):
        if self.value == '+2':
            self.plus_two(player)
        elif self.value == 'Ø':
            self.block()
        elif self.value == '+4':
            self.plus_four(player)
        elif self.value == '🏳‍🌈':
            self.change_color(player)
        elif self.value == '§':
            self.rotate()

    def plus_two(self, player):

        self.give_player_cards(player, 2)
        self.skip_player()
        pass

    def block(self):

        self.skip_player()
        pass

    def plus_four(self, player):

        self.give_player_cards(player, 4)
        self.change_color(player)
        self.skip_player()
        pass

    def give_player_cards(self, player, amount):
        for i in range(amount):
            player.draw_card()

    def change_color(self, player):

        from Players import Bot

        if isinstance(player, Bot):
            self.color = random.randint(0, 3)
        else:
            while True:
                new_color = int(input('Wybierz kolor: 1 - czerowny, 2 - zielony, 3 - żółty, 4 - niebieski: ')) - 1

                if 0 <= new_color <= 3:
                    self.color = new_color
                    break

    def skip_player(self):
        self.game.next_player_turn()

    def rotate(self):
        self.game.change_direction()
