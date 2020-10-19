print('Digite apenas números de 3 dígitos: ')

while True:
    n1 = input('1º número: ')
    n2 = input('2º número: ')

    if 100<=int(n1)<=999 and 100<=int(n2)<=999:
        break
    else:
        print('Números inválidos.')

t = n1[0] + n2[0] + n1[1] + n2[1] + n1[2] + n2[2]
print('T = {}'.format(t))
