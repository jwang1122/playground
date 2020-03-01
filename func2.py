"""
返回功能块的妙用。
"""
def quadratic(a, b, c):
    return lambda x: a*x**2 + b*x + c

f = quadratic(3, 2, 5)
print("08:", type(f))
print("09:", f(4))

f2 = quadratic(2, 6, 1)
print("12:", f2(4))

def quadratic(a, b, c):
    def f(x):
        return a*x**2 + b*x + c
    return f

f = quadratic(3, 2, 5)
print("20:", f(4))
