# practice 1
for n in range(1, 11):
    if n%2 == 0:
        print(n)

# practice 2
for n in range(1, 11):
    if n%2 == 1:
        print(n)

# practice 3.
for n in range(2,11):
#    print(1/n)
    print("1/%d =%5.2f" % (n, 1/n) )

#practice 4
n = 10
triangular = 0
for i in range(1, n+1):
    triangular += i 
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n*(n+1)/2)

# practice 5
n = 6
f = 1
for i in range(1, n):
    f *= i
print("Factorial of {0} is {1}.".format(n, f))

# practice 6
n = 10
f = 1
for j in range(10, 0, -1):
    for i in range(1,j+1):
        f *= i
    print(f)
    f = 1

# practice 7
n = 10
f = 1
sum = 0
for j in range(1, n+1):
    for i in range(1,j):
        f *= i
    sum += 1/f
    f = 1
print(sum)

# practice 8
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

#practice 9
for i in range(1, 5):
    for k in range(5, i, -1):
        print(' ', end='')
    for j in range(i):
        print(i, end=' ')
    print()

# practice 10
n = 5
for i in range(1, n):
    for k in range(n, i, -1):
        print(' ', end='')
    for j in range(i):
        print(i, end=' ')
    print()
for i in range(n-2, 0, -1):
    for k in range(n, i, -1):
        print(' ', end='')
    for j in range(i):
        print(i, end=' ')
    print()
