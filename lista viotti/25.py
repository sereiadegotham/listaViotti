print('''Opções de desconto:
 1 – Desconto:20%, comissão:6%
 2 – Desconto:22%, comissão:4%
 3 – Desconto:24%, comissão:2%
Outros:
 O - Desconto 18%, comissão 8%''')

desc = input("Informe o tipo de desconto desejado: ").upper()
valor = float(input("Informe o valor total da venda: R$"))

if desc=='1':
    valor *= 0.8
    comissao = valor*0.06
elif desc=='2':
    valor *= 0.78
    comissao = valor*0.04
elif desc=='3':
    valor *= 0.76
    comissao = valor*0.02
else:
    valor *= 0.82
    comissao = valor*0.08

print("Valor final da venda: {:.2f}\nComissão: {:.2f}".format(valor, comissao))
