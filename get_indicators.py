
def get_indicators(guess, code):
    '''Indicate how close guess is to code'''

    d = {c: 0 for c in guess}
    print "dict {}".format(d)

    for i, c in enumerate(guess):
        state = d.get(c)
        if state == 2:
            # Already found this colour in the right location
            continue

        if c in code:
            if state == 0:
                # Right colour
                d[c] = 1
            if guess[i] == code[i]:
                # Right colour, right location
                d[c] = 2

    res = list(d.values())
    [res.append(0) for _ in range(4 - len(d))]
    return res

