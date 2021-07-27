import csv
f = open('age.csv', encoding='utf-8')
data = csv.reader(f)
result = []
for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            result.append(i)
print(result)