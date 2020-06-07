from pymonad import *

def isEven(x):
    if(type(x) not in [int]):
        reason = ('Error', 'The input value {0} is not an interger.'.format(x))
        return Left(reason)
    if(x % 2 == 0):
        return Right(x)
    reason = ('Error', "The x=%d mod of 2 equals 1." % x)
    return Left(reason)

def add5(x):
    if(x == 0):
        return Left(x)
    return Right(x+5)

def sub4(x):
    return Right(x-4)

print("20:", isEven(3).bind(add5))
print("21:", isEven(4).bind(add5))
print("22:", isEven(5).bind(add5).bind(sub4).value)
print("23:", isEven(4).bind(sub4).bind(add5).bind(sub4).value)
print("24:", (
    isEven(10)
    >> sub4
    >> add5)
    .value)

def f1(x):  # define all things need to do in a chain, if-else still in place of each function
    return isEven(x) >> sub4 >> add5 >> sub4 >> add5

print("33:", f1(11))
print("34:", f1(12))
print("35:", f1(4))
