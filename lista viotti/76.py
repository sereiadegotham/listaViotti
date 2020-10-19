a = []
b = []

print('Digite 6 valores pares para A:')
x = 0
while x<6:
    y = int(input())
    if y%2==0:
        a.append(y)
        x += 1
    else:
        print('Digite apenas valores pares!')

print('Digite 6 valores ímpares para B:')
x = 0
while x<6:
    y = int(input())
    if y%2==0:
        print('Digite apenas valores ímpares!')
    else:
        b.append(y)
        x += 1
print(a)
print(b)

c = []
x = 0
while x<6:
    c.append(a[x])
    x += 1

x = 0
while x<6:
    c.append(b[x])
    x += 1

print(c)