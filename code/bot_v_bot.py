from __future__ import print_function
# tag::bot_vs_bot[]
from dlgo.agent.naive import RandomBot
from dlgo import goboard_slow
from dlgo import gotypes
from dlgo.utils import print_board, print_move, clear_screen
import time


def main():
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: RandomBot(),
        gotypes.Player.white: RandomBot(),
    }
    while not game.is_over():
        time.sleep(0.3)  # <1>

        bot_move = bots[game.next_player].select_move(game)
        game = game.apply_move(bot_move)
        clear_screen()   # <2>
        print_board(game.board)
        print_move(game.next_player, bot_move)


if __name__ == '__main__':
    main()

# <1> We set a sleep timer to 0.3 seconds so that bot moves aren't printed too fast to observe
# <2> Before each move we clear the screen. This way the board is always printed to the same position on the command line.
# end::bot_vs_bot[]
