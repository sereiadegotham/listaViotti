print('Digite os limites de um intervalo de valores: ')
a = int(input('Limite inferior: '))
b = int(input('Limite superior: '))

if b<a:
    c = a
    a = b
    b = c
print('{} e {}'.format(a, b))

c = a
m2 = m3 = m4 = s2 = s3 = s4 = 0
while c<=b:
    if c%2==0:
        m2 += 1
        s2 += c
    if c%3==0:
        m3 += 1
        s3 += c
    if c%4==0:
        m4 += 1
        s4 += c
    c += 1

print('No intervalo digitado há {} múltiplos de 2 somando {}, {} múltiplos de 3 somando {} e {} múltiplos de 4 somando {}.'.format(m2, s2, m3, s3, m4, s4))