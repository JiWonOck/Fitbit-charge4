"""
영화 추천 시스템
1. 고객들을 그래프 좌표에 나타내기 위해(또는 고객 사이의 유사도 거리 측정을 위해) 특징을 정의하고 데이터를 추출한다.
2. A라는 고객에게 추천을 하기 위해서는 A와 나머지 고객들 간에 유사도 거리를 계산한다.
3. A와 가장 가까운 K명의 이웃을 찾는다.
4. 만약 K명의 이웃들이 X라는 영화를 높게 평가했다면 X를 A에게 추천하면 된다.
"""

import math
import pandas as pd


def distance(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += (p1[i]-p2[i])**2
    return math.sqrt(total)


# K를 설정
K = 3


# 1. 고객 프로파일 데이터를 data_movie_customer.csv 파일로부터 읽는다.
df = pd.read_csv("data_movie_customer.csv")

# 테스트 데이터 입력
print("### 영화선호도 성향 입력 ###")
comedy = int(input("코메디 (1-5) = "))
action = int(input("액션 (1-5) = "))
drama = int(input("드라마 (1-5) = "))
horror = int(input("공포 (1-5) = "))
romance = int(input("로맨스 (1-5) = "))

test_customer_feature = [comedy, action, drama, horror, romance]

# 2. 고객 간에 유사도 거리 계산
dist_result = []
for index, row in df.iterrows():
    train_customer_id = row['customer']                                             # customer 번호 컬럼을 따로 기억
    train_customer_feature = list(row)[1:]                                          # customer 번호 컬럼은 제외하고 장르별 선호도 값만 취함
    dist = distance(test_customer_feature, train_customer_feature)
    dist_result.append((dist, train_customer_id))

# 3. 가장 가까운 K명의 이웃을 찾는다
dist_result.sort()
closest_k = dist_result[:K]
closest_k_neighbors = [id for dist, id in closest_k]
"""아래 세줄을 위에 한줄로 표현 가능
closet_k_neighbors = []
for dist, id in closet_k:
    closet_k_neighbors.append(id)
"""

# 4. 가까운 이웃들이 가장 좋아한 영화를 찾는다
df = pd.read_csv("data_movie_evaluation.csv")                                       # 영화 평가 데이터를 읽어온다
movie2recommend = df[df.customer.isin(closest_k_neighbors)].sum()[1:].idxmax()          # 이웃들의 총점이 최대인 영화 선택

print("\n추천영화 =", movie2recommend)