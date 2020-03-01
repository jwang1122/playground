# practice 1.
for n in range(2,11):
#    print(1/n)
    print("1/%d =%5.2f" % (n, 1/n) )

#practice 2
n = 10
triangular = 0
for i in range(1, n+1):
    triangular += i 
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n*(n+1)/2)

# practice 3
n = 6
f = 1
for i in range(1, n):
    f *= i
print("Factorial of {0} is {1}.".format(n, f))