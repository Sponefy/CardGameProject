from Deck import Deck
from Players import Player, Bot


class Game:
    def __init__(self):
        self.players = []
        self.fresh_deck = Deck()
        self.fresh_deck.create_new_deck(self)

        self.used_deck = Deck()
        self.current_player = 0
        self.direction = 1
        self.number_of_players = None
        self.number_of_starting_cards = 7

        self.current_card = self.fresh_deck.get_starting_card()

    def add_players(self, number):

        for i in range(number):
            player_deck = Deck()

            # tworzenie początkowej tali gracza
            for _ in range(self.number_of_starting_cards):
                player_deck.add_card(self.fresh_deck.get_card())

            self.players.append(Player(player_deck, self.fresh_deck))

    def add_bots(self, number):
        for i in range(number):
            player_deck = Deck()

            # tworzenie początkowej tali gracza
            for _ in range(self.number_of_starting_cards):
                player_deck.add_card(self.fresh_deck.get_card())

            self.players.append(Bot(player_deck, self.fresh_deck))

    # odwórócenie kolejności
    def change_direction(self):
        self.direction = self.direction * (-1)

    def shuffle_used_deck(self):
        self.fresh_deck = self.used_deck.shuffle_deck()
        self.used_deck = Deck()

    # zwraca kolejnego gracza
    def get_next_player(self):
        next_player = self.current_player + self.direction

        if next_player == self.number_of_players:
            next_player = 0
        elif next_player == -1:
            next_player = self.number_of_players - 1

        return self.players[next_player]


    # zmienia kolejkę na następnego gracza
    def next_player_turn(self):
        next_player = self.current_player + self.direction

        if next_player == self.number_of_players:
            next_player = 0
        elif next_player == -1:
            next_player = self.number_of_players - 1

        self.current_player = next_player

    def get_current_player(self):
        return self.players[self.current_player]