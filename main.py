import random

colours = ['orange', 'red', 'green', 'black', 'white', 'yellow']

def main():

    code = generate_code()
    guess = get_guess()
    indicators = get_indicators(code, guess)

    print "Your guess: {}".format(guess)
    print "The code: {}".format(code)
    print "The indicators: {}".format(indicators)

def get_indicators(code, guess):
    indicators = [0, 0, 0, 0]
    for i, g in enumerate(guess):
        if g in code:
            indicators[i] = 1
            if guess[i] == code[i]:
                indicators[i] = 2

    return indicators


def generate_code():
    return random.sample(colours, 4)


def get_guess():
    guess_str = raw_input("make guess: ")
    guess_raw = [c.strip() for c in guess_str.split(',')]
    print guess_raw
    guess = fix_guess_raw(guess_raw)
    print guess
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


