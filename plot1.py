import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6.3, 0.1)
x = ['2019-12-31','2020-01-01','']
y = np.sin(x)
plt.xlabel('Angle')
plt.ylabel('Sin()')
plt.plot(x, y)
plt.show()