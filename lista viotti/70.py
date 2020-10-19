n = int(input('Quantos números deseja digitar? '))

m = 0
i = 1

while i<=n:
    num = int(input('Digite o {}º número: '.format(i)))
    m += num
    i += 1

print('Quantidade de números digitados: {}\nMédia: {}'.format(n, m/n))