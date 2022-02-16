# 2022_02_16_6
# 별찍기 12
n = int(input())

for i in range(n):
    print(" "*(n-i-1)+"*"*(i+1))
for g in range(n-1, 0, -1):
    print(" "*(n-g)+"*"*(g))