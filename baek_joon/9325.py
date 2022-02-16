# 2022_02_16_8
# 얼마?
# 가끔 시간초과로 input 대신 import sys // sys.stdin.readline()사용
# 테스트 케이스 input 사용무방, 반복문으로 여러줄 입력 받을때는 readline 사용
n = int(input())

for _ in range(n):
    price = int(input())
    option = int(input())
    for _ in range(option):
        q, p = map(int, input().split(" "))
        price += q*p
    print(price)