a = []
b = []

print('Digite 5 valores pares para A:')
x = 0
while x<5:
    y = int(input())
    a.append(y)
    x += 1

print('Digite 5 valores ímpares para B:')
x = 0
while x<5:
    y = int(input())
    b.append(y)
    x += 1

c = []
x = 0
while x<5:
    c.append(int(a[x] + b[x]))
    x += 1

print(c)