# 2022_02_26_1
# 점수계산
n = int(input())
problem_list = list(map(int, input().split()))
score = 0
result = 0
for i in problem_list:
    if i == 1:
        score += 1
        result += score
    else:
        score = 0
print(result)