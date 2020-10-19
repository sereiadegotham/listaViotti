n = 1
pares = impares = total = 0

print('Digite vários números. Para parar digite um número negativo.\n')

while n>0:
    n = int(input('Digite um número : '))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    total += 1

print('''Números pares: {}
Números ímpares: {}
Total: {}'''.format(pares, impares, total))