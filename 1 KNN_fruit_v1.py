import math

def distance(x1, x2, y1, y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist

# 학습 데이터
data_fruit = [(3, 1, "오렌지"), (3, 4, "자몽"), (3, 5, "자몽"), (4, 4, "자몽"), (2, 2, "오렌지"), (1, 2, "오렌지")]

# K 설정
K = 3

# 테스트 데이터 입력
test_color = int(input("색상을 입력하세요 (1-5) = "))
test_size = int(input("크기를 입력하세요 (1-5) = "))


# 1. 학습 데이터 안에 있는 모든 아이템들과의 거리를 계산하여 결과를 dist_result 리스트에 담는다
dist_result = []
for fruit in data_fruit:
    train_color, train_size, train_label = fruit

    x1 = test_size
    y1 = test_color
    x2 = train_size
    y2 = train_color

    dist = distance(x1, x2, y1, y2)
    dist_result.append((dist, train_label))


# 2. 거리 기준으로 테스트 케이스와 가장 가까운 K개의 이웃을 찾는다. (dist_result 리스트를 정렬하여 상위 K를 선택)
dist_result.sort()
top_k = dist_result[:K]


# 3. 찾은 이웃들에서 다수의 분류값을 도출
o_count = 0
g_count = 0
for dist, label in top_k:
    if label == "오렌지":
        o_count += 1
    else:
        g_count += 1

if o_count > g_count:
    print("해당 과일은 오렌지일 가능성이 높습니다")
else:
    print("해당 과일은 자몽일 가능성이 높습니다")











