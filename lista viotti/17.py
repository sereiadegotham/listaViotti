s = float(input("Digite seu salário: "))
filhos = float(input("Digite a quantidade de filhos: "))

if filhos<3:
    s += s*0.05
else:
    s += s*0.15

print("Salário reajustado: {}". format(s))
