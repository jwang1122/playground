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
for i in range(1, 5):
    for k in range(4, i, -1):
        print(' ', end='')
    for j in range(i):
        print(i, end=' ')
    print()    
for i in range(3, 0, -1):
    for k in range(4, i, -1):
        print(' ', end='')
    for j in range(i):
        print(i, end=' ')

    print()
