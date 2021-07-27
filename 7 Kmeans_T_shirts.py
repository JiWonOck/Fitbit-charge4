"""
사람별로 체형 특징(상체길이, 가슴둘레)을 조사하여 클러스터링하여 3가지 분류(대중소) 결과와 분류 기준을 발견
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 클러스터링할 데이터 불러오기
df = pd.read_csv("data_body_chest.csv")

# K-means 클러스터링 수행
kmeans = KMeans(n_clusters=3, random_state=1)
kmeans.fit(df)

# 찾은 클러스터 중심점 좌표 출력
print("클러스터별 Centroid")
print(kmeans.cluster_centers_)

# 클러스터 결과를 그래프로 출력
df['category'] = kmeans.labels_
df.plot.scatter(x='body', y='chest', c='category', colormap='viridis')
plt.show()
