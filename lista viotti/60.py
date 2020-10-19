n = int(input('Quantos números deseja digitar? '))
soma = t = 0

while n>0:
    num = int(input('Digite o número: '))
    soma += num
    t += 1
    n -= 1

print('Soma: {}\nMédia: {:.2f}'.format(soma, soma/t))