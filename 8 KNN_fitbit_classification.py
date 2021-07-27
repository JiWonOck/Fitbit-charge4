"""
KNN 알고리즘을 이용하여 핏빗 사용자 상태분류하기
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# 데이터를 파일로부터 읽는다.
df = pd.read_csv("fitbit_hour_steps_bpm_state.csv")
no_of_records = df.shape[0]                 # 데이터의 레코드 수를 파악
df_train = df[:int(no_of_records*0.8)]      # 데이터 레코드 수의 80%를 학습 용도로 이용
df_test = df[-int(no_of_records*0.2):]      # 데이터 레코드 수의 20%를 테스트 용도로 이용

# 테스트용 데이터 확보
column_list = ["steps", "bpm"]
X_test = df_test[column_list]
Y_actual = df_test["state"]

# 학습용 데이터 확보
X_train = df_train[column_list]
Y_train = df_train["state"]

# KNN 알고리즘 기반 기계학습
KNN = KNeighborsClassifier(n_neighbors=3)
KNN.fit(X_train, Y_train)
Y_predict = KNN.predict(X_test)

# 테스트 데이터에 대한 모델의 예측 정확도 계산
correct_counts = 0
total_counts = 0
for state_predicted, state_actual in zip(Y_predict, Y_actual):
    if state_predicted == state_actual:
        correct_counts += 1
    total_counts += 1
accuracy = correct_counts / total_counts

# 결과출력
print("모델의 예측 정확도는", round(accuracy, 3), "입니다.")
