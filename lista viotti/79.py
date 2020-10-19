a = []
b = []

print('Digite 5 valores pares para A:')
x = 0
while x<5:
    y = input()
    a.append(int(y[::]))
    x += 1

print('Digite 5 valores ímpares para B:')
x = 0
while x<5:
    y = input()
    b.append(int(y[::]))
    x += 1

c = []
x = 0
while x<5:
    c.append(a[x])
    c.append(b[x])
    x += 1

print(c)