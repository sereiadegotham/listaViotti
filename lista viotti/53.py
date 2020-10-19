n = int(input('Digite um número para cálculo do fatorial: '))

x = f = 1
while x<=n:
    if x!= n:
        print('{} x '.format(x), end='')
    else:
        print('{} = '.format(x), end='')
    f *= x
    x += 1
print(f)