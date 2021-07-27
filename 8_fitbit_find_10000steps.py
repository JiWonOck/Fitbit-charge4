import csv
import matplotlib.pyplot as plt

f = open('fitbit_daily_steps.csv')
data = csv.reader(f)
next(data)

x_list = []
y_list = []
for row in data:
    date = row[0]
    steps = int(row[1])
    if steps > 10000:
        x_list.append(date)
        y_list.append(steps)
plt.plot(x_list, y_list, 'ro--')
plt.xticks(rotation=90)
plt.show()

