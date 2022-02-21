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
# -----------------------------------------------------------------------------------------------------
# 실전문제: 큰 수의 법칙(가장 큰수와 2번째로 큰 수 활용)
# n = 배열크기, m = 숫자가 더해지는 횟수, k = 숫자를 연속해서 사용할수 있는 횟수
# 케이스 1: 큰 수와 두번째로 큰 수가 같을때 => m번 만큼 더해주면(m을 곱해주면)된다. '4+4+4'+4+'4+4+4'
# 케이스 2: ""      ""              다를때 => 큰 수를 k번 만큼 더해주고 두번째로 큰수를 한번만 더해주고 다시 큰 수를 k번(m번에 도달할 때 까지 반복) 5+5+5+4+5+5+5 


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

# 해설지 유사 구현(단순구현, 시간초과 고려X)
# 1번째 for문에서 m=0일때 for문 탈출->for문이랑 같은 줄에 있는 if에서 m=0이기 때문에 while 탈출 
# n, m, k = map(int, input().split())
# array = list(map(int, input().split()))
# array = sorted(array, reverse=True)
# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += array[0]
#         m -= 1
#     if m == 0:
#         break
#     result += array[1]
#     m -= 1
# print(result)

# m의 크기가 엄청 클 때 고려
# n, m, k = map(int, input().split())
# array = list(map(int, input().split()))
# array = sorted(array, reverse=True)

# # 가장 큰 수가 더해지는 횟수
# # ex) 5 8 3 = n,m,k // 수열 2 4 5 4 6 // 6 6 6 5라는 수열이 반복됨 => k+1가 길이, m/(k+1)이 반복횟수
# #    m > k+1일때 반복 횟수 | m< k+1일때 반복횟수(m % (k+1))== 나머지 횟수경우 고려 
# count = int(m/(k+1)) * k + (m % (k+1))
# # 수열의 계산순서는 결과에 영향을 주지않는다.(6+6+6+5+6+6+6 = 6+6+6+6+6+6+5)
# result = count * array[0] + (m-count) * array[1]
# print(result)
#-------------------------------------------------------------------------------------------------------
# # 2022_02_20_1
# # 숫자 카드 게임
# # n행 m열 카드에서 선택행에서 가장 작은수가 크면 이기는 게임(행에서 가장 작은수들 중 큰 수를 출력)
# n, m = map(int, input().split())
# card_list =[]
# for _ in range(n):
#     card_list.append(min(map(int, input().split())))
# print(max(card_list))

# # 해설 유사 구현
# # 이중 포문과 min_value에 큰값을 부여해 구현하는 방법도 있다.
# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#     card_list = list(map(int, input().split()))
#     min_value = min(card_list)
#     result = max(result, min_value)
# print(result)
#-------------------------------------------------------------------------------------------------------------
# 2022_02_20_2
# 1이 될 때 까지
# n = 수, k = 나누는 수
# 1. n에서 1을 뺀다. 2.n을 k로 나눈다(나누어 떨어질때만) 둘중하나 반복
# 횟수를 줄이기 위해 우선적으로 나눠지는게 많이 되도록 수행한다.
# 최적해가 보장되있나?=> k가 2이상이면 나누는게 더 유리하다.
n, k = map(int, input().split())
count = 0
while n != 1:
    if k > 1 and n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1
print(count)  
# 다른 방법 1
# 이중 while로 n이 k이상, n이 k로 나눈 나머지가 0일때 까지 반복(n=n-1, 카운트 포함)
# 안쪽 while과 같은 줄 n//k 과 카운트 포함
# 이중 while과 같은 줄에 새 while(n<k)에 n-=1과 카운트
# 방법 2
# n이 수가 클 때, n이 k의 배수가 되도록 효율적으로 한번에 빼는 법
n, k = map(int, input().split())
result = 0

# ex) n = 17, k = 5
while True:
    # 나누어 떨어질때까지 1씩 빼기
    # 15 = (17 // 5) * 5
    # 2회차: 0 = 3//5 * 5
    target = (n // k) * k
    # 0->2 += 17-15
    # 나누어지는 구간도달 까지 1씩 차감된 횟수
    # >>> 단!!, n<k 구간에서 break걸리기전 n<k인 n의 횟수만큼 result에 증가, 원래는 n<k일때는 n-1만큼 카운트
    # ===> n<k일때 n만큼 연산횟수를 카운트 한거는 n이 0되는 연산이기 때문 n-1만큼 연산해야 n<k일때 n이 1까지 도달
    # ex) n=3 k=5일때 => 3->2->1->0 3번==n번 3->2->1 2번 == n-1번 
    # 추가 카운트로 인해 맨 마지막에서 카운트-1
    # 2회차: 2-> 5 = 3 - 0
    result += (n-target)
    # 15 = 15
    # 2회차: 3 = 3
    n = target
    # n<k 나눌수 없을 때 while 반복문 탈출
    if n < k:
        break
    # k로 나누기(딱 나누어지는 시기에만 들어옴)
    # 2-> 3 += 1
    # 나눈 횟수(1회) 증감
    result += 1
    # (n:15 -> 3) //= 5
    n //= k

# 남은 수에 1씩 빼기
# n<k일 때 break 걸리기전 n은 0이기 때문에 result에 -1이 더해진다.
result += (n-1)
print(result)
#--------------------------------------------------------------------
# 정리
# 1. 처음 나누어 떨어질때까지 1씩 빼기(타겟) 17->15거나 n < k일때는 n이 0에 도달(=타겟)
# 2. 나누어지는 구간도달 혹은 n<k일때 n이 0까지 가는 1씩 차감된 횟수를 카운트 증가
# => n > k일때: n(원래 수) - (-1씩차감후 첨으로 나눠떨어지는 곳) = 구간도달까지의 차감 횟수
# => n < k일때: n(남은 수) -  (0이 타겟) = n(0까지 도달하는 남은 수이기 때문에 맨 마지막에서 -1더하기)
# 3. n < k 검사 break 반복탈출
# 4. 나누는 조건을 만족해서 나누고 나눈 카운트를 증가
#  <<<<    [n < k] 까지 1~4 반복 >>>>>>
# 5. n < k일때 2번에서 처리된 +1된 카운트를 -1 해주고 결과 출력
# => 전자(3->2->1->0: 3번),후자(3->2->1:2번) n<k일때 0번까지 도달하는 카운트로 증가하기때문에(전자) 정상적인 후자로 처리하기위해 -1를 하고 출력한다.