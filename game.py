import os
import random
from get_indicators import get_indicators

class Game():

    def __init__(self, user_interface):
        self.user_interface = user_interface
        self.code = self.generate_code()
        self.rows = []
        self.user_interface.display_intro()
        self.save_filename = "saved_game"
        self.max_guesses = 10

    def is_saved_game(self):
        return os.path.isfile(self.save_filename)

    def save_game(self):
        with open(self.save_filename, 'w') as f:
            f.write(''.join([str(i) for i in self.code]))
            f.write('\n')

            for row in self.rows:
                l = row[0] + row[1]
                self.save_row(f, row[0], row[1])

    def save_row(self, f, guess, ind):
        f.write(''.join([str(i) for i in guess]))
        f.write(':')
        f.write(''.join([str(i) for i in ind]))
        f.write('\n')


    def restore_game(self):
        with open(self.save_filename, 'r') as f:
            code_str = f.readline().strip()
            self.code = [int(i) for i in code_str]
            for line in f.readlines():
                guess, indicators = line.split(':')
                self.rows.append((guess, indicators))
                self.user_interface.display_row(guess, indicators)

    def play(self):

        for i in range(len(self.rows), self.max_guesses):
            guess = self.user_interface.get_guess(i)
            if guess == "save":
                self.save_game()
                continue
            indicators = get_indicators(guess, self.code)
            self.rows.append((guess, indicators))
            self.user_interface.display_row(guess, indicators)
            if self.code == guess:
                self.user_interface.display_you_win()
                return

        self.user_interface.display_you_lose()


    def generate_code(self):
        """Generates a randon code for the user to guess."""
        return [random.randint(1, 7) for _ in range(4)]


