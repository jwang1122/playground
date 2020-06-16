"""
use ternary statement find minimum value of two numbers
"""

a, b = 10, 20
min0 = min(a, b)
print("07:", min0)

min1 = a if a < b else b
print("10:", min1)

print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a") 

# use tuple and test make decision
min2 = (b, a)[a < b]
print("14:", min2)

# use dict and test make decision
min2 = {True: a, False: b}[a < b]
print("18:", min2)

# min5 = (lambda: a, lambda: b)[a > b]()
# print("21:", min5)

min3 = min(34, 56, 74, 23)
print("24:", min3)

t = (3, 7, 2, 67)
print("27:", min(t))

l = [8, 4, 76, 45]
print("30:", min(l))

