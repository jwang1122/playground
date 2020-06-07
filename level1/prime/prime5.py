from prime3 import *

def rangePrime(x,y):
    list1 = []
    for i in range (x,y+1):
        if (prime(i)):
            list1.append(i)
    return list1


print(rangePrime(40,50))