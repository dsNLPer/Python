import csv


math_scores = []
with open('score2025s.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        math_scores.append(int(row[2])) 

print("数学の点数リスト:", math_scores)

total = sum(math_scores)
average = total / len(math_scores)

print(f"数学の合計点: {total}")
print(f"数学の平均点: {average:.2f}")