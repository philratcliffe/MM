from game import Game
import os

from text_interface import TextInterface


def main():

    user_interface = TextInterface()
    game = Game(user_interface)
    if game.is_saved_game():
        game.restore_game()
    game.play()


if __name__ == '__main__':
    main()



