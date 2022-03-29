# 2022_03_29_1
# N번째 큰 수
for _ in range(int(input())):
    print(sorted(list(map(int, input().split())), reverse=True)[2])
    