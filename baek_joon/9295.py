# 2022_02_17_6
# 주사위
n = int(input())
for i in range(n):
    d1, d2 = map(int, input().split())
    print("Case {0}: {1}".format(i+1, d1+d2))