# 2022_02_17_3
# 플러그
# n 이 500,000일수도 있어 for문내 input으로 시간초과 => 반드시 반복문안에 input을 sys.stdin.readline()로 대체
import sys

n = int(input())
total_plug = 0
for _ in range(n):
    plug = int(sys.stdin.readline())
    total_plug += plug
print(total_plug-n+1)