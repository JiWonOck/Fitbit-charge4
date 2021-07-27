import csv  # csv 모듈 불러오기
f = open('seoul.csv', encoding='utf-8')   # seoul.csv 파일 읽기 모드로 불러오기
data = csv.reader(f)
header = next(data)     # 맨 윗줄을 header변수에 저장하기
max_temp = -999         # 최고 기온을 저장할 변수 초기화
max_date = ''           # 최고 기온이었던 날짜를 저장할 변수 초기화
for row in data:
    if row[-1] == '':  # 만약 데이터가 누락되었다면 최고 기온을 -999로 저장
        row[-1] = -999
    row[-1] = float(row[-1])    # 문자열로 저장된 최고 기온 값을 실수로 변환
    if max_temp < row[-1]:      # 만약 지금까지 최고 기온보다 더 높다면 업데이트
        max_date = row[0]
        max_temp = row[-1]
f.close()                        # 파일 닫기
print('기상 관측 아래 서울 최고 기온이 가장 높았던 날은',max_date+'로,',max_temp,'도 였습니다.')  # 출력