# 2022_03_18_1
# 개수 세기
from collections import Counter
n = int(input())
numbers = Counter(list(map(int, input().split())))
print(numbers[int(input())])