# 2022_03_16_1
# 쉽게 푸는 문제 
a, b = map(int,input().split())
array = []
for i in range(1,b+1):   # 범위 주의
    array.extend([i]*i)
array = array[:b]
print(sum(array[a-1:b]))