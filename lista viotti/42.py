print('Quantidade de grãos de milho no tabuleiro de xadrez:')

g = casa = 1

while casa<=64:
    print('Casa {}: {} grãos.\n'.format(casa, g))
    casa += 1
    g *= 2

