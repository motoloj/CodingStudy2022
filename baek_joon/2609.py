# 2022_02_14_6
n1, n2 = map(int, input().split( ))
mok1 = mok2 = 0
min = min(n1,n2)

# 2, 5와 같은 최대 공약수가 1인 서로소 케이스를 위해 최소범위를 1까지
for i in range(min, 0, -1):
    
    if n1 % i == 0 and n2 % i == 0:
        mok1 = n1 // i
        mok2 = n2 // i
        break
        
# 최대공약수
print(i)

# 최소공배수
print(i*mok1*mok2)

# 유클리드 호제법일 경우, 위에서 쓴 반복문 보다 반복이 적음
# -> n1이 n2보다 작을 때 둘을 교환
# def gcd(n1, n2):
#     while n2 > 0:
#         n1, n2 = n2, n1 % n2

#     return n1

# 최소공배수 = 두 수의 곱 / 두 수의 최대 공약수
# def lcm(n1, n2):
#     return n1 * n2 // gcd(n1, n2)