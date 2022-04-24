# 2022_04_24_1
# 팩토리얼 0의 개수
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
count = 0
for i in str(factorial(int(input())))[::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)