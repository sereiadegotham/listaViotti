print('---------------------------REALIZE UMA OPERÇÃO----------------------------')
n1 = float(input('Digite o primeiro número: '))
op = input('Informe o operador (+, -, *, /): ')
n2 = float(input('Digite o segundo número: '))

if op=='+':
    r = n1 + n2
elif op=='-':
    r = n1 - n2
elif op=='*':
    r = n1 * n2
elif op=='/':
    r = n1 / n2
else:
    r = 'I'

print('{} {} {} = {}'.format(n1, op, n2, r) if r!='I' else 'Operador Inválido')
