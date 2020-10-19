n = int(input('Quantos números deseja digitar? '))
par = impar = 0

while n>0:
    num = int(input('Digite o número: '))
    if num%2==0:
        par += num
    else:
        impar += num
    n -= 1

print('Soma dos pares: {}\nSoma dos ímpares: {}'.format(par, impar))