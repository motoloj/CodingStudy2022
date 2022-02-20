# 2022_02_20_1
# 피보나치 수
#  @lru_cache(maxsize=None) 메모리에 미리 계산된 값을 적재
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))