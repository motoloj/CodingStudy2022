# 2022_03_17_1
# 이진수

for _ in range(int(input())):
    n = bin(int(input()))[2:]
    for j in range(1, len(n)+1):
        if n[-j] == '1':
            print(j-1, end=' ')