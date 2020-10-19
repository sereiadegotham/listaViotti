n = int(input('Digite um número para ver sua tabuada: '))

i = 0
while i<11:
    print('{} x {} = {}'.format(n, i, n*i))
    i += 1