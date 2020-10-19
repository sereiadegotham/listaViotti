s = float(input("Informe seu salário atual: "))

if s<500:
    s += s*0.15
elif 500<=s<=1000:
    s += s*0.1
else:
    s += s*0.5

print("Salário reajustado: {}".format(s))
