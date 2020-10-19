maca = int(input("Quantas maçãs você comprou? "))
pera = int(input("Quantas peras? "))
banana = int(input("Quantas bananas? "))

pmaca = float(input("Qual o preço da maça?"))
ppera = float(input("Qual o preço da pera?"))
pbanana = float(input("Qual o preço da banana?"))

gasto = maca*pmaca + pera*ppera + banana*pbanana

pgto = float(input("Quanto você dá para pagar?"))

if gasto>pgto:
    print("Dinheiro insuficiente.")
else:
    print("Pago. Troco: {}".format(pgto - gasto))
