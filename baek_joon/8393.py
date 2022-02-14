# 2022_02_14_5 RecursionError 발생: 파이썬이 정한 최대 재귀 깊이보다 깊어지기 때문
# 해결법 1 :
# sys.getrecursionlimit(100000) 정도로 변경 -> 서버가 감당할 수 없을 정도로 매우 클 경우 Segmentation fault가 발생
import sys
sys.getrecursionlimit(100000)

n = int(input())
def factorial(n):
    return n * factorial(n-1) if n > 1 else 1
print(factorial(n))

# 해결법 2 <재귀함수를 사용하지마라>
# 동적할당의 경우 단순 반복문으로, DFS는 BFS로 구현
n = int(input())
ans = 0
for i in range(n):
    ans += i+1
print(ans)
