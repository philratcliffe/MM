def get_indicators(guess, code):
    '''Indicate how close guess is to code'''

    guess = guess[:]
    code = code[:]
    ind = []
    ret_val = [0, 0, 0, 0]
    done = []

    # First find any exact guesses
    for i, c in enumerate(guess):
        if c not in code:
            continue

        if guess[i] == code[i]:
            ind.append(2)
            done.append(i)

    # Indicate that any exact matches in guess and code have been used
    for i in range(len(guess)):
        if i in done:
            guess[i] = -1
            code[i] = -2

    # Now find any partial guesses
    while len(guess):

        c = guess[0]
        if c in code:
            ind.append(1)
            code.remove(c)

        guess.pop(0)

    # Prepare return value
    for i, v in enumerate(ind):
        ret_val[i] = ind[i]

    return sorted(ret_val, reverse=True)
