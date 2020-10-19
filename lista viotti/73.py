data = input('Digite uma data no formato dd/mm/aaaa: ')
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

if dia<1 or dia>31:
    print('Dia inválido!')
if mes<1 or mes>12:
    print('Mês inválido!')

print('{}/{}/{}'.format(dia, mes, ano))