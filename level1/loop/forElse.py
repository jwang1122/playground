for n in range(2, 20):
    for x in range(2, n//2+1):
        if n % x == 0:
            print( n, 'equals', x, '*', int(n/x))
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')