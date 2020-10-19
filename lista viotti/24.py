valorp = float(input('Digite o valor do produto: '))
tipo = input('Informe o tipo de cliente (E-Estudante, A-Assalariado, P-aPosentado ou O-Outros): ').upper()
# a função upper() deixa as letras maiúsculas

if tipo=='A':
    valorp *= 0.9 
elif tipo=='E':
    valorp *= 0.85
elif tipo=='P':
    valorp *= 0.75

print('Valor final do produto: {:.2f}'.format(valorp))
