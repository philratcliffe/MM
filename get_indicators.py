
def get_indicators(guess, code):
    '''Indicate how close guess is to code'''
    r = [0, 0, 0, 0]
    d = {}
    for i, c in enumerate(guess):
        state = d.get(c, 0)
        if state == 2:
            continue
        if guess[i] in code:
            if state == 0:
                d[c] = 1
                r[i] = 1
            if guess[i] == code[i]:
                d[c] = 2
                r[i] = 2
    return r

