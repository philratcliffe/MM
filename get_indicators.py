
def get_indicators(guess, code):
    '''Indicate how close guess is to code'''

    ind = [0, 0, 0, 0]

    for i, c in enumerate(code):
        if c not in guess:
            continue

        if guess[i] == code[i]:
            ind[i] = 2
            continue


        if code.count(c) == 1:
            ind[i] = 1

    return sorted(ind, reverse=True)

