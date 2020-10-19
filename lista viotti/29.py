a = float(input('Informe o valor do primeiro lado do triângulo: '))
b = float(input('Informe o valor do segundo lado: '))
c = float(input('Informe o valor do terceiro lado: '))

if a<b+c and b<c+a and c<a+b:
    if a==b==c:
        print('Triângulo Equilátero.')
    elif a==b or b==c or c==a:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')
else:
    print('Valores não formam triângulo.')
