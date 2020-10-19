a = []
b = []

print('Digite 20 valores para A:')
x = 0
while x<20:
    y = int(input())
    a.append(y)
    x += 1

print('Digite 20 valores para B:')
x = 0
while x<20:
    y = int(input())
    b.append(y)
    x += 1

c = []
x = 0
while x<20:
    c.append('{} + {} = {}'.format(a[x], b[x], a[x]+b[x]))
    print(c[x])
    x += 1