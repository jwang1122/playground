def isEven(n):
    return n % 2 == 0

l = []
for i in range(1,11):
    if     

l = [e for e in range(1,10) if e%2==0]
print("10:",l)

a = range(1, 11)


print(list(filter(isEven, a))) # function with name

print(list(filter(lambda n: n%2==0, a))) #anonymous function
print(list(filter(lambda n: n%3==0, a))) #anonymous function

def f(x):
    return x%2!=0 and x%3!=0

for i in filter(f, range(2,25)):
    print(i)
