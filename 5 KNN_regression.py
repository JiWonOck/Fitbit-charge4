import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

# 학습 데이터를 data_bread_sales.csv 파일로부터 읽는다.
df = pd.read_csv("data_bread_sales.csv")

# 테스트 데이터 입력
feature1 = int(input("날씨 상태 (1-5) = "))
feature2 = int(input("휴일 여부 (0, 1) = "))
feature3 = int(input("스포츠 경기 여부 (0, 1) = "))
test = [feature1, feature2, feature3]


column_list = ['weather', 'weekend', 'sports']
X = df[column_list]
Y = df['sales']

# KNN 알고리즘 수행
KNN = KNeighborsRegressor(n_neighbors=4)
KNN.fit(X, Y)
Y_pred = KNN.predict([test])

# 결과 출력
print("오늘은 빵을 ", int(Y_pred), "개 만들면 될 것 같습니다.")











