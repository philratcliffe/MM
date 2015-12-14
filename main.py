import os
import random
import re
from get_indicators import get_indicators

def main():
    """Ties everything together."""
    os.system('clear')
    print
    print '-----------------------------'
    print '       Mastermind Game       '
    print '-----------------------------'
    code = generate_code()

    for i in range(10):
        guess = get_guess(i)
        indicators = get_indicators(guess, code)
        fmt_guess = ' '.join([str(i) for i in guess])
        print "{}\t{}".format(fmt_guess, indicators)
        if code == guess:
            print "Well done the code is {}".format(code)
            return

    print "\n\nYou are a loser my friend - correct code is {}\n\n".format(code)

def generate_code():
    """Generates a randon code for the user to guess."""
    return [random.randint(1, 7) for _ in range(4)]


def get_guess(count):
    """Gets guess from user."""
    guess_str = raw_input("\nguess {}: ".format(count + 1)).strip()
    guess_str = re.sub(r"\s+", "", guess_str, flags=re.UNICODE)

    guess = [int(c) for c in guess_str]
    return guess[:4]

if __name__ == '__main__':
    main()


