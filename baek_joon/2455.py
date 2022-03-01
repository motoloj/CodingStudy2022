# 2022_03_01_1
# 지능형기차
result = 0
passenger_num = []
for _ in range(4):
    out, ride = map(int, input().split())
    result += (ride - out)
    passenger_num.append(result)
print(max(passenger_num))