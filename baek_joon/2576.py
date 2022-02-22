# 2022_02_22_1
# 홀수
# 첫 줄에 홀수들의 합을, 둘째 줄에 홀수들의 최소값을 출력
# 주) sorted 안에 인자로 저 리스트 컴프리헨션이 안 먹힘
odd_num = [i for i in [int(input()) for _ in range(7)] if i % 2 != 0]
odd_num = sorted(odd_num)
if len(odd_num) == 0:
    print(-1)
else:
    print(sum(odd_num))
    print(odd_num[0])