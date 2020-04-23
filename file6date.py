"""
parse covid-19 data
"""
import csv

date1 = []

first = True
with open('data_minimal.csv', 'r') as covid_19:
    reader = csv.reader(covid_19)
    last = ''
    for row in covid_19:
#        print(row)
        if first:
            first = False
        else:
            line = row.split(',')
            s = line[0]
            if(s!=last):
                date1.append(s)
                last = s
    covid_19.close()
print(date1)