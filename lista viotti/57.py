pessoas = []
qtde = m = f = t = 0

while True:
    nome = input('Nome: ')
    while True:
        sexo = input('Sexo (m/f): ').lower()
        if sexo[0]=='m' or sexo[0]=='f':
            break
        else:
            print('Sexo inválido!')
    pessoas.append([nome, sexo])

    if sexo=='m':
        m += 1
    elif sexo=='f':
        f += 1
    t += 1

    r = input('Deseja cadastrar outro usuário? (s/n)').lower()

    if r[0]=='n':
        break

print('''Total de usuários do sexo masculino: {}, {:.2f}%
Total do sexo feminino: {}, {:.2f}%'''.format(m, (m/t)*100, f, (f/t)*100))