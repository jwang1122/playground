import math
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(b * x) + c

    
start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2020, 8, 7)

df = web.DataReader("AAPL", 'yahoo', start, end)
data = df.get("Adj Close")
print(len(data))
samples = 5183
xdata = np.arange(samples)/samples
yData = []
for d in data:
    yData.append(d)

popt, pcov = curve_fit(func, xdata, yData)
plt.plot(xdata,
         func(xdata, *popt),
         'r--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.plot(xdata, yData,label="Real Data")
plt.legend()
plt.show()