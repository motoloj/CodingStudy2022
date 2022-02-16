# 2022_02_16_5
# 별찍기 7
n = int(input())

for i in range(n):    
    print(" "*(n-i-1)+"*"*((2*i)+1))
for g in range(n-1, 0, -1):
    print(" "*(n-g)+"*"*((2*g)-1))
