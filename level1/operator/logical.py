a,b=10,20

# Logical Operator: and; or; not
c = (a==60) and b==13
print("47:",c)
c = (a==60) and b<13
print("49:",c)
c = (a==60) or (b>15)
print("51:", c)
c = (a<60) or (b>15)
print("53:", c)
c = a and b
print("59:",c)  # Strange result
min1 = a<b and a or b # find which one is smaller
print("61:",min1)
max1 = a>b and a or b # find which one is smaller
print("63:",max1)
c = a or b
print("65:",c)  # Strange result
