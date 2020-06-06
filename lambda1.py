from func import *

y = f(4)
print("05:", y)

f1 = lambda x: 3*x + 2 #assign function name to lambda expression
print(f"08:", f1(4))
#传递功能块的例子
print("10:",ff(lambda x: 3*x + 2, 4))
print("11:",ff(lambda x: 1*x**2 + 2*x + 1, 1))
print("12:",ff(lambda x: 2*x**2 + 1*x + 2, 4))
# 看起来似乎有脱了裤子放屁之嫌，实则开启了一个功能块管理功能块的编程思想。

#返回功能块的例子
def build_quatratic_function(a, b, c):
    return lambda x: a*x**2 + b*x + c

f2 = build_quatratic_function(3, 5, 7)
print('20:',type(f2))
print("21:", f2(2))

# map lambda function to each city-temperature data
temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26),("Tokyo", 27),("New York", 28),("London", 22),("Beijing", 32)]
list1=list(map(lambda data: (data[0], round(9/5*data[1] + 32, 2)), temps))
print("25:",list1)

print("28:",ff2(lambda x,y: 3*x + 2*y, 4, 6))