# 2022_02_25_1
# 10부제
n = int(input()) % 10
car_list = list(map(int, input().split()))
result = [i for i in car_list if n == i]
print(len(result))
