print('Soma de todos os números de 0 a 100: ')

i = soma = 0
while i<100:
    soma += i
    i += 1

    if i==100:
        print('{} = '.format(i), end='')
    else:
        print('{} + '.format(i), end='')

print(soma)
