def prime(x):
    flag = True

    for i in range(2, (x//2)):
        if(x % i == 0):
            flag = False
            break

    return flag and x != 1

# number = 7
# print(prime(number))