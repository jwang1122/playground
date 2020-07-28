from numpy import *
import matplotlib.pyplot as plt

t = arange(0, 52, 0.1)

a = 1
w1 = 3
y = sin(t)
z = a*sin(w1*t)
x = y + z
l = a * cos(0.2*t)
m = x + l

fig=plt.figure()
ax=fig.add_subplot(311)

plt.xlabel('Angle')
plt.ylabel('Sin()')
ax.plot(t, y)

ax=fig.add_subplot(312)
ax.plot(t,z)

ax=fig.add_subplot(313)
ax.plot(t,m)

plt.show()