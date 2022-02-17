# 2022_02_17_1
# 별찍기 8
n = int(input())
for i in range(n):
    print("*"*(i+1)+" "*(2*n-2*(i+1))+"*"*(i+1))
for g in range(n-1, 0, -1):
    print("*"*g+" "*(2*n-2*g)+"*"*g)