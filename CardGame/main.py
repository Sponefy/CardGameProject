from Cards import Card
from Players import Player
from Game import Game
from Deck import Deck


game = Game()
game.add_players(int(input('Podaj liczbę graczy: ')))


run_game = True


while run_game:

    current_player = game.get_current_player()
    current_card = game.current_card

    current_card.show()
    print()

    current_player.show_hand()

    selected_card_index = int(input('Wybierz kartę: ')) - 1

    while True:

        selected_card = current_player.hand.cards[selected_card_index]

        if current_card.color != selected_card.color and current_card.value != selected_card.value:
            selected_card_index = int(input('Karta jest niepoprawna. Wybierz kartę ponownie: ')) - 1
            continue
        else:
            current_player.play_card(selected_card_index).show()
            print()
            break

    game.next_player_turn()
