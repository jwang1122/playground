"""
plot sin() wave
"""
import numpy as np
import math
import matplotlib.pyplot as plt

x = np.arange(0, 2*math.pi, 0.1)
y = np.sin(x)
plt.xlabel('Angle')
plt.ylabel('Sin()')
plt.plot(x, y)
plt.show()

samples = 100
w = 3
x = np.arange(samples+1)
y = np.sin(2 * math.pi * w * (x / samples))
plt.xlabel('Sample Rate')
plt.ylabel('Sin()')
plt.plot(x, y)
plt.show()