n = int(input('Digite um número: '))

i = 1
while i<=n:
    print('Numero = {}('.format(i), end="")
    for y in range(i, 0, -1):
        print('{},'.format(y), end="")
    print(')')
    i += 1