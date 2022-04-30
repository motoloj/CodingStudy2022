# 2022_04_30_1
# 주사위 게임
c_score = 100
s_score = 100
for _ in range(int(input())):
    score1, score2 = map(int, input().split())
    if score1 > score2:
        s_score -= score1 
    elif score1 < score2:
        c_score -= score2
    else:
        pass
print(c_score, s_score, sep='\n')