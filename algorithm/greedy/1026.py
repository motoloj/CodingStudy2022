# 2022_03_09_2
# 보물
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b, reverse=True)
result = 0
for i in range(n):
    result += a[i]*b[i]
print(result)

# b 리스트 재배열  X 조건 => b의 최대값을 뽑아 곱해줌
# >>>>>>>>>>>>