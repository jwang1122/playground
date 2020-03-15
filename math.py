print("2020-20 = ",2020-20)

print("The tens digit of 1296 is", "1296"[-2])

D=500
C=100
L=50
X=10
V=5
I=1
sum = 0
for i in "DCLXXVI":
    if(i=="D"): sum += D
    if(i=="C"): sum += C
    if(i=="L"): sum += L
    if(i=="X"): sum += X
    if(i=="V"): sum += V
    if(i=="I"): sum += I

print("DCLXVI in Arabic Numerals is", sum)   

# from math import *
# print(gcd(28,21))