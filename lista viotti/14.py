n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

if n2>n1:
    diferenca = n2 - n1
else:
    diferenca = n1 - n2

print("Diferença do maior pelo menor: {}".format(diferenca))
