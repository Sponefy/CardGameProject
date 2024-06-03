from Cards import Card, FunctionCard
from Players import Player, Bot
from Game import Game
from Deck import Deck


game = Game()
# game.add_players(int(input('Podaj liczbę graczy: ')))


while True:
    x = int(input('Podaj liczbę graczy: '))
    y = int(input('Podaj liczbę botów: '))

    if x > 1 and 0 <= y <= x:
        game.number_of_players = x
        game.add_players(x - y)
        game.add_bots(y)
        break

run_game = True


while run_game:

    current_player = game.get_current_player()
    current_card = game.current_card

    current_card.show()
    print()

    if not isinstance(current_player, Bot):
        print('Gracz: ' + str(game.current_player + 1))
        current_player.show_hand()

        playable_cards = current_player.check_hand_for_card(current_card)

        if not playable_cards:
            current_player.draw_card()
            print()
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

                    if isinstance(played_card, FunctionCard):
                        played_card.perform_action(current_player, game.get_next_player())
                        pass

                    if len(current_player.hand.cards) == 1:
                        print('UNO!')
                    elif len(current_player.hand.cards) == 0:
                        game.players.remove(current_player)

                    print()

                    break

    else:
        print('Bot: ' + str(game.current_player + 1))

        played_card = current_player.play_random_card(current_card, game.get_next_player())
        game.current_card = played_card

        if len(current_player.hand.cards) == 1:
            print('UNO!')
        elif len(current_player.hand.cards) == 0:
            game.players.remove(current_player)

    # x = input()

    if len(game.players) > 1:
        game.next_player_turn()
    else:
        print("Koniec gry")
        break
