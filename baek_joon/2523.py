# 2022_02_16_7
# 별찍기 13
# 주의) 별 뒤에는 공백이 출력되지 않게 해야된다.
n = int(input())

for i in range(n):
    print("*"*(i+1))
for g in range(n-1, 0, -1):
    print("*"*(g))
