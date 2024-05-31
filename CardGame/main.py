from Cards import Card, FunctionCard
from Players import Player
from Game import Game
from Deck import Deck


game = Game()
game.add_players(int(input('Podaj liczbę graczy: ')))


# while True:
#     x = int(input('Podaj liczbę graczy: '))
#
#     if x > 1:
#         game.add_players(x)
#         break


run_game = True


while run_game:

    current_player = game.get_current_player()
    current_card = game.current_card

    current_card.show()
    print()

    print('Gracz: ' + str(game.current_player + 1))
    current_player.show_hand()

    playable_cards = current_player.check_hand_for_card(current_card)

    if not playable_cards:
        current_player.draw_card()
    else:
        selected_card_index = int(input('Wybierz kartę: ')) - 1

        while True:

            selected_card = current_player.hand.cards[selected_card_index]

            if current_card.color != selected_card.color and current_card.value != selected_card.value and selected_card.colorful == True:
                selected_card_index = int(input('Karta jest niepoprawna. Wybierz kartę ponownie: ')) - 1
                continue
            else:
                played_card = current_player.play_card(selected_card_index)
                game.current_card = played_card

                if len(current_player.hand.cards) == 1:
                    print(' UNO!')
                elif len(current_player.hand.cards) == 0:
                    game.players.remove(current_player)

                print()

                if isinstance(played_card, FunctionCard):
                    played_card.perform_action(game.get_next_player())
                    pass

                break

    if len(game.players) > 1:
        game.next_player_turn()
    else:
        print("Koniec gry")
        break
