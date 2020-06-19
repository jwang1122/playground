"""
Readability is higher, but more code compare to prime4.py
"""
def prime(x):
    flag = True

    for i in range(2, (x//2+1)):
        if(x % i == 0):
            flag = False
            break

    return flag and x != 1

if __name__ == '__main__':
    for i in range(0, 20):
        print("prime", i, prime(i)) 