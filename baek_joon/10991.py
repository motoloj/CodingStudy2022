# 2022_02_18_2
# 별찍기 16
n = int(input())

# 한 줄씩 출력
for i in range(1, n+1):
    a = ''
    # 문자열 스택 쌓기
    for g in range(1, 2*i):
        if g % 2 == 1:
            a += '*'
        else:
            a += ' '
    print(" "*(n-i)+a)
# -----------------------------------------------------------------------
# 2
#  *
# * *
# 3
#   *
#  * *
# * * *
# 4
#    *
#   * *
#  * * *
# * * * *
# print end 옵션 사용 
N = int(input())

for i in range(1, N+1):
    print(' '* (N-i), end = '')
    for j in range(i): 
        print('*', end = ' ')
    print()

# 한 줄 규칙 찾기
n = int(input())
for i in range(1,n+1):
     print(" " * (n-i) + "* " * (i-1) + "*")
