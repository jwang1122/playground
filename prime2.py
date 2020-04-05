Number = 5
flag = True

for i in range(2, (Number//2)): #Floor division - division that results into whole number adjusted to the left in the number line
    if(Number % i == 0):
        flag = False
        break

if (flag == 0 and Number != 1):
    print(" %d is a Prime Number" %Number)
else:
    print(" %d is not a Prime Number" %Number)
