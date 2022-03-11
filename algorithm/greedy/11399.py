# 2022_03_11_1
# ATM
# 시간소요가 적은순으로 정렬하여 시간의 합을 최소로 만들어준다.
n = int(input())
time = list(map(int, input().split()))
time.sort()
result = 0

for i in range(n):
    result += time[i]*(n-i)
print(result)


# 아래 같은 방법도 가능
#-------------------------
result = 0

for i in range(1,n):
    time[i] += time[i-1] # 인출 시간 갱신

print(sum(time))