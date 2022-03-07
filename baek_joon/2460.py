# 2022_03_07_1
# 지능형 기차 2
record = []
passenger = 0
for _ in range(10):
    stop, ride = map(int, input().split())
    calculate = ride-stop
    passenger += calculate
    record.append(passenger)
print(max(record))