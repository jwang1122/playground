"""
parse covid-19 data
"""
import csv
import matplotlib.pyplot as plt

date1 = []
newyorkConfirmed = []
date2 = []
texasConfirmed = []

first = True
with open('data_minimal.csv', 'r') as covid_19:
    reader = csv.reader(covid_19)
    last = ''
    for row in covid_19:
#        print(row)
        line = row.split(',')
        if (line[1] == 'US_NY') :
            date1.append(line[0])
            confirmed = int(line[2])
            newyorkConfirmed.append(confirmed)
        if (line[1] == 'US_TX') :
            date2.append(line[0])
            confirmed = int(line[2])
            texasConfirmed.append(confirmed)
    covid_19.close()

# print(len(date1))
# print(len(newyorkConfirmed))
# print(len(date2))
fig=plt.figure()
ax=fig.add_subplot(111)

x = date1
y = newyorkConfirmed
ax.plot(x,y,c='r',marker=(8,2,0),ls='-',label='New York')
ax.plot(date2,texasConfirmed,c='g',marker='v',ls='-',label='Texas')
labels = ax.get_xticklabels()
plt.setp(labels, rotation=90, horizontalalignment='right')
ax.set(xlim=['2020-03-15','2020-04-04'], xlabel='Date', ylabel='Confirmed',
       title='Coronavirus Report')
plt.legend(loc=2)
plt.show()