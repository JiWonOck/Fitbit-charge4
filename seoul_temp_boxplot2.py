import csv

f = open('seoul.csv', encoding='utf-8')
data = csv.reader(f)
next(data)
Jan = []
Aug = []

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '01':
            Jan.append(float(row[-1]))
        if row[0].split('-')[1] == '08':
            Aug.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.boxplot([Aug,Jan])
plt.show()