# 2022_03_03_1
# 소수 찾기(1을 제외한)
# 1과 자기 자신, 여기선 자기자신을 제외한 범위를 넣었다.
# 1과 자기자신을 제외한 범위에서 나눈수가 나올시 break 하는 것이 횟수가 덜 나올것이다.
n = int(input())
p = list(map(int, input().split()))
prime_count = 0
for i in p:
    count = 0
    for g in range(1,i):
        if i % g == 0:
            count += 1
    if count == 1:
        prime_count += 1
print(prime_count) 

# 에라토스테네스의 체(100까지의)
# 1. 자연수 1제거, 2. 2를 제외한 2의 배수 제거
# 3. 3을 제외한 3의배수, 7을 제외한 7의 배수 제거, 11이상의 소수들의 배수는 11>root(100)이기 때문에 지울 필요가 없다.
n=1000
a = [False,False] + [True]*(n-1) # a의 길이는 1001
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)