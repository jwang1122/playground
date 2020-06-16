def prime(x):
    for i in range(2, (x//2+1)):
        if(x % i == 0):
            break
    else:
        return x!=1
    return False

for i in range(1, 20):
    print("prime", i, prime(i))