print('Cadastro de usuários:')
pessoas = []
m = f = 0

while True:
    usuario = []
    usuario[0] = input('Nome: ')
    usuario[1] = int(input('Idade: '))
    usuario[2] = input('Sexo (masc/fem):').lower()

    if usuario[2]!='masc' and usuario[2]!='fem':
        print('Sexo Inválido!\n')
    else:
        pessoas.append(usuario[::])
        if usuario[2] in 'feminino':
            f += 1
        elif usuario[2] in 'masculino':
            m += 1

        r = input('Deseja realizar novo cadastro? (sim/nao)')
        if r=='nao':
            break

print('Usuários do sexo feminino: {}\nUsuários do sexo masculino: {}'.format(f, m))
