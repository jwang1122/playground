"""
use ternary statement find minimum value of two numbers
"""

a, b = 10, 20
min0 = min(a, b)
print("07:", min0)

min1 = a if a < b else b
print("10:", min1)

print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a") 

if a != b: 
    if a > b: 
        print("a is greater than b") 
    else: 
        print("b is greater than a") 
else: 
    print("Both a and b are equal") 

min1 = a<b and a or b
print("23:",min1)

# use tuple and test make decision
min2 = (b, a)[a < b]
print("27:", min2)

# use dict and test make decision
min2 = {True: a, False: b}[a < b]
print("31:", min2)

# min5 = (lambda: a, lambda: b)[a > b]()
# print("21:", min5)

min3 = min(34, 56, 74, 23)
print("37:", min3)

t = (3, 7, 2, 67)
print("40:", min(t))

l = [8, 4, 76, 45]
print("43:", min(l))

