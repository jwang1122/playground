"""
parse covid-19 data
"""
import csv
import matplotlib.pyplot as plt


date1 = []
USConfirmed = []
date2 = []
ChinaConfirmed = []

first = True
with open('data_minimal.csv', 'r') as covid_19:
    reader = csv.reader(covid_19)
    last = ''
    for row in covid_19:
#        print(row)
        line = row.split(',')
        if (line[1] == 'US'):
            date1.append(line[0])
            confirmed = int(line[2])
            USConfirmed.append(confirmed)
        if (line[1] == 'CH'):
            date2.append(line[0])
            confirmed = int(line[2])
            ChinaConfirmed.append(confirmed)
    covid_19.close()

print ((date1))
print ((USConfirmed))
print ((date2))
print ((ChinaConfirmed))

fig=plt.figure()
ax=fig.add_subplot(111)

x = date1
y = USConfirmed
ax.plot(x,y,c='r',marker='*',ls='-',label='US')
ax.plot(date2,ChinaConfirmed,c='g',marker='v',ls='-',label='China')
labels=ax.get_xticklabels()
plt.setp(labels, rotation=90, horizontalalignment='right')
ax.set(xlim=['2020-03-04', '2020-04-04'],xlabel='Date',ylabel='Confirmed',title='Coronavirus Report')
plt.legend(loc=2)
plt.show()