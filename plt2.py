import matplotlib.pyplot as plt
plt.title('marker')     # 제목 설정
plt.plot([10, 20, 30, 40], 'r', label='circle')  # 빨간색 원형 마커 그래프
plt.plot([40, 30, 20, 10], 'g^', label='triangle up')   # 초록색 삼각형 마커 그래프
plt.legend()    # 범례 표시
plt.show()