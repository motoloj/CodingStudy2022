# 2022_04_05_1
# 피보나치 수 5
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
print(fibonacci(n))

# n = int(input())
# def iter_fibonacci(n):
#     now, next = 0, 1
#     for _ in range(n):
#         now, next = next, now + next
#     return now
# print(iter_fibonacci(n))