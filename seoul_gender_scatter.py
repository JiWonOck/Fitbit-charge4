import csv
f = open('gender.csv', encoding='utf-8')
data = csv.reader(f)
m = []
f = []
name = input('궁금한 동네를 입력해주세요:')
for row in data:
    if name in row[0]:
        for i in range(3, 104):
            m.append(int(row[i]))       #남성 데이터 저장하기
            f.append(int(row[i+103]))   #여성 데이터 저장하기
        break

import matplotlib.pyplot as plt
plt.scatter(m, f, c=range(101), alpha=0.5, cmap='jet')  #컬러맵 적용
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g')     #추세선 추가
plt.show()