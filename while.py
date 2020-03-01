a, b = 0, 1
while a < 10:
    print(a+b, end=' ')
    a, b = a+1, a+b
print()

for n in range(10):
    if(n % 2 == 0):
        print(n, end=' ')
print()

for n in range(4, 10, 2):
    if(n % 2 == 0):
        print(n, end=' ')
print()
