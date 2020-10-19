n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
n4 = float(input("Nota 4:"))

media = (n1 + n2 + n3 + n4)/4

if media>=7:
    print("Aprovado.")
else:
    print("Fazer exame.")

    exame = float(input("Informe a nota do exame: "))
    if exame>=6:
        print("Aprovado pelo exame.")
    else:
        print("Reprovado.")
