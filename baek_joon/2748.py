# 2022_02_15_1 테스트중 일반 재귀정리만 사용시 시간초과(제한:1초, n=89일때)
# 재귀함수 +  메모이제이션(Memoization= 이전 계산값을 저장해 중복계산피함) 버전
from functools import lru_cache
n = int(input())

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
print(fibonacci(n))

# 반복문 버전, 위방식과 속도 유사해보임
n = int(input())
def iter_fibonacci(n):
    now, next = 0, 1
    for _ in range(n):
        now, next = next, now + next
    return now
print(iter_fibonacci(n))