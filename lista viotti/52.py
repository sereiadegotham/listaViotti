qtde = int(input('Digite o número de produtos que deseja cadastrar: '))

fisico = servico = 0

while qtde>0:
    prod = input('Nome do produto: ')
    tipo = input('Tipo do produto (F-físico ou S-serviço): ').upper()

    if tipo=='F':
        fisico += 1
    elif tipo=='S':
        servico += 1
    else:
        print('Tipo inválido.')
    qtde -= 1
