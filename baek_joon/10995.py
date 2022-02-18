# 2022_02_18_1
# 별찍기 20
n = int(input())
a = ''
# 문자열 스택생성
for i in range(1, 2*n):
    if i % 2 == 1:
        a += '*'
    else:
        a += ' '

# 한 줄씩 반복 출력
for i in range(1, n+1):
    # 홀수 줄 출력
    if i % 2 == 1:
        print(a)
    # 짝수 줄 출력
    # 위에서 쌓은 a 앞에 공백만 추가해서 출력
    else:
        print(' '+a)
