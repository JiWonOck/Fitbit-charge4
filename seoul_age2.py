import csv
import matplotlib.pyplot as plt

f = open('age.csv', encoding='utf-8')
data = csv.reader(f)
result = []
dong = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요 : ')
#이게 맞나 모르겠음
for row in data:
    if dong in row[0]:
        for i in row[3:]:
            result.append(i)
plt.style.use('ggplot')
plt.plot(result)
plt.show()