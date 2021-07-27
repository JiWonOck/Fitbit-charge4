import csv
import math
import matplotlib.pyplot as plt

f = open('gender.csv', encoding='utf-8')
data = csv.reader(f)
m = []
f = []
size = []
name = input('궁금한 동네를 입력해주세요 : ')
for row in data:
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i]))
            f.append(int(row[i+103]))
            size.append(math.sqrt(int(row[i]) + int(row[i+103])))
        break

plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
# plt.figure(figsize=(10,5), dpi=300)
plt.title(name + ' 지역의 성별 인구 그래프')
plt.scatter(m, f, s=size, c=range(101), alpha=0.5, cmap='jet')
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g')
plt.xlabel('남성 인구 수')
plt.ylabel('여성 인구 수')
plt.show()