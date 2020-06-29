import math 
from my_timer import *

def isPrime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True

def is_prime(n): 
    if n <= 1: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(2, 1 + max_div): 
        if n % i == 0: 
            return False
    return True

def prime(x):
    flag = True

    for i in range(2, (x//2+1)):
        if(x % i == 0):
            flag = False
            break

    return flag and x != 1

@my_timer
def countPrime():
    count = 0
    for n in range(2,100000):
        # if(is_prime(n)):
        # if(prime(n)):
        if(isPrime(n)):
            count += 1
    return count

@my_timer
def SieveOfEratosthenes(n): 
       
    # Create a boolean array "prime[0..n]" and  
    # initialize all entries it as true. A value  
    # in prime[i] will finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n+1)] 
      
    p = 2
    while(p * p <= n): 
           
        # If prime[p] is not changed, then it is  
       # a prime 
        if (prime[p] == True): 
               
            # Update all multiples of p 
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
    c = 0
  
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            c += 1
    return c 

print("Total count ", countPrime())
print(f"Total count of Prime in 100000 is {SieveOfEratosthenes(100000)}")