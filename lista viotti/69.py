n = 1
total = somatotal = somapar = totalpar = 0

print('Digite vários números. Para parar digite um número negativo.\n')

while n>0:
    n = int(input('Digite um número : '))
    if n % 2 == 0:
        totalpar += 1
        somarpar += n
    total += 1
    somatotal += n

print('''Quantidade de números pares: {}
Média de números pares: {}
Quantidade de números digitados: {}
Soma total dos números digitados: {}'''.format(totalpar, somapar/totalpar, total, somatotal))