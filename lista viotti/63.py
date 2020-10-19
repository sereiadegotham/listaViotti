n = int(input('Quantos números deseja digitar? '))
limInf = int(input('Qual o intervalo válido? \nLimite Inferior: '))
limSup = int(input('Limite Superior: '))

i = maior = menor = 1
pares = impares = 0
while i<=n:
    num = int(input('Informe o {}º número: '.format(i)))
    if num<limInf or num>limSup:
        print("Número Inválido!")
    else:
        if i==1:
            maior = num
            menor = num
        else:
            if num>maior:
                maior = num
            elif num<menor:
                menor = num
        if num%2==0:
            pares += 1
        else:
            impares += 1
        i += 1

print('''Maior número: {}
Menor número: {}
Quantidade de pares: {}
Quantidade de ímpares: {}'''.format(maior, menor, pares, impares))