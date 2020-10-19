pessoas = []
qtde = m = f = i = t = 0

while True:
    nome = input('Nome: ')
    sexo = input('Sexo (m/f): ').lower()
    pessoas.append([nome, sexo])

    if sexo=='m':
        m += 1
    elif sexo=='f':
        f += 1
    else:
        i += 1
    t += 1

    r = input('Deseja cadastrar outro usuário? (s/n)').lower()

    if r[0]=='n':
        break

print('''Total de usuários do sexo masculino: {}, {:.2f}%
Total do sexo feminino: {}, {:.2f}%
Total de não binários: {}, {:.2f}%'''.format(m, (m/t)*100, f, (f/t)*100, i, (i/t)*100))