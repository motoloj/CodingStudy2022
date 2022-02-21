# 2022_02_21_1
# 동전 0
# 동전의 종류들이 서로 배수이기때문에 가장큰순서대로 나눠준다.
n, k = map(int, input().split())
types = []
result = 0
for _ in range(n):
    types.append(int(input()))
types = sorted(types, reverse=True)
for i in types:
    result += (k // i)
    k %= i
print(result)