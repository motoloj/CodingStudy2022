# 2022_02_16_3
# 별찍기 5
n = int(input())
for i in range(n):
    print(i)
    print(n-(i+1))
    print(" "*(n-(i+1))+"*"*(2*(i+1)-1))
# 주)print 내 +는 공백없이 이어서 출력 ,(반점)으로 구분시 공백으로 이어서 출력