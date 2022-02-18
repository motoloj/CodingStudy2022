# 2022_02_18_4
# 팩토리얼
def factorial(n):
    a = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            a *= i
        return a
print(factorial(int(input())))

# -----------------------------------------------
# 재귀 함수
n = int(input())

def factorial(n):
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result
print(factorial(n))

# 기존 코드 수정(축소)
n = int(input())
result = 1
if n > 0:
    for i in range(1, n+1):
        result *= i
print(result)