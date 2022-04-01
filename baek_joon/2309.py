# 2022_03_27_1
# 일곱 난쟁이
# 출력 결과 오름차순
# 9C7 = 9C2 = 9*8/2*1 = 36가지, 랜덤?
import random
num = [int(input()) for _ in range(9)]
total = [0]
while sum(total) != 100:
    total = random.sample(num, 7)
print(*sorted(total),sep='\n')
# 전체 값을 더한 상태에서  포문으로 2개값만 빼서 찾는 경우도 있음.