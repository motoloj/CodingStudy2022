# 2022_02_21_2
# 회의실 배정
# 그리디 알고리즘 관점으로 생각하면 끝나는 시간에 접근하는 쪽으로 고려
# 끝나는 시간순으로 정렬시도
# => 빨리 끝날수록 뒤에서 고려해볼 회의가 많기 때문이다. 빨리 시작하는 순서대로 정렬을 우선 한다면, 오히려 늦게 끝날 수 있기 때문 (참조)

import sys
n = int(input())
time_list = []
for i in range(n):
    time_list.append(list(map(int, sys.stdin.readline().split())))
time_list.sort(key = lambda x : (x[1], x[0])) # 끝나는 시간 우선 정렬

count = 1
for _ in range(1, n):
    start, end = map(int, input().split())
    if initial_e <= start:
        result += 1
        initial_e = end
print(result)

# 변수.sort() ==> 리스트만 정렬,단순 문자열등은 정렬x 변수원본에 영향, sorted(변수) ==> 모든것 정렬 가능, 원본에 영향을 안줌
# >>> tuple_list = [('좋은하루', 0),
#     	          ('niceday', 1), 
#     	          ('좋은하루', 5), 
#     	          ('good_morning', 3), 
#     	          ('niceday',5)]
                  
# >>> tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능, reverse=True도 역순, x[0]단독 사용시 x[0]기준으로만 정렬
# >>> print(tuple_list)
# [('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]