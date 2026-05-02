import csv
import matplotlib.pyplot as plt


english_scores = []
with open('score2025s.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        english_scores.append(int(row[1]))  

score_counts = [0]*11  
for score in english_scores:
    if 0 <= score <= 10:
        score_counts[score] += 1

plt.figure(figsize=(10, 6))

bars = plt.bar(range(0, 11), score_counts, color='blue', edgecolor='black')

plt.title('English M25W0149', fontsize=14)
plt.xlabel('score', fontsize=12)
plt.ylabel('histgram', fontsize=12)

plt.xticks(range(0, 11))
plt.xlim(-0.5, 10.5)
plt.ylim(0, max(score_counts) + 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom', fontsize=10)



plt.tight_layout()
plt.subplots_adjust(bottom=0.25)  

plt.savefig('english_histogram.png')  
plt.show()