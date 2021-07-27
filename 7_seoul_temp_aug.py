import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='utf-8')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '':
        if row[0].split('-')[1] == '03' and row[0].split('-')[2]=='30': # 내 생일
            result.append(float(row[-1]))

plt.plot(result, 'hotpink')
plt.show()
