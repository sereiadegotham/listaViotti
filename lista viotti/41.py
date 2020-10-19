def nome():
    n = input('Digite seu nome: ')
    if len(n)<3:
        print('Nome dever ter mais que 3 caracteres.')
        nome()
    return n

def sexo():
    s = input('Digite seu sexo (m/f): ').lower()

    if s=='m' or s=='f':
        return s
    else:
        print('Sexo inválido.')
        sexo()
    

def email():
    m = input('Digite seu email: ')
    if '@' not in m:
        print('Email inválido.')
        email()
    elif len(m)<10:
        print('Email inválido.')
        email()
    return m

def main():
    n = nome()
    s = sexo()
    m = email()

    print('Nome: {}, sexo: {}, email: {}'.format(n, s, m))

main()
