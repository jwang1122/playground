"""
optimized code
"""
def prime(Number):
    flag = True

    for i in range(2, (Number//2)): #Floor division - division that results into whole number adjusted to the left in the number line
        if(Number % i == 0):
            print("can be divided by", i)
            flag = False
            break

    if (flag and Number != 1):
        print(" %d is a Prime Number" %Number)
    else:
        print(" %d is not a Prime Number" %Number)

prime(43)