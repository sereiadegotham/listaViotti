e = -1
r = 1

while e<15:
    e += 1
    i = 1
    r = 1
    while i<=e:
        r *= 3
        i += 1

    print('3^{} = {}'.format(e, r))