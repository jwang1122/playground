import math;

def add(x,y):
    print("%d + %d = %d" % (x,y,x+y))

def sub(x,y):
    print("%d - %d = %d" % (x,y,x-y))

sub(2020,20)
print("2020-20 = ",2020-20)

print("The tens digit of 1296 is", "1296"[-2])

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

    print(s,"in Arabic Numerals is", sum)   

converter("DCLXXVI")
converter("DCLXXXVI")

print(math.gcd(28,21))
print(66 % 4)
import math
print(math.floor((1987+5)/10)*10)

# from math import *
# print(gcd(28,21))