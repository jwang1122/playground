import math
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(b * x) + c

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2020, 7, 11)

df = web.DataReader("AAPL", 'yahoo', start, end)
data = df.get("Adj Close")
print(type(data)) # pandas.core.series.Series
print(len(data))
print(data)
samples = 1390
xdata = np.arange(samples)/samples
yData = []
for d in data:
    yData.append(d)
popt, pcov = curve_fit(func, xdata, yData)
print(popt)
fig=plt.figure()
#ax=fig.add_subplot(211)
# ax=fig.add_subplot(212)
plt.plot(xdata, yData, label="Real Data")

center = 0.674
half_width = 0.01
altitude = 100
expA = 100
center2 = 0.73
center3 = 0.926
center4 = 0.943
half_width1 = 0.004
altitude2 = 400
z1 = altitude*(1.0/(math.e**(expA*(xdata-center-half_width))+1.0) - 1/(math.e**(expA*(xdata-center+half_width)) + 1.0))
z2 = altitude*(1.0/(math.e**(expA*(xdata-center2+half_width)) + 1) - 1.0/(math.e**(expA*(xdata-center2-half_width)) + 1.00))
z3 = altitude2*(1.0/(math.e**(expA*(xdata-center3-half_width1))+1.0) - 1/(math.e**(expA*(xdata-center3+half_width1)) + 1.0))
z4 = altitude2*(1.0/(math.e**(expA*(xdata-center4+half_width1)) + 1) - 1.0/(math.e**(expA*(xdata-center4-half_width1)) + 1.00))
plt.plot(xdata,
         func(xdata, *popt) + z1 + z2 + z3 + z4,
         'r--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.plot(xdata, z1 + z2 + z3 + z4)
plt.legend()
plt.show()
"""
High         float64
Low          float64
Open         float64
Close        float64
Volume       float64
Adj Close    float64
dtype: object
"""