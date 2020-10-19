from math import sqrt

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

delta = b*b -4*a*c

if delta<0:
    print("Não existem raízes.")
elif delta==0:
    x = (-b)/2*a
    print("A equação tem apenas uma raíz: {}".format(x))
else:
    print(sqrt(delta))
    x1 = (-b - sqrt(delta))/(2*a)
    x2 = (-b + sqrt(delta))/(2*a)
    print("A equação tem as seguintes raízes: {} e {}".format(x1, x2))

