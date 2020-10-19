i = 0

while i<10:
    fruta = input('Digite o nome de uma fruta: ').lower()
    a = fruta.count('a')
    i = fruta.count('i')

    print('{} tem {} vezes a letra a e {} vezes a letra i.'. format(fruta.capitalize(), a, i))

    if i==9:
        r = input('Deseja iniciar novamente? (s/n)')
        if r in 'sim':
            i = 0
    
    i += 1
