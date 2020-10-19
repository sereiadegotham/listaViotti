x = y = soma = 0

while x<=100:
    soma += x
    if y==2 or x==100:
        print('{} = {}'.format(x, soma))
        soma = y = 0
    elif y<2:
        print('{} + '.format(x), end='')
        y += 1
    x += 1