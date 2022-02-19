# 2022_02_19_1
# 예제 3-1 거스름돈
# 큰 돈 부터 거슬러준다(동전 종류가 서로 배수이기 때문에)
# 만약 500, 400, 100일때 800원을 거슬러준다면 500+100+100+100이 아닌 400+400 2개가 최적해
# n = int(input())
# coin = 0
# coins = [500, 100, 50, 10]
# for i in coins:
#     coin += n // i
#     n %= i
# print(coin)

# 실전문제: 큰 수의 법칙(가장 큰수와 2번째로 큰 수 활용)
# n = 배열크기, m = 숫자가 더해지는 횟수, k = 숫자를 연속해서 사용할수 있는 횟수
# 케이스 1: 큰 수와 두번째로 큰 수가 같을때 => m번 만큼 더해주면(m을 곱해주면)된다. '4+4+4'+4+'4+4+4'
# 케이스 2: ""      ""              다를때 => 큰 수를 k번 만큼 더해주고 두번째로 큰수를 한번만 더해주고 다시 큰 수를 k번(m번에 도달할 때 까지 반복) 5+5+5+4+5+5+5 
from sympy import re


# n, m, k = map(int, input().split())
# # array = [map(int, input().split())] 이런식으로는 list가 아닌 [ map 주소값] 객체로 생성
# array = list(map(int, input().split()))
# array = sorted(array, reverse=True)
# result = 0
# count = 0
# if array[0] == array[1]:
#     result += array[0]*m
# else:
#     for i in range(1,m+1):
#         if count < k:
#             result += array[0]
#             count += 1
#         else:
#             result += array[1]
#             count = 0    
# print(result)  

# 해설지 유사 구현
# 1번째 for문에서 m=0일때 for문 탈출->for문이랑 같은 줄에 있는 if에서 m=0이기 때문에 while 탈출 
n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array = sorted(array, reverse=True)
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += array[0]
        m -= 1
    if m == 0:
        break
    result += array[1]
    m -= 1
print(result)