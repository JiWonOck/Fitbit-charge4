import csv

f = open('seoul.csv', encoding='utf-8')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.boxplot(result)
plt.show()