# 2022_03_04_1
# 소수
m = int(input())
n = int(input())
primes = [False, False] + [True] * (n-1) # 자연수 0과 1은 소수가 아니기 때문에 리스트에서 flase로 초기화
k = int(n ** 0.5) # == sqrt(n)

for i in range(2, k+1):
    if primes[i] == True:
        for j in range(i+i, n+1, i):
            primes[j] = False

result = [i for i in range(m, n+1) if primes[i] == True]

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))