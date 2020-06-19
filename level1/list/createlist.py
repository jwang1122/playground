import math

l = list(range(10))
print(l)

l = [s for s in range(5)]
print(l)

l = [e for e in range(1,10) if e%2==0]
print("10:",l)

t = tuple(range(5))
print(t)

l = "1,21,32,45,12,9".split(',')
print(l)

l = "Texas Comfirmed:120".partition(':')
print(l)

l = [(f,s) for f in ["A","J","Q","K"] for s in ["Spades","Clubs","Hearts","Diamonds"]]
print(l)

x = [(s*0.1) for s in range(0,127)]
y = [math.cos(s) for s in x]
#print(y)

def plot():
    import matplotlib.pyplot as plt

    plt.plot(x,y)

    plt.xlabel('x (angle in radian)')
    plt.ylabel('cos(x)')
    plt.show()

#plot()