# 2022_02_16_1
# 내 학점을 구해줘
# << 오차를 10^-1(0.1)까지 허용하기 때문에 반올림으로 인한 오사오입 문제는 애초에 고려할 필요가 없었다. >>
# 파이썬이 round half to even 방식을 사용함 반올림 하는 숫자가 5일때 반올림 대상 숫자보다 앞선 위치의 숫자가 짝수면 내림, 홀수면 올림 처리(0~4, 6~9는 기존 사사오입 방식과 동일)
# 라운드 함수를 직접구현하거나 다른 방식(decimal 모듈) 사용권장

import decimal
# 산술연산을 위한 환경 불러오기
context = decimal.getcontext()
# 반올림 방식을 사사오입으로 변경
# 오사오입 방식은 decimal.ROUND_HALF_EVEN
context.rounding = decimal.ROUND_HALF_UP

semester_num = int(input())

for _ in range(semester_num):
    total_c = total_g = 0
    for _ in range(int(input())):
        c, g = map(float, input().split(" "))
        total_g += c*g
        total_c += c
    # 소수점 둘째자리에서 반올림
    print(int(total_c), round(decimal.Decimal(total_g/total_c), 1))
    
    # decimal 안쓰고 print(int(total_c), '%.1f'%(total_g/total_c)) =>'%.1f': 자리는 제한 없으나 소수점 1째자리까지 반올림 하여 표현
    # '%.1f'%(total_g/total_c) 두번째 %는 띄어쓰거나 ()괄호 대신 변수명만 기입해도 됨
    # <<<< 자세한건 파이썬 문자열 포맷 확인 >>>>
    # total = total_g/total_c
    # print(int(total_c), '%.1f' % total)