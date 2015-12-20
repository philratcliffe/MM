import os
import re

class TextInterface(object):

    def display_intro(self):
        os.system('clear')
        print
        print '-----------------------------'
        print '       Mastermind Game       '
        print '-----------------------------'

    def get_guess(self, count):
        """Gets guess from user."""
        guess_str = raw_input("\nguess {}: ".format(count + 1)).strip()
        guess_str = re.sub(r"\s+", "", guess_str, flags=re.UNICODE)
        if "save" in guess_str:
            return "save"

        guess = [int(c) for c in guess_str]
        return guess[:4]

    def display_row(self, guess, indicators):
        fmt_guess = ' '.join([str(i) for i in guess])
        print "{}\t{}".format(fmt_guess, indicators)

    def display_you_win(self, code):
        print "Well done the code is {}".format(code)

    def display_you_lose(self, code):
        print "\n\nYou are a loser my friend - correct code is {}\n\n".format(code)
