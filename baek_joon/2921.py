# 2022_02_17_8
# 도미노
# 순열, 조합(수학)으로 접근? // ex) 도미노 [2/8]와 도미노[8/2]는 동일-> 중복처리
# if n = 3일때 순서쌍 생성
# for i in range(n+1): for g in range(i, n+1): 중복 없는 순서쌍 만드는 반복문, g를 0부터가 아닌 이미 만들어진 i부터 시작
# 0 - 0 1 2 3/ 1- 1 2 3 /2- 2 3/ 3 - 3
n = int(input())
total_dot = 0

for i in range(n+1):
    for g in range(i, n+1):
        total_dot += i+g
            
print(total_dot)