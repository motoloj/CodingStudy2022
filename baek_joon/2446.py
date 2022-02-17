# 2022_02_17_2
# 별찍기 9
n = int(input())
for i in range(n):
    print(" "*i+"*"*(2*n-1-2*i))
for g in range(n-1, 0, -1):
    print(" "*(g-1)+"*"*(2*n+-1-2*(g-1)))