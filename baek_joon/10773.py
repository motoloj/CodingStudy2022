# 2022_03_31_1
# 제로
import sys
account = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        account.pop()
    else:
        account.append(num)
print(sum(account))