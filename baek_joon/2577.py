# 2022_03_08
# 숫자의 개수
a = int(input())
b = int(input())
c = int(input())
total = a*b*c
count = [0]*10
for i in str(total):
    count[int(i)] += 1
for i in range(10):
    print(count[i])