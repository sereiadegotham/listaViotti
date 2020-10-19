n = p2 = p4 = p7 = 0

while n<=1000:
    if n%2==0:
        p2 += 1
    if n%4==0:
        p4 += 1
    if n%7==0:
        p7 += 1

    n+= 1

print('No intervalo de 0 a 1000 há {} números divisíveis por 2, {} números divisíveis por 4 e {} divisíveis por 7.'.format(p2, p4, p7))

                
