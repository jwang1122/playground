from pymonad import *

def isEven(x):
    if(x % 2 == 0):
        reason = ('Success',"The x=%d mod of 2 is 0." % x)
        return Right(reason)
    reason = ('Error',"The x=%d mod of 2 equals 1." % x)
    return Left(reason)

def parser(reason):
    print(reason.getValue()[0]) # Open wrapper box by myself.
    print(reason.getValue()[1])

y = 4
response = isEven(y)
parser(response)
y = 7
response = isEven(y)
parser(response)
