import csv
import matplotlib.pyplot as plt

f = open('fitbit_hour_steps_bpm.csv')
data = csv.reader(f)
header = next(f)
x_list = []
y_list = []
color_list = []
for row in data:
    hour = int(row[0].split(' ')[1])
    step = int(row[1])
    bpm = float(row[2])
    x_list.append(step)
    y_list.append(bpm)
    color_list.append(hour)

plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.title('핏빗 데이터 산점도')
plt.scatter(x_list, y_list, c=color_list)
plt.colorbar()
plt.xlabel('걸음수')
plt.ylabel('심박수')
plt.show()

