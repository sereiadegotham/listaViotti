while True:
    texto = input('Digite um texto de até 60 caracteres: ')

    if len(texto)>60:
        print('Texto muito grande!\n')
    else:
        break
n = int(input('Digite o número da caractere a partir do qual deseja ver o texto: '))
print(texto[n:])

n = int(input('Digite a quantidade de caracteres que deseja ver do texto: '))
print(texto[:n], '\n')
print('Inversão:\n')
print(texto[n::-1]) 
