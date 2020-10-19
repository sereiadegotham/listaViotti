original = []
i = 0

while i<7:
    x = int(input('Original {}: '.format(i+1)))
    original.append(x)
    i += 1

destino = []
i = 0

while i<7:
    destino.append(original[i]*3)
    print('Destino {}: {}'.format(i+1, destino[i]))
    i += 1