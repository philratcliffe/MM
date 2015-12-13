import os
import random
from get_indicators import get_indicators

colours = ['orange', 'red', 'green', 'black', 'white', 'yellow']


def main():
    os.system('clear')
    code = generate_code()

    for i in range(5):
        guess = get_guess(i)
        indicators = get_indicators(guess, code)
        fmt_guess = ' '.join([str(i) for i in guess])
        print "{}\t{}".format(fmt_guess, indicators)
        if code == guess:
            print "Well done the code is {}".format(code)
            return

    print "\n\nYou are a loser my friend - correct code is {}".format(code)

def generate_code():
    return random.sample(range(1, 8), 4)


def get_guess(count):
    guess_str = raw_input("\nguess {}: ".format(count)).strip()

    return [int(c.strip()) for c in guess_str.split(' ')]

if __name__ == '__main__':
    main()


