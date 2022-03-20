# 2022_03_20_1
# 주차의 신
for _ in range(int(input())):
    n = int(input())
    store = list(map(int, input().split()))
    print((max(store) - min(store))*2)