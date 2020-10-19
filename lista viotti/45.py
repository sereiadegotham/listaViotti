n = int(input('Digite um número para ver sua tabuada: '))

i = 10
while i>=0:
    print('{} x {} = {}'.format(n, i, n*i))
    i -= 1