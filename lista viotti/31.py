print('Digite os valores dos lados do triângulo (somente valores entre 0 e 10).')

while True:
    a = float(input('Informe o valor do primeiro lado: '))
    b = float(input('Informe o valor do segundo lado: '))
    c = float(input('Informe o valor do terceiro lado: '))

    if 0<=a<=10 and 0<=b<=10 and 0<=c<=10:
        break
    else:
        print('Digite somente valores entre 0 e 10.\n')

if a<b+c and b<c+a and c<a+b:
    if a==b==c:
        print('Triângulo Equilátero.')
    elif a==b or b==c or c==a:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')
else:
    print('Valores não formam triângulo.')
