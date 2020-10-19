salario = float(input("Informe seu salário: "))

if salario<2000:
    salario += salario*0.1
    print("Você recebeu um aumento de 10% e seu salário agora é de R${}. ".format(salario))
else:
    print("Seu salário não foi alterado. ")

