def prime(x):
    flag = True

    for i in range(2, (x//2+1)):
        if(x % i == 0):
            flag = False
            break

    return flag and x != 1

for i in range(2, 20):
    print("prime", i, prime(i))