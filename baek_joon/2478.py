# 2022_02_14_7 테스트중
n = int(input())
def fibonacci(n):
    if n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))