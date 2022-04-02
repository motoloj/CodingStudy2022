# 2022_04_01_1
# 백설공주와 일곱 난쟁이
# 브루트포스 알고리즘(전체탐색, 모든 조합 찾기)
# import random

# hat = [int(input()) for _ in range(9)]
# total = [0]
# while sum(total) != 100:
#     total = random.sample(hat, 7)
# print(*total, sep='\n')

#----------------------------
hat = [int(input()) for _ in range(9)]
total = sum(hat)
for i in range(len(hat)-1):
    for g in range(i+1, len(hat)):
        cal = total - hat[i] -hat[g]
        if cal == 100:
            fake1 = hat[i]
            fake2 = hat[g]
            break
            
hat.remove(fake1)
hat.remove(fake2)
print(*hat, sep='\n')