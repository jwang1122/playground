a = range(1, 11)

def isEven(n):
    return n % 2 == 0

print(list(filter(isEven, a))) # function with name

print(list(filter(lambda n: n%2==0, a))) #anonymous function
print(list(filter(lambda n: n%3==0, a))) #anonymous function

def f(x):
    return x%2!=0 and x%3!=0

for i in filter(f, range(2,25)):
    print(i)
