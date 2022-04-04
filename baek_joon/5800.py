# 2022_04_04_1
# 성적 통계
for i in range(int(input())):
    difference = []
    score = sorted(list(map(int, input().split()))[1:])
    for g in range(len(score)-1):
        difference.append(score[g+1] - score[g])
    print("Class {0}".format(i+1))
    print("Max {0}, Min {1}, Largest gap {2}".format(max(score), min(score), max(difference)))
   