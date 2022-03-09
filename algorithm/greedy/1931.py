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
time_list.sort(key = lambda x : (x[1], x[0])) # 끝나는 시간 우선 정렬후 시작 시간순으로 정렬(작은순, 오름차순)

count = 1 # 처음 시간은 무조건 회의실에 배정(시간정렬을 가장빨리 끝나고 가장 처음시작해서)포문이 2번째 즉, 인덱스상 1번부터 돌기 때문에 카운트를 미리 1처리
initial_e = time_list[0][1] #가장 빨리 끝나는 시간에서 빠른 시작시간
for i in range(1, n):
    if initial_e <= time_list[i][0]:
        initial_e = time_list[i][1]    # 다음 배정할 회의시간의 끝나는 시간을 엔드 타임 초기값으로 변경
        count += 1
print(count)

# 변수.sort() ==> 리스트만 정렬,단순 문자열등은 정렬x 변수원본에 영향, sorted(변수) ==> 모든것 정렬 가능, 원본에 영향을 안줌
# >>> tuple_list = [('좋은하루', 0),
#     	          ('niceday', 1), 
#     	          ('좋은하루', 5), 
#     	          ('good_morning', 3), 
#     	          ('niceday',5)]
                  
# >>> tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능, reverse=True도 역순, x[0]단독 사용시 x[0]기준으로만 정렬
# >>> print(tuple_list)
# [('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]
