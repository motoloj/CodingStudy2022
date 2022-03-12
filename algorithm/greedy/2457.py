# 2022_03_12_1
# 공주님의 정원
# 회의실 배정과 다르게 빨리 끝나면 더 많은 회의, 늦게 꽃이 져야 덜 적게 심는다.
# 아니면 기간이 긴 것 위주 정렬????
import sys
day_30 = [2,4,6,9,11]
day_31 = [1,3,5,7,8,10,12]
flower = [[2, 15, 3, 23], [2, 28, 4, 25], [4, 12, 6, 5], [5, 2, 5, 31], [6, 3, 6, 15], [6, 15, 9, 27], [6, 15, 9, 3], [7, 14, 9, 1], [9, 14, 12, 24], [10, 5, 12, 31]]
n = int(input())
# for _ in range(n):
#     flower.append(list(map(int, sys.stdin.readline().split())))
flower.sort(key= lambda x: (x[0],-x[1],-x[2],-x[3]))
# def m_to_day(m, d):
#     if m in day_30:
#         return 31*m + d
#     elif m in day_31:
#         return 30*m + d
#     else:
#         return 2
# fall_time = [flower[0][2], flower[0][3]]
for 
print(flower)

# 초기 시작 리스트 설정(3.1)

# 다음 구간 도달할 때 마다 범위가 11.30을 초과하는가?