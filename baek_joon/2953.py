# 2022_03_14_1
# 나는 요리사다
score = []
for _ in range(5):
    score.append(sum(list(map(int, input().split()))))
print(score.index(max(score))+1, max(score))