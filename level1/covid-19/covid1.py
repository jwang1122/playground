"""
parse covid-19 data New York vs Texas
"""
import csv
import matplotlib.pyplot as plt
from datetime import datetime

date1 = []
newyorkConfirmed = []
newyorkDeath = []
date2 = []
texasConfirmed = []
texasDeath = []

first = True
with open('./data/data_minimal.csv', 'r') as covid_19:
    for row in covid_19:
        if first: # Skip first header line
            first = False
            continue
        line = row.split(',') # split by , comma
        if (line[1]=='US_NY'): # if the second column is US_NY, parse the data
            date1.append(datetime.strptime(line[0], '%Y-%m-%d')) # add date 
            confirmed = int(line[2]) # convert the string to integer (very important)
            newyorkConfirmed.append(confirmed)
            death = line[3].strip() # death could be empty string
            death = int(death) if len(death)>0 else 0 # if it is empty, assign 0
            newyorkDeath.append(int(death))
        if(line[1] == 'US_TX'):
            date2.append(datetime.strptime(line[0], '%Y-%m-%d'))
            confirmed = int(line[2])
            texasConfirmed.append(confirmed)
            death=line[3].strip()
            death = int(death) if len(death)>0 else 0
            texasDeath.append(death)
    

fig=plt.figure()

x = date1
y = newyorkConfirmed
z = newyorkDeath

ax=fig.add_subplot(111)
ax.plot(x,y,c='r',marker='o',ls='-',label='New York')
ax.plot(x,texasConfirmed,c='g',marker='v',ls='-',label='Texas')
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[datetime.strptime('2020-03-04','%Y-%m-%d'),datetime.strptime('2020-04-04','%Y-%m-%d')], xlabel='Date', ylabel='Confirmed',
       title='Coronavirus Report')

#ax.locator_params(axis='y', nbins=9)

plt.legend(loc=2)
plt.show()
