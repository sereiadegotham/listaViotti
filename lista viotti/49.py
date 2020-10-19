print('---------------------------Calculo de média---------------------------')

while True:
    i = 0
    n = []

    nome = input('Nome do aluno: ')

    while i<4:
        print('Informe a {}ª nota: '.format(i+1), end='')
        num = float(input())
        n.append(num)
        i += 1

    media = (n[0]*2 + n[1]*3 + n[2]*5 + n[3]*6)/16
    print('Nome: {}\nMédia final: {:.2f}'.format(nome, media))

    r = input('Deseja calcular outra média? (s/n)').lower()
    if r=='n':
        break
