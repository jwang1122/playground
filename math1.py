import math;

def add(x,y):
    print("%d + %d = %d" % (x,y,x+y))

def addList(x):
    sum = 0;
    result = "";
    for s in x:
        sum += s
        result += str(s) + '+'
    result = result[:len(result)-1]
    print(f"{result}={sum}")
    
    # for v in x:
    #     sum += v
    #     print(v, end="+")
    # print("=%d" %sum)

    # result = ""
    # size = len(x)
    # for i in range(size):
    #     sum += x[i]
    #     if (size-1==i):
    #         result += str(x[i])
    #     else:
    #         result += (str(x[i]) + "+")
    # print(f"{result}={sum}")

def sub(x,y):
    print("%d - %d = %d" % (x,y,x-y))


def converter(s):
    D=500
    C=100
    L=50
    X=10
    V=5
    I=1
    sum = 0
    for i in s:
        if(i=="D"): sum += D
        if(i=="C"): sum += C
        if(i=="L"): sum += L
        if(i=="X"): sum += X
        if(i=="V"): sum += V
        if(i=="I"): sum += I

def prime(x):
    """
    Any natural number that is not divisible by any other number 
    except 1 and itself called Prime Number in Python.

    return True if x is a prime number, return False otherwise.
    """
    flag = True

    for i in range(2, (x//2 + 1)):
        if(x % i == 0):
            flag = False
            break

    return flag and x != 1

def rangePrime(x,y):
    """
    return list of prime numbers between x and y.
    """
    list1 = []
    for i in range (x,y+1):
        if (prime(i)):
            list1.append(i)
    return list1