# 2022_02_15_4
a = b = 1
while a != 0 and b != 0:
    a, b = map(int, input().split(" "))
    if a == 0 and b == 0:
        break
    print(a+b)