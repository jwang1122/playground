"""
parse covid-19 data
"""
import csv

list1 = []

first = True
with open('data_minimal.csv', 'r') as covid_19:
    reader = csv.reader(covid_19)
    for row in covid_19:
        if first:
            first = False
        else:
            line = row.split(',')
            s = line[0]
            list1.append(s)
    covid_19.close()
print(list1)