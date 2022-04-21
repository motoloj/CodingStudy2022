# 2022_04_21_1
# !밀비 급일
# read()여러줄 readline() 한 줄씩
import sys
password = sys.stdin.read().split('\n')

for i in password:
    if i == 'END':
        break
    else:
        print(i[::-1])