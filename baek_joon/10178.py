# 2022_02_17_5
# 할로윈의 사탕
n = int(input())
for _ in range(n):
    c,v = map(int, input().split())
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(c//v, c%v))
    # print("You get %d pieces(s) and your dad gets %d pieces(s)." %(c//v, c%d))
    # 여러개 출력시 괄호로 변수를 묶어줌(%s:문자열 %d:정수 %f:부동소수점)