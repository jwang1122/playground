"""
plot sin() wave
"""
import numpy as np
import math
import matplotlib.pyplot as plt

samples = 1000
a = .3
x = np.arange(samples+1)
y = a* np.exp(10* x/samples) + 1
plt.xlabel('Sample Rate')
plt.ylabel('exp(x)')
plt.plot(x, y)
plt.show()