# 2022_02_28_1
# 평균
n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
new_score = [i/max_score*100 for i in score]
print(sum(new_score)/n)