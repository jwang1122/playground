

import datetime
import pandas_datareader.data as web
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2020, 7, 11)
#end = datetime.datetime(2020, 7, 20)
#end = datetime.datetime(2020, 7, 23)

df = web.DataReader("AAPL", 'yahoo', start, end)
# print(df.head())
# print(df.tail())

#The Moving Average makes the line smooth 
#and showcase the increasing or decreasing trend of stocks price.
#Let’s start code out the Rolling Mean (Moving Average) — to determine trend
win = 20
close_px = df['Adj Close']
mavg = close_px.rolling(window=win).mean().shift(-10)
#print(mavg)

mpl.rc('figure', figsize=(8, 7))
#mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.ylabel("Adjusted Close Value")
plt.title('Apple stock 20 Days Rolling Average')
plt.legend()
plt.show()