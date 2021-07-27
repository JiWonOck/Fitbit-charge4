"""
k-Nearest Neighbors based Anomaly Detection
"""
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# 데이터 읽어오기
df = pd.read_csv("data_fitbit_anomaly.csv")
df = df[['steps', 'bpm']]

# 각각의 점들에서 다른 점들까지의 거리를 구함
# 이때, 특징들의 측정단위가 크게 달라서 거리계산이 어려우므로 정규화 작업 필요
normalized_df = (df - df.min()) / (df.max() - df.min())     # 특징값을 최소값0 최대값1로 정규화
X = normalized_df.values                                    # 인덱스와 컬럼명 처럼 불필요한 부분을 제외한 행렬형태 값만을 이용
nbrs = NearestNeighbors(n_neighbors=3)
nbrs.fit(X)
distance, indexes = nbrs.kneighbors(X)                      # 각각의 점들에서 k개의 이웃들까지의 거리를 계산한 결과 행렬 도출

# # k개 이웃들까지의 평균거리를 라인차트로 표현
# plt.rc('font', family='Malgun Gothic')
# plt.title('kNN 평균거리 차트')
# plt.plot(distance.mean(axis=1))
# plt.xlabel('데이터 인스턴스')
# plt.ylabel('거리(proximity score)')
# plt.show()

# 이상치를 구분짓기 위한 임계점(cutoff)을 설정하고, 임계점을 넘는 이상치 탐지
cutoff = 0.125
outlier_index = np.where(distance.mean(axis=1) > cutoff)        # 행렬에서 평균거리가 cutoff이상인 인덱스 검색
outlier_values = df.iloc[outlier_index]                         # 이상치가 위치한 인덱스의 특징값들을 가져옴

# 결과를 산점도 형태로 출력
plt.rc('font', family='Malgun Gothic')
plt.title('핏빗 데이터 이상치 탐지')
plt.scatter(df['steps'], df['bpm'])
plt.scatter(outlier_values['steps'], outlier_values['bpm'])     # 이상치에 해당하는 특징점들을 다른 색으로 표시
plt.xlabel('걸음수')
plt.ylabel('심박수')
plt.show()
