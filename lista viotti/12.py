s = float(input("Informe seu salário: "))

if s<1500:
    s -= s*0.08
else:
    ir = s*0.05
    inss = s*0.11
    s = s - ir - inss

print("Seu salário líquido é de R${}. ".format(s))
    
    
