import random
from get_indicators import get_indicators

colours = ['orange', 'red', 'green', 'black', 'white', 'yellow']

def main():

    code = generate_code()

    for _ in range(10):
        guess = get_guess()
        indicators = get_indicators(code, guess)
        print "Your guess: {} indicators: {}".format(guess, indicators)
        if code == guess:
            print "Well done the code is {}".format(code)
            break

def generate_code():
    return random.sample(colours, 4)


def get_guess():
    guess_str = raw_input("make guess: ")
    guess_raw = [c.strip() for c in guess_str.split(',')]
    guess = fix_guess_raw(guess_raw)
    return guess

def fix_guess_raw(guess_raw):
    guess = guess_raw[::]
    for i, g in enumerate(guess_raw):
        for c in colours:
            if c.startswith(g):
                guess[i] = c
                break
    return guess



if __name__ == '__main__':
    main()


