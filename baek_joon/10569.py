# 2022_02_17_7
# 다면체
#  (Vertex = 꼭짓점의 수) - (Edge = 모서리의 수) + (Plane or face = 면의 수) = 2
n = int(input())
for _ in range(n):
    v, e = map(int, input().split())
    print(2-v+e)