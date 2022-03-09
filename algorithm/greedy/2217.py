# 2022_03_09_1
# 로프
# 생산운영관리 공정당 시간배분문제와 유사?(병렬처리시 가장작은 생산시간에 맞춰 다음 공정으로 넘기는 과정)
# 1 2 3 4 5 6 7 8 9 10
# 10
# 9 10 => 9+9 =18
# 8 9 10=> 8+8+8=> 24
# 7 8 9 10=> 7+7+7+7 =>28
# 6 7 8 9 10=> 6+6+6+6+6 = 30
# 5 6 7 8 9 10 => 5+5+5+5+5+5=30
# 4 5 6 7 8 9 10 => 4*7 = 28
# 로프가 아무리 많아도 최대중량은 연결로프 중 가장작은 로프에 맞춰 들수 밖에 없다. (4,10,10,10,10) => 4+4+4+4+4
# 무게를 오름차순으로 정렬 후 N번째 큰수를 N번만큼 곱해 각 경우의 최대 중량을 구한다.
import sys

n = int(input()) # 로프 수
rope = []
maximum_weight = []
for _ in range(n):
    weight = int(sys.stdin.readline())
    rope.append(weight)
rope = sorted(rope)

for i in range(n):
    maximum_weight.append(rope[i]*(n-i))
print(max(maximum_weight))