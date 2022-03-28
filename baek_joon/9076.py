# 2022_03_28_1
# 점수 집계
# for _ in range(int(input())):
#     score = list(map(int, input().split()))
#     score.remove(max(score))
#     score.remove(min(score))
#     if max(score) - min(score) >= 4:
#         print('KIN')
#     else:
#         print(sum(score))
# 슬라이싱 사용
for _ in range(int(input())):
    score = sorted(list(map(int, input().split())))
    if score[-2] - score[1] >= 4:
        print('KIN')
    else:
        print(sum(score[1:-1]))