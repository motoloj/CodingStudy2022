# 2022_02_21_2
# 회의실 배정
import sys
n = int(input())
initial_s, initial_e = map(int,input().split())
result = 0
for _ in range(1, n):
    start, end = map(int, input().split())
    if initial_e <= start:
        result += 1
        initial_e = end
print(result)