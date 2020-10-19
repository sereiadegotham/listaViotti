a = b = []

print('Digite 20 valores: ')
x = 0
while x<20:
    y = int(input())
    a.append(y)
    x += 1

print('Digite mais 30 valores: ')
x = 0
while x<30:
    y = int(input())
    b.append(y)
    x += 1

c = []
x = 0
while x<20:
    c.append(a[x])
    x += 1
x = 0
while x<30:
    c.append(b[x])
    x += 1

print(c)