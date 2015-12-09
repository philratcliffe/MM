
def check_guess(g, a):
    '''Check if guess equals answer'''
    r = [0, 0, 0, 0]
    for i, c in enumerate(g):
        if g[i] in a:
            r[i] = 1
            if g[i] == a[i]:
                r[i] = 2
    return r

