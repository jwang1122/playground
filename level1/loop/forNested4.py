"""
print a triangle
    1 
   2 2 
  3 3 3 
 4 4 4 4 
  3 3 3
   2 2
    1
"""
def triangle(n):
    for i in range(1, n):
        for k in range(n-1, i, -1):
            print(' ', end='')
        for j in range(i):
            print(i, end=' ')
        print()    
def upsidedown(n):        
    for i in range(n-2, 0, -1):
        for k in range(n-1, i, -1):
            print(' ', end='')
        for j in range(i):
            print(i, end=' ')
        print()

def dimond(n):
    triangle(n)
    upsidedown(n)

#triangle(7)
dimond(8)