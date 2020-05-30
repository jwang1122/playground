from math import pi

a = lambda r:r**2*pi

print(a(1))
print(a(-2))

for i in range(10):
    x = lambda y: y*y
    print(x(i))