"""
scikit-learn 기계학습 패키지를 이용하여 KNN 알고리즘 구현
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# 학습 데이터를 data_fruit.csv 파일로부터 읽는다.
df = pd.read_csv("data_fruit.csv")

# 테스트 데이터 입력
input_data = [(3, 3), (1, 2), (4, 5)]
X_test = pd.DataFrame(input_data)

column_list = ["color", "size"]
X = df[column_list]
Y = df["class"]

# KNN 알고리즘 수행
KNN = KNeighborsClassifier(n_neighbors=3)
KNN.fit(X, Y)
Y_pred = KNN.predict(X_test)

# 결과 출력
kor_name = {'orange':'오렌지', 'grapefruit':'자몽'}
index = 1
for label in Y_pred:
    print(str(index) + "번째 과일은 " + kor_name[label] + "일 가능성이 높습니다.")
    index += 1
