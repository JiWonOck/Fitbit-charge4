import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='utf-8')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))

plt.hist(result, bins=100, color='r')
plt.show()