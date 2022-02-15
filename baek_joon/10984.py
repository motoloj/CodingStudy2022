# 2022_02_15_5
# 파이썬이 round half to even 방식을 사용함 반올림 하는 정수숫자가 짝수면 내림, 홀수면 올림 처리
# 라운드 함수를 직접구현하거나 다른 방식 사용권장
semester_num = int(input())

def new_round():

    return 0

total_c = total_g = 0
for _ in range(semester_num):
    for _ in range(int(input())):
        c, g = map(int, input.split(" "))
        total_g += c*g
        total_c += c
    print(total_c," ",new_round(total_g/total_c))