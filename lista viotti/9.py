from math import sqrt

c1 = float(input("Informe a medida do cateto 1 (em cm): "))
c2 = float(input("Informe a medida do cateto 2 (em cm): "))

h = sqrt(c1**2+c2**2)
a = (c1*c2)/2

print("A hipotenusa do triângulo é {:.2}cm e sua área {:.2}.".format(h, a))
