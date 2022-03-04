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
# 맨앞의 false는 0부분 두번째 false 1, 첫 true 2
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)

# 에라토스테네스의 체 2(원본 코드는 n미만의 소수를 찾아서 두번째 포문과 sieve리스트 초기화, 리턴 포문 범위가 n+1이 아닌 n 이었다.)
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주) => 리스트가 0부터 시작하기 때문에 리스트 맨 처음을 0으로 간주하고  n개요소의 소수를 찾을려면 리스트 길이가 n+1 필요
    # => 리스트 길이는 n+1이나 이는 요소가 0부터 시작해서 n으로 끝나기 위해선 길이를 n+1로
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사 => 모든 숫자는 그 제곱근을 기준으로 약수의 절반이 각각 제곱근의 양옆에 위치하게 된다. (예, 16인 경우 <1, 2, (4),> 8, 16)
    # math 라이브러리의 sqrt 함수는 느리기 때문에 기본연산자로 사용                                                                          (21경우 <1, 3 (4.xxxx)>, 7, 21)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n + 1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]
# 에라토스테네스의 체는 '특정 범위 내의 소수'를 판정하는 데에만 효율적이다. 만약 주어진 수 하나가 소수인가? 만을 따지는 상황이라면 
# 이는 소수판정법이라 해서 에라토스테네스의 체 따위와는 비교도 안되게 빠른방법이 넘쳐난다.
# 1 부터 n까지의 포문을 돌지만 효율적으로 하기위해 루트n(이하)까지 포문을 돌게 설정한다.(루트 n 이후의 약수들은 이미 )
# 루트 n 설명 >>>>>>>>>>>>>

