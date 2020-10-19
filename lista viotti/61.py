print('Análise de números entre 500 e 10000')
n = 500
par = impar = entre = d45 = 0

while n<=10000:
    if n%2==0:
        par += n
    else:
        impar += n
    if 600<=n<=10000:
        entre += n
    if n%4==0 or n%5==0:
        d45 += n
    n += 1
print('''Soma dos pares: {}
Soma dos ímpares: {}
Soma dos valores entre 600 e 8765: {}
Soma dos divisíveis por 4 e 5: {}'''.format(par, impar, entre, d45))