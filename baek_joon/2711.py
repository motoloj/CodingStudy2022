# 2022_03_13
# 오타맨 고창영
# 
from sympy import re


n = int(input())
for _ in range(n):
    remove, s = input().split()
    s = list(s) # 문자를 리스트로 변환하면 한 글자 씩 변환
    del s[int(remove)-1] # del 예약어라 함수랑 같이 못쓰며 인덱스 위치를 한 칸 띄고 쓴다.
    print("".join(s))

# 슬라이싱 방법
n = int(input())
for _ in range(n):
    remove, s = input().split()
    remove = int(remove)
    print(s[:remove-1],s[remove:], sep='')