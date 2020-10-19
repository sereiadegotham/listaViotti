s = 0
x = 1
y = 50

print('S = ', end="")
while x<=50:
    s += x/y
    print('{}/{} + '.format(x,y), end="")
    x += 1
    y -= 1

print('\nValor de S = ', s)