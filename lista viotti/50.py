print('Informe 10 números entre 1 e 100: ')

i = menor10 = maior20 = 0
n = []

while i<10:
    num = int(input())

    if num<1 or num>100:
        print('Número inválido!')
    else:
        if num<10:
            menor10 += 1
        elif num>20:
            maior20 += 1
        i += 1

print('Você digitou {} números menores que 10 e {} números maiores que 20.'.format(menor10, maior20))