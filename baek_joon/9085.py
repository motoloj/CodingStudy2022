# 2022_02_23_1
# 더하기
for _ in range(int(input())):
    num = int(input())
    num_list = list(map(int, input().split()))
    print(sum(num_list))