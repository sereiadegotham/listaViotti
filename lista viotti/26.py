sexo = input("Informe o sexo (M/F): ").lower()

if sexo in 'masculino':
    print("Sexo masculino.")
elif sexo in 'feminino':
    print('Sexo feminino.')
else:
    print('Não binário.')
