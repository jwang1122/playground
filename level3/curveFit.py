import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)

np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)

ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data: a=2.5, b=1.3, c=0.5')
# plt.show()

popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata,
         func(xdata, *popt),
         'r-',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
plt.plot(xdata,
         func(xdata, *popt),
         'g--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()